#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload SHCO SOP/Record masters to the shco-sop-record-v2 Supabase Storage
bucket, and upsert their metadata into the shco_documents table.

This is the SHCO equivalent of the HCO document pipeline (hco_documents /
policy-masters-hco-v2), scoped to SOPs and Records only -- SHCO policy
masters keep using upload_all_shco_masters.py / shco_policy_masters /
policy-masters-v2, untouched by this script.

Reads every policies/build/sop_record_masters/<CHAPTER>/manifest.json and,
for each entry, uploads the referenced .docx to:
    shco-sop-record-v2/<CHAPTER>/<file>
and upserts (on storage_path) a row into shco_documents with document_type,
standard_code, record_index (records only) and title from the manifest.

Adding a new chapter later is just: drop its folder + manifest.json next to
HRM's, then run this script again -- it picks up every chapter it finds.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required
  SUPABASE_URL                                      optional (defaults to project)

Usage:
  python policies\\build\\upload_shco_sop_record.py
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_URL = "https://tbptllgcjtiiqspxqcde.supabase.co"
DOCX_CONTENT_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
BUCKET = "shco-sop-record-v2"
ROOT = Path(__file__).parent / "sop_record_masters"


def service_key() -> str:
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_SECRET_KEY")
    if not key:
        raise SystemExit(
            "SUPABASE_SERVICE_ROLE_KEY (or SUPABASE_SECRET_KEY) is not set. "
            "Required for storage upload and the table upsert."
        )
    return key


def base_url() -> str:
    return os.environ.get("SUPABASE_URL", DEFAULT_URL).rstrip("/")


def upload_file(storage_path: str, local_file: Path) -> None:
    key = service_key()
    body = local_file.read_bytes()
    url = f"{base_url()}/storage/v1/object/{BUCKET}/{storage_path}"
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": DOCX_CONTENT_TYPE,
        "x-upsert": "true",
    }
    req = urllib.request.Request(url, data=body, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            status, raw = resp.status, resp.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, e.read()
    if status not in (200, 201):
        raise SystemExit(f"upload failed for {storage_path}: HTTP {status}: {raw[:400]!r}")
    print(f"  uploaded -> {BUCKET}/{storage_path} ({len(body)} bytes)")


def upsert_row(row: dict) -> None:
    key = service_key()
    url = f"{base_url()}/rest/v1/shco_documents?on_conflict=storage_path"
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates,return=minimal",
    }
    body = json.dumps(row).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status, raw = resp.status, resp.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, e.read()
    if status not in (200, 201, 204):
        raise SystemExit(f"row upsert failed for {row['storage_path']}: HTTP {status}: {raw[:400]!r}")
    print(f"  db row -> {row['standard_code']} {row['document_type']} \"{row['title']}\"")


def main() -> int:
    manifests = sorted(ROOT.glob("*/manifest.json"))
    if not manifests:
        raise SystemExit(f"no manifest.json files found under {ROOT}")

    total = 0
    for manifest_path in manifests:
        chapter = manifest_path.parent.name
        entries = json.loads(manifest_path.read_text(encoding="utf-8"))
        print(f"\n{chapter}: {len(entries)} document(s)")
        for entry in entries:
            local_file = manifest_path.parent / entry["file"]
            if not local_file.exists():
                raise SystemExit(f"manifest references missing file: {local_file}")
            storage_path = f"{chapter}/{entry['file']}"
            upload_file(storage_path, local_file)
            row = {
                "standard_code": entry["standard_code"],
                "document_type": entry["document_type"],
                "title": entry["title"],
                "storage_path": storage_path,
                "version": "1.0",
            }
            if "record_index" in entry:
                row["record_index"] = entry["record_index"]
            upsert_row(row)
            total += 1

    print(f"\nDone. {total} document(s) uploaded and registered across {len(manifests)} chapter(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
