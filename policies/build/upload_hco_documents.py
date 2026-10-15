# -*- coding: utf-8 -*-
"""Upload HCO Full v2 Policy + SOP + Record masters to Supabase.

Walks two source trees:
  1. policies/build/masters_hco/*.docx           -> document_type='policy'
  2. policies/build/chapters_v2/<CHAPTER>/...     -> document_type='sop' | 'record'
     (folder casing and nesting is inconsistent per chapter on purpose --
     this walks generically rather than assuming one pattern.)

Uploads each file to storage bucket policy-masters-hco-v2 at:
    <document_type>/<standard_code>/<filename>
and upserts one row per file into public.hco_documents.

Idempotent: re-running is safe. The DB unique constraint is
(standard_code, document_type, storage_path), so this uses upsert.

Requires SUPABASE_SERVICE_ROLE_KEY in the environment. Never printed,
never hardcoded, never touched by this script beyond reading it once.
Hard-refuses to run for real without it -- same discipline as your
existing apply_*_supabase.py scripts.

Usage:
    python upload_hco_documents.py --dry-run      # no key, no network, just prints the plan
    python upload_hco_documents.py                # the real run, needs the env var set
"""
from __future__ import annotations

import os
import re
import sys
import argparse
from pathlib import Path

SUPABASE_URL = "https://tbptllgcjtiiqspxqcde.supabase.co"
BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parent
MASTERS_HCO_DIR = REPO_ROOT / "masters_hco"
CHAPTERS_V2_DIR = REPO_ROOT / "chapters_v2"

CHAPTERS = ["AAC", "COP", "FMS", "HRM", "IPC", "MOM", "PRE", "PSQ", "ROM", "IMS"]


def humanize(stem: str) -> str:
    """Turn a filename stem into a readable title. Simple, predictable,
    works the same way across every chapter's inconsistent naming."""
    s = stem
    s = re.sub(r"^HCO\.", "", s)
    s = re.sub(r"_v2_master$", "", s)
    s = re.sub(r"^SOP_[A-Z]+\d+_", "", s)
    s = re.sub(r"^([A-Z]+)\.(\d+)_Record_(\d+)_", r"Record \3 — ", s)
    s = s.replace("_", " ").strip()
    return s[:1].upper() + s[1:] if s else stem


def policy_title_from_docx(path: Path) -> str | None:
    """Policy masters have a predictable shape: paragraph 2 is the real
    title (paragraph 1 is the «Hospital Name» placeholder). Best-effort --
    falls back to filename-derived title if python-docx isn't available
    or the shape doesn't match."""
    try:
        from docx import Document
    except ImportError:
        return None
    try:
        d = Document(str(path))
        paras = [p.text.strip() for p in d.paragraphs if p.text.strip()]
        for p in paras[:4]:
            if "Hospital Name" not in p and len(p) > 3:
                return p
    except Exception:
        pass
    return None


def find_policy_masters() -> list[dict]:
    """policies/build/masters_hco/HCO.<CHAPTER>.<N>_v2_master.docx"""
    items = []
    if not MASTERS_HCO_DIR.is_dir():
        return items
    for f in sorted(MASTERS_HCO_DIR.glob("*.docx")):
        m = re.match(r"^HCO\.([A-Z]+)\.(\d+)_v2_master\.docx$", f.name)
        if not m:
            print(f"  ! skipping unrecognised file in masters_hco: {f.name}")
            continue
        chapter, n = m.group(1), m.group(2)
        standard_code = f"{chapter}.{n}"
        title = policy_title_from_docx(f) or humanize(f.stem)
        items.append({
            "standard_code": standard_code,
            "document_type": "policy",
            "record_index": None,
            "title": title,
            "local_path": f,
            "storage_path": f"policy/{standard_code}/{f.name}",
        })
    return items


