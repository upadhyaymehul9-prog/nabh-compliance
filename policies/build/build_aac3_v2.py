# -*- coding: utf-8 -*-
"""AAC.3 v2 — initial assessment and reassessment.

Shape follows PRE v2 adoptable-policy shape. Wording from AAC.3 OEs (NABH SHCO
3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 57.
Stop-work section 6. Disclaimer P2 accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, emit_pre_v2

STANDARD_CODE = "AAC.3"
CHAPTER = "AAC"
OE_CODES = ["AAC.3.a", "AAC.3.b", "AAC.3.c", "AAC.3.d", "AAC.3.e"]
POLICY_TITLE = "Initial Assessment and Reassessment"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "AAC v2 template: plain English, AAC roles, five steps, stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Patients cared for by the organisation undergo an established initial assessment "
    "and regular reassessment — so that care is planned, monitored and adjusted."
)

PURPOSE = f"""This policy says how {HOSPITAL} performs initial assessment for out-patients, day-care, in-patients and emergency patients; documents a care plan from the initial assessment; reassesses patients at appropriate intervals; informs out-patients of follow-up; and identifies early warning signs for prompt intervention.

The chapter intent is that every patient receives a timely, documented assessment that drives a care plan, and that reassessment detects deterioration early.

This policy owns assessment and reassessment. AAC.2 owns registration and admission. AAC.7 owns continuity and handover. COP standards own specific clinical procedures. PRE.3 owns consent.

EWS — early warning score. Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to treating doctors, nurses and allied health staff at {HOSPITAL} who assess or reassess patients across out-patient, day-care, in-patient and emergency settings.

It covers the five elements AAC.3.a–e: initial assessment, documented care plan, reassessment, out-patient follow-up, and early warning guidelines.

Boundaries:

- AAC.2 owns registration, admission and acceptance criteria. This policy begins after the patient is accepted.
- AAC.7 owns continuity and handover communication. This policy owns the clinical assessment and reassessment that handover communicates.
- AAC.4/AAC.5 own laboratory and imaging results. This policy owns that those results inform assessment and reassessment.
- PSQ.2 owns quality indicators. Assessment timeliness and EWS compliance feed PSQ.2.
- Spell out: early warning score (EWS), turnaround time (TAT)."""

POLICY_STATEMENT = f"""{HOSPITAL} performs initial assessment for every out-patient, day-care, in-patient and emergency patient. The initial assessment results in a documented care plan. Patients are reassessed at appropriate intervals. Out-patients are informed of follow-up. Early warning guidelines are implemented to detect deterioration and initiate prompt intervention.

{HOSPITAL} does not leave a deteriorating patient without escalation when the early warning score triggers, and does not proceed without a documented care plan."""

NON_NEGOTIABLES = f"""1. Do not admit or continue in-patient care without a documented care plan resulting from the initial assessment.
2. Do not ignore an early warning score trigger — escalate to the treating doctor or the designated responder within the time the guideline states.
3. Do not discharge or transfer an out-patient without informing them of the next follow-up, where appropriate.
4. Do not omit reassessment when the clinical condition changes or at the interval the care plan specifies.
5. Staff who find an assessment or EWS rule not followed report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

STOP_WORK = f"""Do not leave a deteriorating patient without escalation when the early warning score triggers — escalate immediately per the EWS protocol and document the response.

Do not proceed with in-patient care without a documented care plan from the initial assessment — complete the assessment and document the plan before proceeding with treatment beyond emergency stabilisation.

Stop-work applies to the clinical pathway, not to emergency stabilisation.

The person responsible tells the {D('Medical Superintendent')} or the {D('treating doctor')} the same shift. Refusing to proceed without a documented care plan is not a disciplinary matter."""

