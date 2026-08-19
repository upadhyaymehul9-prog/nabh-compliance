#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provision FMS.1–FMS.5 v2 master .docx files for storage-based delivery.

Renders finished v2 masters with the «Hospital Name» placeholder, uploads them
to the policy-masters-v2 Supabase Storage bucket, and sets master_docx_path on
each shco_policy_masters row. Does not touch v1 fields or approve any row.

Prerequisites (run once in Supabase SQL Editor):
  supabase/migrations/20260819_shco_policy_masters_master_docx_path.sql

Deploy the edge function:
  npx supabase functions deploy download-v2-policy --project-ref tbptllgcjtiiqspxqcde

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required for upload + PATCH
  SUPABASE_URL                                      optional (defaults to project)

Usage:
  python3 policies/build/provision_v2_fms_masters.py --render-masters
  python3 policies/build/provision_v2_fms_masters.py --upload --set-paths
  python3 policies/build/provision_v2_fms_masters.py --all
  python3 policies/build/provision_v2_fms_masters.py --test-download --hospital-name "HMP Foundation" --standard-code FMS.4
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO = _HERE.parent.parent
_MASTERS = _HERE / "masters"
_PREVIEW = _HERE / "preview"

DEFAULT_URL = "https://tbptllgcjtiiqspxqcde.supabase.co"
PUBLISHABLE_KEY = "sb_publishable_tEu-kA8f9VLW-5uvU4E7ZA_PtaX59bw"
BUCKET = "policy-masters-v2"
PLACEHOLDER = "«Hospital Name»"
CODES = [f"FMS.{n}" for n in range(1, 6)]


def service_key() -> str:
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_SECRET_KEY")
    if not key:
        raise SystemExit(
            "SUPABASE_SERVICE_ROLE_KEY (or SUPABASE_SECRET_KEY) is not set. "
            "Required for storage upload and database PATCH."
        )
    return key


def base_url() -> str:
    return os.environ.get("SUPABASE_URL", DEFAULT_URL).rstrip("/")


def storage_path(code: str) -> str:
    return f"FMS/{code}_v2.docx"


def master_local_path(code: str) -> Path:
    return _MASTERS / f"{code}_v2_master.docx"


def request(method: str, url: str, key: str, body: bytes | dict | None = None, headers=None):
    hdrs = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
    }
    if headers:
        hdrs.update(headers)
    data = None
    if isinstance(body, dict):
        hdrs["Content-Type"] = "application/json"
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    elif isinstance(body, bytes):
        data = body
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def render_masters() -> None:
    _MASTERS.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["HOSPITAL_PLACEHOLDER"] = PLACEHOLDER
    env["OUT_DIR"] = "policies/build/masters/"
    env["OUT_SUFFIX"] = "_v2_master"

    print("Rendering FMS.1–FMS.4 v2 masters …")
    subprocess.run(
        ["deno", "run", "--allow-read", "--allow-write", "--allow-net", "--allow-env", str(_HERE / "render_fms_v2.ts")],
        check=True,
        cwd=_REPO,
        env=env,
    )
    print("Rendering FMS.5 v2 master …")
    subprocess.run(
        ["deno", "run", "--allow-read", "--allow-write", "--allow-net", "--allow-env", str(_HERE / "render_fms5_v2.ts")],
        check=True,
        cwd=_REPO,
        env=env,
    )

    for code in CODES:
        dst = master_local_path(code)
        if not dst.exists():
            raise SystemExit(f"missing master after render: {dst}")
        verify_master_docx(dst)
        print(f"  master OK: {dst.relative_to(_REPO)} ({dst.stat().st_size} bytes)")


def verify_master_docx(path: Path) -> None:
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    if PLACEHOLDER not in xml:
        raise SystemExit(f"{path.name}: «Hospital Name» placeholder not found in document.xml")
    if "Preview Hospital" in xml:
        raise SystemExit(f"{path.name}: still contains Preview Hospital — re-render with HOSPITAL_PLACEHOLDER")


def upload_masters(key: str) -> None:
    for code in CODES:
        local = master_local_path(code)
        if not local.exists():
            raise SystemExit(f"missing master file: {local} — run --render-masters first")
        obj_path = storage_path(code)
        url = f"{base_url()}/storage/v1/object/{BUCKET}/{obj_path}"
        body = local.read_bytes()
        status, raw = request(
            "POST",
            url,
            key,
            body=body,
            headers={
                "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "x-upsert": "true",
            },
        )
        if status not in (200, 201):
            raise SystemExit(f"upload {code} failed HTTP {status}: {raw[:400]!r}")
        print(f"  uploaded {code} -> {BUCKET}/{obj_path} ({len(body)} bytes)")


