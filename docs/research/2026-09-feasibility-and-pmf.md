# BankBuddy: Feasibility & Product-Market-Fit Research (South Africa)

**Date:** 25 September 2026
**Question:** Is there a viable business in an app that combines all of a South African's bank accounts and uses an AI assistant to do banking admin for them? Admin here means closing accounts, stopping and disputing debit orders, querying transactions, fetching statements and letters, and lodging and escalating complaints.
**Method:** Desk research across four workstreams: demand and market size, competitors and global comparables, regulation and data access, and bank-by-bank operational feasibility. Sources are linked at the end, and anything flagged **[unverified]** needs checking with primary research.
**Not legal advice:** the licensing and POPIA points need an opinion from an SA fintech lawyer.

---

## 1. Bottom line

**Verdict: the idea is worth pursuing, but not as first pitched.**

| Version of the idea | Assessment |
|---|---|
| **"One app that shows all my bank accounts"** | **Weak business.** SA has no open banking, and none is realistically expected before about 2027. Logging in with customers' passwords breaks bank terms (and the Code of Banking Practice). 22seven, SA's only scaled aggregator, never managed to charge for it and has since pivoted to B2B as Vault22. Banks, and in the US ChatGPT, are making the "all accounts" dashboard free. |
| **"An AI that fights my banking admin battles across every bank and every debit-order company"** | **Real, sharp, under-served pain with no dedicated SA player found.** 46% of banked adults had a bank problem last year, and a third never reported it. The ombud's formal banking cases rose 25% in 2025. Fraud losses rose 29%. From April 2026 you have **only 60 days** to dispute a debit order. Every bank's own AI assistant only works inside that bank; none will fight another bank or a funeral-policy debit-order company for you. |

**Scorecard**

| Dimension | Rating | Why |
|---|---|---|
| Pain severity | 🟢 High | FinScope 2025, the National Financial Ombud (NFO) and SABRIC data, plus the new 60-day dispute window (Section 3) |
| Differentiation | 🟢 Good | Bank assistants only work inside their own bank. No SA "consumer banking advocate" app found. |
| Willingness to pay | 🟡 Unproven | Aggregation alone won't sell (22seven). Paying monthly for someone to fight your battles does sell (LegalWise, R151–R405/month). Must be tested. |
| Data feasibility | 🟡 Medium–Low | No bank APIs except Investec and Nedbank (via partners). Statement PDFs are universal and compliant, but not real-time. |
| Action feasibility | 🟡 Medium | Most bank-side actions still need the user's own tap, call or branch visit. BankBuddy can fully own the merchant side, complaints and ombud escalation. |
| Regulatory risk | 🟡 Medium | The FAIS "advice/intermediary" classification is the big one; POPIA is second. Both are manageable with the right design and a legal opinion. |
| Competitive threat | 🟡 Medium | Banks' AI assistants (Absa Abby at 1.6m users, FNB NAVi, Discovery AI) will solve problems inside their own bank. Big-tech finance agents (ChatGPT Finances) are US-only for now. |

**The product that works in 2026 is an AI case manager, not an aggregator.**

- **Statements in, not passwords.** Users forward the stamped PDF statements every SA bank app already lets them email. No credentials, no scraping.
- **Monitor everything, especially debit orders.** Every debit order across every account is identified, explained and flagged if it is new, unknown, duplicated or rising, with a countdown to the 60-day dispute deadline.
- **Prepare, then one tap.** BankBuddy drafts every letter, complaint and dispute and deep-links the user to the exact screen in their bank app for the final tap.
- **Act directly where it legally can:**
  - cancellation letters to merchants, sent from the user's own email;
  - complaints to the bank;
  - escalation to the NFO as the user's representative under a signed mandate;
  - driving account closures through the new bank's switching service.

**Recommended entry point:** a **"Debit Order Guard"**. It audits every debit order across all your banks, raises a 60-day dispute alarm, and cancels at the merchant and suspends at the bank in one flow. It is concrete, the savings are measurable in rands, it is time-critical, and it is where banks structurally can't help you.

**Biggest risks:**
1. FAIS licensing classification.
2. Data access fragility.
3. Low everyday engagement, which is the classic killer of finance apps.
4. Banks' own assistants getting good enough.

The 90-day validation plan in Section 11 is designed to test these cheaply before building.

---

## 2. What was evaluated

**The concept:**
1. Aggregate all of a user's SA bank accounts into one view.
2. Add an AI assistant that does the admin: close accounts, stop and dispute debit orders, query transactions, get statements and confirmation letters, and lodge and escalate complaints.

**Four research workstreams:**
1. **Demand:** customer pain and market size.
2. **Competition:** SA players and global comparables, and what worked.
3. **Regulation and data access:** open banking status, screen scraping, licensing, POPIA and debit-order rules.
4. **Operational feasibility:** how each admin task actually works at each major bank today, and what a third party can automate.

---

## 3. Demand: the pain is real and measurable

### Headline evidence

