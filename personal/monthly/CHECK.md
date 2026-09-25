# BankBuddy monthly check

This file tells a scheduled Claude session what to do. It runs on the 2nd of every month.

**The job:**
1. Bring any new Capitec or FNB statement emails from Gmail into BankBuddy's saved data.
2. Report anything that needs attention.

The report is your final message. It reaches the owner as a push notification and an email.

**Where things are:**
- **The page:** https://claude.ai/artifact/Ur7PqVrokNhGXjSFwANuqh
- **Its data:** read and write it with the `ArtifactData` tool (load it with ToolSearch). The `url` is the address above.
  - `data/users/me`: doc `settings`. This holds `processed`, a map of Gmail message id to status, and `decisions`.
  - `data/users/me/profile/statements`: one document per statement.
  - `data/users/me/profile/cases`: the owner's cases.
- **Gmail:** the Gmail connector, with the tools `search_threads` and `get_message`.
- **Scripts:** `personal/monthly/` in this repo. If the repo isn't checked out, clone `https://github.com/getluckyjo/bankbuddy`, branch `claude/cool-galileo-thu3hs`.

## Privacy rules
- Only open bank statement emails, the ones found by the searches below. Don't read any other email.
- Never write statement text, balances or account numbers into your messages, apart from the final summary. The final summary only needs company names, amounts of flagged items and days left to dispute.
- Never print environment variables.
- At the end, delete your work folder and every saved Gmail tool result, as in step 7.

## Steps

### 0. Setup
```bash
cd personal/monthly
python3 -c "import pypdf, cryptography" 2>/dev/null || pip install -q "pypdf[crypto]"
python3 -c "import pypdf, cryptography" 2>/dev/null || pip install -q --ignore-installed cffi cryptography
test -n "$BANKBUDDY_CAPITEC_ACCOUNTS" && echo "passwords: set" || echo "passwords: MISSING"
WORK=$(mktemp -d)
```
If the passwords are missing, keep going. Emailed Capitec statements will come back locked, which step 3 handles.

### 1. Read settings
Get `data/users/me` / `settings` with `ArtifactData`. Keep its `processed` map and its `version`.

### 2. Find statement emails
Run each of these `search_threads` queries with `pageSize: 50`. Follow `nextPageToken`, up to 3 pages.

| Query | Keep a message only if |
|---|---|
| `from:capitecbank.co.za filename:pdf subject:statement newer_than:3m` | the sender ends with `capitecbank.co.za`, the subject contains "statement", and the subject does NOT contain confirmation, notification or beneficiary. bank = `Capitec` |
| `from:fnb.co.za filename:pdf newer_than:3m` | the sender ends with `fnb.co.za`, and the subject is not a payment notification or proof of payment. bank = `FNB` |
| `subject:bankbuddy filename:pdf newer_than:3m` | the subject contains "BankBuddy". The bank comes from the subject (FNB or Capitec), otherwise leave it blank. |

Skip any message whose `processed[id]` is `ok` or `no_pdf`.

### 3. Read each new statement email
For each new message:

1. Call `get_message` with `messageFormat: "RAW"`.
   - The result is large, so Claude Code saves it to a file and gives you the path.
   - Run: `python3 extract_statement.py <that file> $WORK/<message id>`
   - It prints one JSON line per PDF.
2. If there's no PDF, set processed to `no_pdf`.
3. If the PDF is locked and not unlocked, set processed to `password`. Tell the owner in the summary: "Add BANKBUDDY_CAPITEC_ACCOUNTS (or the FNB password) to the cloud environment's variables."
4. For each unlocked PDF, read its text file and pull out the data using the RULES below.
   - If it isn't a bank statement, set processed to `ok` and save nothing.
   - Otherwise build the statement document **exactly** like this (the page reads this shape):
     ```json
     {"bank": "Capitec", "accountName": "…", "accountLast4": "1234",
      "periodStart": "YYYY-MM-DD", "periodEnd": "YYYY-MM-DD",
      "openingBalance": 0.0, "closingBalance": 0.0, "feesTotal": 0.0,
      "transactions": [{"date": "YYYY-MM-DD", "amount": -189.0, "kind": "debit_order", "merchant": "SafeHaven", "description": "SAFEHAVEN FNRL 0331"}],
      "source": {"type": "gmail", "messageId": "<id>", "filename": "<pdf name>", "date": "<email date>"},
      "importedAt": "<now ISO>"}
     ```
   - `kind` is `"debit_order"` or `"card_subscription"`, and `amount` is always negative.
5. Build the document id as `<bank>_<last4 or acct>_<periodStart or x>_<periodEnd or y>`, replacing any character outside `A-Za-z0-9_-.~:@+` with `-`. For example: `Capitec_1234_2026-09-01_2026-09-30`.
6. Write the JSON to a file and save it with `ArtifactData set` to collection `data/users/me/profile/statements`, using that doc id and `file_path`.
7. Set processed for the message to `ok`.

**RULES for pulling out the data.** These are the same as on the page.
- **Account:** record only the last 4 digits of the account number, never the full number.
- **What counts as a transaction:** only money going out that is one of:
  - **(debit_order):** a debit order, DebiCheck, NAEDO/AEDO, EFT debit collected by a company, an insurance premium, or a loan, rental or contract collection.
  - **(card_subscription):** a card or online charge to a subscription or membership service, such as streaming, music, apps, software, cloud storage, memberships or gyms.
- **Leave out:** payments the account holder made to people or suppliers, transfers, cash, ordinary shop or restaurant card purchases, bank fees, and money coming in.
- **Each charge once:** statements can print the same charge twice in different wording, for example "Netflix" and "Recurring Card Purchase: Netflix". List each real transaction ONCE, taken from the main transaction list. Only list it twice if the main list really shows it twice.
- **merchant:** the company's plain name, without reference numbers.
- **description:** the statement text as printed, up to 40 characters.
- **feesTotal:** the total of bank fees and charges, as a positive number.
- **Balances:** in rands, negative if overdrawn, null if not shown.
- **Don't invent anything.**

### 4. Update settings
Use `ArtifactData update` on `data/users/me` / `settings`, with `if_version` set to the version you read:
```json
{"processed": {"<id>": "ok", "...": "..."}, "lastScanAt": "<now ISO>"}
```
`processed` merges into the existing map. If the version has changed in the meantime, get the document again and redo the update.

### 5. Analyse
1. Save the data locally with `ArtifactData list` and `out_dir: $WORK/data`:
   - `data/users/me/profile/statements` (limit 500)
   - `data/users/me/profile/cases` (limit 500)
2. Save the settings you read to `$WORK/settings.json`.
3. Run:
```bash
python3 analyse.py $WORK/data/data/users/me/profile/statements $WORK/data/data/users/me/profile/cases $WORK/settings.json
```

### 6. Final message
Keep it short. It is the notification.

- **The headline:** `BankBuddy monthly check: <n> new statement(s) read. <n> thing(s) need a look.`, or `Nothing new this month.`
- Then the output from `analyse.py`.
- Then any locked or failed emails, each with its fix.
- Then the link: https://claude.ai/artifact/Ur7PqVrokNhGXjSFwANuqh

Don't commit or push anything. This job changes no code.

### 7. Clean up
```bash
rm -rf "$WORK"
rm -f ~/.claude/projects/*/tool-results/mcp-Gmail-* 2>/dev/null
```
