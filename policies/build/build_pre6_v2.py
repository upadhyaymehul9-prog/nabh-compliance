# -*- coding: utf-8 -*-
"""PRE.6 v2 — patient feedback and complaint redressal.

Wording from PRE.6 OEs (NABH SHCO 3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed page 89 / PDF index 95. Header uses "organization"; OEs use "organisation".
No stop-work. Disclaimer accreditation-only (v2 template).
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PRE.6"
CHAPTER = "PRE"
OE_CODES = ["PRE.6.a", "PRE.6.b", "PRE.6.c", "PRE.6.d"]
POLICY_TITLE = "Patient Feedback and Complaint Redressal"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PRE v2 template: four steps, grievance officer role, no stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation has a mechanism to capture patient's feedback and to redress complaints — "
    "not a suggestion box that is never opened, or a route that sends the complaint only to the person complained of."
)

PURPOSE = f"""This policy says how {HOSPITAL} captures feedback including patient satisfaction; captures the patient experience; redresses complaints as per a defined mechanism and makes patients and families aware of the procedure; and reviews and analyses within a defined time frame with corrective and/or preventive action where appropriate.

A complaint that is also a rights violation is received here and is also a PRE.1.d report. PRE.1.e owns leadership review of violations. Neither record replaces the other.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies wherever a patient or family can give feedback or lodge a complaint: registration, out-patient, emergency, in-patient, day-care, and after discharge if this hospital accepts post-discharge feedback.

It binds staff who collect feedback, the {D('grievance and feedback officer')} who receives complaints, the {D('Patient Rights Officer')}, and the {D('Medical Superintendent')} who reviews analysis.

Boundaries:

- PRE.2.h lists the right to complain; this policy owns the mechanism.
- PRE.6.c awareness of this procedure is not the PRE.1.a rights board counted twice.
- PRE.5 cost disputes are complaints here; tariff remains PRE.5.
- MOM.7 still captures medication events; family complaints about them are redressed here."""

POLICY_STATEMENT = f"""{HOSPITAL} has a mechanism to capture feedback from patients, which includes patient satisfaction.

{HOSPITAL} has a mechanism to capture the patient experience.

{HOSPITAL} redresses patient complaints as per the defined mechanism. Patients and/or family members are made aware of the procedure for giving feedback and/or lodging complaints.

{HOSPITAL} reviews and/or analyses feedback and complaints within a defined time frame and takes corrective and/or preventive action based on the analysis where appropriate.

{HOSPITAL} does not treat an unopened box, or a complaint route that goes only to the person complained of, as that mechanism."""

NON_NEGOTIABLES = f"""The following are prohibited.

1. Receiving complaints only through the person alleged to have caused the harm.
2. Treating a suggestion box as redressal without opening, recording and responding.
3. Harvesting a "no complaint" signature at discharge as awareness of the procedure.
4. Letting a rights-violation complaint skip the PRE.1.d violation log when it is also a rights violation.
5. Printing District Commission forms or rupee ex-gratia tables as NABH mandates.

