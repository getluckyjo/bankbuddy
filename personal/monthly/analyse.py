#!/usr/bin/env python3
"""Summarise BankBuddy's saved data for the monthly check.

Usage: analyse.py <statements-dir> [<cases-dir>] [<settings-json>]

Reads the statement (and case) documents that ArtifactData saved with
out_dir, applies the same rules as the BankBuddy page (bankbuddy.html:
dedupeWithin, allTransactions, analyse) and prints a short Markdown
summary: what needs a look, debit orders still inside the 60-day dispute
window, open cases with deadlines, and the monthly total.
"""
import glob
import json
import os
import re
import sys
from datetime import date, timedelta

DISPUTE_DAYS = 60
TODAY = date.today()


def load_docs(folder):
    docs = []
    for path in sorted(glob.glob(os.path.join(folder, "*.json"))):
        raw = json.load(open(path, encoding="utf-8"))
        body = raw.get("data", raw) if isinstance(raw, dict) else raw
        if isinstance(body, dict):
            body = dict(body)
            body.setdefault("id", os.path.splitext(os.path.basename(path))[0])
            docs.append(body)
    return docs


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


def d(s):
    try:
        return date.fromisoformat(str(s)[:10])
    except ValueError:
        return None


def money(n):
    return ("−R" if n < 0 else "R") + f"{abs(n):,.2f}"


def dedupe_within(txs):
    """Same date, amount and company with different wording is one charge."""
    seen, out = {}, []
    for t in txs:
        k = f"{t['date']}|{t['amount']}|{norm(t.get('merchant'))[:60]}"
        text = norm(t.get("description"))
        if k in seen and text not in seen[k]:
            continue
        seen.setdefault(k, []).append(text)
        out.append(t)
    return out


def all_transactions(statements):
    by_acct = {}
    for s in statements:
        by_acct.setdefault((s.get("bank"), s.get("accountLast4")), []).append(s)
    out = []
    for sts in by_acct.values():
        def span(s):
            ds = sorted(t["date"] for t in s.get("transactions", []) if t.get("date"))
            return (s.get("periodStart") or (ds[0] if ds else ""), s.get("periodEnd") or (ds[-1] if ds else ""))

        def length(s):
            a, b = (d(x) for x in span(s))
            return (b - a).days if a and b else 10 ** 6

        sts.sort(key=lambda s: (length(s), span(s)[1]))
        covered = []
        for s in sts:
            for t in dedupe_within(s.get("transactions", [])):
                if any(a <= t["date"] <= b for a, b in covered):
                    continue
                out.append(dict(t, bank=s.get("bank"), last4=s.get("accountLast4")))
            a, b = span(s)
            if a and b:
                covered.append((a, b))
    return sorted(out, key=lambda t: t["date"])


