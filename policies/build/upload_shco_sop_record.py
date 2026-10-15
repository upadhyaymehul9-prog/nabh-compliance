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
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_URL = "https://tbptllgcjtiiqspxqcde.supabase.co"
DOCX_CONTENT_TYPE = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
BUCKET = "shco-sop-record-v2"
ROOT = Path(__file__).parent / "sop_record_masters"


def storage_key() -> str:
    """Storage still accepts the legacy service_role JWT on this project even
    though legacy keys were disabled for the Data API -- prefer it, fall
    back to the new secret key if that's all that's set."""
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_SECRET_KEY")
    if not key:
        raise SystemExit(
            "SUPABASE_SERVICE_ROLE_KEY (or SUPABASE_SECRET_KEY) is not set. "
            "Required for storage upload."
        )
    return key


def data_key() -> str:
    """The Data API (PostgREST / shco_documents) rejects legacy keys now --
    prefer the new secret key, fall back to the legacy key if that's all
    that's set."""
    key = os.environ.get("SUPABASE_SECRET_KEY") or os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not key:
        raise SystemExit(
            "SUPABASE_SECRET_KEY (or SUPABASE_SERVICE_ROLE_KEY) is not set. "
            "Required for the shco_documents table upsert."
        )
    return key


def base_url() -> str:
    return os.environ.get("SUPABASE_URL", DEFAULT_URL).rstrip("/")


def upload_file(storage_path: str, local_file: Path) -> None:
    key = storage_key()
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
    key = data_key()
    url = f"{base_url()}/rest/v1/shco_documents?on_conflict=storage_path"
    headers = {
        "apikey": key,
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


def existing_storage_paths(chapter: str) -> set[str]:
    """Every storage_path currently registered in shco_documents for this
    chapter, regardless of whether it's still in the manifest."""
    key = data_key()
    pattern = urllib.parse.quote(f"{chapter}/%", safe="")
    url = f"{base_url()}/rest/v1/shco_documents?select=storage_path&storage_path=like.{pattern}"
    headers = {"apikey": key}
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status, raw = resp.status, resp.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, e.read()
    if status != 200:
        raise SystemExit(f"listing existing rows failed for {chapter}: HTTP {status}: {raw[:400]!r}")
    return {row["storage_path"] for row in json.loads(raw)}


def delete_orphan_rows(storage_paths: list[str]) -> None:
    if not storage_paths:
        return
    key = data_key()
    in_list = ",".join(urllib.parse.quote(p, safe="") for p in storage_paths)
    url = f"{base_url()}/rest/v1/shco_documents?storage_path=in.({in_list})"
    headers = {
        "apikey": key,
        "Prefer": "return=minimal",
    }
    req = urllib.request.Request(url, headers=headers, method="DELETE")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status, raw = resp.status, resp.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, e.read()
    if status not in (200, 204):
        raise SystemExit(f"orphan row delete failed: HTTP {status}: {raw[:400]!r}")


def delete_orphan_objects(storage_paths: list[str]) -> None:
    if not storage_paths:
        return
    key = storage_key()
    url = f"{base_url()}/storage/v1/object/{BUCKET}"
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    body = json.dumps({"prefixes": storage_paths}).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="DELETE")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status, raw = resp.status, resp.read()
    except urllib.error.HTTPError as e:
        status, raw = e.code, e.read()
    if status not in (200, 204):
        raise SystemExit(f"orphan storage-object delete failed: HTTP {status}: {raw[:400]!r}")


def main() -> int:
    manifests = sorted(ROOT.glob("*/manifest.json"))
    if not manifests:
        raise SystemExit(f"no manifest.json files found under {ROOT}")

    total = 0
    total_orphans = 0
    for manifest_path in manifests:
        chapter = manifest_path.parent.name
        entries = json.loads(manifest_path.read_text(encoding="utf-8"))
        print(f"\n{chapter}: {len(entries)} document(s)")
        current_paths: set[str] = set()
        for entry in entries:
            local_file = manifest_path.parent / entry["file"]
            if not local_file.exists():
                raise SystemExit(f"manifest references missing file: {local_file}")
            storage_path = f"{chapter}/{entry['file']}"
            current_paths.add(storage_path)
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

        # Clean up anything still registered for this chapter that is no
        # longer in its manifest -- a renamed or renumbered file otherwise
        # leaves a stale duplicate row (and a stale blob in Storage) behind
        # forever, since the upsert above only ever adds/updates, never
        # removes.
        orphans = sorted(existing_storage_paths(chapter) - current_paths)
        if orphans:
            for path in orphans:
                print(f"  removing orphan -> {BUCKET}/{path}")
            delete_orphan_rows(orphans)
            delete_orphan_objects(orphans)
            total_orphans += len(orphans)

    print(f"\nDone. {total} document(s) uploaded and registered across {len(manifests)} chapter(s).")
    if total_orphans:
        print(f"Cleaned up {total_orphans} orphaned row(s)/file(s) left over from earlier renames.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