PROCEDURE_STEPS = [
f"""5.1 Initial assessment

The treating doctor performs an initial assessment for every patient presenting to {HOSPITAL}:

- Out-patients: history, examination and provisional diagnosis documented in the out-patient record within {D('30 minutes of consultation start')}.
- Day-care patients: pre-procedure assessment including fitness for the planned procedure.
- In-patients: history, examination, provisional diagnosis and initial investigations documented within {D('one hour of admission')}.
- Emergency patients: rapid assessment and stabilisation documented within {D('15 minutes of arrival')}; full assessment within {D('one hour')}.

Nurses complete nursing assessment (vital signs, allergy status, pain score, fall risk) within {D('30 minutes of admission')} for in-patients and emergency patients.""",

f"""5.2 Documented care plan

The initial assessment results in a documented care plan. The care plan includes:

- provisional or confirmed diagnosis;
- planned investigations;
- treatment plan (medications, procedures, therapies);
- nursing care requirements;
- expected duration of stay for in-patients;
- goals of care discussed with the patient and/or family (PRE.2 owns the right to consultation; this policy owns the clinical plan).

The care plan is recorded in the patient file and is accessible to all treating team members. It is reviewed and updated at every reassessment.""",

f"""5.3 Reassessment

Patients are reassessed at appropriate intervals to determine their response to treatment and to plan further treatment or discharge:

- In-patients: reassessed by the treating doctor at least {D('once daily')} and by nurses at least {D('once per shift')}.
- Emergency patients: reassessed as clinical condition requires, at minimum before any decision to admit, discharge or transfer.
- Day-care patients: reassessed before discharge from the day-care unit.

Reassessment findings, response to treatment and any change in the care plan are documented in the patient file.""",

f"""5.4 Out-patient follow-up information

Out-patients are informed of their next follow-up, where appropriate. The treating doctor or nurse tells the patient:

- when to return (date or timeframe);
- what to watch for that should prompt an earlier visit;
- whom to contact if symptoms worsen before the follow-up date.

The follow-up instruction is recorded in the out-patient record and, where the hospital issues a follow-up card, on the card.""",

f"""5.5 Early warning guidelines

{HOSPITAL} implements guidelines and processes to identify early warning signs of change or deterioration in clinical conditions for initiating prompt intervention. The guideline uses an early warning score (EWS) — {D("a modified early warning score (MEWS) or the hospital's chosen validated tool")}.

EWS parameters: {D('respiratory rate, oxygen saturation, heart rate, systolic blood pressure, level of consciousness, temperature')}.

Frequency of observations: {D('every four hours for routine in-patients; more frequently as the score or clinical condition dictates')}.

Escalation: when the EWS reaches the trigger threshold, the nurse contacts the treating doctor within {D('15 minutes')}. The treating doctor reviews the patient within {D('30 minutes')} of being contacted. The response is documented.

Training: all nursing staff and doctors are trained on the EWS tool at induction and {D('annually')}.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that assessment, care planning, reassessment and EWS processes are defined and followed.

Treating doctors
- Perform initial assessment, document the care plan, reassess at intervals, and respond to EWS triggers.

Nurses
- Complete nursing assessment, perform EWS observations, escalate triggers, and document reassessment.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when assessment or EWS defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Initial assessment completed within defined timeframes for each patient category.
- Documented care plan present in every in-patient file.
- Reassessment documented at defined intervals.
- Out-patient follow-up information recorded.
- EWS observations at defined frequency; triggers escalated and responded to within time limits.
- Training records for EWS tool.

Root-cause analysis is required when the same assessment or EWS defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when clinical protocols, EWS tools or staffing patterns change."""

TRAINING_ACKNOWLEDGEMENT = f"""All treating doctors, nurses and allied health staff are trained on this policy at induction and {D('once a year')} after that. Training covers initial assessment, care plan documentation, reassessment, follow-up information, and the EWS tool and escalation.

Staff acknowledgement

I have read this Initial Assessment and Reassessment policy of {HOSPITAL}. I will assess, plan, reassess and escalate as described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('AAC/POL/03')}
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

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.3.
- Royal College of Physicians, National Early Warning Score (NEWS) 2 — framework for early warning score tools; not pasted as this hospital's tool.
- Internal documents of {HOSPITAL}: assessment forms; care plan template; EWS observation chart; escalation protocol; out-patient follow-up card."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: emergency; every in-patient ward; out-patient; day-care; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 2)
CAPA — corrective and preventive action
EWS — early warning score
MEWS — modified early warning score
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations
TAT — turnaround time"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.3.a",
        "requirement": "The initial assessment for the out-patients, day-care, in-patients and emergency patients is done.",
        "steps": "Section 3; 5.1 Initial assessment; Section 4 items 1, 2",
        "responsible": "Treating doctors (perform); nurses (nursing assessment); Quality Coordinator (audit)",
        "records": [
            "Initial assessment records for out-patient, day-care, in-patient and emergency patients.",
            "Nursing assessment records (vital signs, allergy, pain, fall risk).",
            "Quarterly audit of assessment completion within defined timeframes.",
        ],
    },
    {
        "oe_code": "AAC.3.b",
        "requirement": "The initial assessment results in a documented care plan.",
        "steps": "Section 3; 5.2 Documented care plan; Section 4 item 1",
        "responsible": "Treating doctors (document); nurses (nursing care requirements)",
        "records": [
            "Care plan in every in-patient file with diagnosis, investigations, treatment and goals.",
            "Evidence of care plan review and update at reassessment.",
            "Quarterly audit sample of care plan completeness.",
        ],
    },
    {
        "oe_code": "AAC.3.c",
        "requirement": "Patients are reassessed at appropriate intervals to determine their response to treatment and to plan further treatment or discharge.",
        "steps": "Section 3; 5.3 Reassessment; Section 4 item 4",
        "responsible": "Treating doctors (reassess); nurses (shift reassessment)",
        "records": [
            "Reassessment entries in patient files with response to treatment.",
            "Evidence of care plan update after reassessment.",
            "Quarterly audit sample of reassessment frequency.",
        ],
    },
    {
        "oe_code": "AAC.3.d",
        "requirement": "Out-patients are informed of their next follow-up, where appropriate.",
        "steps": "Section 3; 5.4 Out-patient follow-up information; Section 4 item 3",
        "responsible": "Treating doctors or nurses (inform); registration staff (follow-up card where used)",
        "records": [
            "Follow-up instruction recorded in the out-patient record.",
            "Follow-up card issued where applicable.",
            "Quarterly audit sample of follow-up documentation.",
        ],
    },
    {
        "oe_code": "AAC.3.e",
        "requirement": "The organization lays down guidelines and implements processes to identify early warning signs of change or deterioration in clinical conditions for initiating prompt intervention.",
        "steps": "Section 3; 5.5 Early warning guidelines; Section 4 item 2",
        "responsible": "Nurses (observe and escalate); treating doctors (respond); Quality Coordinator (audit)",
        "records": [
            "EWS protocol document specifying tool, parameters, frequency and escalation thresholds.",
            "EWS observation charts for in-patients.",
            "Escalation and response records when trigger threshold reached.",
            "Training records for EWS tool.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """AAC.3 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. AAC.3.a asterisked. Stop-work section 6. P2: accreditation-only. Five OEs, five What-we-do subsections."""


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
        "stop_work": STOP_WORK,
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
        "subtitle": "Assessment, care planning, reassessment and early warning.",
        "doc_no": D("AAC/POL/03"),
    }
    emit_pre_v2(
        draft,
        "aac3_v2_draft.json",
        "AAC.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