| Signal | Data | Source |
|---|---|---|
| Banked adults | **89% of adults, 40.8m people** | FinScope Consumer SA 2025 (Jul 2026) |
| Multi-banked | **41% of banked adults hold 2+ bank accounts (about 16.7m)**, up from 39%. Many extra accounts exist to receive grants rather than by choice. | FinScope 2025 |
| Bank relationships | About 90m reported customer relationships against 40.8m banked adults, **about 2.2 per banked adult** (crude; includes inactive accounts) | Bank annual results 2025–26 |
| Capitec as a second bank | Of Capitec's 25.2m personal clients, only **9.9m are "fully banked"** there. About 15m hold it as a secondary account. | Capitec FY2026 results |
| Bank problems | **46% of consumers had a problem with their bank in the last year.** Top problems: unexpected fees, outages, complex fees, poor service, **illegal debit orders**. **About 1 in 3 never reported it.** | FinScope 2025 |
| Ombud complaints | NFO: 50,065 cases (+16%). Banking division: 14,685 cases, **formal cases +25%**. **Only 17% of banking findings went in the customer's favour.** Average **85 working days** to close. | NFO 2025 annual figures (Jun 2026) |
| Fraud | Digital banking crime **R2.41bn (+29%)** across 110,074 incidents, **average R21,865 each**. 39% of NFO banking cases involve digital fraud. | SABRIC 2025 (Aug 2026); NFO |
| Debit orders | **414.6m EFT debit orders a year worth R1.13 trillion.** Since 13 Apr 2026 there is **one 60-day dispute window**, replacing the old 40-day automatic reversal plus disputes of up to 365 days. After that you must chase the company yourself. | PayInc FY2025; PASA 2026 FAQ |
| Funeral-policy abuse | The FAIS Ombud reports **steadily rising complaints about unauthorised funeral-policy deductions**, including people tricked into approving the SMS that authorises a new debit order (DebiCheck). | FAIS Ombud (7 Sep 2026) |
| Account closure | Most traditional banks still require a **branch visit or phone call** to close a main account. | MyBroadband (Nov 2025); bank sites |
| Customer experience | University of Pretoria's 2025 Customer Experience Index: **problem resolution is customers' #1 complaint.** The typical path is "chat → call centre → *you'll have to go to the branch*". | EWN (Apr 2026) |
| Switching | People describe switching banks as tedious (28%) or difficult (23%). | FSCA study (2023) |

### What this means

- **The pain is not "I can't see my balances".** Banking apps are good at that. The pain is **getting problems resolved**, especially when a problem spans a bank and a third party (an insurer, gym, telco or lender), or several banks.
- **The 60-day rule creates urgency.** Before April 2026 a missed rogue debit order could be clawed back for up to a year. Now a consumer who checks statements only occasionally loses that right fast. Continuous monitoring across every account went from "nice" to "necessary".
- **Fraud is the emotional trigger; admin is the everyday one.** Fraud gets attention but banks invest heavily there. Debit orders, fees, closures and complaints are where people are left alone.

---

## 4. Who will pay: segments and sizing

The figures below are the research agent's estimates. The multi-banking rates for the affluent segments are **assumptions to validate**.

| Layer | Definition | Size | Revenue potential |
|---|---|---|---|
| **TAM** (whole market) | Middle and top-income adults (BrandMapp top 30%, about 13m) × an assumed 55% multi-banked | **about 7m people** | About R8bn/year at R99/month (theoretical) |
| **SAM** (market we could serve) | SARS taxpayers earning over R350k (**3.04m**) × an assumed 70% with several banks or products | **about 2.1m people** | About R2.5bn/year at R99/month |
| **SOM** (share we could win in 3–5 years) | 1.5–3% of SAM paying | **30k–65k subscribers** | **About R30m–R115m annual recurring revenue** at R79–R149/month |
| **Small businesses** (adjacent) | About 0.84m–1.34m formal micro and small businesses **[unverified]**, many owner-run and juggling business and personal accounts | About 1m | 1–2% at R199–R399/month gives **about R25m–R95m ARR** |

**Most likely early adopters, in priority order:**

1. **Affluent, time-poor, multi-banked professionals (roughly 30–55).**
   - They have the most accounts, debit orders and insurance policies, the highest opportunity cost of time, and can afford R79–R149/month.
   - Investec alone estimates about 700k affluent South Africans.
2. **Owner-managed small businesses.**
   - They have recurring needs for statements and confirmation letters (SARS, VAT, lenders, tenders), mixed personal and business banking, and a higher willingness to pay.
3. **B2B2C partner channels: employers, insurers and debt counsellors.**
   - Employers can offer it as a financial-wellness benefit. Paymenow alone reaches 750k+ employees.
   - This is how most surviving personal-finance apps reached scale abroad.
4. **Hypotheses not yet researched, but worth testing in interviews:**
   - **"Sandwich generation"** users managing elderly parents' banking.
   - **Deceased-estate banking admin:** closing a late relative's accounts and stopping their debit orders. This is notoriously painful and emotionally loaded.

**Warning:** much of SA's 41% multi-banking comes from low-income people with grant-receiving accounts. That group has real debit-order abuse pain (the funeral-policy complaints), but very low ability to pay. Serving them is better done through B2B2C (employers, NGOs, SASSA-adjacent partners) or a free tier than by direct subscription.

---

## 5. Competitive landscape

### South Africa

