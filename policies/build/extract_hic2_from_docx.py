"""Reconstruct hic2_draft.json from a rendered HIC.2 .docx.

WHY THIS EXISTS
HIC.2 is the only approved master with no local draft file and no build script —
it lives solely as a row in shco_policy_masters. That table has RLS enabled with
zero policies, so only the service role can read it, and this project's standing
rule is that the service role key never enters the terminal. The remaining
credential-safe source is a previously rendered document.

This script is therefore a RECONSTRUCTION, not an export. It is only trustworthy
because every field it produces is verified byte-for-byte against md5 hashes taken
from the live row (see verify_hic2_draft.py). Do not use its output unverified.

The docx was rendered for a specific hospital, so the hospital name is reversed
back to the {{HOSPITAL_NAME}} placeholder the master actually stores.
"""

import argparse
import html
import json
import re
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def paragraphs(docx_path):
    """Yield (text, is_bullet) for each paragraph, in document order."""
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>|<w:p/>", xml, re.S):
        text = html.unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S)))
        is_bullet = "<w:numPr>" in p
        out.append((text, is_bullet))
    return out


def rebuild_steps(paras, start_idx, end_idx, hospital_name):
    """Invert renderProcedureStep(): title paragraph + body paragraphs + bullets
    back into the single fused "N. Title\r\n\r\nbody" string the DB stores.

    The renderer appends " (OE.CODE, ...)" to each step title; that annotation is
    generated at render time from oe_mapping and is NOT part of the stored text,
    so it is stripped here.
    """
    steps = []
    current = None
    for text, is_bullet in paras[start_idx:end_idx]:
        if not text.strip():
            continue
        title = re.match(r"^(\d+)\.\s(.*)$", text)
        # A new step begins at a numbered title that is not a bullet.
        if title and not is_bullet:
            if current:
                steps.append(current)
            num, rest = title.group(1), title.group(2)
            rest = re.sub(r"\s*\((?:[A-Z]{2,4}\.\d+\.[a-z](?:,\s*)?)+\)\s*$", "", rest)
            current = {"num": int(num), "title": rest, "blocks": []}
        elif current is not None:
            current["blocks"].append(("bullet" if is_bullet else "para", text))
    if current:
        steps.append(current)

    fused = []
    for s in steps:
        parts = []
        buffer = []
        for kind, text in s["blocks"]:
            if kind == "bullet":
                buffer.append("- " + text)
            else:
                if buffer:
                    parts.append("\n".join(buffer))
                    buffer = []
                parts.append(text)
        if buffer:
            parts.append("\n".join(buffer))
        body = "\n\n".join(parts)
        fused.append(f"{s['num']}. {s['title']}\n\n{body}")

    # The DB stores CRLF line endings for HIC.1-HIC.5; restore them, then put the
    # hospital-name placeholder back.
    fused = [f.replace("\n", "\r\n") for f in fused]
    if hospital_name:
        fused = [f.replace(hospital_name, "{{HOSPITAL_NAME}}") for f in fused]
    return fused


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docx", default=str(REPO / "policies/documents/HIC2_check_today.docx"))
    ap.add_argument("--hospital-name", default="HMP Foundation")
    ap.add_argument("--out", default=str(REPO / "policies/drafts/hic2_draft.json"))
    args = ap.parse_args()

    paras = paragraphs(args.docx)
    labels = [t for t, _ in paras]

    def find(label):
        for i, t in enumerate(labels):
            if t.strip() == label:
                return i
        raise SystemExit(f"Heading not found in docx: {label!r}")

    proc_i = find("4. Procedure")
    resp_i = find("5. Responsibility")
    steps = rebuild_steps(paras, proc_i + 1, resp_i, args.hospital_name)

    out = {
        "standard_code": "HIC.2",
        "_source": "RECONSTRUCTED from %s — verify against the live row before trusting"
        % Path(args.docx).name,
        "procedure_steps": steps,
    }
    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out}: {len(steps)} steps")
    for s in steps[:3]:
        print("  ", repr(s[:70]))


if __name__ == "__main__":
    main()
