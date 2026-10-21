# PlayCall — prelaunch website

Exact website folder: `/Users/mattschiaffino/Documents/Codex/2026-09-29/PlayCallWebsite`.

This is the recovered Phase 3F website, refined in Phase 4W. It keeps the dependency-free Python/static HTML approach and the separate local Git repository. The private iPhone application repository is not part of this website repository.

## Preview on this Mac

```sh
cd /Users/mattschiaffino/Documents/Codex/2026-09-29/PlayCallWebsite
python3 scripts/preview.py
```

Open **http://127.0.0.1:8873/** (also `http://localhost:8873/`). The server serves **dist only**. Keep that Terminal window running. Stop with **Control-C** in that window. To use another port: `python3 scripts/preview.py --port 8874`.

Why the old localhost link did not work: the earlier review server had been stopped; static HTML files do not start a server themselves. No Vite/Node app or missing npm install is involved. A server on your Mac is not a public website and cannot be reached from another device using its own localhost address.

## Make changes

- Homepage text/structure: `content/home.html`.
- Support and league guidance: `content/support.html`, `content/league-rules.html` (preserved from Phase 3F).
- App privacy sections: `content/policy.json`; website/waitlist policy sections and shared page shell: `scripts/build.py`.
- Colors, fonts and responsive layouts: `dist/assets/styles.css`.
- Public MailerLite form markup: `content/mailerlite-form.html`. Public account/form identifiers are not API secrets. Never add a MailerLite API key.
- Form mode and verified public share URL: `content/waitlist.json`.
- Publication decisions, approved identity/date and final URLs: `content/release.json`.
- Exact current brand assets and real native app previews: `dist/assets/`; see `ASSET-PROVENANCE.md`.

After editing content, run `python3 scripts/build.py` and refresh the browser. Restarting `scripts/preview.py` also rebuilds pages. Asset-only CSS/image edits require only a refresh. Do not hand-edit generated HTML in `dist` because the builder replaces it.

## Check before deployment

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 scripts/validate.py --release
```

The last command intentionally fails while explicit policy approvals, actual URLs and verified provider tests are pending. It must not be bypassed. The manual GitHub Pages workflow calls the same gate, then uploads **dist only**. No automatic deployment runs on push.

Optional repeatable responsive browser checks use Node and Playwright, with screenshots saved **outside the public repository**:

```sh
node scripts/browser-check.mjs /private/tmp/playcall-website-checks
```

Install Playwright separately if needed. The script uses installed Chrome on macOS; override its executable with `PLAYCALL_CHROME`. It checks desktop, tablet, mobile, compact iPhone width, larger text, navigation and images. It does not assert actual email delivery or public HTTPS deployment.

`make_brand_assets.py` needs Pillow only if regenerating the bundled favicon/social preview. The website itself needs no pip/npm packages.

## Current status

The website is a local review candidate, **not a verified public launch**. The dedicated MailerLite form/group has been created. Official email signup is loaded only after an intentional button press; provider confirmation/errors are real, never simulated. The provider handles email storage, double opt-in, duplicate records and unsubscribe status. A fresh test address completed signup → delivered confirmation email → confirmed Active membership in the dedicated group. The test alias was subsequently unsubscribed through the dashboard. Email-footer unsubscribe-link and live-site-origin tests remain pending. No website email database, local email storage, remote push, app backend or analytics tags were added.

See `WAITLIST.md` for provider setup and verification, `PRIVACY-REVIEW.md` for pending approval decisions, and `DEPLOYMENT.md` for publishing and custom domains. Production iPhone audio, PTT, routes, purchases and preferences remain unchanged.

## Explicit launch hold

On October 19, the developer approved the public operator name and waitlist retention schedule, and requested that launch stay on hold while a PO box/private mailbox is arranged. Do not publish, send a waitlist campaign, or use the existing private postal address in subscriber-facing footers. The local website and provider test form can still be reviewed.

## GitHub source repository

The separate public website repository is https://github.com/mattschiaff/playcall-site. Uploading source does not activate GitHub Pages. Public website deployment remains guarded pending the approved mailing address and remaining release checks. Only the standalone website files belong in this repository.
