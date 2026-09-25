#!/usr/bin/env python3
"""Pull the PDF statements out of one saved Gmail message and unlock them.

Usage: extract_statement.py <saved-get_message-RAW-result> <out-dir>

The input is the Gmail connector's get_message(messageFormat="RAW") result,
as Claude Code saves a large tool result to a file. Each PDF attachment is
decrypted with the passwords in BANKBUDDY_CAPITEC_ACCOUNTS,
BANKBUDDY_FNB_PASSWORD and BANKBUDDY_OTHER_PASSWORDS (comma or newline
separated) and its text is written to <out-dir>/<n>.txt, one
"--- page N ---" block per page.

Prints one JSON line per PDF with its status only. Never prints statement
text, passwords or account numbers.
"""
import base64
import email
import io
import json
import os
import re
import sys
from email import policy

from pypdf import PdfReader

PASSWORD_VARS = ("BANKBUDDY_CAPITEC_ACCOUNTS", "BANKBUDDY_FNB_PASSWORD", "BANKBUDDY_OTHER_PASSWORDS")


def load_raw(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r'"raw"\s*:\s*"([A-Za-z0-9_\-=]+)"', text)
    if not m:
        sys.exit(json.dumps({"error": "no raw field in " + path}))
    return m.group(1)


def b64url(s):
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def pdf_parts(message_bytes):
    msg = email.message_from_bytes(message_bytes, policy=policy.default)
    for part in msg.walk():
        if part.is_multipart():
            continue
        name = part.get_filename() or ""
        if part.get_content_type() == "application/pdf" or name.lower().endswith(".pdf"):
            data = part.get_payload(decode=True)
            if data and data[:4] == b"%PDF":
                yield name or "statement.pdf", data


def passwords():
    out = []
    for var in PASSWORD_VARS:
        for p in re.split(r"[\s,;]+", os.environ.get(var, "")):
            if p and p not in out:
                out.append(p)
    return out


def open_pdf(data):
    """Return (pages, was_locked); pages is None when no password worked."""
    reader = PdfReader(io.BytesIO(data))
    if not reader.is_encrypted:
        return [p.extract_text() or "" for p in reader.pages], False
    for pw in [""] + passwords():
        reader = PdfReader(io.BytesIO(data))
        try:
            if reader.decrypt(pw):
                return [p.extract_text() or "" for p in reader.pages], True
        except Exception:
            continue
    return None, True


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    message = b64url(load_raw(src))
    found = 0
    for i, (name, data) in enumerate(pdf_parts(message), 1):
        found += 1
        pages, locked = open_pdf(data)
        status = {"pdf": i, "filename": name, "locked": locked, "unlocked": pages is not None}
        if pages is not None:
            path = os.path.join(out_dir, f"{i}.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(f"--- page {n} ---\n{t}" for n, t in enumerate(pages, 1)))
            status.update(pages=len(pages), chars=sum(len(t) for t in pages), text_file=path)
        print(json.dumps(status))
    if not found:
        print(json.dumps({"pdf": 0, "note": "no PDF attachment in this message"}))


if __name__ == "__main__":
    main()
