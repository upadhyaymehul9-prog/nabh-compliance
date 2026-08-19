# -*- coding: utf-8 -*-
"""AAC.8 v2 — discharge process and discharge summary.

Shape follows PRE v2 adoptable-policy shape. Wording from AAC.8 OEs (NABH SHCO
3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 60.
No stop-work. Disclaimer P2 accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, emit_pre_v2

STANDARD_CODE = "AAC.8"
CHAPTER = "AAC"
OE_CODES = [
    "AAC.8.a", "AAC.8.b", "AAC.8.c", "AAC.8.d",
    "AAC.8.e", "AAC.8.f", "AAC.8.g",
]
POLICY_TITLE = "Discharge Process and Discharge Summary"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "AAC v2 template: plain English, AAC roles, seven steps, no stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation has an established discharge process, and defines the content of "
    "the discharge summary — so that every patient leaves with a complete, understandable record."
)

PURPOSE = f"""This policy says how {HOSPITAL} gives a discharge summary to all patients leaving the organisation (including those leaving against medical advice), what the discharge summary contains (identification, dates, reasons, findings, diagnosis, condition, investigations, procedures, medications, treatment, follow-up, urgent-care instructions, and cause of death where applicable), how the organisation adheres to planned discharge, and how special needs following discharge are identified.

The chapter intent is that the discharge process is orderly and the discharge summary is complete and understandable.

