"""
Run this on SERVER, inside the nabh-compliance folder:

    cd C:\\Users\\SERVER\\Desktop\\nabh-compliance
    python check_placeholders.py

Checks all 71 v2 masters for the literal, unbroken «Hospital Name»
placeholder inside word/document.xml -- the same check the edge
function relies on. Uses Python's built-in zipfile module, so no
extra install needed. Prints only -- touches nothing.
"""

import zipfile
import glob
import os

MASTERS_DIR = os.path.join("policies", "build", "masters")
PLACEHOLDER = "\u00ab" + "Hospital Name" + "\u00bb"  # «Hospital Name»

files = sorted(glob.glob(os.path.join(MASTERS_DIR, "*_v2_master.docx")))

if not files:
    print(f"No files found matching {MASTERS_DIR}\\*_v2_master.docx -- check you're in the right folder.")
    raise SystemExit(1)

print(f"Checking {len(files)} files for an unbroken placeholder in word/document.xml...\n")

ok = []
broken = []
errored = []

for path in files:
    name = os.path.basename(path)
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8")
        if PLACEHOLDER in xml:
            ok.append(name)
        else:
            broken.append(name)
    except Exception as e:
        errored.append((name, str(e)))

print(f"OK (placeholder intact):     {len(ok)}")
print(f"BROKEN (missing/split):      {len(broken)}")
print(f"ERRORED (couldn't open):     {len(errored)}")
print()

if broken:
    print("-- Files with a MISSING or SPLIT placeholder (need a look before deploy) --")
    for n in broken:
        print("   ", n)
    print()

if errored:
    print("-- Files that failed to open/read --")
    for n, e in errored:
        print("   ", n, "->", e)
    print()

if not broken and not errored:
    print("All 71 clear. Safe to proceed with upload + live test.")
