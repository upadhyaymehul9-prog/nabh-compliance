# -*- coding: utf-8 -*-
"""AAC.7 v2 — continuity and multidisciplinary care.

Shape follows PRE v2 adoptable-policy shape. Wording from AAC.7 OEs (NABH SHCO
3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 59–60.
No stop-work. Disclaimer P2 accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, emit_pre_v2

STANDARD_CODE = "AAC.7"
CHAPTER = "AAC"
OE_CODES = ["AAC.7.a", "AAC.7.b", "AAC.7.c", "AAC.7.d"]
POLICY_TITLE = "Continuity and Multidisciplinary Care"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "AAC v2 template: plain English, AAC roles, four steps, no stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Patient care is continuous and multidisciplinary in nature — "
    "so that the patient is never without a responsible clinician and information flows across the team."
)

PURPOSE = f"""This policy says how {HOSPITAL} ensures that during all phases of care a qualified individual is identified as responsible for the patient, that information about care and response to treatment is shared among medical, nursing and other care-providers, that standardised handover communication is implemented during each staffing shift, between shifts and during transfers, and that patient transfer within the organisation is done safely.

The chapter intent is that care is continuous, coordinated and safely handed over.

This policy owns continuity and handover. AAC.2 owns registration, admission and transfer in/out of the hospital. AAC.3 owns assessment and care planning. AAC.8 owns discharge. PRE owns patient consent for transfer (PRE.3).

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to treating doctors, nurses, allied health staff, the Medical Superintendent and the Quality Coordinator at {HOSPITAL}.

It covers the four elements AAC.7.a–d: responsible individual identified, information sharing, standardised handover, and safe internal transfer.

Boundaries:

- AAC.2 owns transfer-in and transfer-out of the hospital. This policy owns transfer within the hospital (ward to ward, department to department, floor to floor).
- PRE.3 owns consent. This policy owns the clinical handover that accompanies a transfer.
- AAC.3 owns the care plan. This policy owns that the care plan information is shared during handover.
- HIC owns infection-control precautions during transfer. This policy owns the transfer process."""

POLICY_STATEMENT = f"""{HOSPITAL} ensures that during all phases of care a qualified individual is identified as responsible for the patient. Information about the patient's care and response to treatment is shared among the care team. Standardised handover communication is implemented at every shift change and during transfers between units and departments. Patient transfer within the organisation is done safely.

{HOSPITAL} does not leave a patient without an identified responsible clinician, and does not hand over without standardised communication."""

NON_NEGOTIABLES = f"""1. Do not leave a patient at any phase of care without a qualified individual identified as responsible.
2. Do not omit standardised handover communication at shift change or during internal transfer.
3. Do not transfer a patient within the hospital without documenting the clinical status, reason for transfer and handover to the receiving team.
4. Staff who see a handover or continuity rule broken report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Responsible individual identified

During all phases of care — out-patient consultation, emergency, in-patient stay, day-care, transfer and discharge — there is a qualified individual identified as responsible for the patient's care at {HOSPITAL}.

The responsible individual is recorded in the patient file: the treating doctor's name, contact number and expected availability. When the treating doctor is off duty, the covering doctor is identified and the handover recorded.

No patient is at any time without an identified responsible clinician.""",

f"""5.2 Information sharing among care-providers

Information about the patient's care and response to treatment is shared among medical, nursing and other care-providers, including referrals to other departments:

- the patient file is the primary record and is accessible to all authorised members of the treating team;
- nursing notes, doctor's progress notes and allied health entries are written in the same file or linked system;
- when a referral to another department is made, the referring doctor communicates the clinical question, relevant history and urgency, and the referred department documents its opinion in the patient file;
- verbal orders are documented by the nurse immediately and countersigned by the doctor within {D('24 hours')}.

The care team discusses the patient at {D('morning rounds or a scheduled team meeting')} where multidisciplinary input is needed.""",

f"""5.3 Standardised handover communication

{HOSPITAL} implements standardised handover communication during each staffing shift, between shifts and during transfers between units and departments. The handover tool is {D("SBAR (Situation, Background, Assessment, Recommendation) or the hospital's chosen standardised format")}.

Handover includes:

- patient identification (name, unique identification number, location);
- current diagnosis and condition;
- key events since the last handover (investigations, procedures, changes in treatment);
- pending tasks and follow-up required;
- any safety concern or early warning score (EWS) trigger.

Handover is documented: {D('in a handover register, the patient file or the electronic system')}. The receiving team acknowledges receipt. Interruptions during handover are minimised.""",

f"""5.4 Safe internal transfer

