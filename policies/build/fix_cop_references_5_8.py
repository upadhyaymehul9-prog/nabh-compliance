# -*- coding: utf-8 -*-
"""
fix_cop_references_5_8.py
Check 5.8 (v1.8) audit and repair for all 20 COP chapters_v2 documents.

Actions per file:
  1. Delete any paragraph matching 'Guidebook interpretation supplied' in References.
  2. COP.3 only: insert proper NABH Accreditation Standards citation as the
     first Reference entry (it was missing).
  3. Save DOCX in-place.
  4. Re-render PDF in-place.
  5. Report every action taken, file by file.
"""
import os
import copy
from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from lxml import etree

COP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chapters_v2", "COP")

ARTIFACT_MARKER = "Guidebook interpretation supplied"
NABH_STD_PREFIX = "National Accreditation Board for Hospitals and Healthcare Providers. NABH Accreditation Standards"

COP3_NABH_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. "
    "NABH Accreditation Standards for Hospitals, 6th Edition. COP.3."
)


def para_is_in_references(doc, para_idx):
    """Return True if the paragraph at para_idx falls inside a References heading block."""
    in_refs = False
    for i, p in enumerate(doc.paragraphs):
        sn = p.style.name if p.style else ""
        if "Heading 1" in sn and "References" in p.text:
            in_refs = True
            continue
        if "Heading 1" in sn and in_refs:
            in_refs = False
        if i == para_idx:
            return in_refs
    return False


def delete_paragraph(para):
    """Remove a paragraph element from its parent XML node."""
    p = para._element
    p.getparent().remove(p)


def insert_para_before(doc, ref_para, text, style_name):
    """Insert a new paragraph with given text/style immediately before ref_para."""
    new_p = OxmlElement("w:p")
    new_pPr = OxmlElement("w:pPr")
    new_pStyle = OxmlElement("w:pStyle")
    # Resolve style id from name
    style_id = None
    for s in doc.styles:
        if s.name == style_name:
            style_id = s.style_id
            break
    if style_id:
        new_pStyle.set(qn("w:val"), style_id)
        new_pPr.append(new_pStyle)
    new_p.append(new_pPr)

    new_r = OxmlElement("w:r")
    new_t = OxmlElement("w:t")
    new_t.text = text
    new_t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    new_r.append(new_t)
    new_p.append(new_r)

    ref_para._element.addprevious(new_p)


def process_file(num):
    fname = f"HCO_COP_{num}_v2_REWRITE_DRAFT.docx"
    docx_path = os.path.join(COP_DIR, fname)
    pdf_path = docx_path.replace(".docx", ".pdf")

    doc = Document(docx_path)
    paras = doc.paragraphs

    # Locate References heading
    ref_heading_idx = None
    for i, p in enumerate(paras):
        sn = p.style.name if p.style else ""
        if "Heading 1" in sn and "References" in p.text:
            ref_heading_idx = i
            break

    if ref_heading_idx is None:
        return {"num": num, "error": "No References heading found", "removed": 0, "added": False}

    # Collect ref paragraphs (until next Heading 1)
    ref_para_indices = []
    for i in range(ref_heading_idx + 1, len(paras)):
        sn = paras[i].style.name if paras[i].style else ""
        if "Heading 1" in sn:
            break
        if paras[i].text.strip():
            ref_para_indices.append(i)

    # Find artifact paragraphs (do NOT modify list while iterating — collect first)
    artifact_paras = [i for i in ref_para_indices if ARTIFACT_MARKER in paras[i].text]
    nabh_paras = [i for i in ref_para_indices if NABH_STD_PREFIX in paras[i].text]
    has_nabh = len(nabh_paras) > 0

    removed_texts = []
    added_nabh = False

    # For COP.3: insert NABH citation BEFORE deleting artifact
    # (so we have the first real ref para to insert before)
    if num == 3 and not has_nabh:
        # The first ref para is the one to insert before
        if ref_para_indices:
            first_ref_para = paras[ref_para_indices[0]]
            ref_style = first_ref_para.style.name if first_ref_para.style else "List Number"
            insert_para_before(doc, first_ref_para, COP3_NABH_CITE, ref_style)
            added_nabh = True

    # Re-collect paragraphs after potential insertion (doc.paragraphs is live)
    # We need to find artifact paragraphs again since indices shifted
    artifact_elements = []
    in_refs = False
    for p in doc.paragraphs:
        sn = p.style.name if p.style else ""
        if "Heading 1" in sn and "References" in p.text:
            in_refs = True
            continue
        if "Heading 1" in sn and in_refs:
            break
        if in_refs and ARTIFACT_MARKER in p.text:
            artifact_elements.append(p)

    for p in artifact_elements:
        removed_texts.append(p.text)
        delete_paragraph(p)

    doc.save(docx_path)

    # Convert to PDF
    try:
        from docx2pdf import convert
        convert(docx_path, pdf_path)
        pdf_ok = True
    except Exception as e:
        pdf_ok = False
        pdf_err = str(e)

    return {
        "num": num,
        "removed": len(removed_texts),
        "removed_texts": removed_texts,
        "added_nabh": added_nabh,
        "had_nabh": has_nabh,
        "pdf_ok": pdf_ok,
    }


