#!/usr/bin/env python3
"""
Build a *useful* private-hospital contact list for AccredReady outreach.

Unlike the PMJAY nodal list (mostly PHC/BMO inboxes), this script combines:

1. Private / multispecialty hospitals from PMJAY (filtered — no PHC/CHC)
2. NABH-accredited hospitals from cghshospitals.com public API (phone + address)
3. Contact emails scraped from major hospital chain websites (public contact pages)

Output: data/private-hospital-contacts.csv

Usage:
  pip install pypdf   # only if you also run build_hospital_contacts.py
  python3 .claude/skills/accredready-marketing-agent/scripts/build_private_hospital_contacts.py
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PMJAY_CSV = ROOT / "data" / "hospital-contacts-public.csv"
OUT = ROOT / "data" / "private-hospital-contacts.csv"

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", re.I)

SKIP_NAME = re.compile(
    r"\b(PHC|CHC|SDH|Sub.?Division|Primary Health|Community Health|Ayushman Bharat HWC|"
    r"Health and Wellness|UPHC|HWC|PHSC|RBSY|Rural Hospital|Taluka Hospital|Block Hospital|"
    r"Sub Centre|Subcentre|Dispensary|Ayurvedic Hospital|Homeopathic|Unani|Siddha)\b",
    re.I,
)
SKIP_EMAIL = re.compile(r"\b(phc|chc|bmo|mophc|smo|sdh|hwc|uphc|rbsy)\b", re.I)
PRIVATE_MARKERS = re.compile(
    r"\b(Pvt\.?|Private|Ltd\.?|Limited|Multispecialty|Multi.?Speciality|Super.?Speciality|"
    r"Superspeciality|Nursing Home|Healthcare|Health Care|Medical Centre|Medical Center|"
    r"Hospital and Research|Trauma Centre|Trauma Center|Memorial|Institute)\b",
    re.I,
)

CHAIN_CONTACT_PAGES = [
    ("Manipal Hospitals", "Pan-India", "https://www.manipalhospitals.com/contact-us/"),
    ("KIMS Health", "Kerala/South", "https://www.kimshealth.org/contact-us/"),
    ("Noble Hospital", "Pune", "https://www.noblehospital.co.in/contact-us/"),
    ("Omega Hospitals", "Bengaluru", "https://www.omegahospitals.com/contact/"),
    ("Yashoda Hospitals", "Hyderabad", "https://www.yashodahospitals.com/contact-us/"),
    ("KIMS Hospitals Hyderabad", "Hyderabad", "https://www.kimshospitals.com/contact-us/"),
    ("Rainbow Hospitals", "Hyderabad", "https://www.rainbowhospitals.in/contact-us"),
    ("Aster Hospitals", "Pan-India", "https://www.asterhospitals.in/contact-us"),
    ("HCG Oncology", "Pan-India", "https://www.hcgoncology.com/contact-us/"),
    ("Lilavati Hospital", "Mumbai", "https://www.lilavatihospital.com/contact"),
    ("Breach Candy Hospital", "Mumbai", "https://www.breachcandyhospital.org/contact-us"),
    ("Medanta", "Gurugram", "https://www.medanta.org/contact-us/"),
    ("Paras Hospitals", "Pan-India", "https://www.parashospitals.com/contact-us"),
    ("Shalby Hospitals", "Gujarat", "https://www.shalby.org/contact-us/"),
    ("Metro Hospitals", "Delhi NCR", "https://www.metrohospitals.com/contact-us"),
]

SKIP_EMAIL_FRAG = ("wixpress", "sentry", "webpack", "cloudflare", "example", "glitchtip", "facebook")


def clean_email(raw: str) -> str | None:
    e = raw.lower().strip().strip(".")
    if "@" not in e or len(e) < 8:
        return None
    if any(f in e for f in SKIP_EMAIL_FRAG):
        return None
    local, domain = e.rsplit("@", 1)
    if domain in ("gmail.co", "yahoo.co"):
        return None
    if local in ("na", "info", "admin", "contact") and domain.endswith(".nic.in"):
        return None
    return e


def fetch_url(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 AccredReady/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_state_from_address(address: str | None) -> str:
    if not address:
        return ""
    # Indian addresses usually end with "..., State PIN, India"
    m = re.search(r",\s*([A-Za-z &]+),\s*\d{6},\s*India", address)
    if m:
        return m.group(1).strip().title()
    return ""


def load_private_pmjay_rows() -> list[dict]:
    if not PMJAY_CSV.exists():
        return []
    rows: list[dict] = []
    with PMJAY_CSV.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            name = r.get("hospital_name", "")
            email = r.get("email", "")
            if SKIP_NAME.search(name) or SKIP_EMAIL.search(email):
                continue
            if not PRIVATE_MARKERS.search(name):
                continue
            ce = clean_email(email)
            if not ce:
                continue
            rows.append({
                "source": "PMJAY_PRIVATE",
                "tier": "A",
                "state": r.get("state", ""),
                "city": r.get("district", ""),
                "hospital_name": name[:120],
                "contact_role": "Hospital admin / nodal (private)",
                "email": ce,
                "phone": r.get("phone", ""),
                "website_source": "",
                "notes": "Private/multispecialty from PMJAY empanelment — ask for Quality/NABH desk",
            })
    return rows


def fetch_nabh_hospitals() -> list[dict]:
    rows: list[dict] = []
    offset = 0
    limit = 100
    total = None
    while total is None or offset < total:
        url = (
            "https://cghshospitals.com/api/facilities?"
            f"accreditation=nabh&category=hospital&limit={limit}&offset={offset}"
        )
        try:
            data = json.loads(fetch_url(url))
        except (urllib.error.URLError, json.JSONDecodeError) as exc:
            print(f"Warning: NABH API offset {offset}: {exc}", file=sys.stderr)
            break
        total = data["pagination"]["total"]
        for item in data["data"]:
            state = parse_state_from_address(item.get("address", ""))
            rows.append({
                "source": "NABH_CGHS_REGISTRY",
                "tier": "B",
                "state": state,
                "city": item.get("city", ""),
                "hospital_name": item.get("name", "")[:120],
                "contact_role": "NABH-accredited hospital (find QM on LinkedIn)",
                "email": "",
                "phone": item.get("phone", ""),
                "website_source": "https://cghshospitals.com",
                "notes": (
                    f"NABH status: {item.get('accreditationStatus', 'NABH')}; "
                    "no public email — use phone or LinkedIn search for quality manager"
                ),
            })
        offset += limit
        time.sleep(0.12)
    return rows


def scrape_chain_contacts() -> list[dict]:
    rows: list[dict] = []
    seen: set[str] = set()
    for chain, region, url in CHAIN_CONTACT_PAGES:
        try:
            html = fetch_url(url)
        except (urllib.error.URLError, OSError) as exc:
            print(f"Warning: chain {chain}: {exc}", file=sys.stderr)
            continue
        for raw in EMAIL_RE.findall(html):
            email = clean_email(raw)
            if not email or email in seen:
                continue
            seen.add(email)
            rows.append({
                "source": "HOSPITAL_WEBSITE",
                "tier": "A",
                "state": region,
                "city": "",
                "hospital_name": chain,
                "contact_role": "Corporate / hospital contact desk",
                "email": email,
                "phone": "",
                "website_source": url,
                "notes": "Public contact page — route to quality/NABH team",
            })
    return rows


def dedupe_email_rows(rows: list[dict]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for r in rows:
        if not r.get("email"):
            out.append(r)
            continue
        key = r["email"].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def dedupe_nabh_phone_rows(rows: list[dict], emails_seen: set[str]) -> list[dict]:
    seen: set[str] = set()
    out: list[dict] = []
    for r in rows:
        if r.get("email"):
            continue
        key = (r.get("hospital_name", "").lower(), r.get("city", "").lower())
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-api", action="store_true", help="Skip live NABH API fetch")
    args = parser.parse_args()

    all_rows: list[dict] = []
    all_rows.extend(load_private_pmjay_rows())
    all_rows.extend(scrape_chain_contacts())

    email_rows = dedupe_email_rows([r for r in all_rows if r.get("email")])
    emails_seen = {r["email"].lower() for r in email_rows}

    nabh_rows: list[dict] = []
    if not args.skip_api:
        nabh_rows = fetch_nabh_hospitals()
    nabh_rows = dedupe_nabh_phone_rows(nabh_rows, emails_seen)

    combined = email_rows + nabh_rows
    combined.sort(key=lambda r: (r["tier"], r["state"], r["city"], r["hospital_name"]))

    fields = [
        "id", "tier", "source", "state", "city", "hospital_name",
        "contact_role", "email", "phone", "website_source", "notes",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, r in enumerate(combined, 1):
            r["id"] = f"P{i:04d}"
            w.writerow({k: r.get(k, "") for k in fields})

    tier_a = sum(1 for r in combined if r["tier"] == "A")
    tier_b = sum(1 for r in combined if r["tier"] == "B")
    print(json.dumps({
        "output": str(OUT),
        "total_rows": len(combined),
        "tier_a_with_email": tier_a,
        "tier_b_nabh_phone_only": tier_b,
        "by_source": {
            s: sum(1 for r in combined if r["source"] == s)
            for s in sorted({r["source"] for r in combined})
        },
        "usage": (
            "Tier A = email outreach (private hospitals + chain contact desks). "
            "Tier B = NABH hospitals with phone — find QM on LinkedIn, then call/WhatsApp."
        ),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
