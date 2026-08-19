# -*- coding: utf-8 -*-
"""COP.4 v2 — nursing care.

Shape follows PRE.1 v2 (section list and order only). Wording from COP.4 OEs
(NABH SHCO 3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed page 69 / PDF index 69.

No stop-work. Disclaimer accreditation-only. Four OEs (COP.4.a–d).
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.4"
CHAPTER = "COP"
OE_CODES = ["COP.4.a", "COP.4.b", "COP.4.c", "COP.4.d"]
POLICY_TITLE = "Nursing Care"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: plain English, COP roles, four OEs, no stop-work, accreditation-only disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "Nursing care is provided to patients in the organization in consonance with clinical "
    "protocols — not a staffing roster that exists on paper while wards run on individual habit."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides nursing care to patients in consonance with clinical protocols.

It covers four elements: nursing care aligned and integrated with overall patient care and documented in the patient record; assignment of patient care as per current good clinical and nursing practice guidelines; appropriate and adequate equipment for safe and efficient nursing services; and development and implementation of nursing clinical practice guidelines reflecting current standards of practice.

The chapter intent is that nursing care is aligned with patient care, follows guidelines, is equipped, and is guided by current practice.

This policy owns nursing care delivery. AAC.3 owns the care plan as a clinical document. COP.1 owns uniform care across settings.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every nursing staff member at {HOSPITAL} and to the settings in which nursing care is provided: in-patient wards, emergency department, out-patient clinics, ICU where it exists, and any other area where nurses deliver care.

It covers the four elements COP.4.a–d name. It does not cover the care plan as a clinical document (AAC.3), uniform care across settings (COP.1), or medication administration as a system (MOM).

Boundaries with other policies of {HOSPITAL}:

- AAC.3 owns the care plan as a clinical document. This policy owns that nursing care is aligned and integrated with that plan.
- COP.1 owns uniform care. This policy owns that nursing care follows adopted guidelines uniformly.
- MOM owns medication management. This policy owns that nurses administer medications as part of nursing care following nursing practice guidelines.
- HIC owns the infection-control programme. This policy owns that nurses follow infection-control practices as part of nursing care."""

POLICY_STATEMENT = f"""{HOSPITAL} aligns nursing care with the overall patient care plan and documents nursing assessments, interventions and outcomes in the patient record. Nursing documentation is part of the patient record, not a separate file that clinicians never read.

{HOSPITAL} assigns patient care as per current good clinical and nursing practice guidelines. Assignment considers patient acuity, nurse competency and workload. A nurse is not assigned more patients than safe practice allows.

{HOSPITAL} provides nurses with appropriate and adequate equipment for safe and efficient nursing services, including {D('patient monitoring equipment, wound care supplies, medication administration equipment, and personal protective equipment')}.

{HOSPITAL} develops and implements nursing clinical practice guidelines reflecting current standards of practice. Guidelines are reviewed {D('annually')} and updated when standards change.

{HOSPITAL} does not treat any of these as meeting this policy: nursing notes that are never read by the treating doctor; patient assignment that ignores acuity; equipment requests that are never fulfilled; or nursing guidelines that exist on paper but are not followed at the bedside."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no staffing convenience exception.

1. Delivering nursing care that is not documented in the patient record, or maintaining nursing documentation separate from the patient record so that treating doctors cannot see it.
2. Assigning patients to nurses without considering patient acuity and nurse competency, or assigning more patients than safe practice allows without escalation to the {D('Nursing Superintendent')}.
3. Continuing to provide nursing care with equipment known to be broken, missing or inadequate without escalating the equipment need.
4. Adopting a nursing clinical practice guideline on paper while the nurses who deliver the care have never read or been trained on it.

Staff who see one of these acts report it the same shift to the {D('Nursing Superintendent')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Nursing care aligned and integrated with overall patient care

Nursing care is aligned and integrated with overall patient care. Nursing assessments, interventions and outcomes are documented in the patient record — the same record the treating doctor uses. AAC.3 owns the care plan as a clinical document; nursing care follows and contributes to that plan.

The nurse documents: initial nursing assessment; ongoing assessments at intervals defined by acuity; nursing interventions performed; patient response; and handover notes. Documentation is legible, timed and signed.

The {D('Nursing Superintendent')} holds the nursing documentation standards and reviews them {D('annually')}.""",

