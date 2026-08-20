# -*- coding: utf-8 -*-
"""HCO AAC.13 v2 — content of the discharge summary.

Shape: pre_v2_common.emit_pre_v2 + hco_v2_disclaimer accreditation-only.
Wording from NABH HCO Full Accreditation 6th Edition Guidebook
(PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices ~92–93 /
policies/source/hco6_aac_ocr.txt. Do not copy SHCO AAC wording.

Five OEs a–e. No asterisk. No stop-work.
Boundary: AAC.12 owns process; AAC.13 owns summary content. Cross-ref; do not
duplicate process steps.
"""
from __future__ import annotations

import sys

from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import (
    BLANK,
    D,
    HCO_EDITION_LABEL,
    HOSPITAL,
    document_control,
    emit_pre_v2,
)

STANDARD_CODE = "AAC.13"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.13.a", "AAC.13.b", "AAC.13.c", "AAC.13.d", "AAC.13.e",
]
POLICY_TITLE = "Content of the Discharge Summary"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": (
            "HCO Full 6th Edition AAC.13 v2 draft from guidebook OCR; "
            "five steps; no asterisk; no stop-work; accreditation-only P2."
        ),
    },
]

STATEMENT_OF_INTENT = (
    "The organisation defines the content of the discharge summary — signed, "
    "acknowledged, standardised, understandable, and clear about urgent care "
    "and cause of death where applicable."
)

PURPOSE = f"""This policy says how {HOSPITAL} defines and fills the content of the discharge summary.

It covers five jobs that match the standard:

- provide the discharge summary at discharge, signed, with receipt acknowledged;
- use standardised content (identity, treating doctor, dates, reasons, findings/diagnosis/condition, investigations, procedures, medications, other treatment);
- include follow-up advice, medication and other instructions in an understandable manner (no BD/TID/QID; equipment and wound care where needed);
- include instructions on when and how to obtain urgent care;
- in case of death, include the cause of death (and post-mortem documentation when the cause is unclear or MLC).

The chapter intent is that discharge protocols are well defined and that the patient leaves with a usable clinical record.

This policy owns summary content. AAC.12 owns the discharge process (planning, coordination, LAMA guidance, that a summary is given, planned discharge, domiciliary visits, discharge-time monitoring). Cross-reference AAC.12 for process; do not rewrite process steps here. Cross-reference AAC.4.g for continued-care education elements that appear as instructions. Cross-reference PSQ.4.d for urgent-care instruction alignment.

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every discharge summary and death summary issued at {HOSPITAL}, including summaries for patients leaving against medical advice.

It binds:

- treating doctors (or a doctor member of the treating team) who write and sign the summary;
- nurses who explain instructions and support acknowledgement of receipt;
- registration / front-office who may record hand-over of the copy;
- the {D('discharge coordinator')} if used, who checks that a signed summary is present before the patient leaves;
- the {D('Medical Superintendent')} who is accountable for the standardised template;
- the {D('Quality Coordinator')} who audits content completeness.

Boundaries with other policies of {HOSPITAL}:

- AAC.12 owns the discharge process and the duty to give a summary to all leavers. This policy owns what that summary contains and how instructions are written.
- AAC.4.g owns related continued-care education elements; this policy owns how follow-up, medication and equipment instructions appear on the summary.
- PSQ.4.d owns related urgent-care communication expectations; this policy owns that the discharge summary incorporates when and how to obtain urgent care.
- AAC.2 owns the unique identification number used on the summary.
- MOM owns implant batch/serial traceability where implants are used; if implant identifiers are required on the summary by that chapter, they are not redefined here."""