This policy owns the discharge process and discharge summary content. AAC.7 owns continuity during care. AAC.3 owns assessment and care planning. MOM.9 owns implant batch/serial in the discharge summary (boundary: implant traceability is MOM.9's requirement, not duplicated here). PRE.2 owns the patient's right of access to records.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to treating doctors, nurses, registration/front-office staff, the Medical Superintendent and the Quality Coordinator at {HOSPITAL}.

It covers the seven elements AAC.8.a–g: discharge summary given to all patients, identification and dates, clinical content, follow-up and instructions, urgent-care instructions, death summary, and planned discharge with special-needs identification.

Boundaries:

- MOM.9 owns implant batch/serial in the discharge summary. This policy does not duplicate that requirement.
- AAC.2 owns transfer-out. This policy owns discharge (patient leaving the hospital's care).
- PRE.3 owns consent including for discharge against medical advice.
- PRE.5 owns final billing explanation. This policy owns the clinical discharge summary."""

POLICY_STATEMENT = f"""{HOSPITAL} gives a discharge summary to every patient leaving the organisation, including patients leaving against medical advice. The discharge summary contains identification, dates, clinical content, follow-up advice and urgent-care instructions in an understandable manner. In case of death the summary includes the cause of death. The organisation adheres to planned discharge and identifies special needs following discharge.

{HOSPITAL} does not discharge a patient without a complete discharge summary, and does not ignore special needs that affect care after discharge."""

NON_NEGOTIABLES = f"""1. Do not discharge a patient (including against medical advice) without giving a discharge summary.
2. Do not issue a discharge summary missing the patient's name, unique identification number, date of admission or date of discharge.
3. Do not issue a discharge summary that omits the reason for admission, significant findings, diagnosis, condition at discharge, investigation results, procedures, medications, treatment, follow-up advice or urgent-care instructions.
4. Do not discharge without identifying special needs that affect care following discharge (e.g. wound care, mobility aids, home nursing, dietary needs).
5. Staff who see a discharge rule broken report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Discharge summary given to all patients

A discharge summary is given to all patients leaving {HOSPITAL}, including patients leaving against medical advice (LAMA). The discharge summary is prepared by the treating doctor or under the treating doctor's supervision and is given to the patient or the patient's representative before or at the time of discharge.

For LAMA patients, the discharge summary includes what was advised, the risks of leaving, and that the patient left against medical advice. The LAMA documentation stays with PRE.3 (consent); this step owns the summary content.""",

f"""5.2 Patient identification and dates

The discharge summary contains:

- patient's name;
- unique identification number (as generated under AAC.2.b);
- date of admission;
- date of discharge.

These four fields are mandatory on every discharge summary. The registration/front-office team verifies that the identification and dates are correct before the summary is released.""",

f"""5.3 Clinical content

The discharge summary contains:

- reasons for admission;
- significant findings;
- diagnosis (provisional and/or final);
- the patient's condition at the time of discharge;
- information regarding investigation results;
- any procedure performed;
- medication administered during the stay;
- other treatment given.

The treating doctor ensures that the clinical content is accurate, complete and written in language the patient or family can understand (medical terminology may be used alongside a plain-language explanation where needed).""",

f"""5.4 Follow-up advice, medication and instructions

The discharge summary contains follow-up advice, medication and other instructions in an understandable manner:

- follow-up date or timeframe;
- medications prescribed at discharge with dose, frequency, route and duration;
- diet, activity and wound-care instructions where applicable;
- warning signs that should prompt an earlier visit;
- contact number for queries after discharge.

Instructions are explained verbally to the patient and/or family by the treating doctor or nurse and are documented in the discharge summary in the language the patient understands — {D('Hindi and English')}.""",

f"""5.5 Urgent-care instructions

The discharge summary incorporates instructions about when and how to obtain urgent care:

- symptoms or signs that require immediate return to the hospital;
- how to reach {HOSPITAL}'s emergency department — {D('telephone number and address')};
- alternative emergency contact if {HOSPITAL} is unreachable — {D('nearest referral hospital name and number, or 108/112 ambulance service')}.

These instructions are explained verbally and documented in the discharge summary.""",

f"""5.6 Death summary

In case of death, the summary of the case also includes the cause of death. The death summary contains:

- all fields of the discharge summary (identification, dates, clinical content);
- the cause of death as determined by the treating doctor;
- time of death;
- whether a post-mortem was advised and the family's decision;
- any medico-legal reporting done.

The death summary is given to the next of kin. A copy is retained in the patient file.""",

f"""5.7 Planned discharge and special needs

The organisation adheres to planned discharge and identifies special needs regarding care following discharge:

- the treating doctor discusses the expected date of discharge with the patient and family early in the stay and updates it as the clinical situation changes;
- before discharge, special needs are identified: {D('wound care, physiotherapy, mobility aids, home nursing, dietary needs, oxygen, follow-up investigations, referral to another facility')};
- where special needs are identified, the discharge plan includes how those needs will be met — {D('written instructions, referral letter, equipment arranged, or family trained')};
- the nurse confirms that the patient and family understand the discharge plan and special-needs arrangements before the patient leaves.

Planned discharge reduces unexpected delays and readmissions.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that the discharge process is established and discharge summaries are complete.

Treating doctors
- Prepare the discharge summary, explain follow-up and urgent-care instructions, identify special needs, and write the death summary where applicable.

Nurses
- Assist with discharge planning, explain instructions, confirm understanding, and identify special needs.

Registration / front-office staff
- Verify identification and dates on the discharge summary; coordinate the administrative discharge process.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when discharge-summary defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Every discharged patient (including LAMA) received a discharge summary.
- Discharge summaries contain all mandatory fields: name, unique ID, dates, clinical content, follow-up, medications, urgent-care instructions.
- Death summaries include cause of death.
- Planned discharge discussed early; special needs identified and addressed.
- Patient and family understanding confirmed before discharge.

Root-cause analysis is required when the same discharge-summary defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when discharge processes, summary templates or clinical protocols change."""

TRAINING_ACKNOWLEDGEMENT = f"""All treating doctors, nurses and registration staff are trained on this policy at induction and {D('once a year')} after that. Training covers the discharge summary template, follow-up and urgent-care instructions, death summary, planned discharge and special-needs identification.

Staff acknowledgement

I have read this Discharge Process and Discharge Summary policy of {HOSPITAL}. I will prepare, check and explain the discharge summary as described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('AAC/POL/08')}
Issue number: {D('01')}
Version: {VERSION} (AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.8.
- Internal documents of {HOSPITAL}: discharge summary template; death summary template; discharge checklist; special-needs assessment form; LAMA documentation."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every in-patient ward; emergency; day-care; registration; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 2)
CAPA — corrective and preventive action
LAMA — leaving against medical advice
MOM — Management of Medication (NABH SHCO chapter)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PRE — Patient Rights and Education (NABH SHCO chapter 4)
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.8.a",
        "requirement": "A discharge summary is given to all the patients leaving the organization (including patients leaving against medical advice).",
        "steps": "Section 3; 5.1 Discharge summary given to all patients; Section 4 item 1",
        "responsible": "Treating doctors (prepare); registration staff (release); Quality Coordinator (audit)",
        "records": [
            "Discharge summary for every discharged patient including LAMA.",
            "LAMA discharge summary with advice given, risks stated and LAMA noted.",
            "Quarterly audit of discharge-summary issuance rate.",
        ],
    },
    {
        "oe_code": "AAC.8.b",
        "requirement": "Discharge summary contains the patient's name, unique identification number, date of admission and date of discharge.",
        "steps": "Section 3; 5.2 Patient identification and dates; Section 4 item 2",
        "responsible": "Registration staff (verify); treating doctors (complete)",
        "records": [
            "Discharge summary with name, unique ID, admission date and discharge date.",
            "Registration verification record before summary release.",
            "Quarterly audit sample of identification completeness.",
        ],
    },
    {
        "oe_code": "AAC.8.c",
        "requirement": "Discharge summary contains the reasons for admission, significant findings and diagnosis, the patient's condition at the time of discharge, information regarding investigation results, any procedure performed, medication administered and other treatment given.",
        "steps": "Section 3; 5.3 Clinical content; Section 4 item 3",
        "responsible": "Treating doctors (write clinical content accurately and completely)",
        "records": [
            "Discharge summary with all clinical content fields completed.",
            "Investigation results referenced or attached.",
            "Quarterly audit sample of clinical-content completeness.",
        ],
    },
    {
        "oe_code": "AAC.8.d",
        "requirement": "Discharge summary contains follow-up advice, medication and other instructions in an understandable manner.",
        "steps": "Section 3; 5.4 Follow-up advice, medication and instructions; Section 4 item 3",
        "responsible": "Treating doctors (prescribe and explain); nurses (explain and confirm understanding)",
        "records": [
            "Discharge summary with follow-up date, medications, diet, activity and warning signs.",
            "Record of verbal explanation to patient and/or family.",
            "Quarterly audit sample of instruction completeness and understandability.",
        ],
    },
    {
        "oe_code": "AAC.8.e",
        "requirement": "Discharge summary incorporates instructions about when and how to obtain urgent care.",
        "steps": "Section 3; 5.5 Urgent-care instructions; Section 4 item 3",
        "responsible": "Treating doctors (write); nurses (explain)",
        "records": [
            "Discharge summary with urgent-care symptoms, hospital emergency contact and alternative contact.",
            "Record of verbal explanation of urgent-care instructions.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "AAC.8.f",
        "requirement": "In case of death, the summary of the case also includes the cause of death.",
        "steps": "Section 3; 5.6 Death summary",
        "responsible": "Treating doctors (write death summary); Medical Superintendent (review where required)",
        "records": [
            "Death summary with cause of death, time of death and all clinical content fields.",
            "Record of post-mortem advice and family decision.",
            "Copy retained in patient file and given to next of kin.",
        ],
    },
    {
        "oe_code": "AAC.8.g",
        "requirement": "The organisation adheres to planned discharge and identify special needs regarding care following discharge.",
        "steps": "Section 3; 5.7 Planned discharge and special needs; Section 4 item 4",
        "responsible": "Treating doctors (plan and identify); nurses (confirm understanding); Quality Coordinator (audit)",
        "records": [
            "Expected discharge date discussed and documented early in the stay.",
            "Special-needs assessment before discharge with plan for meeting each need.",
            "Patient and family confirmation of understanding before discharge.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """AAC.8 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. No asterisked OEs in a–f; AAC.8.e is Achievement, AAC.8.g is Excellence. No stop-work. P2: accreditation-only. Seven OEs, seven What-we-do subsections."""


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
        "template_test": "aac_v2_adoptable_shape",
        "subtitle": "Discharge process, discharge summary and death summary.",
        "doc_no": D("AAC/POL/08"),
    }
    emit_pre_v2(
        draft,
        "aac8_v2_draft.json",
        "AAC.8_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
