# -*- coding: utf-8 -*-
"""HCO AAC.4 v2 — initial assessment (HCO Full, 6th Edition).

Shape follows PRE/SHCO v2 adoptable-policy shape via pre_v2_common.
Wording from NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition
— AAC chapter (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices 69–72.
OCR source: policies/source/hco6_aac_ocr.txt.

Seven OEs (a–g). Asterisk on a, b, c. Core on a, e. Achievement f. Excellence g.
No stop-work (no genuine do-not-proceed gate beyond emergency stabilisation).
Does NOT overwrite SHCO AAC builders or drafts.
"""
from __future__ import annotations

import sys

from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, document_control, emit_pre_v2

STANDARD_CODE = "AAC.4"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.4.a",
    "AAC.4.b",
    "AAC.4.c",
    "AAC.4.d",
    "AAC.4.e",
    "AAC.4.f",
    "AAC.4.g",
]
POLICY_TITLE = "Initial Assessment"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO Full 6th Edition AAC.4 v2 draft: plain English, seven steps, no stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Every patient undergoes a standardised initial assessment by qualified personnel "
    "within a defined time — producing a documented care plan for in-patients that the "
    "clinician in-charge authorises and that notes special needs after discharge."
)

PURPOSE = f"""This policy says how {HOSPITAL} performs standardised initial assessment for out-patients, day-care, in-patients and emergency patients; ensures assessment is done by qualified personnel within their scope of practice; completes assessment within a time frame based on patient need; includes nursing assessment at admission for day-care and in-patients; documents a care plan from the in-patient initial assessment; obtains countersignature by the clinician in-charge within 24 hours; and identifies special needs regarding care following discharge.

The chapter intent is that patients undergo initial assessment and periodic reassessments resulting in a care plan.

This policy owns initial assessment and the care plan that results from it. AAC.5 owns re-assessment and modification of the care plan. AAC.2 owns registration before assessment. COP.10.d and COP.11.e are correlated where the guidebook points (procedural/daycare pathways) — this policy does not rewrite those COP procedures.

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to treating doctors, nurses and other caregivers who perform initial assessment at {HOSPITAL} in out-patient, day-care (including dialysis day-care), in-patient wards and emergency. It binds department heads who define who may assess, the Medical Superintendent, Medical Records, and the Quality Coordinator.

It covers AAC.4.a–g.

Boundaries:

- AAC.5 owns re-assessment intervals, care-plan modification after initial assessment, and early-warning escalation.
- AAC.2 owns that the patient is registered and admitted before or alongside assessment.
- COP.10 / COP.11 own specific procedural pathways referenced by the guidebook (COP 10.d, COP 11.e); initial assessment for those pathways still uses this standard's formats.
- Lab and imaging own result reporting; this policy owns that available diagnostics inform the care plan.
- Psychological, spiritual, cultural, social and economic aspects of in-patient assessment may be done by various healthcare professionals within their scope — named in the assessment privilege list under AAC.4.b."""

POLICY_STATEMENT = f"""{HOSPITAL} performs initial assessment of out-patients, day-care, in-patients and emergency patients in a standardised manner. Assessment is performed by qualified personnel within their scope of practice, registration and applicable laws. Assessment is completed within a documented time frame based on patient needs — for in-patients within a maximum of 24 hours from arrival at the ward; for emergency from the time of arrival. Day-care and in-patient initial assessment includes nursing assessment at admission. The in-patient initial assessment results in a documented care plan. The care plan is countersigned by the clinician in-charge within 24 hours. The care plan identifies special needs regarding care following discharge.

{HOSPITAL} does not leave an in-patient without a documented care plan, and does not treat the 24-hour maximum as a target when clinical need requires earlier assessment."""