f"""5.2 Patient care assignment as per good clinical and nursing practice

Assignment of patient care is done as per current good clinical and nursing practice guidelines. Assignment considers: patient acuity; complexity of care required; nurse competency and experience; and workload.

The {D('ward in-charge nurse')} assigns patients at each shift using a written assignment method. When the patient load exceeds safe limits, the ward in-charge escalates to the {D('Nursing Superintendent')} the same shift.

The assignment method is reviewed {D('annually')} by the Nursing Superintendent.""",

f"""5.3 Appropriate and adequate equipment for nursing services

Nurses are provided with appropriate and adequate equipment for providing safe and efficient nursing services. Equipment includes: {D('patient monitoring equipment, wound care supplies, medication administration equipment, personal protective equipment, and mobility aids')}.

Equipment needs are assessed {D('annually')} by the Nursing Superintendent in consultation with ward in-charge nurses. Equipment that is broken or missing is reported the same shift and replaced or repaired within {D('the defined turnaround time')}.

An equipment inventory is maintained for each nursing area and reviewed {D('quarterly')}.""",

f"""5.4 Nursing clinical practice guidelines

{HOSPITAL} develops and implements nursing clinical practice guidelines reflecting current standards of practice. Guidelines cover at minimum: {D('nursing assessment, pain management, wound care, medication administration, patient safety, infection prevention, and patient education as they apply to nursing')}.

Guidelines are developed by the {D('Nursing Superintendent in consultation with senior nurses and treating doctors')}, adopted formally, and made available to all nursing staff.

Guidelines are reviewed {D('annually')} and updated when standards of practice change. A guideline that is adopted but never read by the nurses who use it is not an adopted guideline. Training on updated guidelines is completed before the updated guideline takes effect.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that nursing care is provided as this policy requires.
- Approves nursing clinical practice guidelines.

{D('Nursing Superintendent')}
- Holds nursing documentation standards, patient assignment method, equipment inventory and nursing clinical practice guidelines.
- Reviews and updates guidelines annually.
- Receives escalations when patient load exceeds safe limits.

{D('Ward in-charge nurses')}
- Assign patients at each shift using the written assignment method.
- Report broken or missing equipment the same shift.
- Ensure nursing documentation is completed in the patient record.

Nurses
- Document nursing assessments, interventions and outcomes in the patient record.
- Follow adopted nursing clinical practice guidelines at the bedside.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when nursing documentation, assignment or guideline adherence findings recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at records and at the ward.

What is monitored each quarter:

- Nursing assessments, interventions and outcomes are documented in the patient record and aligned with the care plan.
- Patient assignment considers acuity and competency, with escalation records where load exceeded safe limits.
- Equipment inventory is current and broken or missing items are reported and replaced within the defined turnaround.
- Nursing clinical practice guidelines are available to and read by the nurses who use them.

Root-cause analysis is required when the same nursing documentation gap or the same assignment overload finding recurs twice within six months.

This policy is reviewed {D('annually')}, and sooner when a nursing clinical practice guideline is updated or the scope of nursing services changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All nursing staff are trained on this policy at induction and {D('once a year')} after that. Training covers nursing documentation standards, patient assignment, equipment escalation, and adopted nursing clinical practice guidelines.

Staff acknowledgement

I have read this Nursing Care policy of {HOSPITAL}. I will document nursing care in the patient record. I will follow adopted nursing clinical practice guidelines at the bedside.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Nursing Superintendent holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/04"),
    version=VERSION,
    prepared_by=D("Nursing Superintendent"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.4.
- Internal documents of {HOSPITAL}: nursing documentation standards; patient assignment method; nursing equipment inventory; nursing clinical practice guidelines; AAC.3 care plan policy; COP.1 uniform care policy; MOM medication management policy; HIC infection-control programme."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Nursing Superintendent and the Quality Coordinator.

Copies issued to: every in-patient ward; emergency department; out-patient clinics; ICU where it exists; nursing administration.

The current version is available to all nursing staff at the {D('nursing office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
HIC — Hospital Infection Control (NABH SHCO chapter 7)
ICU — intensive care unit
MOM — Management of Medication (NABH SHCO chapter 6)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.4.a",
        "requirement": "Nursing care is aligned and integrated with overall patient care, and is documented in the patient record.",
        "steps": "Section 3; 5.1 Nursing care aligned and integrated with overall patient care; Section 4 item 1",
        "responsible": "Nurses (document); Nursing Superintendent (standards); ward in-charge (ensure completion)",
        "records": [
            "Nursing documentation standards reviewed annually.",
            "Sample patient records showing nursing assessments, interventions and outcomes in the patient record.",
            "Quarterly audit of nursing documentation completeness and alignment with care plan.",
            "Handover notes in the patient record.",
        ],
    },
    {
        "oe_code": "COP.4.b",
        "requirement": "Assignment of patient care is done as per current good clinical / nursing practice guidelines.",
        "steps": "Section 3; 5.2 Patient care assignment as per good clinical and nursing practice; Section 4 item 2",
        "responsible": "Ward in-charge nurses (assign); Nursing Superintendent (method and escalation)",
        "records": [
            "Written patient assignment method reviewed annually.",
            "Shift assignment records showing acuity and competency considered.",
            "Escalation records when patient load exceeded safe limits.",
        ],
    },
    {
        "oe_code": "COP.4.c",
        "requirement": "Nurses are provided with appropriate and adequate equipment for providing safe and efficient nursing services.",
        "steps": "Section 3; 5.3 Appropriate and adequate equipment for nursing services; Section 4 item 3",
        "responsible": "Nursing Superintendent (needs assessment); ward in-charge (report and replace)",
        "records": [
            "Equipment inventory for each nursing area reviewed quarterly.",
            "Annual needs assessment record.",
            "Broken or missing equipment reports and replacement records.",
        ],
    },
    {
        "oe_code": "COP.4.d",
        "requirement": "The organization develops and implements nursing clinical practice guidelines reflecting current standards of practice.",
        "steps": "Section 3; 5.4 Nursing clinical practice guidelines; Section 4 item 4",
        "responsible": "Nursing Superintendent (develop and review); nurses (follow); Medical Superintendent (approve)",
        "records": [
            "List of adopted nursing clinical practice guidelines with adoption and review dates.",
            "Evidence that nursing staff have read the guidelines.",
            "Annual review records for each guideline.",
            "Training records when guidelines are updated.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.4 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Nursing care is provided to patients in the organization in consonance with clinical protocols." COP.4.a–d PDF page 69. COP.4.a asterisked (Commitment). COP.4.d asterisked (Excellence). COP.4.b Commitment. COP.4.c Commitment.

SHAPE: Four What-we-do subsections (5.1–5.4). No stop-work. Disclaimer accreditation-only. COP roles only."""


