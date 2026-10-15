# -*- coding: utf-8 -*-
"""Fixes 4 unsourced/fabricated numeric claims found in the AAC/ROM audit
on 2026-10-10 (same bug class as COP.2.c/d, per audit_chapter.py). Confirmed
against the approved shco_policy_masters content via Supabase: none of
"24 hour", "15 minute", "countersign", or "vacan*" appear anywhere in the
approved master policy text for AAC.3, AAC.4, AAC.7 or ROM.1 -- these
specific numbers were invented at SOP-drafting time with no source.

Unlike COP.2.d (where CTAS gave a real, verified, published reassessment
interval to cite), a web search for each of these three turned up no
single authoritative external standard -- critical-lab-value callback
time, verbal-order countersign window, and governance-vacancy notification
period are all institution-defined in every source found, not set by one
citable body. Per Rule 2.9 (master-policy-todos.md), fabricating a
citation to match an invented number is not an option; the correct fix is
to strip the invented example back to pure "hospital to define", same as
done for the rest of the (uncited) content in these same files.

Run once. Checks old text is present before replacing.
"""
from __future__ import annotations

from pathlib import Path

from docx import Document

FIXES = [
    {
        "path": Path(__file__).parent / "sop_record_masters" / "AAC" / "SOP_AAC.3.a_initial_assessment.docx",
        "old": "2. In-patient assessments are documented within «the hospital-defined time frame, e.g. within 24 hours of admission».",
        "new": "2. In-patient assessments are documented within «the hospital-defined time frame» -- the hospital states this as a specific number of hours in its own SOP; no external body prescribes it.",
    },
    {
        "path": Path(__file__).parent / "sop_record_masters" / "AAC" / "SOP_AAC.4.c_d_e_lab_specimen_tat_critical_results.docx",
        "old": "3. If the treating clinician cannot be reached within a defined time (e.g. 15 minutes), the laboratory escalates to the next person on the facility's on-call or escalation list, and every attempt is logged, not just the one that finally succeeded. (Record 4)",
        "new": "3. If the treating clinician cannot be reached within «the hospital-defined escalation time» -- the hospital states this as a specific number of minutes in its own SOP; no external body prescribes it -- the laboratory escalates to the next person on the facility's on-call or escalation list, and every attempt is logged, not just the one that finally succeeded. (Record 4)",
    },
    {
        "path": Path(__file__).parent / "sop_record_masters" / "AAC" / "SOP_AAC.7.a_b_c_d_continuity_multidisciplinary_care.docx",
        "old": "3. Document every verbal order immediately in the patient file and have the ordering doctor countersign it within «24 hours»; flag any order not countersigned within that window to the Quality Coordinator.",
        "new": "3. Document every verbal order immediately in the patient file and have the ordering doctor countersign it within «the hospital-defined countersignature window» -- the hospital states this as a specific number of hours in its own SOP; no external body prescribes it -- flagging any order not countersigned within that window to the Quality Coordinator.",
    },
    {
        "path": Path(__file__).parent / "sop_record_masters" / "ROM" / "SOP_ROM.1.a_governance_roles.docx",
        "old": "1. When a governance role becomes vacant, the Medical Superintendent notifies the governing body within a defined period (e.g. 7 days).",
        "new": "1. When a governance role becomes vacant, the Medical Superintendent notifies the governing body within «the hospital-defined notification period» -- the hospital states this as a specific number of days in its own SOP; no external body prescribes it.",
    },
    {
        "path": Path(__file__).parent / "sop_record_masters" / "HRM" / "SOP_HRM.4.a_performance_appraisal.docx",
        "old": "1. Where an appraisal finds performance unsatisfactory against the stated criteria, the department head opens a performance improvement plan the same day, naming the specific gaps, the support or training to be provided, and a follow-up review date within a defined period (e.g. 60 days).",
        "new": "1. Where an appraisal finds performance unsatisfactory against the stated criteria, the department head opens a performance improvement plan the same day, naming the specific gaps, the support or training to be provided, and a follow-up review date within «the hospital-defined review period» -- the hospital states this as a specific number of days in its own SOP; no external body prescribes it.",
    },
]


def main() -> None:
    for fix in FIXES:
        doc = Document(str(fix["path"]))
        found = False
        already_done = False
        for p in doc.paragraphs:
            if p.text == fix["old"]:
                p.runs[0].text = fix["new"]
                for r in p.runs[1:]:
                    r.text = ""
                found = True
                break
            if p.text == fix["new"]:
                already_done = True
        if already_done:
            print(f"already fixed, skipping: {fix['path'].name}")
            continue
        if not found:
            raise SystemExit(f"EXPECTED TEXT NOT FOUND in {fix['path'].name} (file changed under this script, or already fixed and not caught above?):\n{fix['old']!r}")
        doc.save(str(fix["path"]))
        print(f"fixed {fix['path'].name}")


if __name__ == "__main__":
    main()
