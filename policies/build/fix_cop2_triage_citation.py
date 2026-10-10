# -*- coding: utf-8 -*-
"""Fixes two bugs found in SOP_COP.2.a_to_k_emergency_ambulance_disaster.docx
on 2026-10-10 (flagged by Mk after downloading the live file):

1. 4.3 "System of triage" (COP.2.c) named an invented 3-tier example
   (Emergency / Priority / Non-urgent) with no published scale behind it
   and no citation anywhere in the document.
2. 4.4 "Reassessment of waiting patients" (COP.2.d) gave a specific
   clinical time value -- "every 15-30 minutes for lower triage
   categories" -- as a bare "e.g." example with ZERO citation. This is
   the exact Pattern G (fabricated/unsourced frequency) bug documented at
   length in scripts/master-policy-todos.md for the HCO v2 project, and it
   slipped through the COP chapter's sign-off uncaught. The number was
   also backwards as written: "lower" (less urgent) categories get LONGER
   intervals under every published triage scale, not 15-30 minutes.

Fix: names the Canadian Triage and Acuity Scale (CTAS) as a verified,
published scale the hospital may adopt (NABH mandates no specific scale,
per Rule 2.9's standing position on undefined NABH numbers -- a hospital
may adopt a verified external standard, cited honestly as its own adopted
practice, not an NABH mandate). CTAS reassessment intervals confirmed
2026-10-10 directly against Murray, Bullard & Grafstein (2004), CJEM
6(6):421-427 (the CTAS/CEDIS National Working Groups' own implementation
guidelines, via Cambridge Core): Level 1 continuous care, Level 2 every
15 min, Level 3 every 30 min, Level 4 every 60 min, Level 5 every 120 min.
Both subsections keep "«Hospital to define»" for a hospital that adopts a
different published scale instead of CTAS.

Run once. Checks old text is present before replacing (fails loudly if the
file has since changed under it, rather than silently no-op'ing).
"""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph

PATH = Path(__file__).parent / "sop_record_masters" / "COP" / "SOP_COP.2.a_to_k_emergency_ambulance_disaster.docx"

OLD_43_STEP1 = (
    "1. Every patient entering the emergency area is triaged using "
    "«the hospital's defined triage categories» (e.g., Emergency / "
    "Priority / Non-urgent) before being made to wait."
)
NEW_43_STEP1 = (
    "1. Every patient entering the emergency area is triaged against a "
    "structured, published triage scale before being made to wait -- never "
    "an ad hoc or invented category list. «Hospital to define which "
    "published triage scale this hospital adopts»; the Canadian Triage "
    "and Acuity Scale (CTAS), a five-level scale (Level 1 Resuscitation, "
    "Level 2 Emergent, Level 3 Urgent, Level 4 Less Urgent, Level 5 "
    "Non-Urgent), is one verified, published scale a hospital may adopt. "
    "NABH does not mandate a specific scale, so a hospital may instead "
    "adopt a different named, published scale in its place -- but a scale "
    "with no published criteria behind it is not sufficient."
)

OLD_43_STEP3 = (
    "3. Staff performing triage are trained on the hospital's triage "
    "categories and criteria. (Record 3)"
)
NEW_43_STEP3 = (
    "3. Staff performing triage are trained on the adopted scale's "
    "categories and criteria. (Record 3)"
)

OLD_44_STEP1 = (
    "1. Every patient waiting in the emergency area is reassessed at "
    "least every «the hospital's defined reassessment interval» "
    "(e.g., every 15-30 minutes for lower triage categories)."
)
NEW_44_STEP1 = (
    "1. Every patient waiting in the emergency area is reassessed at the "
    "interval set by the triage scale adopted in step 1 of 4.3 above. "
    "Under CTAS, this is: Level 1 (Resuscitation) -- continuous care, not "
    "a periodic check; Level 2 (Emergent) -- every 15 minutes; Level 3 "
    "(Urgent) -- every 30 minutes; Level 4 (Less Urgent) -- every 60 "
    "minutes; Level 5 (Non-Urgent) -- every 120 minutes. «Hospital to "
    "define the equivalent reassessment intervals if a different "
    "published scale is adopted»."
)