| Player | What it does | Relevance |
|---|---|---|
| **Vault22 (formerly 22seven, Old Mutual)** | The only scaled SA aggregator: 400k users in 2021. Went free in 2014. Merged into SC Ventures-backed Vault22 in Nov 2024. Now positions itself mainly as B2B/white-label and is expanding to the UAE. Free / R75 / R150 tiers; Google Play rating 3.0, with reviews complaining about product pushing. Links banks by having users enter one-time PINs, which suggests it logs in with their credentials. | **Proof that aggregation alone doesn't monetise in SA.** Its move towards selling products eroded trust. It is also a potential white-label partner or acquirer. |
| **FinWise** | Small independent budgeting app, R79.99/month, "doesn't sell you products" | Price anchor. Budgeting-focused, not admin. |
| **Bank money tools** (FNB nav>>Money, Nedbank Money, Capitec, Discovery) | Budgeting and categorising **within their own bank**. Discovery links only partner accounts (EasyEquities, Luno). | They make the single-bank dashboard free. None consolidates external banks (as of Jul 2026). |
| **Bank AI assistants** | **Absa Abby** (1.6m users, doing multistep tasks since 2025); **FNB NAVi** (FNB is building end-to-end agents, including for disputes); **Discovery AI** (about 55% of queries resolved at first contact); **Capitec Pulse** (contact-centre AI); **Nedbank Enbi** (statements, tax certificates) | **The main long-term competitor for problems inside one bank.** Structurally, none will cancel your gym contract, fight another bank or escalate against itself to the ombud. |
| **truID** | Consent-based bank data: statements, transactions, balances, affordability. Clients include FNB, TymeBank, Old Mutual and many lenders. | **Likely data partner.** It does not say how it collects data **[unverified]**. |
| **Stitch / Ozow / Peach** | Pay-by-bank and payments infrastructure. Stitch raised a $55m Series B (Apr 2025) and has pivoted to payments; whether its old data API still exists is **[unverified]**. | Payment rails if BankBuddy ever initiates payments. Not competitors. |
| **Debit-order management or complaints startups** | **None found.** | **The gap.** |

### Global comparables and what they teach

| Company | Outcome | Lesson for BankBuddy |
|---|---|---|
| **Rocket Money (formerly Truebill, US)** | Acquired for **$1.275bn** (2021). 10m+ members. Pay-what-you-want Premium at $7–14/month. **Bill-negotiation success fee of 35–60% of first-year savings.** Says it has saved members $1bn+, $490m of it from cancelled subscriptions. | **Selling outcomes (cancellations, savings) beats selling insight.** Report value in rands saved. |
| **Mint (Intuit, US)** | **Shut down in March 2024.** Free, ad- and referral-funded, then neglected. | Free aggregation plus lead-gen doesn't work. |
| **Yolt (ING, EU)** | Consumer app closed (2021–22) because it couldn't reach scale. The B2B business was later closed too. | Aggregation infrastructure alone isn't a business either. |
| **Emma (UK)** | Profitable, about 90% subscription revenue, about 22 staff | A lean paid consumer model can work. |
| **Snoop (UK)** | Bought by Vanquis, a lender, in 2023 and used as "an efficient acquisition channel" | The exit path: become a large financial firm's engagement or acquisition channel. |
| **Cleo (US, AI assistant)** | **2025 revenue $254m; 1.3m paying subscribers.** But it paid **$17m to settle FTC charges** over deceptive claims and hard-to-cancel subscriptions. | AI money assistants can scale. Be scrupulously honest in claims and make cancelling easy. |
| **DoNotPay (US)** | **FTC order (Feb 2025)** for untested "robot lawyer" claims | Don't over-promise AI legal abilities. Keep a human reviewing high-stakes work. |
| **Pine AI (US)** | An AI agent that phones companies to cancel, negotiate and get refunds | Validates the "AI does the admin" concept. Its claimed success rates are **[unverified]**. |
| **Klarna** | Replaced about 700 agents with AI, then partly reversed after quality dropped (2025) | Full automation of customer service has limits, and the same applies to our agent. |
| **ChatGPT "Finances" (US, May 2026)** | Connects US bank accounts via Plaid. OpenAI says 200m people a month ask ChatGPT money questions. | A **future threat** if it reaches SA. It depends on SA bank connectivity, which barely exists. Local process know-how is the defence. |

**Why standalone personal-finance apps fail:**
- Engagement decays; only about 4–8% of finance-app users are still active at day 30.
- Users won't pay "to be told they overspend".
- Credential-based bank connections break.
- Banks copy the features for free.
- Lead-gen revenue destroys trust.

**What the survivors did:**
- sold **outcomes** (Rocket Money);
- charged **from day one** (Emma);
- owned a **money flow** (Plum, Cleo);
- or became a **channel** for a larger financial firm (Snoop, Truebill).

---

## 6. Feasibility: getting the data

### The regulatory reality (September 2026)

- **No mandated open banking or open finance in SA, and no firm date.**
  - The FSCA's March 2024 recommendations proposed a mandatory, licensed regime, with API standards by March 2026 and a consent framework by September 2026. **Neither appears to have been delivered.**
  - The Reserve Bank's 2025/26 payments oversight report says open finance will be phased in **starting with payment initiation, not data**.
  - Industry (Stitch, July 2026) expects hard API requirements to be "a 2027 and beyond conversation".