POLICY_STATEMENT = f"""{HOSPITAL} provides a discharge summary to the patient at the time of discharge. The summary is signed by the treating doctor or a doctor member of the treating team. The patient or family acknowledges receipt.

{HOSPITAL} uses standardised discharge-summary content covering identification, treating doctor, dates, reasons for admission, significant findings, diagnosis and condition at discharge, investigation results, procedures, medications administered and other treatment given.

{HOSPITAL} writes follow-up advice, medication and other instructions in an understandable manner, includes when and how to obtain urgent care, and in case of death includes the cause of death.

{HOSPITAL} does not issue a summary that uses only Latin dose abbreviations the patient cannot understand, and does not leave process ownership to this document — process remains AAC.12."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no ward convenience exception.

1. Discharging a patient without providing a signed discharge summary at the time of discharge, or without recording acknowledgement of receipt.
2. Issuing a summary missing standardised minimum content: name, unique ID, treating doctor, admission and discharge dates, reasons for admission, significant findings/diagnosis/condition at discharge, investigation results, procedures, medications administered, or other treatment given.
3. Writing follow-up or medication instructions only as BD, TID, QID or other abbreviations the patient cannot understand, or omitting equipment/wound-care instructions when they apply.
4. Omitting specific instructions on when and how to obtain urgent care for that patient's diagnosis and condition.
5. Issuing a death summary without the cause of death, or failing to document post-mortem when the cause is unclear or the case is medico-legal as required.

Staff who see one of these acts report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Summary provided, signed and receipt acknowledged

A discharge summary is provided to the patient at the time of discharge at {HOSPITAL}.

The discharge summary is signed by the treating doctor or a doctor member of the treating team. The patient or family acknowledges receipt of the summary. Acknowledgement is recorded — {D('on the summary copy retained in the record, or on a receipt slip')} — with date and name of the person receiving it.""",

f"""5.2 Standardised content

Discharge summaries at {HOSPITAL} have standardised content. The minimum content is:

- patient's name;
- unique identification number;
- name of the treating doctor;
- date of admission and date of discharge;
- reasons for admission;
- significant findings, diagnosis and the patient's condition at the time of discharge;
- information regarding investigation results;
- any procedure performed;
- medication administered;
- any other treatment given.

In addition to the treating doctor, the summary may name other consultants involved in treatment. The {D('Medical Superintendent')} holds the current template; treating doctors complete every field or mark a field as not applicable with reason.""",

f"""5.3 Understandable follow-up, medication and other instructions

The discharge summary contains follow-up advice, medication and other instructions in an understandable manner. Preventive aspects are incorporated where appropriate.

Follow-up advice, medication and other instructions are explained to the patient and/or relatives in a language and manner they understand. Medical terms such as BD, TID and QID are not used; frequencies are written in plain words (for example morning and night, three times a day).

Other instructions include safe and effective use of medical equipment at home — for example CPAP, nebulizer, rehab equipment — where applicable. For post-operative patients the summary includes wound-care instructions and pressure-ulcer care after discharge where relevant.

Cross-reference AAC.4.g for related continued-care education. Explanation is documented.""",

f"""5.4 When and how to obtain urgent care

The discharge summary incorporates instructions about when and how to obtain urgent care.

Advice on when the patient shall seek urgent care is specific to the patient's diagnosis and clinical condition at discharge — for example development of fever, or bleeding or discharge from the operative site. Advice may state what medicines to take, when to consult a doctor, how to seek medical help, and the contact number of the hospital or doctor.

Instructions about when and how to obtain urgent care are explained to the patient and/or relatives in a language and manner they understand. Follow-up of post-operative and at-risk patients is good practice from a patient-safety point of view. Cross-reference PSQ.4.d.""",

f"""5.5 Cause of death in the death summary

In case of death, the summary of the case also includes the cause of death.

When the cause of death is not clear, a post-mortem is performed (for example in MLC) and the same is documented. The death summary is given to the next of kin under AAC.12 process; this step owns that cause of death (and post-mortem documentation where required) appears in the summary content.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Holds the standardised discharge-summary template.
- Accountable that content rules are followed.

Treating doctors (or doctor member of treating team)
- Write and sign the summary; include all standardised fields; write understandable instructions and urgent-care advice; include cause of death where applicable.

Nurses
- Explain instructions in a language the patient/family understands; support acknowledgement of receipt.

Discharge coordinator (if used)
- Confirms a signed summary with acknowledgement is present before the patient leaves.

Registration / front-office
- May record hand-over of the patient copy where that is local practice.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when summary-content defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Sampled summaries signed; receipt acknowledged.
- All standardised minimum content fields present or marked not applicable with reason.
- Follow-up and medication instructions without BD/TID/QID; equipment and wound-care instructions present when applicable.
- Urgent-care instructions specific to diagnosis/condition, with contact route.
- Death summaries include cause of death; post-mortem documented when cause unclear or MLC.

Root-cause analysis is required when the same summary-content defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when the summary template or urgent-care contact routes change."""