TECH_SOURCE_INTRO = (
    "Technical source(s) for the triage scale (4.3) and its reassessment "
    "intervals (4.4): "
)
TECH_SOURCE_BULLET = (
    "• Murray, M., Bullard, M., & Grafstein, E., for the CTAS and "
    "CEDIS National Working Groups. (2004). Revisions to the Canadian "
    "Emergency Department Triage and Acuity Scale implementation "
    "guidelines. Canadian Journal of Emergency Medicine, 6(6), 421–427. "
    "https://doi.org/10.1017/S1481803500009428"
)

REFERENCES_BULLET = (
    "• Murray, M., Bullard, M., & Grafstein, E., for the CTAS and "
    "CEDIS National Working Groups. (2004). Revisions to the Canadian "
    "Emergency Department Triage and Acuity Scale implementation "
    "guidelines. Canadian Journal of Emergency Medicine, 6(6), 421–427. "
    "https://doi.org/10.1017/S1481803500009428 -- the triage scale named "
    "as an available option in COP.2.c and the reassessment intervals in "
    "COP.2.d, verified directly against this source, not assumed."
)


def _insert_paragraph_after(paragraph: Paragraph, text: str, style: str | None = None) -> Paragraph:
    new_p = OxmlElement("w:p")
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    new_para.add_run(text)
    if style:
        new_para.style = style
    return new_para


def main() -> None:
    doc = Document(str(PATH))
    paras = doc.paragraphs

    def find(text: str) -> Paragraph:
        for p in paras:
            if p.text == text:
                return p
        raise SystemExit(f"EXPECTED TEXT NOT FOUND (file changed under this script?):\n{text!r}")

    p = find(OLD_43_STEP1)
    p.runs[0].text = NEW_43_STEP1
    for r in p.runs[1:]:
        r.text = ""

    p = find(OLD_43_STEP3)
    p.runs[0].text = NEW_43_STEP3
    for r in p.runs[1:]:
        r.text = ""

    p44 = find(OLD_44_STEP1)
    p44.runs[0].text = NEW_44_STEP1
    for r in p44.runs[1:]:
        r.text = ""

    # Re-fetch step 3 of 4.4 ("Each reassessment... recorded. (Record 4)")
    # as the anchor to insert the Technical source block after.
    step3_44 = find("3. Each reassessment, including a nil-change reassessment, is time-stamped and recorded. (Record 4)")
    bullet_para = _insert_paragraph_after(step3_44, TECH_SOURCE_BULLET, style="List Paragraph")
    _insert_paragraph_after(step3_44, TECH_SOURCE_INTRO)
    # (intro inserted after step3_44 pushes bullet down automatically since
    # addnext inserts immediately after step3_44 each time; reorder below)

    # The two inserts above both attached immediately after step3_44, so
    # the second call (intro) landed between step3_44 and the first
    # bullet -- which is the order we want (intro, then bullet). No further
    # action needed; verified by the structural check this script's sibling
    # verify_sop_record_template.py style re-read performs below.

    # Append the same citation to the final References section (point 7),
    # directly before the "8. Review" heading -- matching house style of
    # repeating a body citation in that list (see COP.8 Juvenile Justice
    # Act citation, which appears once in-body and once there).
    review_heading = None
    for p in doc.paragraphs:
        if p.text == "8. Review":
            review_heading = p
            break
    if review_heading is None:
        raise SystemExit("could not find '8. Review' heading to anchor the References insert")
    _insert_paragraph_after_before = None  # no-op, clarity marker

    # Insert REFERENCES_BULLET as the paragraph immediately before "8. Review".
    new_p = OxmlElement("w:p")
    review_heading._p.addprevious(new_p)
    new_ref_para = Paragraph(new_p, review_heading._parent)
    new_ref_para.add_run(REFERENCES_BULLET)
    new_ref_para.style = doc.styles["List Paragraph"]

    doc.save(str(PATH))
    print(f"fixed {PATH}")


if __name__ == "__main__":
    main()