- **Logging in with users' bank passwords ("screen scraping") is not licensed, but it is contractually toxic.**
  - For read-only data access it is neither licensed nor banned.
  - But bank terms forbid sharing credentials. Standard Bank's digital terms put all losses on the customer if they do.
  - The Code of Banking Practice (Jul 2025, s22) tells customers to "never disclose your access credentials… to anyone".
  - Banks have blocked aggregators before: Absa and Capitec blocked 22seven in 2012.
  - Cybercrimes Act exposure is **untested**.
- **Moving money this way needs registration.** Initiating payments with scraped credentials requires Reserve Bank registration under Directive 2 of 2024; penalties go up to R1m and/or 5 years.

### Bank APIs open to third parties

| Bank | Account data API for third parties? |
|---|---|
| **Investec** | **Yes.** OAuth consent plus formal third-party onboarding (about 6–8 weeks). It explicitly lists aggregator apps as a use case. |
| **Nedbank** | **Yes, for approved partners.** Its API Marketplace has UK-style account-information consent endpoints. |
| Standard Bank, Absa, FNB, Capitec | **None found** (payments or business-only APIs) |
| Discovery, GoTyme (formerly TymeBank) | **[unverified]** |

### Recommended data strategy: statements first, no passwords

1. **Tier 1: statement PDFs (all banks, launch).**
   - Every major bank app lets users download or email a **stamped PDF statement** (Capitec, Standard Bank, Absa, Nedbank, Discovery, GoTyme; FNB **[unverified]**).
   - Users set up a monthly forward to a personal BankBuddy inbox, or upload directly.
   - PDF parsers for SA statements already exist (e.g. Spike), and modern AI models handle this well.
   - It is **user-initiated, needs no credentials, is POPIA-consented and can't be blocked by banks.**
   - The trade-off is monthly rather than real-time data, which is fine for admin work.
2. **Tier 2: forwarded bank notifications (near real-time).**
   - Users forward bank email alerts. On Android, an opt-in notification or SMS listener can read bank alerts.
   - iOS doesn't allow reading notifications, so iOS users rely on email alerts.
   - This catches new debit orders within hours, not weeks.
3. **Tier 3: consented APIs and partners (grow into).**
   - Investec's API (onboard early; it suits the affluent segment), Nedbank's API Marketplace, and truID for broader coverage (due diligence on its collection method first).
   - Sit ready for the open-finance regime from 2027.
4. **Backstop: POPIA s23 / PAIA access requests.**
   - This is a lawful, 30-day route to obtain records from a bank or merchant on a user's behalf, with proof of capacity.
   - Too slow for monitoring, but powerful in disputes.
5. **Avoid:** collecting bank passwords or one-time PINs.
   - It is also a **marketing asset**: *"BankBuddy will never ask for your banking password, PIN or OTP."* In a country losing R2.4bn a year to digital banking fraud, that message sells trust.

---

## 7. Feasibility: doing the admin

### How each task works at each bank today (Sep 2026)

| Bank | Close main account | Stop/suspend debit order | Dispute debit order in app | Stamped statement / confirmation letter | Complaint by email |
|---|---|---|---|---|---|
| **Capitec** | Branch (R6 fee) | App | App, **under R800** | App (PDF, e-stamped) | Yes |
| **FNB** | Branch/phone; Premier/Private can use email or Secure Chat **[guide dated 2019]** | App, at least 5 business days before the debit | App, **R200 or less** | App **[unverified]** | Yes |
| **Standard Bank** | Phone or branch **[unverified]** | App | App | App (3/6-month stamped) | Yes |
| **Absa** | Branch **[old source]** | App/online, under R500 | App, **under R500** | App **[unverified]** | Yes |
| **Nedbank** | Branch or phone; all debt settled first | App/online | App/online/phone, 60 days | App/online (PDF/CSV/OFX) | Yes |
| **GoTyme** | Unclear (call/chat) **[unverified]** | Via support **[unverified]** | Phone/email | App (emailed within minutes) | Yes |
| **Discovery** | Phone | App ("suspend") | App | App | Yes |

**Critical process facts:**
- **Stopping a debit order at the bank does not cancel the contract with the company collecting it.**
  - The Code of Banking Practice (s19) expects the customer to **contact the merchant first**, then approach the bank.
  - Disputing a *valid* debit order can get a policy cancelled or an account handed over to collections.
  - Matching DebiCheck collections generally can't be reversed.
  - **This two-sided process (merchant + bank) is exactly what a cross-bank agent can orchestrate and a bank's own assistant can't.**
- **Account closure: banks are legally obliged to help.**
  - The FSCA Conduct Standard for Banks (s10) and the Code of Banking Practice (s26) prohibit "unreasonable barriers" to closing or switching accounts and oblige banks to help.
  - **Switching services** already exist: e.g. Standard Bank's service will close the old account and move debit orders on a signed instruction.
  - So BankBuddy can close an account at Bank A by driving Bank B's switching service, and cite the Conduct Standard when a bank stonewalls.
- **Complaints and the ombud:**
  - The NFO (formerly the banking ombudsman, merged in March 2024) requires the complaint to go to the bank first; the bank gets about 6 weeks.
  - **A representative may lodge a complaint with a written mandate**, and the NFO publishes a sample mandate form.
  - It is free to consumers, with limits of R5m plus up to R50k for distress.
- **Acting on the customer's behalf directly with a bank is hard.**
  - Banks must verify an agent's identity and authority (FIC Act s21) and generally accept only **their own** power-of-attorney forms, often signed in a branch.
  - No bank was found that accepts a standing company mandate for general admin.
