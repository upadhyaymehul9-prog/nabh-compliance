"""
Run this on SERVER, inside the nabh-compliance folder:

    cd C:\\Users\\SERVER\\Desktop\\nabh-compliance
    python make_hrm_ims_sql.py

Fixed version: skips the «Hospital Name» placeholder line (which sits
first in every master, probably a letterhead line) and takes the next
real paragraph as the title. Also prints the first few paragraphs of
each file so you and Claude can both sanity-check the guess.

Prints only — touches nothing in Supabase.
"""

import os
from docx import Document

MASTERS_DIR = os.path.join("policies", "build", "masters")
PLACEHOLDER = "«Hospital Name»"

CODES = [f"HRM.{i}" for i in range(1, 10)] + [f"IMS.{i}" for i in range(1, 7)]
CHAPTER_OF = lambda code: code.split(".")[0]


def get_paragraphs(path, limit=6):
    doc = Document(path)
    out = []
    for p in doc.paragraphs:
        text = p.text.strip()
        if text:
            out.append(text)
        if len(out) >= limit:
            break
    return out


def guess_title(paragraphs):
    for text in paragraphs:
        if PLACEHOLDER not in text and text.strip():
            return text
    return "(no non-placeholder text found in first paragraphs)"


def sql_escape(s):
    return s.replace("'", "''")


rows = []
missing = []

print("-- DEBUG: first few paragraphs per file, so we can verify the title guess --\n")

for code in CODES:
    fname = f"{code}_v2_master.docx"
    fpath = os.path.join(MASTERS_DIR, fname)
    if not os.path.exists(fpath):
        missing.append(fname)
        continue
    paras = get_paragraphs(fpath)
    title = guess_title(paras)
    rows.append((code, CHAPTER_OF(code), title, fname))
    print(f"{code} ({fname}):")
    for i, p in enumerate(paras):
        marker = "  <- guessed title" if p == title else ""
        print(f"    [{i}] {p}{marker}")
    print()

if missing:
    print("!! MISSING FILES:")
    for m in missing:
        print("   ", m)
    print()

print(f"-- Guessed {len(rows)} of {len(CODES)} titles. CHECK THE ABOVE BEFORE TRUSTING THIS SQL. --\n")

print("INSERT INTO shco_policy_masters")
print("  (standard_code, chapter, policy_title, master_docx_path,")
print("   oe_codes, purpose, scope, policy_statement, procedure_steps,")
print("   responsibility, references_text, distribution)")
print("VALUES")

lines = []
for code, chapter, title, fname in rows:
    t = sql_escape(title)
    lines.append(
        f"  ('{code}', '{chapter}', '{t}', '{fname}',\n"
        f"   '{{}}', 'Delivered via v2 master document.', "
        f"'Delivered via v2 master document.', 'Delivered via v2 master document.',\n"
        f"   '{{}}', 'Delivered via v2 master document.', "
        f"'Delivered via v2 master document.', 'Delivered via v2 master document.')"
    )
print(",\n".join(lines) + "\n")
print("ON CONFLICT (standard_code) DO UPDATE")
print("  SET master_docx_path = EXCLUDED.master_docx_path,")
print("      policy_title     = EXCLUDED.policy_title;")