def set_paths(key: str) -> None:
    for code in CODES:
        obj_path = storage_path(code)
        status, raw = request(
            "GET",
            f"{base_url()}/rest/v1/shco_policy_masters?standard_code=eq.{code}&select=standard_code",
            key,
        )
        if status != 200:
            raise SystemExit(f"row check {code}: HTTP {status}: {raw[:200]!r}")
        rows = json.loads(raw)
        if not rows:
            raise SystemExit(
                f"No shco_policy_masters row for {code}. Insert the draft row first "
                f"(python3 policies/build/apply_fms_drafts_supabase.py --insert)."
            )
        status, raw = request(
            "PATCH",
            f"{base_url()}/rest/v1/shco_policy_masters?standard_code=eq.{code}",
            key,
            body={"master_docx_path": obj_path},
            headers={"Prefer": "return=representation"},
        )
        if status not in (200, 204):
            raise SystemExit(f"PATCH {code} failed HTTP {status}: {raw[:400]!r}")
        updated = json.loads(raw)[0] if raw else {}
        live_path = updated.get("master_docx_path")
        print(f"  {code} master_docx_path = {live_path!r}")


def test_download(hospital_name: str, standard_code: str = "FMS.4") -> Path:
    url = f"{base_url()}/functions/v1/download-v2-policy"
    payload = json.dumps({
        "standard_code": standard_code,
        "hospital_name": hospital_name,
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "apikey": PUBLISHABLE_KEY,
            "Authorization": f"Bearer {PUBLISHABLE_KEY}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = resp.read()
            ctype = resp.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"download-v2-policy HTTP {e.code}: {e.read()[:500]!r}")

    if "wordprocessingml" not in ctype and not data.startswith(b"PK"):
        raise SystemExit(f"unexpected response ({ctype}): {data[:300]!r}")

    out = Path(f"/tmp/{standard_code}_{re.sub(r'[^A-Za-z0-9]+', '_', hospital_name)}_v2_download.docx")
    out.write_bytes(data)
    verify_download_docx(out, hospital_name)
    print(f"download OK: {len(data)} bytes -> {out}")
    return out


def verify_download_docx(path: Path, hospital_name: str) -> None:
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    if PLACEHOLDER in xml:
        raise SystemExit(f"{path.name}: placeholder «Hospital Name» still present after download")
    if hospital_name not in xml:
        raise SystemExit(f"{path.name}: hospital name {hospital_name!r} not found in document")
    print(f"  verified: {hospital_name!r} present, placeholder absent")


def local_personalize_test(hospital_name: str = "HMP Foundation", standard_code: str = "FMS.4") -> Path:
    """Offline substitute test using the same Deno module as the edge function."""
    master = master_local_path(standard_code)
    if not master.exists():
        render_masters()
    out = Path(f"/tmp/{standard_code}_local_personalize.docx")
    script = _HERE / "_local_personalize_test.ts"
    subprocess.run(
        [
            "deno", "run", "--allow-read", "--allow-write", "--allow-net",
            str(script),
            str(master),
            hospital_name,
            str(out),
        ],
        check=True,
        cwd=_REPO,
    )
    verify_download_docx(out, hospital_name)
    print(f"local personalize OK -> {out}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--render-masters", action="store_true")
    ap.add_argument("--upload", action="store_true")
    ap.add_argument("--set-paths", action="store_true")
    ap.add_argument("--test-download", action="store_true")
    ap.add_argument("--local-test", action="store_true", help="personalize a master locally (no Supabase)")
    ap.add_argument("--all", action="store_true", help="render + upload + set-paths")
    ap.add_argument("--hospital-name", default="HMP Foundation")
    ap.add_argument("--standard-code", default="FMS.4")
    args = ap.parse_args()

    if args.all:
        args.render_masters = True
        args.upload = True
        args.set_paths = True

    if not any([args.render_masters, args.upload, args.set_paths, args.test_download, args.local_test]):
        ap.print_help()
        return 1

    if args.render_masters:
        render_masters()

    key = None
    if args.upload or args.set_paths:
        key = service_key()

    if args.upload:
        print("Uploading masters to Supabase Storage …")
        upload_masters(key)

    if args.set_paths:
        print("Setting master_docx_path on shco_policy_masters …")
        set_paths(key)

    if args.local_test:
        local_personalize_test(args.hospital_name, args.standard_code)

    if args.test_download:
        test_download(args.hospital_name, args.standard_code)

    return 0


if __name__ == "__main__":
    sys.exit(main())
