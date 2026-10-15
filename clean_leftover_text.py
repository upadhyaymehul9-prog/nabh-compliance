"""
Run this on SERVER, inside the nabh-compliance folder:

    cd C:\\Users\\SERVER\\Desktop\\nabh-compliance
    python clean_leftover_text.py

Removes the leftover build-note sentence (one of three known variants,
all ending in "not an approved master.") from each master's
word/document.xml, using direct XML string replacement -- the same
safe technique the delivery pipeline itself uses -- so nothing else
in the file (formatting, other text, the «Hospital Name» placeholder)
is touched.

IMPORTANT: this does NOT overwrite your existing masters. It writes
cleaned copies into a new folder:

    policies\\build\\masters_cleaned\\

Review a few of those in Word first. Only after you're happy, copy
them over the originals (or re-run the upload script pointed at the
cleaned folder) -- that's a separate, deliberate step, not automatic.
"""

import zipfile
import shutil
import glob
import os

MASTERS_DIR = os.path.join("policies", "build", "masters")
OUTPUT_DIR = os.path.join("policies", "build", "masters_cleaned")

# Exact sentences found by the scan -- including the leading em-dash
# and trailing period, so removal doesn't leave a stray dash or gap
# in punctuation.
VARIANTS_TO_REMOVE = [
    "PRE v2 draft \u2014 not an approved master.",
    "Template-test rebuild \u2014 not an approved master.",
    "PRE chapter template test \u2014 not an approved master.",
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

files = sorted(glob.glob(os.path.join(MASTERS_DIR, "*_v2_master.docx")))

if not files:
    print(f"No files found in {MASTERS_DIR}. Check you're in the right folder.")
    raise SystemExit(1)

print(f"Cleaning {len(files)} files -> writing to {OUTPUT_DIR}\n")

cleaned = []
unchanged = []
errored = []

for path in files:
    name = os.path.basename(path)
    out_path = os.path.join(OUTPUT_DIR, name)

    try:
        # Copy the whole docx (zip) first, then patch just document.xml
        shutil.copyfile(path, out_path)

        with zipfile.ZipFile(path, "r") as zin:
            xml = zin.read("word/document.xml").decode("utf-8")

        original_xml = xml
        removed_any = False
        for variant in VARIANTS_TO_REMOVE:
            if variant in xml:
                xml = xml.replace(variant, "")
                removed_any = True

        if not removed_any:
            unchanged.append(name)
            continue

        # Rebuild the zip with the patched document.xml, everything
        # else copied through unchanged.
        with zipfile.ZipFile(path, "r") as zin:
            with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    if item.filename == "word/document.xml":
                        zout.writestr(item, xml)
                    else:
                        zout.writestr(item, zin.read(item.filename))

        cleaned.append(name)

    except Exception as e:
        errored.append((name, str(e)))

print(f"Cleaned (leftover text removed): {len(cleaned)}")
print(f"Unchanged (no match found):      {len(unchanged)}")
print(f"Errored:                         {len(errored)}")
print()

if unchanged:
    print("-- Files with no match (unexpected -- check these manually) --")
    for n in unchanged:
        print("   ", n)
    print()

if errored:
    print("-- Files that failed --")
    for n, e in errored:
        print("   ", n, "->", e)
    print()

print(f"Cleaned copies are in: {OUTPUT_DIR}")
print("Originals in policies\\build\\masters were NOT touched.")
print("Open a few cleaned files in Word to check before doing anything further.")