def analyse(statements, settings):
    txs = [t for t in all_transactions(statements) if t.get("amount", 0) < 0]
    groups = {}
    for t in txs:
        fam = "debit" if t.get("kind") == "debit_order" else "card" if t.get("kind") in ("card_subscription", "card_purchase") else None
        if not fam:
            continue
        g = groups.setdefault(f"{fam}:{norm(t.get('merchant') or t.get('description'))[:60]}",
                              {"fam": fam, "merchant": t.get("merchant") or t.get("description"), "charges": [], "sub": False})
        g["charges"].append(t)
        g["sub"] |= t.get("kind") == "card_subscription"

    def coverage_start(bank, last4):
        vals = [s["periodStart"] for s in statements if s.get("bank") == bank and s.get("accountLast4") == last4 and s.get("periodStart")]
        return min(vals) if vals else None

    def latest_end(bank, last4):
        vals = [s["periodEnd"] for s in statements if s.get("bank") == bank and s.get("accountLast4") == last4 and s.get("periodEnd")]
        return max(vals) if vals else None

    decisions = (settings or {}).get("decisions") or {}
    result = []
    for key, g in groups.items():
        ch = sorted(g["charges"], key=lambda c: c["date"])
        months = sorted({c["date"][:7] for c in ch})
        if g["fam"] == "card":
            amts = [abs(c["amount"]) for c in ch]
            similar = sum(1 for a in amts if abs(a - amts[-1]) <= max(5, amts[-1] * 0.15))
            if not g["sub"] and not (len(months) >= 2 and similar >= 2 and len(ch) / len(months) <= 1.5):
                continue
        last = ch[-1]
        prev = next((c for c in reversed(ch[:-1]) if c["date"][:7] != last["date"][:7]), None)
        g.update(key=key, last=last, amount=abs(last["amount"]), prev=abs(prev["amount"]) if prev else None,
                 account=f"{last.get('bank')} ··{last.get('last4')}", flags=[])
        cov, first = coverage_start(last.get("bank"), last.get("last4")), ch[0]
        if cov and (d(first["date"]) - d(cov)).days >= 40 and (TODAY - d(first["date"])).days <= 75:
            g["flags"].append("new")
        for a, b in zip(ch, ch[1:]):
            if abs(a["amount"] - b["amount"]) < 0.01 and (d(b["date"]) - d(a["date"])).days <= 5 and (TODAY - d(b["date"])).days <= 120:
                g["flags"].append("double")
                g["double_date"] = b["date"]
                break
        if g["prev"] and g["amount"] > g["prev"] * 1.02 and g["amount"] - g["prev"] >= 2:
            g["flags"].append("price_up")
        if g["fam"] == "debit":
            left = [DISPUTE_DAYS - (TODAY - d(c["date"])).days for c in ch if (TODAY - d(c["date"])).days <= DISPUTE_DAYS]
            g["days_left"] = min(left) if left else None
        end = latest_end(last.get("bank"), last.get("last4"))
        g["stopped"] = bool(end and (d(end) - d(last["date"])).days > 50)
        g["keep"] = decisions.get(key) == "keep"
        result.append(g)
    return result


def summary(statements, cases, settings):
    groups = analyse(statements, settings)
    active = [g for g in groups if not g["stopped"]]
    look = [g for g in active if g["flags"] and not g["keep"]]
    lines = []
    total = sum(g["amount"] for g in active)
    lines.append(f"**Debit orders and subscriptions:** {len(active)} active, about {money(total)} a month.")
    if look:
        lines.append("")
        lines.append(f"**Needs a look ({len(look)}):**")
        for g in sorted(look, key=lambda g: -g["amount"]):
            why = []
            if "new" in g["flags"]:
                why.append(f"new since {g['charges'][0]['date']}")
            if "double" in g["flags"]:
                why.append(f"same amount taken twice around {g['double_date']}")
            if "price_up" in g["flags"]:
                why.append(f"up from {money(g['prev'])} to {money(g['amount'])}")
            window = f", {g['days_left']} days left to dispute" if g.get("days_left") is not None else ""
            kind = "debit order" if g["fam"] == "debit" else "subscription"
            lines.append(f"- {g['merchant']} ({kind}, {g['account']}): {money(-g['amount'])}; {'; '.join(why)}{window}")
    else:
        lines.append("Nothing new, doubled or pricier this month.")
    open_cases = [c for c in cases if c.get("status") not in ("resolved", "closed")]
    due = []
    for c in open_cases:
        if c.get("fam") == "debit" and c.get("lastDate") and d(c["lastDate"]):
            left = DISPUTE_DAYS - (TODAY - d(c["lastDate"])).days
            if 0 < left <= 14:
                due.append(f"- {c.get('merchant')}: dispute with {c.get('bank')} within {left} days")
    if open_cases:
        lines.append("")
        lines.append(f"**Open cases:** {len(open_cases)}")
        lines.extend(due)
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    statements = load_docs(sys.argv[1])
    cases = load_docs(sys.argv[2]) if len(sys.argv) > 2 and os.path.isdir(sys.argv[2]) else []
    settings = {}
    if len(sys.argv) > 3 and os.path.isfile(sys.argv[3]):
        raw = json.load(open(sys.argv[3], encoding="utf-8"))
        settings = raw.get("data", raw) if isinstance(raw, dict) else {}
    print(summary(statements, cases, settings))


if __name__ == "__main__":
    main()