def main() -> int:
    draft = {
        "standard_code": STANDARD_CODE,
        "chapter": CHAPTER,
        "oe_codes": OE_CODES,
        "policy_title": POLICY_TITLE,
        "purpose": PURPOSE,
        "scope": SCOPE,
        "policy_statement": POLICY_STATEMENT,
        "procedure_steps": PROCEDURE_STEPS,
        "responsibility": RESPONSIBILITY,
        "references_text": REFERENCES,
        "distribution": DISTRIBUTION,
        "abbreviations": ABBREVIATIONS,
        "disclaimer": DISCLAIMER,
        "oe_mapping": OE_MAPPING,
        "universal_facts_checklist": UNIVERSAL_FACTS_CHECKLIST,
        "version": VERSION,
        "revision_history": REVISION_HISTORY,
        "status": "draft",
        "definitions": STATEMENT_OF_INTENT,
        "exceptions": NON_NEGOTIABLES,
        "monitoring_audit": MONITORING_AUDIT,
        "training_competency": TRAINING_ACKNOWLEDGEMENT,
        "resources_required": DOCUMENT_CONTROL,
        "template_test": "cop_v2_adoptable_shape",
        "subtitle": "Nursing care in consonance with clinical protocols.",
        "doc_no": D("COP/POL/04"),
    }
    emit_pre_v2(
        draft,
        "cop4_v2_draft.json",
        "COP.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