def verify_file(num):
    """Post-edit verification: count NABH cites and artifact lines in References."""
    fname = f"HCO_COP_{num}_v2_REWRITE_DRAFT.docx"
    doc = Document(os.path.join(COP_DIR, fname))

    in_refs = False
    nabh_count = 0
    artifact_count = 0
    ref_lines = []
    for p in doc.paragraphs:
        sn = p.style.name if p.style else ""
        if "Heading 1" in sn and "References" in p.text:
            in_refs = True
            continue
        if "Heading 1" in sn and in_refs:
            break
        if in_refs and p.text.strip():
            ref_lines.append(p.text)
            if NABH_STD_PREFIX in p.text:
                nabh_count += 1
            if ARTIFACT_MARKER in p.text:
                artifact_count += 1

    return {
        "num": num,
        "nabh_count": nabh_count,
        "artifact_count": artifact_count,
        "ref_lines": ref_lines,
    }


if __name__ == "__main__":
    print("=" * 70)
    print("Check 5.8 (v1.8) — COP chapter References repair")
    print("=" * 70)
    print()

    results = []
    for num in range(1, 21):
        print(f"Processing COP.{num}...", end=" ", flush=True)
        r = process_file(num)
        results.append(r)
        status_parts = []
        if r.get("removed", 0):
            status_parts.append(f"REMOVED artifact")
        if r.get("added_nabh"):
            status_parts.append("ADDED NABH citation")
        if r.get("pdf_ok"):
            status_parts.append("PDF rendered")
        elif "error" in r:
            status_parts.append(f"ERROR: {r['error']}")
        print(", ".join(status_parts) if status_parts else "no changes")

    print()
    print("=" * 70)
    print("File-by-file detail")
    print("=" * 70)
    for r in results:
        num = r["num"]
        print(f"\nCOP.{num}:")
        if "error" in r:
            print(f"  ERROR: {r['error']}")
            continue
        for t in r.get("removed_texts", []):
            print(f"  REMOVED: {t}")
        if r.get("added_nabh"):
            print(f"  ADDED:   {COP3_NABH_CITE}")
        if r.get("pdf_ok"):
            print(f"  PDF:     re-rendered OK")

    print()
    print("=" * 70)
    print("Post-edit verification — References section contents")
    print("=" * 70)
    print()

    all_pass = True
    summary_rows = []
    for num in range(1, 21):
        v = verify_file(num)
        nabh_ok = v["nabh_count"] == 1
        art_ok = v["artifact_count"] == 0
        status = "PASS" if (nabh_ok and art_ok) else "FAIL"
        if status == "FAIL":
            all_pass = False
        summary_rows.append((num, v["nabh_count"], v["artifact_count"], status))
        print(f"COP.{num}: NABH citations={v['nabh_count']}, Artifacts={v['artifact_count']} => {status}")
        for line in v["ref_lines"]:
            marker = "  [NABH]  " if NABH_STD_PREFIX in line else ("  [ART!] " if ARTIFACT_MARKER in line else "         ")
            print(f"{marker}{line[:90]}")
        print()

    print()
    print("=" * 70)
    print("FINAL CONFIRMATION TABLE")
    print("=" * 70)
    print(f"{'File':<10} {'NABH cites':>12} {'Artifacts':>10} {'Status':>8}")
    print("-" * 46)
    for num, nabh, art, status in summary_rows:
        print(f"COP.{num:<6} {nabh:>12} {art:>10} {status:>8}")
    print("-" * 46)
    total_artifacts = sum(r[2] for r in summary_rows)
    total_nabh_ok = sum(1 for r in summary_rows if r[1] == 1)
    print(f"{'TOTAL':<10} {total_nabh_ok}/20 with 1 NABH   {total_artifacts} remaining artifacts")
    print()
    if all_pass:
        print("ALL 20 FILES PASS: exactly 1 NABH citation, 0 artifacts in References.")
    else:
        print("FAILURES detected — see above.")