TRAINING_ACKNOWLEDGEMENT = f"""All treating doctors and nurses who prepare or explain discharge summaries are trained on this policy at induction and {D('once a year')} after that. Training covers the template fields, plain-language medication instructions, urgent-care wording and death-summary cause of death.

Staff acknowledgement

I have read this Content of the Discharge Summary policy of {HOSPITAL}. I will complete the standardised fields, write understandable instructions, include urgent-care advice and document cause of death where applicable.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/13"),
    version=VERSION,
    prepared_by=D("Medical Superintendent"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care chapter, standard AAC.13 (PDF indices ~92–93; source OCR policies/source/hco6_aac_ocr.txt; PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- Cross-reference within the same guidebook: AAC.12 (discharge process); AAC.4.g (continued-care education); PSQ.4.d (urgent care).
- Internal documents of {HOSPITAL}: discharge-summary template; receipt acknowledgement method; death-summary template; urgent-care contact list."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every in-patient ward; emergency; intensive care; nursing administration; discharge coordinator if that role exists; medical records.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH HCO chapter)
CAPA — corrective and preventive action
CPAP — continuous positive airway pressure
HCO — Hospital Accreditation Programme (NABH Full Accreditation)
MLC — medico-legal case
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality (NABH HCO chapter)"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.13.a",
        "requirement": "A discharge summary is provided to the patients at the time of discharge.",
        "steps": "Section 3; 5.1 Summary provided, signed and receipt acknowledged; Section 4 item 1",
        "responsible": "Treating doctors (sign); patient/family (acknowledge); nurses (support)",
        "records": [
            "Signed discharge summary issued at discharge.",
            "Acknowledgement of receipt by patient or family.",
            "Quarterly audit sample of signed summaries with acknowledgement.",
        ],
    },
    {
        "oe_code": "AAC.13.b",
        "requirement": "Discharge summary has a standardised content.",
        "steps": "Section 3; 5.2 Standardised content; Section 4 item 2",
        "responsible": "Medical Superintendent (template); treating doctors (complete fields)",
        "records": [
            "Current standardised discharge-summary template.",
            "Completed summaries with name, unique ID, treating doctor, dates, reasons, findings/diagnosis/condition, investigations, procedures, medications, other treatment.",
            "Quarterly completeness audit against the minimum content list.",
        ],
    },
    {
        "oe_code": "AAC.13.c",
        "requirement": (
            "Discharge summary contains follow-up advice, medication and other "
            "instructions in an understandable manner."
        ),
        "steps": "Section 3; 5.3 Understandable follow-up, medication and other instructions; Section 4 item 3",
        "responsible": "Treating doctors (write); nurses (explain)",
        "records": [
            "Summaries with plain-language medication frequencies (no BD/TID/QID).",
            "Equipment, wound-care or pressure-ulcer instructions where applicable.",
            "Record that instructions were explained in a language the patient/family understands.",
        ],
    },
    {
        "oe_code": "AAC.13.d",
        "requirement": (
            "Discharge summary incorporates instructions about when and how to obtain "
            "urgent care."
        ),
        "steps": "Section 3; 5.4 When and how to obtain urgent care; Section 4 item 4",
        "responsible": "Treating doctors (write); nurses (explain); Quality Coordinator (audit)",
        "records": [
            "Urgent-care section specific to diagnosis and condition at discharge.",
            "Hospital or doctor contact number on the summary.",
            "Record of explanation of urgent-care instructions to patient/relatives.",
        ],
    },
    {
        "oe_code": "AAC.13.e",
        "requirement": "In case of death, the summary of the case also includes the cause of death.",
        "steps": "Section 3; 5.5 Cause of death in the death summary; Section 4 item 5",
        "responsible": "Treating doctors (write death summary); Medical Superintendent (MLC/post-mortem oversight)",
        "records": [
            "Death summary stating cause of death.",
            "Post-mortem documentation when cause unclear or MLC.",
            "Copy retained in the medical record and given to next of kin under AAC.12 process.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.13 v2 (2026-08-20). PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. Source OCR policies/source/hco6_aac_ocr.txt (PDF idxs ~92–93). Five OEs a–e. No asterisked OEs — whole standard Tier-2 depth under HCO drafting choice; accuracy from guidebook retained. No stop-work. P2: accreditation-only. chapter=HCO. doc_no «HCO/AAC/POL/13». Boundary: AAC.12 owns process; AAC.13 owns summary content — cross-ref only. Cross-ref AAC.4.g and PSQ.4.d. Do not copy SHCO AAC.8 wording."""


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
        "stop_work": "",
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "Standardised discharge-summary content, understandable instructions and death summary.",
        "doc_no": D("HCO/AAC/POL/13"),
        "programme": "HCO Full Accreditation, 6th Edition",
    }
    emit_pre_v2(
        draft,
        "hco_aac13_v2_draft.json",
        "HCO.AAC.13_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