def find_sop_and_records() -> list[dict]:
    """Walks chapters_v2/<CHAPTER>/ generically: finds any folder whose
    name is 'document' or 'documents' (any case), then standard
    sub-folders like AAC1, IMS10 inside it (optionally nested one level
    under a *_Package_v2 folder -- doesn't matter, we just look for the
    <CHAPTER><N> folder name pattern wherever it sits)."""
    items = []
    for chapter in CHAPTERS:
        chapter_dir = CHAPTERS_V2_DIR / chapter
        if not chapter_dir.is_dir():
            print(f"  ! no chapters_v2/{chapter} folder found, skipping")
            continue

        doc_roots = [p for p in chapter_dir.rglob("*") if p.is_dir() and p.name.lower() in ("document", "documents")]
        if not doc_roots:
            print(f"  ! {chapter}: no SOP/Record document folder found")
            continue

        std_pattern = re.compile(rf"^{chapter}(\d+)$", re.IGNORECASE)
        for doc_root in doc_roots:
            for std_dir in [p for p in doc_root.rglob("*") if p.is_dir()]:
                m = std_pattern.match(std_dir.name)
                if not m:
                    continue
                standard_code = f"{chapter}.{m.group(1)}"

                # SOP: direct .docx files in the standard folder (not in Records/)
                for f in std_dir.glob("*.docx"):
                    items.append({
                        "standard_code": standard_code,
                        "document_type": "sop",
                        "record_index": None,
                        "title": humanize(f.stem),
                        "local_path": f,
                        "storage_path": f"sop/{standard_code}/{f.name}",
                    })

                # Records: everything inside a Records/ subfolder (any case)
                records_dirs = [p for p in std_dir.iterdir() if p.is_dir() and p.name.lower() == "records"]
                for rdir in records_dirs:
                    for idx, f in enumerate(sorted(rdir.glob("*.docx")), start=1):
                        rm = re.search(r"_Record_(\d+)_", f.name)
                        record_index = int(rm.group(1)) if rm else idx
                        items.append({
                            "standard_code": standard_code,
                            "document_type": "record",
                            "record_index": record_index,
                            "title": humanize(f.stem),
                            "local_path": f,
                            "storage_path": f"record/{standard_code}/{f.name}",
                        })
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Print the plan, touch nothing, no key needed.")
    args = ap.parse_args()

    print("Scanning policy masters...")
    policies = find_policy_masters()
    print(f"  found {len(policies)} policy files")

    print("Scanning SOP + Record packages...")
    sops_records = find_sop_and_records()
    sops = [i for i in sops_records if i["document_type"] == "sop"]
    records = [i for i in sops_records if i["document_type"] == "record"]
    print(f"  found {len(sops)} SOP files, {len(records)} record files")

    all_items = policies + sops_records
    print(f"\nTotal: {len(all_items)} files to upload/upsert.\n")

    if args.dry_run:
        print("--dry-run: showing first 3 of each type, then stopping. No network calls made.\n")
        for doctype in ("policy", "sop", "record"):
            sample = [i for i in all_items if i["document_type"] == doctype][:3]
            print(f"--- {doctype} ({len([i for i in all_items if i['document_type']==doctype])} total) ---")
            for i in sample:
                print(f"  {i['standard_code']:10s} {i['title'][:60]:60s} -> {i['storage_path']}")
        return 0

    service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not service_key:
        print("ERROR: SUPABASE_SERVICE_ROLE_KEY is not set in the environment.", file=sys.stderr)
        print("This script will not run for real without it. Set it and try again,", file=sys.stderr)
        print("or use --dry-run to preview the plan without the key.", file=sys.stderr)
        return 1

    try:
        from supabase import create_client
    except ImportError:
        print("ERROR: the 'supabase' Python package isn't installed.", file=sys.stderr)
        print("Run: pip install supabase", file=sys.stderr)
        return 1

    client = create_client(SUPABASE_URL, service_key)

    uploaded, skipped, failed = 0, 0, 0
    for i, item in enumerate(all_items, 1):
        local_path = item["local_path"]
        storage_path = item["storage_path"]
        print(f"[{i}/{len(all_items)}] {item['standard_code']} {item['document_type']:7s} {local_path.name}")
        try:
            data = local_path.read_bytes()
            client.storage.from_(BUCKET).upload(
                storage_path, data,
                {"content-type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                 "upsert": "true"},
            )
            client.table("hco_documents").upsert({
                "chapter": "HCO",
                "standard_code": item["standard_code"],
                "document_type": item["document_type"],
                "record_index": item["record_index"],
                "title": item["title"],
                "storage_path": storage_path,
                "version": "2.0",
            }, on_conflict="standard_code,document_type,storage_path").execute()
            uploaded += 1
        except Exception as e:
            print(f"    ! FAILED: {e}", file=sys.stderr)
            failed += 1

    print(f"\nDone. uploaded={uploaded} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
