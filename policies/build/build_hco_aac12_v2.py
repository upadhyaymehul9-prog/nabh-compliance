# -*- coding: utf-8 -*-
"""HCO AAC.12 v2 — established discharge process.

Shape: pre_v2_common.emit_pre_v2 + hco_v2_disclaimer accreditation-only.
Wording from NABH HCO Full Accreditation 6th Edition Guidebook
(PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices ~90–92 /
policies/source/hco6_aac_ocr.txt. Do not copy SHCO AAC wording.

Seven OEs a–g. Asterisk: b, c. No stop-work.
Boundary: AAC.12 owns process; AAC.13 owns discharge-summary content.
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

STANDARD_CODE = "AAC.12"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.12.a", "AAC.12.b", "AAC.12.c", "AAC.12.d",
    "AAC.12.e", "AAC.12.f", "AAC.12.g",
]
POLICY_TITLE = "Established Discharge Process"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": (
            "HCO Full 6th Edition AAC.12 v2 draft from guidebook OCR; "
            "seven steps; asterisk b,c; no stop-work; accreditation-only P2."
        ),
    },
]

STATEMENT_OF_INTENT = (
    "The organisation has an established discharge process — planned with the "
    "patient and family, coordinated across departments, and monitored from "
    "fit-for-discharge to bed vacated."
)

PURPOSE = f"""This policy says how {HOSPITAL} runs an established discharge process.

It covers seven jobs that match the standard:

