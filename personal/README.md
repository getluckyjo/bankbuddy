# BankBuddy (personal)

A private Claude artifact for one person. It is not the product yet.

- **Reads statements** from Gmail (Capitec and FNB statement emails, plus anything forwarded with "BankBuddy" in the subject) or from PDFs you upload.
- **Opens password-locked PDFs in the browser** with pdf.js. Capitec uses the full account number as the password. Passwords stay in the browser (localStorage, opt-in) and are never saved online.
- **Has Claude read each statement** into transactions (the artifact `sample` capability, on your own Claude usage).
- **Finds every debit order and card subscription.** It flags new, doubled and pricier ones and shows the 60-day dispute window.
- **Drafts letters** (cancel, unauthorised-debit refund, CPA s14 contract notice, double charge, complaint) straight into Gmail drafts. It never sends anything.
- **Tracks cases and balances** in the artifact's private per-user store (`data/users/<id>/…`).

Live page: https://claude.ai/artifact/Ur7PqVrokNhGXjSFwANuqh (private).

## Monthly automatic check

A scheduled job ("BankBuddy monthly check") runs at 06:53 SAST on the 2nd of every month in a fresh cloud session and follows [`monthly/CHECK.md`](monthly/CHECK.md):

1. Finds new statement emails in Gmail.
2. Unlocks them with `monthly/extract_statement.py`, using the passwords in the environment variables `BANKBUDDY_CAPITEC_ACCOUNTS`, `BANKBUDDY_FNB_PASSWORD` and `BANKBUDDY_OTHER_PASSWORDS`.
3. Saves them to the page's data.
4. Summarises what needs a look with `monthly/analyse.py`.

The summary arrives as a push notification and an email.
