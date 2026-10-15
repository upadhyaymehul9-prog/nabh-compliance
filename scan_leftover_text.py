"""
Run this on SERVER, inside the nabh-compliance folder:

    cd C:\\Users\\SERVER\\Desktop\\nabh-compliance
    python scan_leftover_text.py

Scans all 71 v2 masters for lines containing "not an approved master"
(the leftover build-note text) and prints the FULL line as it appears
in each file, so we can see every wording variant before deciding on
a fix. Prints only -- touches nothing.
"""

import zipfile
import glob
import os
import re

MASTERS_DIR = os.path.join("policies", "build", "masters")
TARGET = "not an approved master"

files = sorted(glob.glob(os.path.join(MASTERS_DIR, "*_v2_master.docx")))

if not files:
    print(f"No files found in {MASTERS_DIR}. Check you're in the right folder.")
    raise SystemExit(1)

print(f"Scanning {len(files)} files for '{TARGET}'...\n")

variants = {}  # exact sentence -> list of filenames
clean_files = []

for path in files:
    name = os.path.basename(path)
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")

    # Strip XML tags crudely to get plain-ish text for matching.
    # This is just for scanning/reporting -- not used for the actual fix.
    plain = re.sub(r"<[^>]+>", "", xml)

    if TARGET not in plain:
        clean_files.append(name)
        continue

    # Try to isolate the sentence containing the target phrase.
    # Split on sentence-ish boundaries and find the chunk with our phrase.
    idx = plain.find(TARGET)
    start = max(0, plain.rfind(".", 0, idx) + 1)
    end = plain.find(".", idx)
    end = end + 1 if end != -1 else idx + len(TARGET) + 20
    sentence = plain[start:end].strip()
    sentence = re.sub(r"\s+", " ", sentence)

    variants.setdefault(sentence, []).append(name)

print(f"Files WITHOUT the leftover line: {len(clean_files)}")
if clean_files:
    for n in clean_files:
        print("   ", n)
print()

print(f"Files WITH the leftover line, grouped by exact wording:\n")
for i, (sentence, names) in enumerate(variants.items(), 1):
    print(f"-- Variant {i} ({len(names)} files) --")
    print(f"   Text: {sentence}")
    print(f"   Files: {', '.join(names)}")
    print()

total_affected = sum(len(v) for v in variants.values())
print(f"TOTAL affected: {total_affected} / {len(files)}")