- **AI voice calls:** an AI that **pretends to be the customer** to pass call-centre identity checks risks misrepresentation or fraud under the Cybercrimes Act. Voice AI is useful for:
  - navigating phone menus and hold queues, then handing the call over to the user;
  - calling **merchants** openly as the customer's agent.

### What BankBuddy can automate

| Level | Tasks |
|---|---|
| **A: BankBuddy does it end-to-end** | Parse statements and alerts; find unknown, duplicate or rising debit orders; track deadlines (60-day dispute window, 6-week bank response, ombud time limits). **Write and send merchant cancellation letters** (from the user's mailbox). **Draft and lodge bank complaints by email.** **Lodge and follow up ombud complaints as the user's mandated representative.** File POPIA/PAIA access requests. |
| **B: AI prepares everything, the user does 1–2 taps** | Stop or suspend a debit order. Dispute an EFT debit order within 60 days (within app limits). Approve or reject a DebiCheck mandate. Download and forward a stamped statement or letter. Stop a card and make the first fraud report. Close notice or savings accounts in-app. FNB Premier / GoTyme / Discovery chat requests using pre-drafted text. |
| **C: the user must be on a call or in a branch (AI preps, books and coaches)** | Close the main transactional account at most banks. Disputes above the app limits. Fraud cases needing a police affidavit. Signing a bank power of attorney. Anything requiring call-centre identity checks. |

**Conclusion:** the realistic product is **"prepare → one tap → we chase"**, not "fully autonomous agent". The value is still large, because the pain is the **research, drafting, deadlines, follow-up and escalation**, not the final tap.

---

## 8. Regulation and licensing

| Area | Risk | Implication and mitigation |
|---|---|---|
| **FAIS (financial advice and intermediary services)** | 🔴 **Highest.** Bank deposits are "financial products". Recommending that someone **terminate** a product ("close this account, move to X") is **advice**. Acting "on behalf of a client" to **administer or service** a product may be an **intermediary service**. Either needs a licence as a financial services provider (FSP). "Factual information" and "routine administrative queries" are excluded. | Get a legal opinion before launch. Design the MVP as **factual and customer-directed**: "here's what this debit order is, here are your options, you choose." Don't recommend products. Consider an FSP licence or partnering with a licensed FSP before adding recommendations. Track the **COFI Bill** (in Parliament since Apr 2026; it will replace FAIS over about 3 years). |
| **POPIA (data protection)** | 🟡 Account numbers are "unique identifiers", so linking them with data from other parties may need **prior authorisation from the Information Regulator (s57)**. Sending data to offshore AI models raises **cross-border transfer** questions (s72). | Explicit, granular consent. Data minimisation and redaction before AI processing. Choose AI providers with adequate contractual protections. Get an opinion on s57. |
| **Screen scraping and Cybercrimes Act** | 🟡 An untested criminal risk plus a breach of bank terms | **Avoid entirely.** Statements-first strategy (Section 6). |
| **Payments (Directive 2 of 2024 / Authorisation Framework)** | 🟡 Only if BankBuddy initiates payments | Out of MVP scope. Use a registered partner (e.g. Stitch or Ozow) if needed later. |
| **National Credit Act** | 🟢 Low | Applies only to lending or debt counselling. Stay out of both, or partner with registered debt counsellors. |
| **FIC Act (anti-money-laundering) / bank mandates** | 🟡 Banks must verify agents | Use the bank's own forms where representation is needed. Focus BankBuddy's direct representation on merchants and the ombud, where mandates are accepted. |
| **AI-specific regulation** | 🟢 None yet | The draft National AI Policy was withdrawn in Apr 2026. The FSCA prefers "principles rather than rules". A joint SARB/Prudential Authority/FSCA discussion paper on agentic AI is coming, so engage early. |
| **Reputation with the ombud** | 🟡 The NFO's CEO publicly complained (Sep 2026) about **100+ page AI-generated complaints citing court cases that don't exist** | Make **short, factual, evidence-backed complaints** a core design principle. Never cite case law. A human reviews every ombud filing. This could become a positive relationship with the NFO. |

**Tailwinds:** the Conduct Standard for Banks (no unreasonable barriers to closure or switching; banks must help); the Code of Banking Practice; the NFO's acceptance of mandated representatives; and the regulators' stated direction towards open finance.

---

## 9. Business model

**What doesn't work in this category:** free, ad-funded or lead-gen models (Mint, 22seven), selling user data (reputational and POPIA risk), and payday-style lending (Cleo's growth engine, but it drew regulatory action).

**Proposed model to test:**

| Tier | Price (to test) | What's included |
|---|---|---|
| **Free** | R0 | Upload statements; one-off debit-order audit; 60-day deadline alerts; DIY letter templates |
| **Plus** | **R79–R99/month** | Continuous monitoring of all accounts; unlimited cases (cancellations, disputes, complaints, ombud escalation); account-closure concierge; on-demand statements and confirmation letters; fraud-response playbooks |
| **Business** | **R199–R399/month** | The above for business and personal accounts; SARS, VAT and lender document packs; reconciliation help |
| **Per-case packs** (alternative to test) | e.g. about R99 once | "Close my account", "Deceased-estate banking pack", "Fight this debit order" |
| **B2B2C** | Per-employee or per-member | Employers (financial wellness), insurers, Investec/Discovery-style white-label, debt counsellors |