- plan discharge in consultation with the patient and/or family;
- coordinate discharge among departments and agencies involved, including medico-legal and absconded cases;
- written guidance for patients leaving against medical advice (LAMA);
- give a discharge summary to all patients leaving, including LAMA, and a death summary to next of kin;
- adhere to planned discharge (at least 24 hours' advance planning; minimise unplanned discharges);
- expand access through domiciliary visits wherever applicable;
- monitor discharge time, set benchmarks and make continual improvement.

The chapter intent is that transfer and discharge protocols are well defined and that continuity of care may extend to the community through home health care services where applicable.

This policy owns the discharge process. AAC.13 owns the content of the discharge summary. Cross-reference AAC.13 for what the summary must contain; do not duplicate that content list here. AAC.4.g is cross-referenced for planned-discharge education elements. AAC.3 owns transfer-out to another facility (not discharge home).

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every patient leaving {HOSPITAL}'s care by planned discharge, LAMA, absconding recovery workflows, or death (death summary to next of kin), and to the staff who run that process.

It binds:

- treating doctors who determine readiness and plan discharge with the patient and family;
- nurses who prepare the patient for leaving and support education;
- registration / front-office and accounts who complete papers within time;
- the {D('discharge coordinator')} where this hospital uses that role;
- the {D('Medical Superintendent')} who is accountable for coordination including MLC and police intimation;
- the {D('Quality Coordinator')} who audits discharge time and process.

Boundaries with other policies of {HOSPITAL}:

- AAC.13 owns discharge-summary content (identification, clinical fields, follow-up wording, urgent care, cause of death). This policy owns that a summary is given and that the process runs; it does not redefine summary fields.
- AAC.3 owns transfer-out / referral to another facility. This policy owns discharge from the organisation's care.
- AAC.4.g owns elements of patient education for continued care that planned discharge prepares; this policy owns the 24-hour planning and minimising unplanned discharges.
- PRE owns rights and consent method for refusal / LAMA declaration. This policy owns LAMA written guidance for the discharge act and that a summary is still given.
- Billing / PRE cost explanation owns tariff conversation. This policy owns coordination with accounts so papers complete in time."""

POLICY_STATEMENT = f"""{HOSPITAL} plans the patient's discharge in consultation with the patient and/or family. Discharge is coordinated among the departments and agencies involved, including medico-legal and absconded cases. Written guidance governs LAMA. A discharge summary is given to all patients leaving, including LAMA; in case of death, a death summary is given to the next of kin.

{HOSPITAL} adheres to planned discharge, expands access through domiciliary visits wherever applicable, monitors discharge time against benchmarks and improves continually.

{HOSPITAL} does not discharge without consultation and coordination, and does not treat AAC.13 summary content as a substitute for this process."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no ward convenience exception.

1. Declaring a patient ready for discharge without consulting the patient and/or family.
2. Completing discharge without coordinating the departments and agencies involved — including accounts, and police intimation for medico-legal cases.
3. Allowing LAMA without following written guidance and without recording the patient/attendant declaration.
4. Letting a patient leave (including LAMA) without a discharge summary, or failing to give a death summary to next of kin.
5. Treating same-day surprise discharge as planned when the standard requires planning at least 24 hours in advance, without documenting why unplanned discharge could not be avoided.
6. Ignoring domiciliary visit arrangements where this hospital's scope makes them applicable and they were part of the discharge plan.
7. Failing to measure discharge time from fit-for-discharge to bed vacated, or ignoring repeated delay without improvement action.

Staff who see one of these acts report it the same shift to the {D('treating doctor')}, the {D('discharge coordinator')} if used, or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Discharge planned with patient and family

The patient's discharge process is planned in consultation with the patient and/or family at {HOSPITAL}.

The treating doctor determines readiness for discharge during regular reassessments and discusses the plan with the patient and family. The discussion covers expected timing, continued care needs and who will receive the discharge summary. Agreement or concerns are recorded in the patient file.""",

f"""5.2 Coordinated discharge including MLC and absconded cases

The discharge process is coordinated among various departments and agencies involved at {HOSPITAL}, including medico-legal and absconded cases.

Discharge procedures are documented so that departments — including accounts — complete discharge papers within time. For medico-legal cases (MLC), the organisation ensures that the police are informed about the discharge. Absconded-patient workflows follow the same coordination discipline when the patient is found or when the case is closed under this hospital's written process. The {D('discharge coordinator or ward nurse in charge')} tracks open tasks until the patient vacates the bed or the case is otherwise closed.""",

f"""5.3 Written guidance for leaving against medical advice

Written guidance governs the discharge of patients leaving against medical advice at {HOSPITAL}.

The treating doctor explains the consequences of leaving to the patient or attendant. The written guidance addresses reasons for LAMA so the organisation can take corrective and/or preventive action where patterns appear. The patient/attendant declaration is recorded in a proper format. LAMA does not cancel the duty to hand over a discharge summary and reports (see section 5.4). The {D('Medical Superintendent')} holds the current LAMA written guidance.""",

f"""5.4 Discharge summary given to all leaving patients

A discharge summary is given to all patients leaving {HOSPITAL}, including patients leaving against medical advice. In case of death, a death summary is given to the next of kin or relatives.

The organisation hands over the discharge summary and reports to the patient or attendant in all cases, and retains a copy in the medical record. For LAMA, the patient's right to refuse treatment and request to leave is respected; the declaration is recorded; the summary and reports are still handed over. Terminology for such patients may differ; the intent of issuing the summary with reports remains the same.

What the summary must contain is owned by AAC.13. This step owns that the summary is issued as part of the discharge process.""",

f"""5.5 Adherence to planned discharge

{HOSPITAL} adheres to planned discharge. Discharge is planned at least 24 hours in advance. Planning includes preparation of the draft discharge summary, refund of medications where applicable, patient education on continued care, and identified special needs — for example requirement of special equipment, devices, transportation (wheelchair), and safe and effective use of medical equipment. Unplanned discharges are minimised.

Cross-reference AAC.4.g for related continued-care education elements. Cross-reference AAC.13 for summary content and understandable instructions.""",

f"""5.6 Domiciliary visits wherever applicable

Wherever applicable, care is provided by expanding access through domiciliary visits.

Trained healthcare workers visit patients at their residences to deliver medical care, treatment and/or support when this hospital's scope includes that service. Domiciliary visits may address chronic conditions, fall prevention, memory care, nutrition, exercise and other health concerns. For palliative care patients, home visits for change of catheters and/or other support care may be conducted. Visits are scheduled at discharge planning when applicable and recorded.""",

f"""5.7 Monitoring discharge time and continual improvement

{HOSPITAL} monitors the discharge time, sets appropriate benchmarks and makes continual improvement.

The organisation defines the time taken for discharge. The timeframe may differ by payer mix — for example cash, insurance, corporate. The organisation conforms to the defined timeframe. Delays are monitored; reasons are identified; improvement activities are performed.

The start-point for calculating discharge time is when the treating doctor declares the patient fit for discharge. The end-point is when the patient vacates the bed. The {D('Quality Coordinator')} reviews delay themes {D('monthly')} and reports to the Medical Superintendent.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable for the discharge process, MLC police intimation and LAMA written guidance.
- Reviews discharge-time improvement actions.

Treating doctors
- Determine readiness; consult patient/family; explain LAMA consequences; declare fit for discharge; ensure summary is issued (content per AAC.13).

Nurses
- Support preparation, education and hand-over of reports; record LAMA declaration support; confirm bed vacated time.

Discharge coordinator (if used)
- Tracks department tasks (ward, accounts, pharmacy, MLC paperwork) until papers complete and bed vacated.

Registration / front-office and accounts
- Complete discharge papers within the defined timeframe; support payer-mix timing benchmarks.

Quality Coordinator
- Audits this policy {D('quarterly')} and monitors discharge-time data (see monitoring section).
- Tracks CAPA when discharge-process defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')} and reviews discharge-time data {D('monthly')}.

What is monitored:

- Evidence of patient/family consultation before discharge.
- Coordination completeness including accounts and MLC police intimation where applicable.
- LAMA cases following written guidance with recorded declaration and summary issued.
- Discharge or death summary handed over for all sampled leavers.
- Proportion of discharges planned ≥24 hours in advance; reasons for unplanned discharges.
- Domiciliary visits completed where applicable and planned.
- Discharge time from fit-for-discharge to bed vacated against benchmarks by payer mix; delay reasons and CAPA.

Root-cause analysis is required when the same discharge-process defect or delay theme recurs within six months.

This policy is reviewed {D('annually')}, and sooner when bed management, payer mix or MLC workflows change."""

TRAINING_ACKNOWLEDGEMENT = f"""All treating doctors, nurses, registration/accounts staff and the discharge coordinator (if used) are trained on this policy at induction and {D('once a year')} after that. Training covers consultation, coordination including MLC, LAMA guidance, issuing summaries, 24-hour planning, domiciliary visits where applicable and discharge-time measurement.

Staff acknowledgement

I have read this Established Discharge Process policy of {HOSPITAL}. I will plan discharge with the patient and family, coordinate departments, follow LAMA guidance and measure discharge time from fit-for-discharge to bed vacated.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/12"),
    version=VERSION,
    prepared_by=D("Medical Superintendent"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care chapter, standard AAC.12 (PDF indices ~90–92; source OCR policies/source/hco6_aac_ocr.txt; PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- Cross-reference within the same guidebook: AAC.13 (discharge summary content); AAC.4.g (continued-care education elements).
- Internal documents of {HOSPITAL}: discharge checklist; LAMA written guidance and declaration form; MLC police intimation log; discharge-time register; domiciliary visit records where applicable."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every in-patient ward; emergency; intensive care; accounts; registration/front-office; nursing administration; discharge coordinator if that role exists.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH HCO chapter)
CAPA — corrective and preventive action
HCO — Hospital Accreditation Programme (NABH Full Accreditation)
LAMA — leaving against medical advice
MLC — medico-legal case
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PRE — Patient Rights and Education (NABH HCO chapter)"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.12.a",
        "requirement": (
            "The patient's discharge process is planned in consultation with the patient "
            "and / or family."
        ),
        "steps": "Section 3; 5.1 Discharge planned with patient and family; Section 4 item 1",
        "responsible": "Treating doctors (plan and consult); nurses (support)",
        "records": [
            "Reassessment note stating readiness for discharge.",
            "Record of discussion with patient and/or family about the discharge plan.",
            "Quarterly audit sample of consultation before discharge.",
        ],
    },
    {
        "oe_code": "AAC.12.b",
        "requirement": (
            "The discharge process is coordinated among various departments and agencies "
            "involved (including medico-legal and absconded cases)."
        ),
        "steps": "Section 3; 5.2 Coordinated discharge including MLC and absconded cases; Section 4 item 2",
        "responsible": "Discharge coordinator if used; ward nurse in charge; accounts; Medical Superintendent (MLC/police)",
        "records": [
            "Documented discharge procedure covering department coordination including accounts.",
            "MLC discharge file with police intimation record.",
            "Absconded-case coordination record where applicable.",
        ],
    },
    {
        "oe_code": "AAC.12.c",
        "requirement": (
            "Written guidance governs the discharge of patients leaving against medical advice."
        ),
        "steps": "Section 3; 5.3 Written guidance for leaving against medical advice; Section 4 item 3",
        "responsible": "Medical Superintendent (holds guidance); treating doctors (explain and record)",
        "records": [
            "Current LAMA written guidance.",
            "Patient/attendant LAMA declaration in the required format.",
            "Record that consequences of leaving were explained by the treating doctor.",
        ],
    },
    {
        "oe_code": "AAC.12.d",
        "requirement": (
            "A discharge summary is given to all the patients leaving the organisation "
            "including patients leaving against medical advice."
        ),
        "steps": "Section 3; 5.4 Discharge summary given to all leaving patients; Section 4 item 4",
        "responsible": "Treating doctors (issue); nurses/registration (hand-over support)",
        "records": [
            "Copy of discharge summary retained in the medical record for every leaver sampled.",
            "LAMA cases with summary and reports handed over.",
            "Death summary acknowledgement by next of kin where applicable.",
        ],
    },
    {
        "oe_code": "AAC.12.e",
        "requirement": "The organisation adheres to planned discharge.",
        "steps": "Section 3; 5.5 Adherence to planned discharge; Section 4 item 5",
        "responsible": "Treating doctors and nurses; Quality Coordinator (audit)",
        "records": [
            "Expected discharge noted at least 24 hours in advance for planned cases.",
            "Draft discharge summary and special-needs preparation before discharge.",
            "Log of unplanned discharges with reasons and minimisation actions.",
        ],
    },
    {
        "oe_code": "AAC.12.f",
        "requirement": (
            "The care shall be provided by expanding access to health practices through "
            "domiciliary visits, wherever applicable."
        ),
        "steps": "Section 3; 5.6 Domiciliary visits wherever applicable; Section 4 item 6",
        "responsible": "Treating doctors (plan); trained healthcare workers (visit); Quality Coordinator (audit)",
        "records": [
            "Scope statement or written note of when domiciliary visits apply.",
            "Domiciliary visit schedule and visit notes for eligible patients.",
            "Discharge plan entries linking home visits where applicable.",
        ],
    },
    {
        "oe_code": "AAC.12.g",
        "requirement": (
            "The organisation monitors the discharge time, sets appropriate benchmarks "
            "and makes continual improvement."
        ),
        "steps": "Section 3; 5.7 Monitoring discharge time and continual improvement; Section 4 item 7",
        "responsible": "Quality Coordinator (monitor); Medical Superintendent (improvement); ward and accounts (timestamps)",
        "records": [
            "Defined discharge-time benchmarks (including by payer mix where used).",
            "Discharge-time log from fit-for-discharge to bed vacated.",
            "Delay analysis and continual-improvement actions.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.12 v2 (2026-08-20). PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. Source OCR policies/source/hco6_aac_ocr.txt (PDF idxs ~90–92). Seven OEs a–g. Asterisk: b (coordination incl MLC/absconded), c (LAMA written guidance) — fuller procedure and evidence. No stop-work. P2: accreditation-only. chapter=HCO. doc_no «HCO/AAC/POL/12». Boundary: AAC.12 owns process; AAC.13 owns summary content — cross-ref, do not duplicate field list. Cross-ref AAC.4.g for planned-discharge education. Do not copy SHCO AAC.8 wording."""


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
        "prepared_by": D("Medical Superintendent"),
        "stop_work": "",
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "Planned, coordinated discharge process including LAMA and time monitoring.",
        "doc_no": D("HCO/AAC/POL/12"),
        "programme": "HCO Full Accreditation, 6th Edition",
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.12",
    }
    emit_pre_v2(
        draft,
        "hco_aac12_v2_draft.json",
        "HCO.AAC.12_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
