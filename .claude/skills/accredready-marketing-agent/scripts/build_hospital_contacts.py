#!/usr/bin/env python3
"""
Extract publicly listed hospital contact emails from government empanelment lists.

Sources (all public, government-published):
- PMJAY national hospital list (NHA) — bundled text extract
- Haryana AB-PMJAY district PDFs (22 districts, live download)

Output: data/hospital-contacts-public.csv

Usage:
  python3 .claude/skills/accredready-marketing-agent/scripts/build_hospital_contacts.py
  python3 .../build_hospital_contacts.py --no-download   # skip Haryana PDF fetch
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "hospital-contacts-public.csv"
PMJAY_SOURCE = ROOT / "data" / "sources" / "pmjay-nha-extract.txt"

EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
    re.I,
)

STATES = {
    "ANDAMAN AND NICOBAR ISLANDS", "ANDHRA PRADESH", "ARUNACHAL PRADESH",
    "ASSAM", "BIHAR", "CHANDIGARH", "CHHATTISGARH", "DADRA AND NAGAR HAVELI",
    "DAMAN AND DIU", "DELHI", "GOA", "GUJARAT", "HARYANA", "HIMACHAL PRADESH",
    "JAMMU AND KASHMIR", "JHARKHAND", "KARNATAKA", "KERALA", "LADAKH",
    "LAKSHADWEEP", "MADHYA PRADESH", "MAHARASHTRA", "MANIPUR", "MEGHALAYA",
    "MIZORAM", "NAGALAND", "ODISHA", "PUDUCHERRY", "PUNJAB", "RAJASTHAN",
    "SIKKIM", "TAMIL NADU", "TELANGANA", "TRIPURA", "UTTAR PRADESH",
    "UTTARAKHAND", "WEST BENGAL",
}

PHONE_RE = re.compile(r"\b[6-9]\d{9}\b|\b0\d{10,11}\b|\b1[89]\d{9}\b")

BAD_LOCAL = re.compile(
    r"^(0|1|2|9|11|18|14|a|aa|aaa|test|na|info|admin|contact)$",
    re.I,
)

HARYANA_DISTRICTS = [
    ("Ambala", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/20251219636779206.pdf"),
    ("Bhiwani", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2026/03/202603171263094101.pdf"),
    ("Charki Dadri", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191982485429.pdf"),
    ("Faridabad", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/20251219286405504.pdf"),
    ("Fatehabad", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191376671891.pdf"),
    ("Gurugram", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/20251219137455268.pdf"),
    ("Hisar", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191699068062.pdf"),
    ("Jhajjar", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191757371609.pdf"),
    ("Jind", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191155448641.pdf"),
    ("Kaithal", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2026/04/202604031989511076.pdf"),
    ("Karnal", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/20251219416725671.pdf"),
    ("Kurukshetra", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/20251219403653582.pdf"),
    ("Mahendragarh", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191849599284.pdf"),
    ("Mewat", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/20251219580570351.pdf"),
    ("Palwal", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191933776557.pdf"),
    ("Panchkula", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191935101544.pdf"),
    ("Panipat", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191706886760.pdf"),
    ("Rewari", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191257605822.pdf"),
    ("Rohtak", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/2025121933909373.pdf"),
    ("Sirsa", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/20251219138417912.pdf"),
    ("Sonipat", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/202512191603243912.pdf"),
    ("Yamuna Nagar", "https://cdnbbsr.s3waas.gov.in/s3169779d3852b32ce8b1a1724dbf5217d/uploads/2025/12/20251219699138290.pdf"),
]

HOSP_BLOCK_RE = re.compile(
    r"(HOSP[A-Z0-9]+)\s+(.+?)\s+(?:Government|Private)\s+.+?"
    r"(\d{10,11})\s+(" + EMAIL_RE.pattern + r")",
    re.I | re.S,
)


def clean_email(raw: str) -> str | None:
    e = raw.lower().strip().strip(".")
    if "@" not in e or len(e) < 8 or ".." in e:
        return None
    local, domain = e.rsplit("@", 1)
    if BAD_LOCAL.match(local) or len(local) < 3:
        return None
    if domain in ("gmail.co", "yahoo.co", "rediffmail.co"):
        return None
    if local.endswith("gm") or domain.startswith("ail."):
        return None
    return e


def normalize_pmjay_text(text: str) -> str:
    text = text.replace("@gm\nail.com", "@gmail.com")
    text = text.replace("@gm ail.com", "@gmail.com")
    text = text.replace("@rediff\nmail.com", "@rediffmail.com")
    text = text.replace("@rediff mail.com", "@rediffmail.com")
    text = text.replace("@yahoo.\nco.in", "@yahoo.co.in")
    text = text.replace("@yahoo. co.in", "@yahoo.co.in")
    text = text.replace("@gmail.\ncom", "@gmail.com")
    # join lines where email was split: foo@bar + .com on next line
    text = re.sub(
        r"([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+)\n([a-z]{2,}\.[a-z]{2,})",
        r"\1\2",
        text,
        flags=re.I,
    )
    return text


def parse_pmjay_text(text: str) -> list[dict]:
    rows: list[dict] = []
    text = normalize_pmjay_text(text)
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("State District"):
            continue
        upper = line.upper()
        state = None
        rest = line
        for st in sorted(STATES, key=len, reverse=True):
            if upper.startswith(st + " "):
                state = st.title()
                rest = line[len(st):].strip()
                break
        if not state:
            continue
        emails = EMAIL_RE.findall(line)
        emails = [clean_email(e) for e in emails]
        emails = [e for e in emails if e]
        if not emails:
            continue
        email = emails[0]
        phones = PHONE_RE.findall(line)
        frag = EMAIL_RE.sub("", line)
        frag = PHONE_RE.sub("", frag)
        rest_parts = rest.split()
        district = rest_parts[0] if rest_parts else ""
        hospital = " ".join(rest_parts[1:]).strip() if len(rest_parts) > 1 else rest
        hospital = re.sub(r"\s+", " ", hospital)[:120]
        rows.append({
            "source": "PMJAY_NHA",
            "state": state,
            "district": district.title(),
            "hospital_name": hospital[:120] if hospital else "Unknown",
            "contact_name": "",
            "contact_role": "Nodal Officer (PMJAY)",
            "email": email,
            "phone": phones[0] if phones else "",
            "email_type": "nodal_officer",
            "notes": "Public PMJAY empanelment list (NHA) — facility/nodal inbox",
        })
    return rows


def parse_haryana_pdf_text(text: str, district: str) -> list[dict]:
    rows: list[dict] = []
    text = normalize_pmjay_text(text)
    text = re.sub(r"\s+", " ", text)

    for m in HOSP_BLOCK_RE.finditer(text):
        hosp_id, name, phone, email_raw = m.groups()
        email = clean_email(email_raw)
        if not email:
            continue
        name = re.sub(r"\s+", " ", name).strip()[:120]
        rows.append({
            "source": "PMJAY_HARYANA",
            "state": "Haryana",
            "district": district,
            "hospital_name": name or "AB-PMJAY empanelled HCO",
            "contact_name": "",
            "contact_role": "Hospital Nodal Officer (PMJAY)",
            "email": email,
            "phone": phone,
            "email_type": "nodal_officer",
            "notes": f"Public Haryana AB-PMJAY list — {district}",
        })

    # Fallback: any remaining emails with nearby HOSP id
    seen = {r["email"] for r in rows}
    for email_raw in EMAIL_RE.findall(text):
        email = clean_email(email_raw)
        if not email or email in seen:
            continue
        pos = text.lower().find(email)
        window = text[max(0, pos - 200):pos]
        hosp_m = re.search(r"HOSP[A-Z0-9]+\s+([^0-9]{5,80})", window, re.I)
        name = hosp_m.group(1).strip() if hosp_m else "AB-PMJAY empanelled HCO"
        rows.append({
            "source": "PMJAY_HARYANA",
            "state": "Haryana",
            "district": district,
            "hospital_name": name[:120],
            "contact_name": "",
            "contact_role": "Hospital Nodal Officer (PMJAY)",
            "email": email,
            "phone": "",
            "email_type": "nodal_officer",
            "notes": f"Public Haryana AB-PMJAY list — {district}",
        })
        seen.add(email)
    return rows


def fetch_pdf_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 AccredReady/1.0"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = resp.read()
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SystemExit("pypdf required: pip install pypdf") from exc
    reader = PdfReader(io.BytesIO(data))
    return "".join(page.extract_text() or "" for page in reader.pages)


def dedupe(rows: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for r in rows:
        key = r["email"].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Build public hospital contact CSV")
    parser.add_argument("--no-download", action="store_true", help="Skip Haryana PDF downloads")
    args = parser.parse_args()

    all_rows: list[dict] = []

    if PMJAY_SOURCE.exists():
        all_rows.extend(parse_pmjay_text(PMJAY_SOURCE.read_text(errors="ignore")))
    else:
        print(f"Warning: missing {PMJAY_SOURCE}", file=sys.stderr)

    if not args.no_download:
        for district, url in HARYANA_DISTRICTS:
            try:
                text = fetch_pdf_text(url)
                all_rows.extend(parse_haryana_pdf_text(text, district))
            except (urllib.error.URLError, OSError, ValueError) as exc:
                print(f"Warning: {district} failed: {exc}", file=sys.stderr)

    all_rows = dedupe(all_rows)
    all_rows.sort(key=lambda r: (r["state"], r["district"], r["hospital_name"]))

    fields = [
        "id", "source", "state", "district", "hospital_name",
        "contact_name", "contact_role", "email", "phone", "email_type", "notes",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, r in enumerate(all_rows, 1):
            r["id"] = f"H{i:04d}"
            w.writerow({k: r.get(k, "") for k in fields})

    summary = {
        "output": str(OUT),
        "total_rows": len(all_rows),
        "unique_emails": len({r["email"] for r in all_rows}),
        "by_source": {
            s: sum(1 for r in all_rows if r["source"] == s)
            for s in sorted({r["source"] for r in all_rows})
        },
        "usage_note": (
            "Facility/nodal officer emails from government PMJAY lists. "
            "Not personal QM inboxes. Use targeted outreach only; comply with DPDP Act."
        ),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