NON_NEGOTIABLES = f"""1. Do not use a non-standard assessment format in an area that has an approved standardised format for that area.
2. Do not omit vital parameters in emergency initial assessment; do not omit history, examination including vitals, drug allergies and provisional diagnosis for in-patients; do not omit medication reconciliation for in-patients.
3. Do not allow a person to perform an assessment outside their defined scope of practice and privilege.
4. Do not exceed the defined time frames — in-patient initial assessment maximum 24 hours from ward arrival; emergency from arrival to completion as defined.
5. Do not omit nursing assessment at admission for day-care and in-patients.
6. Do not continue planned in-patient treatment beyond emergency stabilisation without a documented care plan from the initial assessment.
7. Do not leave a care plan initiated by a junior doctor without countersignature by the clinician in-charge within 24 hours.
8. Staff who find assessment or care-plan rules not followed report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Standardised initial assessment (OP, day-care, IP, emergency)

{HOSPITAL} uses a standardised format for initial assessment in the OPD, day-care, in-patient and emergency areas. Formats may differ by department need but are the same within a particular area or unit. Formats capture the laid-down parameters.

Emergency initial assessment includes recording vital parameters.

In-patient initial assessment covers history, examination including vital signs, documentation of any drug allergies, and provisional diagnosis. If a detailed assessment was done earlier the same day in OPD or emergency, it need not be rewritten in full; a comment links to the earlier assessment, and findings of all such assessments are reviewed and/or verified.

Initial assessment includes reconciliation of medications for in-patients.

Abridged documentation may be used for day-care as appropriate, including patients coming for dialysis.

Where pathways intersect COP.10.d or COP.11.e, use those COP procedures for the procedural elements and this policy's formats for the initial assessment elements.""",

f"""5.2 Performed by qualified personnel within scope of practice

{HOSPITAL} determines who can do which assessment. Caregivers perform initial assessment within their scope of practice, registration and applicable laws and regulations. Psychological, spiritual, cultural, social and economic aspects of in-patient initial assessment may be done by various healthcare professionals as named on the privilege list.

The organisation defines how contents of assessment (initial and diagnostic) performed by a qualified and privileged healthcare professional associated with the hospital — for example a visiting consultant's referral assessment — are accepted into the patient-care system.

Department heads maintain the assessment privilege list; the Medical Superintendent approves it.""",

f"""5.3 Within a time frame based on patient needs

{HOSPITAL} defines and documents the time frame for completing initial assessment for day-care, in-patients and emergency, and implements it.

For in-patients, the clock starts when the patient arrives at the ward and stops when initial assessment is completed. The maximum time is 24 hours. Patients are assessed earlier when clinical need requires — defaults: {D('unstable or high-dependency within 1 hour; routine ward within 6 hours where staffing allows, and always within 24 hours')}.

For emergency, the clock starts at arrival at emergency and stops when initial assessment is completed — default {D('primary survey and vitals immediately; full emergency initial assessment within 30 minutes unless resuscitation is ongoing')}.

Day-care time frames are defined per service — default {D('before the planned procedure or dialysis session begins')}.""",

f"""5.4 Nursing assessment at admission for day-care and in-patients

Initial assessment of day-care and in-patients includes nursing assessment at the time of admission, documented in the record. It identifies nursing needs and any special needs of the patient, completed within a defined time frame — default {D('within 1 hour of ward or day-care arrival')}.

A checklist or template may be used. Abridged nursing documentation may be used for day-care as appropriate. Templates may be specific to the speciality or type of admission.""",

f"""5.5 Documented care plan from in-patient initial assessment

For in-patients, the initial assessment results in a documented care plan. The care plan is written by the treating doctor or a doctor member of the treating team in the patient record and is followed.

The care plan is based on the initial assessment and results of diagnostic tests if available. It includes provisional diagnosis or differential diagnosis, relevant diagnostic investigations when required, initial treatment suggested, and specific instructions if any. It reflects the desired results of the treatment, care or service. It is subject to modification at re-assessment under AAC.5.""",

f"""5.6 Care plan countersigned by clinician in-charge within 24 hours

Treatment may be initiated by a junior doctor, but the care plan is countersigned and authorised by the treating doctor — the clinician in-charge — within 24 hours. Countersignature is dated and timed in the record.

If the clinician in-charge will be unavailable beyond 24 hours, the covering consultant named for that period countersigns and the Medical Superintendent is informed.""",

