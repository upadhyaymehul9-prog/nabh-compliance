#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Upload/overwrite a single file in a Supabase Storage bucket.

Generic one-off uploader for fixes to already-published Records/SOPs/Policy
files that live in Supabase Storage (policy-masters-v2 / policy-masters-hco-v2),
separate from the per-chapter provisioning scripts. Overwrites in place
(upsert) at the exact storage path given.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required
  SUPABASE_URL                                      optional (defaults to project)

Usage:
  python3 policies/build/upload_storage_file.py \
      --bucket policy-masters-hco-v2 \
      --path "sop/COP.2/SOP_Emergency_Triage.docx" \
      --file "policies/build/chapters_v2/COP/document/COP2/SOP_Emergency_Triage.docx"
"""
from __future__ import annotations

import argparse
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_URL = "https://tbptllgcjtiiqspxqcde.supabase.co"
DOCX_CONTENT_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)


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


def upload(bucket: str, storage_path: str, local_file: Path) -> None:
    key = service_key()
    body = local_file.read_bytes()
    url = f"{base_url()}/storage/v1/object/{bucket}/{storage_path}"
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
        raise SystemExit(f"upload failed HTTP {status}: {raw[:400]!r}")

    print(f"uploaded -> {bucket}/{storage_path} ({len(body)} bytes)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bucket", required=True)
    ap.add_argument("--path", required=True, help="destination path inside the bucket")
    ap.add_argument("--file", required=True, help="local file to upload")
    args = ap.parse_args()

    local_file = Path(args.file)
    if not local_file.exists():
        raise SystemExit(f"local file not found: {local_file}")

    upload(args.bucket, args.path, local_file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
