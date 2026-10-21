#!/usr/bin/env python3
"""Check public paths, semantic HTML and the explicit publication gates."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import argparse,json,re,sys
R=Path(__file__).resolve().parents[1];D=R/'dist';p=argparse.ArgumentParser();p.add_argument('--release',action='store_true');a=p.parse_args();errors=[];links=0;external=set()
cfg=json.loads((R/'content/release.json').read_text());wait=json.loads((R/'content/waitlist.json').read_text())
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.h1=0;self.main=0;self.lang=False;self.meta=set()
 def handle_starttag(self,t,attrs):
  b=dict(attrs)
  if t=='html':self.lang=b.get('lang')=='en'
  if t=='h1':self.h1+=1
  if t=='main':self.main+=1
  if t=='meta':self.meta.add(b.get('name') or b.get('property'))
  if 'id' in b:
   if b['id'] in self.ids:errors.append('Duplicate id '+b['id'])
   self.ids.add(b['id'])
  if t=='img' and 'alt' not in b:errors.append('Image missing alt')
  if t=='nav' and not b.get('aria-label'):errors.append('Navigation lacks accessible name')
  if t=='form' and wait['mode']=='unconfigured':errors.append('Unexpected signup form while unconfigured')
  for k in ['href','src']:
   if b.get(k):self.refs.append((b[k],t,b.get('rel','')))
pages={}
for f in D.glob('*.html'):
 d=Page();d.feed(f.read_text());pages[f.resolve()]=d
 if d.h1!=1 or d.main!=1 or not d.lang:errors.append(f.name+': heading/main/lang')
 for meta in ['description','og:title','og:description','og:image','twitter:card']:
  if meta not in d.meta:errors.append(f.name+': missing '+meta)
for f,d in pages.items():
 for ref,t,rel in d.refs:
  links+=1;u=urlsplit(ref)
  if u.scheme in ['https','mailto']:
   external.add(ref)
   if t=='link' and rel=='canonical':
    expected=(cfg.get('siteURL') or '').rstrip('/')+'/'+('' if f.name=='index.html' else f.name)
    if ref!=expected:errors.append('Invalid canonical URL '+ref)
   elif t!='a' and 'mailerlite' not in (u.hostname or ''):errors.append('Unexpected external runtime dependency '+ref)
   continue
  if u.scheme or u.netloc or u.path.startswith('/'):errors.append('Invalid/root-relative path '+ref);continue
  dest=(f.parent/unquote(u.path)).resolve() if u.path else f
  if not dest.is_relative_to(D.resolve()) or not dest.is_file():errors.append('Missing asset/link '+ref+' in '+f.name)
  if u.fragment and dest in pages and u.fragment not in pages[dest].ids:errors.append('Missing anchor '+ref)
allowed_roots={'.github','.gitignore','README.md','DEPLOYMENT.md','WAITLIST.md','PRIVACY-REVIEW.md','ASSET-PROVENANCE.md','content','dist','scripts','requirements-artwork.txt'}
for f in R.iterdir():
 if f.name not in allowed_roots and f.name!='.git':errors.append('Unexpected repository-root candidate '+f.name)
allowed_dist={'.nojekyll','index.html','privacy.html','support.html','league-rules.html','check-your-email.html','confirmed.html','robots.txt','assets/styles.css','assets/waitlist.js','assets/app-icon.png','assets/wordmark.png','assets/favicon.png','assets/apple-touch-icon.png','assets/social-preview.png','assets/fonts/Barlow-Regular.ttf','assets/fonts/Barlow-SemiBold.ttf','assets/fonts/BarlowCondensed-Bold.ttf','assets/fonts/OFL.txt','assets/fonts/OFL-BarlowCondensed.txt','assets/screenshots/ready.png','assets/screenshots/transmitting.png','assets/screenshots/microphone.png','assets/screenshots/headphones.png'}
if cfg.get('customDomain'):allowed_dist.add('CNAME')
if cfg.get('publicationApproved') and cfg.get('websitePrivacyApproved') and cfg.get('siteURL'):allowed_dist.add('sitemap.xml')
actual_dist={str(f.relative_to(D)) for f in D.rglob('*') if f.is_file()}
if actual_dist!=allowed_dist:errors.append('Unexpected/missing public artifact files '+repr(actual_dist^allowed_dist))
for f in D.rglob('*'):
 if f.is_symlink():errors.append('Symlink forbidden '+str(f))
 if f.is_file() and (f.suffix.lower() in ['.swift','.log','.patch','.p12','.mobileprovision','.csv'] or f.name.startswith('.env')):errors.append('Private or unexpected file '+str(f))
for f in [p for p in R.rglob('*') if '.git' not in p.parts and '__pycache__' not in p.parts]:
 if f.is_file() and f.suffix in ['.html','.json','.js','.mjs','.py','.css','.txt','.yml','.md']:
  text=f.read_text()
  if re.search(r'(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY|Bearer [A-Za-z0-9._-]{20,})',text):errors.append('Possible credential '+str(f))
if a.release:
 if cfg.get('publicLaunchOnHold'):errors.append('Developer hold: arrange approved subscriber-facing postal address before public launch')
 for k in ['publicationApproved','websitePrivacyApproved','waitlistRetentionApproved','hostingPrivacyReviewed','providerFormReviewed','providerTrackingReviewed','senderIdentityVerified','waitlistVerified','unsubscribeVerified']:
  if cfg.get(k) is not True:errors.append('Release gate: '+k)
 for k in ['providerName','effectiveDate','siteURL','repositoryURL','policyURL']:
  if not cfg.get(k):errors.append('Missing publication input: '+k)
 if wait.get('doubleOptInRequired') is True:
  if cfg.get('doubleOptInVerified') is not True:errors.append('Release gate: doubleOptInVerified')
 elif wait.get('optInMode')=='single':
  if cfg.get('singleOptInVerified') is not True:errors.append('Release gate: singleOptInVerified')
 else:errors.append('Release gate: explicit verified opt-in mode required')
 if wait['mode']=='unconfigured':errors.append('Waitlist is not activated')
 for f in D.glob('*.html'):
  if re.search(r'\[TO BE PROVIDED\]|review draft|local review preview|proposed for approval',f.read_text(),re.I):errors.append('Unresolved public draft '+f.name)
 if not (D/'sitemap.xml').exists():errors.append('Missing release sitemap')
report={'mode':'release' if a.release else 'preview','pages':len(pages),'referencesChecked':links,'externalLinks':sorted(external),'waitlistMode':wait['mode'],'publicFiles':[str(f.relative_to(D)) for f in sorted(D.rglob('*')) if f.is_file()],'errors':errors}
print(json.dumps(report,indent=2));sys.exit(bool(errors))