f"""5.7 Special needs regarding care following discharge

The care plan includes identification of special needs regarding care following discharge. Identification is critical for groups such as extremes of age, restricted mobility, continuing nursing and rehabilitation needs, and assistance with activities of daily living.

{HOSPITAL} begins identifying special discharge needs early in the assessment process — not only on the day of discharge. Nursing and medical assessments both contribute. Detailed discharge process remains under AAC.12; this step owns early identification inside the care plan.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable for standardised formats, privilege lists and time frames.
- Approves assessment formats and privilege lists.

Department heads
- Maintain area-specific formats and who may assess.
- Ensure medication reconciliation and care-plan quality in their units.

Treating doctors / clinician in-charge
- Perform or supervise initial assessment; document care plan; countersign within 24 hours; identify special discharge needs.

Junior doctors
- May initiate assessment and treatment; must obtain countersignature within 24 hours.

Nurses
- Complete nursing assessment at admission for day-care and in-patients; contribute special-needs identification.

Medical Records
- Ensure formats are available in records; flag missing care plans or countersignatures in record review.

Quality Coordinator
- Audits formats, time frames, nursing assessment, care plans, countersignatures and discharge-needs identification {D('quarterly')}."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Standardised formats in use in OPD, day-care, IP and emergency; vitals in emergency; IP content and medication reconciliation complete.
- Persons who performed initial assessment match the privilege list.
- In-patient assessments completed within 24 hours of ward arrival; emergency within defined time from arrival.
- Nursing assessment documented at admission for day-care and IP sample.
- Care plan present for IP sample; countersigned by clinician in-charge within 24 hours.
- Special discharge needs identified in care plans for applicable patients.

Root-cause analysis is required when missing care plans or late countersignatures recur within six months.

This policy is reviewed {D('annually')}, and sooner when formats or privilege lists change."""