**Notes:**
- **Put the paywall at the moment of need** (when a case starts). Upfront paywalls convert at about **10.7% vs 2.1%** for freemium (RevenueCat), though AI apps retain subscribers worse (21% vs 31% at 12 months).
- **Success fees, e.g. a share of money recovered, are strong elsewhere (Rocket Money's 35–60%) but risky here.** The ombud is free, and the UK brought its "claims management" industry under regulation after abuses. If used at all, cap it and never charge for ombud recoveries.
- **Keep any affiliate revenue small and optional (about 10%, as Emma does).** Never push products; that is how 22seven lost trust.
- **The real cost of service will be human review of cases, not AI running costs.** Measure both in the pilot.

---

## 10. Recommended product shape

**Positioning:** *"Your personal banking admin department. BankBuddy watches every account, catches every rogue debit order, and fights your bank battles, without ever asking for your password."*

**MVP (Debit Order Guard + Case Manager):**
1. **Onboard:** the user forwards the last 3 months of stamped statements from each bank. WhatsApp-first, because that is how South Africans do admin.
2. **Audit:** every debit order across all banks is identified and explained (company, product, since when, price history). Unknown, duplicate, rising and funeral-policy-type debits are flagged.
3. **Act:** for each flagged item, a one-tap flow:
   - a merchant cancellation letter sent from the user's email;
   - a deep link to the exact "stop / suspend / dispute" screen in their bank app;
   - a 60-day countdown.
4. **Chase:** BankBuddy tracks responses, follows up, escalates to the bank's complaints desk, and after the bank's response period files with the NFO as the user's representative (signed mandate).
5. **Monthly ritual:** a "statement day" reminder and a report card: *"You saved R___ this month; 2 cases open; 1 deadline in 9 days."*

**Next (months 4–12):** account-closure concierge (switching-service orchestration, checklists, branch booking, Conduct Standard escalation); on-demand document pack (statements and confirmation letters from all banks in one request); fraud-response playbook; Investec and Nedbank API connections; business tier; first B2B2C pilot.

**Later (2027+):** plug into regulated open-finance APIs as they arrive; payment initiation via a licensed partner; consider an FSP licence to add advice (e.g. "you'd save R1,200/year on fees at bank X").

**Moat:**
- **Process intelligence:** the playbook of what works at each bank and with each debit-order collector, with outcome data.
- **Signed mandates on file:** users have already authorised BankBuddy to act for them.
- **Trust:** the no-passwords stance.
- **Cross-bank neutrality:** no bank can credibly offer it.
- Aggregation itself is not a moat.

---

## 11. 90-day validation plan

| Weeks | Activity | Output |
|---|---|---|
| 1–3 | **25–30 problem interviews** with affluent multi-banked professionals and small-business owners (plus a few "sandwich generation" and deceased-estate cases). **Survey (n ≥ 200).** | Pain ranking, current workarounds, willingness to pay |
| 1–4 | **Legal opinion** scoped on FAIS, POPIA (s57, s72), the Cybercrimes Act and the NFO mandate format | Go/no-go on an execution-only model without an FSP licence; mandate templates |
| 2–4 | **Mystery-shop** account closure, debit-order dispute over app limits, and confirmation-letter requests at all 7 major banks | Fill the **[unverified]** cells in Section 7; first version of the per-bank playbook |
| 3–10 | **Concierge MVP ("Wizard of Oz")**: 30–50 users forward statements via WhatsApp or email; the team, AI-assisted, runs the audit and handles cases end-to-end | Real outcomes: rands saved or recovered, time to resolution, cases per user |
| 6–10 | **Landing-page smoke test** with two to three price points and a paid pre-order | Conversion and price sensitivity |
| 8–12 | **Partnership conversations:** truID (data), Investec (API onboarding), Nedbank API Marketplace, Paymenow or an employer (B2B2C), a debt-counselling firm | Data-coverage plan and first channel partner |

**Proposed go criteria (my suggested thresholds, to be agreed):**
- ≥ 50% of concierge users have at least one debit order they want to stop, cancel or dispute.
- Median annualised waste or recoverable money identified per user ≥ **R1,500**.
- ≥ 30% of interviewees say they'd pay ≥ R79/month, and ≥ 10% of landing-page leads actually pre-pay.
- Cases resolved within the banks' own complaint timelines in most instances.
- The legal opinion confirms a viable model, either without an FSP licence or with a clear licensing path.

**Kill or pivot signals:** audits rarely find anything actionable; users won't forward statements monthly; the legal opinion says every action is an intermediary service needing a full licence (then pivot to B2B2C under a licensed partner).

---

## 12. Open questions and items to verify

- Current account-closure process at Standard Bank, Absa, GoTyme, African Bank and Bank Zero (sources are old or missing).
- FNB in-app statement formats and history. FNB's debit-order page still shows 40 days, pre-dating the 60-day rule.
- Whether any bank accepts a remotely signed power of attorney or a standing third-party mandate.
- truID's data-collection method; whether Stitch still offers a data API; whether Discovery and GoTyme have data APIs.
- Status of the Reserve Bank's Authorisation Framework, the NPS Bill and the FSCA consent framework (expected Q3 2026).
- Average number of accounts and debit orders per affluent adult (no SA source found; measure it in the concierge pilot).
- Vault22's actual pricing and user numbers (sources conflict: 800k / 1m / 2.2m).
- Name check: availability of the "BankBuddy" trademark and domain in SA.

---

## Sources

**Demand and market**
- FinScope Consumer SA 2025: https://finmark.org.za/knowledge-hub/articles/media-release-finscope-consumer-south-africa-2025?entity=blog
- Capitec FY2026 results: https://www.capitecbank.co.za/blog/news/2026/annual-results/
- Bank customer numbers: https://businesstech.co.za/news/banking/876479/battle-of-the-banks-2026-capitec-vs-fnb-vs-standard-bank-vs-absa-vs-nedbank/
- Standard Bank SA 2025 annual report: https://www.standardbank.com/static_file/StandardBankGroup/filedownloads/RTS/2025/SBSA_AnnualReport2025.pdf
- Investec results (Reuters, May 2026): https://www.reuters.com/world/africa/south-africas-investec-reports-marginal-rise-full-year-earnings-2026-05-21/
- NFO 2025 figures: https://www.moonstone.co.za/nfo-recovers-r442-99m-for-consumers-as-complaints-climb/ and https://nfosa.co.za/nfo-banking-division-returns-r60-million-to-consumers-in-2025/
- SABRIC Annual Crime Statistics 2025: https://www.sabric.co.za/wp-content/uploads/2026/08/SABRIC-Annual-Crime-Statistics-Report-2025.pdf
- PayInc Business Report 2025: https://businessreports.payinc.co.za/pdf/PayInc_Business_Report_2025.pdf
- PASA debit-order 60-day FAQ (2026): https://pasa.org.za/wp-content/uploads/2026/04/PASA_DODE_FAQ_v3.pdf and https://netcash.co.za/blog/south-africa-debit-order-dispute-rule-change/
- FAIS Ombud on funeral-policy deductions (Sep 2026): https://www.faisombud.co.za/wp-content/uploads/2026/09/Press-Release-Unauthorised-Funeral-Policy-Deductions-%E2%80%93-SASSA-Grant-Recipients.pdf
- Account closure online (MyBroadband): https://mybroadband.co.za/news/banking/620748-one-thing-most-south-african-banks-will-not-let-you-do-online.html
- UP Customer Experience Index (EWN, Apr 2026): https://www.ewn.co.za/2026/04/21/problem-resolution-clients-biggest-beef-with-sa-banks-index-reveals-customer-experience-ratings
- SARS Tax Statistics 2025: https://www.sars.gov.za/wp-content/uploads/2025taxstats/2025-Tax-Statistics-Highlights.pdf
- BrandMapp: https://telmarhelixa.com/datahub/brandmapp
- FinScope MSME 2024: https://finmark.org.za/knowledge-hub/articles/finscope-msme-south-africa-2024-key-findings-highlight-urgent-need-for-informal-sector-support?entity=blog
- LegalWise premiums 2026: https://www.legalwise.co.za/insurance-cover-benefits-and-premiums-2026
- DataReportal Digital 2026 SA: https://datareportal.com/reports/digital-2026-south-africa

**Competition and comparables**
- 22seven becomes Vault22: https://htxt.co.za/2024/11/22seven-is-now-vault22-offering-financial-wellness-to-all/
- Maya on Money, "What happened to 22seven" (News24): https://www.news24.com/business/money/maya-on-money-what-happened-to-22seven-20241125
- Bank budgeting tools overview (Jul 2026): https://smartaboutmoney.co.za/hot-topics/let-your-bank-track-your-budget/
- Absa Abby 1.6m users: https://techafricanews.com/2026/08/20/absas-ai-chatbot-reaches-1-6-million-users-as-it-spending-rises-7-percent/
- Discovery Bank strategy: https://www.moonstone.co.za/discovery-bank-enters-next-phase-of-super-bank-strategy/
- FNB NAVi: https://www.itnewsafrica.com/2026/04/fnb-upgrades-navi-virtual-assistant-to-strengthen-advisor-led-services/
- AI-generated complaints warning (EWN, Sep 2026): https://www.ewn.co.za/ai-generated-complaints-creating-new-challenges-for-financial-ombuds-in-south-africa/
- Rocket Money acquisition: https://www.rocketcompanies.com/press-release/rocket-companies-to-acquire-truebill-adding-rapidly-expanding-financial-empowerment-fintech-to-the-rocket-platform/
- Rocket Money pricing: https://www.rocketmoney.com/learn/personal-finance/how-much-does-rocket-money-cost
- Mint shutdown (CNBC): https://www.cnbc.com/2023/11/07/budgeting-app-mint-is-shutting-down-users-are-disappointed.html
- Yolt closure (ING): https://ing.com/news/2021/09/yolt-to-focus-on-growth-of-yolt-technology-services-as-it-intends-to-close-its-smart-money-app.html
- Emma: https://www.fintechgrowthinsider.com/p/edoardo-moreni-emma
- Snoop / Vanquis: https://www.vanquis.com/investors/annual-report/chief-executive-officer-review/
- Cleo 2025 annual report: https://web.meetcleo.com/2025-annual-report
- Cleo FTC settlement: https://www.ftc.gov/news-events/news/press-releases/2025/03/cash-advance-company-cleo-ai-agrees-pay-17-million-result-ftc-lawsuit-charging-it-deceives-consumers
- DoNotPay FTC order: https://www.ftc.gov/news-events/news/press-releases/2025/02/ftc-finalizes-order-donotpay-prohibits-deceptive-ai-lawyer-claims-imposes-monetary-relief-requires
- ChatGPT personal finance: https://openai.com/index/personal-finance-chatgpt/
- Subscription app benchmarks (RevenueCat): https://www.revenuecat.com/state-of-subscription-apps
- Finance app retention benchmarks: https://www.businessofapps.com/data/finance-app-benchmarks/

**Regulation and data access**
- SARB open-banking consultation paper (2020): https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/regulation-oversight/Consultation%20Paper%20on%20open%20banking.pdf
- SARB NPS Regulatory and Oversight Report 2025/26: https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/regulation-oversight-and-supervision/regulatory-and-oversight-reports/NPS%20Regulatory%20and%20Oversight%20Report%202025-2026.pdf
- SARB Working Paper WP/26/07: https://www.resbank.co.za/content/dam/sarb/publications/working-papers/2026/26-07/financial-inclusion-sa.pdf
- FSCA Regulation Plan 2026–29 (Clyde & Co): https://www.clydeco.com/en/insights/2026/07/the-fsca-has-published-its-three-year-regulation-p
- Directive 2 of 2024 on screen scraping for payments: https://www.werksmans.com/legal-updates-and-opinions/the-south-african-reserve-bank-tightens-instant-payment-framework-in-south-africa-screen-scrapers-beware/
- Standard Bank digital banking T&Cs: https://www.standardbank.co.za/static_file/South%20Africa/PDF/Personal%20Ts%20and%20Cs/Digital_Banking_terms_and_conditions.pdf
- Cybercrimes Act 19 of 2020: https://lawlibrary.org.za/akn/za/act/2020/19/eng@2021-06-01
- Investec third-party API access: https://developer.investec.com/third-parties
- Nedbank API Marketplace (account access consents): https://apim.nedbank.co.za/static/docs/accounts-intent
- truID: https://www.truid.co.za/
- FAIS Act: https://www.saflii.org/za/legis/consol_act/faaisa2002423/
- COFI Bill introduced (Apr 2026): https://www.horizoncompliance.co.za/complianceblog/the-cofi-bill-has-been-introduced-to-parliament-heres-what-we-know-so-far
- FSCA Conduct Standard for Banks: https://lawlibrary.org.za/akn/za/act/standard/fsca/2020/3/eng@2020-07-03
- Code of Banking Practice (Jul 2025): https://www.capitecbank.co.za/globalassets/pages/documents-library/general/code-of-banking-practice-july-2025.pdf
- POPIA prior authorisation guidance: https://inforegulator.org.za/wp-content/uploads/2020/07/InfoRegSA-GuidanceNote-PriorAuthorisation-20210311-1.pdf
- NFO how to complain / rules: https://www.nfosa.co.za/how-to-complain/ and https://ombudcouncil.org.za/wp-content/uploads/2024/02/NFO-Scheme-Rules-Final-approved-version-published-on-Ombud-Council-website.23-February-2024.pdf
- FIC Act: https://www.saflii.org/za/legis/consol_act/fica382001243/
- FSCA stance on AI rules (Sep 2026): https://mybroadband.co.za/news/ai/668243-south-african-financial-regulator-holds-back-on-ai-rules.html

**Bank processes**
- Capitec debit-order disputes: https://www.capitecbank.co.za/were-here-to-help/how-to/how-to-dispute-a-debit-order/
- Capitec statements by email: https://www.capitecbank.co.za/were-here-to-help/how-to/how-to-email-statements-from-your-phone/
- FNB fraud and disputes: https://www.fnb.co.za/security-centre/fraud-and-disputes.html
- FNB account closure guide (2019): https://www.fnb.co.za/downloads/AccountClosureGuide/FNB_Transactional_Account_Closure_Guide.pdf
- Standard Bank stop debit orders: https://www.standardbank.co.za/southafrica/personal/learn/how-to-stop-debit-orders
- Standard Bank documents: https://www.standardbank.co.za/southafrica/personal/products-and-services/ways-to-bank/help-centre/bank-account-documents
- Standard Bank switching service: https://www.standardbank.co.za/southafrica/personal/products-and-services/bank-with-us/bank-accounts/switch-your-bank-account
- Standard Bank complaints: https://www.standardbank.co.za/southafrica/personal/about-us/regulatory/complaints-process
- Absa stop/reverse debit orders: https://onlinebanking.help.absa.co.za/en/help/debicheck-and-debit-orders/my-debit-orders/step-1/how-do-i-reverse-or-stop-a-debit-order/
- Nedbank account closure: https://personal.nedbank.co.za/legal/account-closures-and-termination-of-agreements.html
- Nedbank debit-order disputes: https://personal.nedbank.co.za/learn/help-centre/bank/dispute-debit-order.html
- Discovery Bank account management: https://www.discovery.co.za/bank/info-and-tips-managing-your-accounts
- GoTyme FAQs: https://gotyme.co.za/personal/help/faqs
- PASA debit-order FAQ (2024): https://pasa.org.za/wp-content/uploads/2024/08/Debit-Order-FAQ-1.pdf
