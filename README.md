# PlayCall — prelaunch website

Live website: https://mattschiaff.github.io/playcall-site/

Separate public source: https://github.com/mattschiaff/playcall-site

This dependency-free Python/static HTML website is separate from the private iPhone application repository. Do not upload native app source, signing files, subscriber exports, diagnostic reports or secrets.

## Verified publication — October 21, 2026

GitHub Pages build and deployment succeeded. All 24 served pages and assets returned HTTPS 200 and matched the approved release files. Responsive checks passed all 28 cases, including compact widths and 200% text.

The official MailerLite form loads after an intentional visitor action. A fresh signup on the live website delivered its confirmation email. Confirming produced an Active subscriber in PlayCall Prelaunch Waitlist with a confirmed-signup event. The disposable test alias was then unsubscribed. A separate controlled one-recipient delivery test verified the actual email unsubscribe link. No launch announcement was sent.

The developer approved the operator identity, retention schedule and existing MailerLite postal address for subscriber-facing footers. That street address remains outside this repository. Optional open tracking, link tracking and UTM tags were off for the controlled email; provider-generated service redirects still apply. Check tracking and the complete mailing footer before every future campaign. Monthly retention review and deletion remain operator responsibilities. Native purchase privacy and App Store disclosures require their separate final audit.

## Preview locally

```sh
cd /Users/mattschiaffino/Documents/Codex/2026-09-29/PlayCallWebsite
python3 scripts/preview.py
```

Open http://127.0.0.1:8873/ while that Terminal is running. The server serves dist only. Stop with Control-C. Use --port 8874 if another preview occupies the default port. Localhost is a local preview, not the public site.

## Edit and validate

- Page copy: content/home.html, content/support.html and content/league-rules.html.
- App privacy sections: content/policy.json; shared HTML and website policy: scripts/build.py.
- Styling, fonts and authentic app previews: dist/assets/. See ASSET-PROVENANCE.md.
- Public provider embed: content/mailerlite-form.html and content/waitlist.json. Public form identifiers are not API secrets. Never add provider API keys.
- Verified publication decisions and URLs: content/release.json.

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 scripts/validate.py --release
```

Generated dist HTML is replaced by the builder; edit source content instead. The release validator must pass before deployment. The manual GitHub Pages workflow builds and validates, then publishes dist only. Pushes do not automatically deploy. Later verification-only metadata and README commits do not change the served artifact.

Optional responsive tests use Node, Playwright and installed Chrome; save their output outside the public repository:

```sh
node scripts/browser-check.mjs /private/tmp/playcall-website-checks
```

Use PLAYCALL_CHROME for another Chrome executable and PLAYCALL_NODE_MODULES for an external Playwright installation. These layout checks do not themselves assert provider delivery or subscription confirmation. The website has no pip/npm runtime dependencies; Pillow is needed only to regenerate brand artwork with scripts/make_brand_assets.py.

WAITLIST.md, PRIVACY-REVIEW.md and DEPLOYMENT.md retain preparation history. Their earlier hold/pending notes are superseded by the verified publication status above and the current release configuration. Production iPhone audio, PTT, routes, purchases and preferences are unchanged.
