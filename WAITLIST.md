> October 21 update: the developer approved website publication and the existing MailerLite subscriber-footer address. This supersedes the earlier postal-address hold below. Street-address details remain only in MailerLite. Verify outgoing unsubscribe and public-origin signup, and retain the guarded manual release workflow.

# MailerLite — PlayCall Prelaunch Waitlist

## Created configuration

- Dedicated group: **PlayCall Prelaunch Waitlist**.
- Embedded form: **PlayCall Prelaunch Waitlist**.
- Form dashboard: https://dashboard.mailerlite.com/forms/201768539077478020/overview
- Official public form: https://preview.mailerlite.io/forms/2725162/201768539077478020/share
- Public account ID `2725162`; public widget ID `5Lc0DN`. These are provider-generated public embed identifiers, not API credentials.
- Email is the only requested data field. Visible Email label; no name, role, school, team or phone field.
- Confirmation checkbox, privacy statement and reCAPTCHA enabled. Double opt-in is on.
- Signup action: Join the waitlist. Initial success: “You’re almost on the list.”, followed by check-your-email instructions. It does not claim an unconfirmed record is subscribed.
- Sender shown by the provider: PlayCall, playcall.support@gmail.com.
- Default future campaign open tracking was turned off; default automation open tracking was also turned off. Google Analytics defaults were already off. Recheck outgoing messages because defaults do not prove the behavior of every provider-generated message.
- No campaigns or automations were created or sent.

The website loads the **official provider widget** on an intentional “Load email signup” action after identifying MailerLite/Google reCAPTCHA processing. Before that action, the website loads no provider script. A direct official form link is available if the widget fails or scripts are blocked. Email submission, validation and success messages are owned by MailerLite; the website never fabricates a successful signup.

## Confirmation pages and plan limits

The free plan rejects editing the double opt-in email and provider thank-you content. No paid plan was purchased. Keep the supported default confirmation email, or choose a paid plan yourself if customized emails are important.

The site includes:

- `check-your-email.html`: initial submission, awaiting confirmation.
- `confirmed.html`: landing page after provider-recorded confirmation.

Neither static page can determine membership from its URL. No `?confirmed=true` trick or local flag is used as proof of subscription. Set redirects only once the actual HTTPS base URL exists:

1. Form → Edit design → Settings → Custom success page: `[actual-site-base]/check-your-email.html`.
2. Form → Double opt-in → Confirmation thank you page → “Or use your own landing page”: `[actual-site-base]/confirmed.html`.

Do not point either redirect to localhost for production. If provider plan limits prevent a redirect, keep the real provider confirmation destination and document that limitation.

## Required end-to-end verification

Use an inbox you control and a **fresh address/alias**, such as `your-inbox+waitlist-test@example.com`. It delivers to the same Gmail inbox but is a distinct MailerLite record. An existing active subscriber may be added to a new group without another confirmation email, so that does not test double opt-in.

1. Submit invalid/empty input and verify the real provider errors.
2. Submit a fresh address with explicit consent and complete reCAPTCHA.
3. Verify the initial almost-on-the-list message.
4. In MailerLite Subscribers, locate that test record. Confirm it is unconfirmed before the email link is used; do not count it as an active member.
5. Verify the actual confirmation email arrives (check spam/promotions).
6. Use its confirmation link and verify the configured provider/website destination.
7. Verify the same record is active in **PlayCall Prelaunch Waitlist**.
8. Submit the same active address again; verify no duplicate record. Do not promise a second confirmation email for an already active address.
9. Test unsubscribe from a test message when sending is approved; verify status changes and the group cannot mail the unsubscribed address. Do not send a campaign to the entire group as a test.
10. Repeat the real signup from the **live website URL** after deployment; local widget rendering alone does not pass this requirement.

A CAPTCHA needs user confirmation/interaction; do not disable spam protection just to automate the test. The existing main support address was added to the dedicated group without a duplicate; it was already active from manual setup and did not receive a new DOI email. A fresh plus-alias test was then submitted and its PlayCall confirmation email arrived in Gmail. The fresh alias’s confirmation email was received, the developer used its confirmation link, and MailerLite displayed Active status, an opt-in date and “Subscriber activated by confirming signup.” The alias was then unsubscribed through MailerLite’s subscriber action and its status changed to Unsubscribed. The original main support subscriber was left active. This verifies provider signup/DOI and operator suppression; the actual outgoing-email unsubscribe link and live website-origin submission remain unverified.

## Manage subscribers

In MailerLite: **Subscribers → Groups → PlayCall Prelaunch Waitlist**. Review status, not just the group count. Only confirmed active subscribers should receive the waitlist campaign. Never add this audience to unrelated lists or promise beta access.

For a CSV: filter the dedicated group and the status you actually need, choose visible columns, select records, then Actions → Export CSV/CSV for Excel. MailerLite requires administrator privileges for exports. Store exports in private controlled storage, never this repository; remove unnecessary downloads and backup copies under the approved retention procedure.

To email the waitlist: create a draft campaign, choose only this group with active subscribers, use the verified sender/footer, disable optional tracking, include the working unsubscribe link, send a test to your own inbox, review it, then explicitly authorize sending. No campaign is authorized merely by building this site.

For unsubscribe/deletion requests: stop further marketing using MailerLite’s unsubscribe status first. Confirm whether the person wants deletion too. Use provider-supported deletion/forgetting and independently review exports/attachments/backups; do not remove suppression protections in a way that allows accidental re-subscription. Do not re-import unsubscribed records as active.

## Official help

- https://www.mailerlite.com/help/how-to-create-an-embedded-form
- https://www.mailerlite.com/help/how-to-use-double-opt-in-when-collecting-subscribers
- https://www.mailerlite.com/help/which-cookies-are-used-by-mailerlite-forms
- https://www.mailerlite.com/help/how-to-export-subscribers
- https://www.mailerlite.com/legal/privacy-policy

Checked October 19, 2026. Exact menus and account-plan capabilities may change.
