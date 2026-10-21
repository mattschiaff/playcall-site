> October 21 update: the developer approved website publication and the existing MailerLite subscriber-footer address. This supersedes the earlier postal-address hold below. Street-address details remain only in MailerLite. Verify outgoing unsubscribe and public-origin signup, and retain the guarded manual release workflow.

# GitHub Pages publication and operations

## Current boundaries

Website checkout: `/Users/mattschiaffino/Documents/Codex/2026-09-29/PlayCallWebsite`.

Requested dedicated public repository name: **playcall-site**. Safari shows the GitHub account **mattschiaff** signed in. The dedicated public source repository was created at https://github.com/mattschiaff/playcall-site on October 20, 2026. Its file upload is verified separately from Pages deployment; no live website is claimed until deployment passes. The native app repository is separate and must remain private. Do not push the parent PlayCallApp directory.

Only website source/configuration, public assets, provider embed identifiers, this operating documentation and the manual Pages workflow belong in the website repository. No Swift, signing files, private audits, test/build logs, local checkpoints, screenshots of private dashboards, secrets, subscriber CSVs or personal sender postal addresses belong here.

## Before making the repository public

1. Complete `PRIVACY-REVIEW.md` and the provider/local portions of the real `WAITLIST.md` test matrix; the live-origin portion is a post-deployment verification. Obtain the operator’s public identity, policy date and retention approval; inspect actual provider cookies/requests and sender footer.
2. Confirm the final GitHub owner/repository. The expected project-site shape is `https://OWNER.github.io/playcall-site/`, but that is a pattern, not a verified deployed URL.
3. In `content/release.json`, set actual `repositoryURL`, HTTPS `siteURL` **including the project path**, `policyURL`, operator identity and effective date. Set approval/test booleans only for completed checks. Public app purchase disclosure review remains a separate release responsibility.
4. Update the policy’s proposed/draft sections to the approved actual practice, including the active-subscriber cutoff and suppression/backups limitations. Add the real policy link to the provider form’s privacy text.
5. Build and run both validators. The release validator must pass honestly before publication.
6. Audit the full website file list and Git diff. Run a private-data/secret review on **all repository source**, not only deployed assets. Do not include local preview screenshots or exported subscriber records. The Pages artifact is `dist` only.

## Publish

Using GitHub’s signed-in UI, create `playcall-site` under the approved owner as a separate repository. Only upload/commit the audited website folder contents. Do not upload the private parent project. If using Git locally, run commands **inside the exact website checkout**, inspect `git remote -v` and `git status`, then connect the new remote and push only website history. The standalone local checkout is connected only to the dedicated playcall-site remote. Public source upload and live Pages publication are separate steps.

In the new repository:

1. Settings → Pages → Build and deployment → Source: **GitHub Actions**.
2. Actions → **Publish approved PlayCall website** → Run workflow on the publishing/default branch.
3. The manual workflow builds pages, runs `validate.py --release`, configures Pages, uploads `dist` and deploys that artifact. The workflow has no automatic push trigger.
4. Wait for the workflow and `github-pages` deployment environment to show success. Record the actual URL from the deployment, not an assumed username-derived address.
5. Settings → Pages → enforce HTTPS when available. Test the public HTTPS URL, page navigation, assets and provider signup flow.
6. Set the actual HTTPS confirmation redirects in MailerLite and repeat a fresh-address signup from the live site, including double opt-in and unsubscribe verification.
7. Validate canonical/OG image URLs and the generated sitemap at the live project path. Confirm the social card returns the correct PNG. Share this real URL in social account bios only after those checks.

## Update and redeploy

Edit content/assets → build → preview locally → validate → inspect diff → commit/push only the website changes → run the manual workflow → verify the public URL. A push alone does not publish. Keep the operator approval flags accurate; changed data handling requires renewed privacy review, not just a date change.

For privacy updates, first reconcile the actual provider/app behavior and retention procedure, update the public policy text and effective date, review changed consent purposes, then deploy. Material purpose changes may require fresh opt-in. Do not overwrite the in-app draft or enable native public links automatically; those require their own reviewed app change after real URLs exist.

## Custom domain later

Confirm ownership of the domain. In GitHub Pages settings add the approved custom domain and configure the domain provider’s GitHub-recommended DNS records. Set `customDomain` and the new `siteURL` / `policyURL` in release configuration; rebuild canonical, OG, sitemap and CNAME output. Revalidate HTTPS and provider redirects at the new domain before changing social links. Do not invent or purchase a domain without a separate instruction.

## Official GitHub guidance

- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
