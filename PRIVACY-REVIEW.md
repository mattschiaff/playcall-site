# Public policy review — required before publication

The existing Phase 3F app policy is preserved and extended with website/waitlist sections in `scripts/build.py`. Review the generated `dist/privacy.html`. This is a concrete review draft, not a compliance certification or a submitted App Store disclosure.

## Approved October 19, 2026

Operator name: **PlayCall, operated by Matt Schiaffino**. The proposed 30-day unconfirmed / 12-month active / 180-day postlaunch schedule below was approved. Public launch is explicitly **on hold** while the developer arranges a PO box/private mailbox. The existing postal address is not approved for subscriber-facing use. It has not been changed or copied into this repository.

## Remaining publication review

1. Public operator identity: approve the legal/display identity to name in the policy. The support contact is already approved as playcall.support@gmail.com; no company identity is invented.
2. Effective date: use the actual publication date once approved, not an invented backdated date.
3. Approved waitlist retention: unconfirmed records **30 days**; active subscriptions until unsubscribe/deletion, **12 months after confirmation**, or **180 days after public launch**, whichever comes first. Monthly operator review; no automatic extension into an unrelated product-news list. Minimal consent/suppression records and provider backups require a separate justified schedule, not blanket deletion promises. This schedule is adopted; enforcement is an operator responsibility and still needs verification.
4. Approve the existing MailerLite sender postal address for subscriber-facing email footers, or replace it with an appropriate business mailing address in MailerLite. It is intentionally not copied into this repository.
5. Review the actual provider form/storage/requests, Google reCAPTCHA and outgoing email measurement. Website HTML is not proof that provider scripts make no additional requests. Check regional consent requirements for the final configuration.
6. Confirm operator access/security, retention enforcement, opt-out/deletion handling and final public policy text. A policy does not enforce its own promises.

The approved **support** retention remains separate: developer-held support emails, downloaded logs/attachments and downloaded TestFlight feedback are deleted within 90 days after issue resolution. Non-identifying bug notes may remain as needed. Active waitlist subscribers are not automatically deleted under that support rule. Apple-managed original TestFlight data follows Apple’s separate practices.

## Actual data-flow boundaries

| Flow | Handling |
| --- | --- |
| Website page/assets | Static GitHub Pages delivery once deployed; host receives web request information under GitHub’s policy. No authored analytics, ads or email storage. |
| Optional form load | Visitor deliberately loads the official MailerLite widget; provider/reCAPTCHA processing then applies. Provider request and cookie inspection remains a release test. |
| Email signup | Email + checkbox consent + provider technical/confirmation records go directly to MailerLite. No API key, PlayCall database or subscriber file in Git. |
| Double opt-in | MailerLite sends a confirmation email and owns the subscriber state. A static success page is not subscription verification. |
| Developer access | MailerLite dashboard/exports; access is controlled by the operator. No public subscriber count or identifying data exposed. |
| Marketing delivery | Approved launch/beta messages only; sender, unsubscribe and final tracking behavior must be checked. No campaigns have been sent by this task. |
| Support | Messages sent voluntarily to the approved Gmail; developer downloads/backups need separate manual deletion. |
| Native iPhone app | Existing local audio, setup preferences, diagnostics, Apple StoreKit and optional local reminders remain unchanged. Website collection is not silently attributed to app-server audio collection. |

UTM URLs work as normal links; authored code does not store or profile them. No overall cookie-free, no-collection, league-approval, compatibility or privacy-compliance guarantee is made. Required App Store disclosures remain subject to the existing final production purchase audit; website work does not finalize them.

Before publishing, replace draft/proposed language with **approved, operationally verified** behavior and set the specific release flags truthfully. Never simply change all flags to true to make the workflow pass.

## Form render observation

At 1440, 390 and 320 px widths, exactly one official form/email input rendered without horizontal overflow. No external requests occurred before the intentional load action. Afterward, MailerLite asset/CDN/font/form endpoints and Google/gstatic reCAPTCHA endpoints were observed. No cookies or local/session storage keys were seen immediately after clean-browser rendering. This is not evidence about submission, CAPTCHA completion, email links or all future provider behavior.

The city/state-only footer alternative was reviewed against FTC and MailerLite guidance and was not adopted. A registered PO box or qualifying private mailbox is an alternative to the home street address. Public launch remains held at the developer’s explicit request.

Sources: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business and https://www.mailerlite.com/help/how-to-update-your-company-profile

## Verified provider test

Fresh-address signup delivered its confirmation email. The developer confirmed it, and MailerLite showed Active membership with an explicit confirmation activation event. Operator-side unsubscribe changed only the test alias to Unsubscribed. No campaign was sent. The outgoing email unsubscribe link and live-site-origin signup still need testing after the approved mailing address is available.

## October 21 update

The developer explicitly approved using the existing address in MailerLite subscriber-facing footers and requested website publication. This supersedes the October 19 mailbox hold. No street address is included in this repository. The operator identity and retention schedule remain approved. Publication metadata targets the project-specific GitHub Pages HTTPS URL.

A controlled delivery draft targets exactly the public support inbox, with optional open tracking, link tracking and UTM switches all observed off. Sending is paused for the operator to review MailerLite terms; actual receipt and email-link unsubscribe are not yet recorded as verified. Default confirmation links can redirect through MailerLite services. The policy explains this rather than promising measurement-free email. Native app distribution and final App Privacy review remain separate.
