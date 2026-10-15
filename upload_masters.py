"""
Uploads all 71 v2 policy masters to the Supabase Storage bucket
'policy-masters-v2', matching the master_docx_path already set in
shco_policy_masters (i.e. just the filename, e.g. 'FMS.4_v2_master.docx').

SETUP (do this once, before running):

  1. Get your service role key from:
     https://supabase.com/dashboard/project/tbptllgcjtiiqspxqcde/settings/api
     (the "service_role" secret key -- NOT the anon/public key)

  2. Set it as an environment variable in THIS CMD SESSION ONLY
     (do not save it into any file, do not paste it into chat):

     set SUPABASE_SERVICE_ROLE_KEY=paste_your_key_here

  3. Then run:

     pip install requests --break-system-packages
     python upload_masters.py

  This only uploads. It does not touch the database rows (already done)
  and does not deploy anything. Safe to re-run -- it overwrites existing
  objects at the same path rather than erroring or duplicating.
"""

import os
import glob
import sys
import requests

PROJECT_REF = "tbptllgcjtiiqspxqcde"
BUCKET = "policy-masters-v2"
MASTERS_DIR = os.path.join("policies", "build", "masters")

SUPABASE_URL = f"https://{PROJECT_REF}.supabase.co"
SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

if not SERVICE_KEY:
    print("ERROR: SUPABASE_SERVICE_ROLE_KEY is not set in this session.")
    print("Run:  set SUPABASE_SERVICE_ROLE_KEY=your_key_here")
    print("...then run this script again in the SAME cmd window.")
    sys.exit(1)

files = sorted(glob.glob(os.path.join(MASTERS_DIR, "*_v2_master.docx")))

if not files:
    print(f"No files found in {MASTERS_DIR}. Check you're in the right folder.")
    sys.exit(1)

print(f"Found {len(files)} files to upload to bucket '{BUCKET}'.\n")

DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

ok = []
failed = []

for path in files:
    filename = os.path.basename(path)
    url = f"{SUPABASE_URL}/storage/v1/object/{BUCKET}/{filename}"

    with open(path, "rb") as f:
        data = f.read()

    resp = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {SERVICE_KEY}",
            "apikey": SERVICE_KEY,
            "Content-Type": DOCX_MIME,
            "x-upsert": "true",  # overwrite if it already exists, don't error
        },
        data=data,
    )

    if resp.status_code in (200, 201):
        ok.append(filename)
        print(f"  OK   {filename}")
    else:
        failed.append((filename, resp.status_code, resp.text))
        print(f"  FAIL {filename}  [{resp.status_code}] {resp.text[:200]}")

print()
print(f"Uploaded OK: {len(ok)} / {len(files)}")
if failed:
    print(f"Failed: {len(failed)}")
    print("\n-- Failures --")
    for filename, code, text in failed:
        print(f"  {filename}: HTTP {code} -- {text[:300]}")
else:
    print("All 71 uploaded successfully.")