Patient transfer within {HOSPITAL} is done safely. Before transferring a patient between wards, units or departments:

- the reason for transfer is documented;
- the patient's clinical status is assessed and documented immediately before transfer;
- the receiving unit is informed and confirms readiness;
- the patient is accompanied by {D('a nurse or a trained attendant')} with appropriate monitoring and equipment for the patient's condition;
- medications, infusions and oxygen are continued during transfer;
- standardised handover (section 5.3) is completed between the transferring and receiving teams;
- the transfer is documented in the patient file with time of departure and arrival.

Critical or unstable patients are accompanied by a doctor.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that continuity, handover and internal transfer processes are defined and followed.

Treating doctors
- Identified as responsible for the patient during their phase of care; hand over to the covering doctor; share information with the team.

Nurses
- Perform shift handover using standardised communication; accompany patients during transfer; document handover.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when handover or continuity defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Responsible individual identified and documented in patient files.
- Information sharing: referral documentation complete; verbal orders countersigned within time limit.
- Standardised handover: tool used, documentation present, acknowledgement by receiving team.
- Internal transfer: documentation complete, patient accompanied, receiving team handed over to.

Root-cause analysis is required when the same handover or continuity defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when staffing patterns, ward layout or handover tools change."""

TRAINING_ACKNOWLEDGEMENT = f"""All treating doctors, nurses and allied health staff are trained on this policy at induction and {D('once a year')} after that. Training covers the handover tool, documentation requirements, information sharing and safe internal transfer.

Staff acknowledgement

I have read this Continuity and Multidisciplinary Care policy of {HOSPITAL}. I will identify myself as responsible, hand over using the standardised tool, share information and transfer patients safely.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('AAC/POL/07')}
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

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.7.
- Internal documents of {HOSPITAL}: handover register or tool; internal transfer checklist; patient file documentation standards; referral process."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every in-patient ward; emergency; out-patient; day-care; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 2)
CAPA — corrective and preventive action
EWS — early warning score
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PRE — Patient Rights and Education (NABH SHCO chapter 4)
SBAR — Situation, Background, Assessment, Recommendation
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.7.a",
        "requirement": "During all phases of care, there is a qualified individual identified as responsible for the patient's care.",
        "steps": "Section 3; 5.1 Responsible individual identified; Section 4 item 1",
        "responsible": "Treating doctors (identify and record); Medical Superintendent (accountable)",
        "records": [
            "Patient file entry showing responsible clinician for each phase of care.",
            "Covering-doctor record when treating doctor is off duty.",
            "Quarterly audit sample of responsible-clinician documentation.",
        ],
    },
    {
        "oe_code": "AAC.7.b",
        "requirement": "Information about the patient's care and response to treatment is shared among medical, nursing and other care-providers, including referrals to other departments.",
        "steps": "Section 3; 5.2 Information sharing among care-providers; Section 4 item 2",
        "responsible": "Treating doctors and nurses (share); referring and referred departments (document)",
        "records": [
            "Patient file with nursing notes, doctor notes and allied health entries.",
            "Referral documentation with clinical question, history, opinion and countersignature.",
            "Verbal-order documentation and countersignature within time limit.",
        ],
    },
    {
        "oe_code": "AAC.7.c",
        "requirement": "The organization implements standardised hand-over communication during each staffing shift, between shifts and during transfers between units/departments.",
        "steps": "Section 3; 5.3 Standardised handover communication; Section 4 item 2",
        "responsible": "Nurses (shift handover); treating doctors (doctor-to-doctor handover); Quality Coordinator (audit)",
        "records": [
            "Handover documentation using the standardised tool for each shift.",
            "Acknowledgement by receiving team.",
            "Quarterly audit sample of handover completeness.",
        ],
    },
    {
        "oe_code": "AAC.7.d",
        "requirement": "Patient transfer within the organization is done safely.",
        "steps": "Section 3; 5.4 Safe internal transfer; Section 4 item 3",
        "responsible": "Nurses (accompany); treating doctors (assess and authorise); Quality Coordinator (audit)",
        "records": [
            "Internal transfer documentation with reason, clinical status, receiving confirmation and times.",
            "Handover record between transferring and receiving teams.",
            "Critical-patient transfer records showing doctor accompaniment.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """AAC.7 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. No asterisked OEs. No stop-work. P2: accreditation-only. Four OEs, four What-we-do subsections."""


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
        "subtitle": "Continuity of care, handover and internal transfer.",
        "doc_no": D("AAC/POL/07"),
    }
    emit_pre_v2(
        draft,
        "aac7_v2_draft.json",
        "AAC.7_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