TRAINING_ACKNOWLEDGEMENT = f"""Doctors, nurses and other caregivers who assess patients are informed of this policy at induction and {D('once a year')} after that. Training covers area formats, privilege limits, time frames, medication reconciliation, nursing assessment, care-plan content, 24-hour countersignature, and early identification of special discharge needs.

Staff acknowledgement

I have read this Initial Assessment policy of {HOSPITAL}. I will assess only within my privilege, complete assessment within the defined time, document the care plan for in-patients, and obtain or provide countersignature within 24 hours.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with clinical induction records.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/04"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care (AAC), standard AAC.4.
- Correlated standards named in the guidebook interpretation: COP.10.d; COP.11.e.
- Internal documents of {HOSPITAL}: initial-assessment formats (OP, day-care, IP, emergency); assessment privilege list; nursing-assessment templates; care-plan template; medication-reconciliation form; AAC.5 re-assessment policy; AAC.12 discharge policy."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every clinical department; emergency; day-care; nursing administration; medical records; OPD.

The current version is available to all staff at the {D('clinical policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH Hospitals chapter)
CAPA — corrective and preventive action
COP — Care of Patients (NABH chapter)
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
IP — in-patient
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
OP / OPD — out-patient / out-patient department"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.4.a",
        "requirement": "The initial assessment of the out-patients, daycare, in-patients and emergency patients is done in a standardised manner.",
        "steps": "Section 3; 5.1 Standardised initial assessment (OP, day-care, IP, emergency); Section 4 items 1–2",
        "responsible": "Department heads (formats); treating doctors (complete); nurses (contribute); Quality Coordinator (hold formats)",
        "records": [
            "Approved standardised initial-assessment formats for OPD, day-care, IP and emergency.",
            "Emergency records showing vital parameters recorded at initial assessment.",
            "IP records showing history, examination including vitals, drug allergies, provisional diagnosis and medication reconciliation.",
            "Day-care records using abridged documentation where appropriate (including dialysis).",
            "Linking comments when same-day OPD/emergency assessment is reused for IP.",
        ],
    },
    {
        "oe_code": "AAC.4.b",
        "requirement": "The initial assessment is performed by qualified personnel.",
        "steps": "Section 3; 5.2 Performed by qualified personnel within scope of practice; Section 4 item 3",
        "responsible": "Medical Superintendent (approve privilege list); department heads (maintain); caregivers (assess within scope)",
        "records": [
            "Assessment privilege list naming who may perform which assessment.",
            "Credentials and registration evidence for privileged clinicians who perform assessment.",
            "Process document for accepting assessments from qualified privileged professionals associated with the hospital (e.g. visiting consultant).",
            "Sample records showing the person who assessed matches the privilege list.",
        ],
    },
    {
        "oe_code": "AAC.4.c",
        "requirement": "The initial assessment is performed within a time frame based on the needs of the patient.",
        "steps": "Section 3; 5.3 Within a time frame based on patient needs; Section 4 item 4",
        "responsible": "Treating doctors (complete on time); department heads (define specialty defaults); Quality Coordinator (audit)",
        "records": [
            "Written time-frame document for day-care, IP and emergency initial assessment.",
            "IP sample with ward-arrival time and assessment-completion time within 24 hours.",
            "Emergency sample with arrival time and assessment-completion time within the defined frame.",
            "Day-care sample showing assessment before procedure/session as defined.",
        ],
    },
    {
        "oe_code": "AAC.4.d",
        "requirement": "Initial assessment of daycare and in-patients includes nursing assessment, which is done at the time of admission and documented.",
        "steps": "Section 3; 5.4 Nursing assessment at admission for day-care and in-patients; Section 4 item 5",
        "responsible": "Nurses (perform and document); nursing administration (templates and time frames)",
        "records": [
            "Nursing-assessment templates/checklists for IP and day-care.",
            "Documented nursing assessments at admission identifying nursing and special needs.",
            "Abridged day-care nursing documentation samples where used.",
            "Defined time frame for completing nursing assessment and audit against it.",
        ],
    },
    {
        "oe_code": "AAC.4.e",
        "requirement": "The initial assessment for in-patients results in a documented care plan.",
        "steps": "Section 3; 5.5 Documented care plan from in-patient initial assessment; Section 4 item 6",
        "responsible": "Treating doctor or doctor member of treating team (document); Medical Records (presence in record)",
        "records": [
            "Documented care plans in IP records including provisional/differential diagnosis.",
            "Care-plan entries for relevant investigations, initial treatment and specific instructions.",
            "Evidence the care plan reflects desired results of treatment, care or service.",
            "Audit sample of IP admissions with care plan present after initial assessment.",
        ],
    },
    {
        "oe_code": "AAC.4.f",
        "requirement": "The care plan is countersigned by the clinician in-charge of the patient within 24 hours.",
        "steps": "Section 3; 5.6 Care plan countersigned by clinician in-charge within 24 hours; Section 4 item 7",
        "responsible": "Clinician in-charge / treating doctor (countersign); junior doctors (seek countersignature)",
        "records": [
            "Care plans with dated/timed countersignature by clinician in-charge within 24 hours.",
            "Covering-consultant countersignatures when treating doctor unavailable, with Medical Superintendent notified.",
            "Audit log of late or missing countersignatures with corrective action.",
        ],
    },
    {
        "oe_code": "AAC.4.g",
        "requirement": "The care plan includes the identification of special needs regarding care following discharge.",
        "steps": "Section 3; 5.7 Special needs regarding care following discharge; Section 4 item 8",
        "responsible": "Treating doctors and nurses (identify early); AAC.12 owners (execute discharge planning)",
        "records": [
            "Care-plan fields or notes identifying special post-discharge needs (age extremes, mobility, nursing/rehab, ADL assistance).",
            "Evidence identification began early in the assessment process, not only on discharge day.",
            "Sample of applicable patients with special needs flagged and handed to discharge planning.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.4 v2 (2026-08-20). HCO Full Accreditation, NABH Hospitals 6th Edition.
PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. OCR: policies/source/hco6_aac_ocr.txt (PDF indices 69–72).

OE COUNT: 7 (a–g). Asterisked: AAC.4.a, AAC.4.b, AAC.4.c (Tier 1). Core: AAC.4.a, AAC.4.e. Achievement: AAC.4.f. Excellence: AAC.4.g. AAC.4.d Commitment without asterisk (Tier 2).

SHAPE: Seven What-we-do subsections (5.1–5.7). No stop-work (no genuine do-not-proceed gate beyond ordinary clinical escalation). Disclaimer accreditation-only. chapter=HCO, doc_no HCO/AAC/POL/04.

GUIDEBOOK CORRELATION: COP 10.d and COP 11.e referenced in AAC.4.a interpretation — cross-noted, not duplicated.

FLAG: OCR level chrome (C@RE / HM core) ignored; OE letters a–g recovered from inventory + interpretation blocks. No unclear OE remaining."""


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
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "HCO Full Accreditation, 6th Edition — initial assessment.",
        "doc_no": D("HCO/AAC/POL/04"),
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with clinical induction records.",
        "stop_work": "",
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.4",
    }
    emit_pre_v2(
        draft,
        "hco_aac4_v2_draft.json",
        "HCO.AAC.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