Staff report an unusable route to the {D('grievance and feedback officer')} or {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Feedback including patient satisfaction

The organisation has a mechanism to capture feedback from patients, which includes patient satisfaction.

Feedback is captured by {D('a form at registration, a post-discharge phone call, and a conversation when the patient is leaving the ward')}. Dissatisfied feedback that asks for redressal is also a complaint at section 5.3.""",

f"""5.2 Patient experience

The organisation has a mechanism to capture the patient experience.

Experience capture asks what happened to this patient — {D('wait time, dignity, communication, pain control')} — not only whether they would recommend the hospital. It is distinct from the satisfaction score in section 5.1.""",

f"""5.3 Complaint redressal and awareness of the procedure

The organisation redresses patient complaints as per the defined mechanism. Patient and/or family members are made aware of the procedure for giving feedback and/or lodging complaints.

Complaints are received by the {D('grievance and feedback officer')} using {D('complaint box, helpline number on the display board, and written form at registration')}. The route is not only the person complained of. Investigation, outcome to the complainant, and recording are defined in writing held with the Patient Rights Officer.

Patients and families are told the procedure at entry, during stay, and at discharge if post-discharge feedback is accepted — in {D('Hindi and English')}. Awareness of this procedure is not the PRE.1 rights board counted twice.

A complaint that alleges a rights violation also enters the PRE.1.d violation log. PRE.1.e still owns leadership review of violations. Reader et al. (2014) is a taxonomy framework, not a pasted coding protocol.""",

f"""5.4 Review, analysis and CAPA within a defined time frame

Feedback and complaints are reviewed and/or analysed within a defined time frame. Corrective and/or preventive action(s) are taken based on the analysis where appropriate.

The Medical Superintendent reviews the complaint log {D('monthly')} (every month). CAPA is dated with an owner. PRE.1.e analyses rights violations as violations; this step analyses feedback and complaints as feedback and complaints.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable for capture, redressal, awareness and analysis.
- Reviews complaint log monthly; signs CAPA.

Grievance and feedback officer
- Receives complaints unless the alleged actor is this officer — then the Medical Superintendent receives them.
- Authors feedback, experience, redressal and awareness methods with Patient Rights Officer.

Patient Rights Officer
- Holds display of the procedure and links rights-violation complaints to PRE.1.d.

Registration and ward staff — collect feedback and tell patients the procedure.

Quality Coordinator — audits {D('quarterly')}."""

MONITORING_AUDIT = f"""The Quality Coordinator audits {D('quarterly')} for: feedback including satisfaction captured; experience distinct from score; complaints not received only by alleged actor; patients made aware of procedure; analysis within defined time frame with CAPA; rights-violation complaints also in PRE.1.d log.

Reviewed {D('annually')} or when PRE.1 or PRE.2 change."""

TRAINING_ACKNOWLEDGEMENT = f"""Registration, ward and billing staff train at induction and {D('once a year')} on how a patient lodges feedback or a complaint and who receives it.

Staff acknowledgement — I will not send a complaint only to the person complained of.


Name: ___________________________    Designation: ___________________________

Date: ____________    Signature: ___________________________


(Grievance and feedback officer holds acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PRE/POL/06"),
    version=VERSION,
    prepared_by=D("grievance and feedback officer"),
    extra_lines=f"Complaint route: {D('complaint box / helpline / registration form')}\nReview time frame: {D('monthly')}",
)

REFERENCES = f"""- NABH SHCO 3rd Edition — standard PRE.6.
- Reader TW, Gillespie A and Roberts J (2014) — ch 17; complaint taxonomy framework; not pasted protocol.
- Internal documents of {HOSPITAL}: feedback mechanism; experience mechanism; complaint-redressal mechanism; awareness method; PRE.1 violation log; PRE.5 expected-costs policy."""

DISTRIBUTION = f"""Master copy: Medical Superintendent, grievance and feedback officer, Patient Rights Officer, Quality Coordinator.

Copies: registration, every ward, nursing administration, billing desk.

Procedure posted at {D('registration counter and each ward entrance')}. Policy at {D('front-office policy file')}."""

ABBREVIATIONS = """CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
PRE — Patient Rights and Education
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PRE.6.a",
        "requirement": "The organisation has a mechanism to capture feedback from patients, which includes patient satisfaction.",
        "steps": "Statement of intent; Section 3; 5.1 Feedback including patient satisfaction",
        "responsible": "Grievance and feedback officer (mechanism); staff who collect feedback",
        "records": [
            "Written feedback mechanism including how satisfaction is captured.",
            "Sample feedback records with date and setting.",
            "Record that dissatisfied feedback asking for redressal enters complaint process.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.6.b",
        "requirement": "The organisation has a mechanism to capture the patient experience.",
        "steps": "Section 3; 5.2 Patient experience",
        "responsible": "Grievance and feedback officer (experience method); ward and registration staff",
        "records": [
            "Written experience-capture method distinct from satisfaction score.",
            "Sample experience records — what happened to this patient.",
            "Quarterly audit sample.",
            "No named survey printed as NABH mandate.",
        ],
    },
    {
        "oe_code": "PRE.6.c",
        "requirement": "The organisation redresses patient complaints as per the defined mechanism. Patient and/or family members are made aware of the procedure for giving feedback and/or lodging complaints.",
        "steps": "Statement of intent; Section 3; 5.3 Complaint redressal and awareness; Section 4 items 3, 5",
        "responsible": "Grievance and feedback officer (redressal and awareness); Medical Superintendent if alleged actor is officer; PRE.1.d for rights violations",
        "records": [
            "Written complaint-redressal mechanism: who receives, investigation, outcome to complainant.",
            "Written awareness method at entry, during stay and after discharge if accepted.",
            "Sample complaints redressed and sample awareness records.",
            "Rights-violation complaints also in PRE.1.d log without replacing PRE.1.e review.",
        ],
    },
    {
        "oe_code": "PRE.6.d",
        "requirement": "Feedback and complaints are reviewed and/or analysed within a defined time frame. Corrective and/or preventive action(s) are taken based on the analysis where appropriate.",
        "steps": "Section 3; 5.4 Review, analysis and CAPA",
        "responsible": "Medical Superintendent (review); Quality Coordinator (audit trail); PRE.1.e (violation CAPA when applicable)",
        "records": [
            "Written defined time frame and who reviews.",
            "Monthly review minutes with dated CAPA and owner where appropriate.",
            "Recorded split that PRE.1.e analyses rights violations separately.",
            "Quarterly audit sample of reviews within time frame.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PRE.6 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Header "organization"; OEs "organisation". PRE.6.c asterisked. Accreditation-only P2 (v2 template). No stop-work. Split with PRE.1.d/e documented."""


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
        "template_test": "pre_v2_adoptable_shape",
        "subtitle": "Feedback, complaints and redressal patients can actually use.",
        "doc_no": D("PRE/POL/06"),
    }
    emit_pre_v2(
        draft,
        "pre6_v2_draft.json",
        "PRE.6_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
