import fs from 'node:fs';import path from 'node:path';import{createRequire}from'node:module';
const require=createRequire(import.meta.url);let pw;try{pw=require('playwright')}catch{pw=require(path.join(process.env.PLAYCALL_NODE_MODULES||'', 'playwright'))}
const out=process.argv[2];if(!out)throw Error('Pass an output directory outside the public repository');fs.mkdirSync(out,{recursive:true});
const base=process.env.PLAYCALL_PREVIEW_URL||'http://127.0.0.1:8873/';const browser=await pw.chromium.launch({headless:true,executablePath:process.env.PLAYCALL_CHROME||'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
const results=[];const problems=[];const external=new Set();
for(const size of [{name:'desktop',width:1440,height:1000},{name:'tablet',width:768,height:1024},{name:'mobile',width:390,height:844},{name:'compact',width:320,height:568}]){
 const context=await browser.newContext({viewport:{width:size.width,height:size.height}});
 for(const file of ['index.html','privacy.html','support.html','league-rules.html','check-your-email.html','confirmed.html']){
  const page=await context.newPage();page.on('request',r=>{if(!r.url().startsWith(base)&&!r.url().startsWith('data:'))external.add(r.url())});page.on('pageerror',e=>problems.push(file+': '+e.message));
  const response=await page.goto(base+file,{waitUntil:'networkidle'});await page.evaluate(async()=>{for(const i of document.images)i.loading='eager';await document.fonts.ready;await Promise.all([...document.images].map(i=>i.complete?Promise.resolve():new Promise(r=>{i.onload=r;i.onerror=r})));});
  const status=response.status();if(status!==200)problems.push(file+': HTTP '+status);
  const checks=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),h1:document.querySelectorAll('h1').length,main:document.querySelectorAll('main').length,unlabelledImages:[...document.images].filter(i=>!i.hasAttribute('alt')).length}));
  if(checks.overflow||checks.brokenImages.length||checks.h1!==1||checks.main!==1||checks.unlabelledImages)problems.push(size.name+'/'+file+': '+JSON.stringify(checks));
  if(file==='index.html'){
   await page.keyboard.press('Tab');if(await page.locator(':focus').textContent()!=='Skip to content')problems.push(size.name+': skip link not first');
   for(const d of await page.locator('details').all()){await d.locator('summary').click();if(!await d.getAttribute('open')&&await d.getAttribute('open')!== '')problems.push('FAQ did not open');await d.locator('summary').click()}
   await page.screenshot({path:path.join(out,size.name+'-home-full.png'),fullPage:true});await page.evaluate(()=>scrollTo(0,0));await page.screenshot({path:path.join(out,size.name+'-home.png')});
   // Actual footer navigation and return path.
   await page.getByRole('link',{name:'Privacy Policy',exact:true}).click();if(!page.url().endsWith('privacy.html'))problems.push('Privacy navigation failed');await page.getByRole('link',{name:'PlayCall home'}).first().click();if(!page.url().endsWith('index.html'))problems.push('Home navigation failed');
  }
  results.push({viewport:size.name,file,status,...checks});await page.close();
 }
 await context.close();
}
for(const file of ['index.html','privacy.html','support.html','league-rules.html']){
 const page=await browser.newPage({viewport:{width:390,height:844}});await page.goto(base+file);await page.addStyleTag({content:':root{font-size:32px!important}'});await page.evaluate(()=>document.fonts.ready);const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);if(overflow)problems.push('200% text overflow '+file);results.push({viewport:'mobile-200%-text',file,overflow});await page.screenshot({path:path.join(out,'large-text-'+file+'.png'),fullPage:true});await page.close();
}
await browser.close();const report={base,cases:results.length,results,externalRequests:[...external],problems,scope:'Local static preview. Provider submission, CAPTCHA, email delivery, double opt-in, unsubscribe and live HTTPS are not asserted.'};fs.writeFileSync(path.join(out,'browser-results.json'),JSON.stringify(report,null,2));console.log(JSON.stringify({cases:results.length,problems,externalRequests:external.size}));process.exitCode=problems.length?1:0;
