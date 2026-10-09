#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload every SHCO policy master in policies/build/masters/ to the
policy-masters-v2 Supabase Storage bucket, at its exact filename (bucket
root -- same path convention as master_docx_path in shco_policy_masters).

Reuses the same single-file upload logic as upload_storage_file.py, just
looped over all 71 files so this is one command instead of 71.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required
  SUPABASE_URL                                      optional (defaults to project)

Usage:
  python policies\\build\\upload_all_shco_masters.py
"""
from __future__ import annotations

import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_URL = "https://tbptllgcjtiiqspxqcde.supabase.co"
DOCX_CONTENT_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
BUCKET = "policy-masters-v2"
MASTERS_DIR = Path(__file__).parent / "masters"


def service_key() -> str:
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_SECRET_KEY")
    if not key:
        raise SystemExit(
            "SUPABASE_SERVICE_ROLE_KEY (or SUPABASE_SECRET_KEY) is not set. "
            "Required for storage upload."
        )
    return key


def base_url() -> str:
    return os.environ.get("SUPABASE_URL", DEFAULT_URL).rstrip("/")


def upload(storage_path: str, local_file: Path) -> None:
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

    print(f"uploaded -> {BUCKET}/{storage_path} ({len(body)} bytes)")


def main() -> int:
    files = sorted(MASTERS_DIR.glob("*.docx"))
    if not files:
        raise SystemExit(f"no .docx files found in {MASTERS_DIR}")
    print(f"Uploading {len(files)} files to {BUCKET}...")
    for f in files:
        upload(f.name, f)
    print(f"Done. {len(files)} files uploaded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
