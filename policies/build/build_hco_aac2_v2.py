# -*- coding: utf-8 -*-
"""HCO AAC.2 v2 — registration and admission (HCO Full, 6th Edition).

Shape follows PRE/SHCO v2 adoptable-policy shape via pre_v2_common.
Wording from NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition
— AAC chapter (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices 66–68.
OCR source: policies/source/hco6_aac_ocr.txt.

Five OEs (a–e). Asterisk on a, d, e. Core on b. No stop-work.
General consent at entry cross-ref PRE — do not duplicate informed-consent procedure.
Does NOT overwrite SHCO AAC builders or drafts.
"""
from __future__ import annotations

import sys

from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, document_control, emit_pre_v2

STANDARD_CODE = "AAC.2"
CHAPTER = "HCO"
OE_CODES = ["AAC.2.a", "AAC.2.b", "AAC.2.c", "AAC.2.d", "AAC.2.e"]
POLICY_TITLE = "Registration and Admission"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO Full 6th Edition AAC.2 v2 draft: plain English, five steps, no stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Every patient who is assessed is registered; every admission is authorised by a "
    "doctor; a unique number follows the patient; beds and clinical priority are managed "
    "so that the hospital accepts only what it can care for."
)

PURPOSE = f"""This policy says how {HOSPITAL} uses written guidance to register and admit patients (including unidentified patients); generates a unique identification number at the end of registration; accepts patients only when it can provide the required service (with life-saving treatment first in emergency); manages non-availability of beds; and prioritises access according to clinical need.

The chapter intent is that only those patients who can be cared for by the organisation are admitted, and that emergency patients receive life-stabilising treatment and are then either admitted or transferred appropriately.

This policy owns registration and admission. AAC.1 owns which services exist. AAC.3 owns transfer when the hospital cannot continue care. PRE owns the detailed informed-consent method; this policy only requires that general consent at entry is obtained and its scope explained — not the invasive-procedure consent procedure.

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies at every registration and admission point at {HOSPITAL}: front office, out-patient registration, emergency, day-care and in-patient admission desks. It binds registration and front-office staff, treating doctors who authorise admission, nurses who receive admitted patients, the Medical Superintendent, department heads, and the Quality Coordinator.

It covers AAC.2.a–e for out-patients, day-care, in-patients and emergency patients.

Boundaries:

- AAC.1 owns the service directory used to decide acceptance.
- AAC.3 owns transfer-out when beds or services are unavailable beyond temporary holding.
- PRE.3 (informed consent) owns the method for specific and invasive consent. This policy owns that general consent for treatment is obtained at entry and that its scope is defined and explained; general consent must not include invasive procedures that need specific consent.
- Billing owns tariffs; this policy owns explaining financial implications when the desired bed category is unavailable.
- Medical Records owns the unique-number master index in coordination with registration."""

POLICY_STATEMENT = f"""{HOSPITAL} uses written guidance for registering and admitting patients, including unidentified patients. All patients assessed in the hospital are registered. Every admission is authorised by a doctor. A unique identification number is generated at the end of registration and used across the organisation. Patients are accepted only if the organisation can provide the required service; in emergency, life-saving treatment is started before any acceptance decision. Written guidance manages non-availability of beds. Access is prioritised according to clinical need.

{HOSPITAL} does not admit without doctor authorisation, does not leave an assessed patient unregistered, and does not refuse life-saving emergency treatment while deciding acceptance."""

NON_NEGOTIABLES = f"""1. Do not leave an assessed patient unregistered — including unidentified patients, who are registered under the unidentified-patient process.
2. Do not admit a patient without authorisation by a doctor.
3. Do not complete registration without generating the unique identification number at the end of registration, and do not give a second unique number to the same patient.
4. Do not accept a non-emergency patient for a service the hospital cannot provide; in emergency, start life-saving treatment before deciding acceptance.
5. Do not hold a patient on a temporary bed beyond the defined time without a decision to transfer or place; explain financial implications when the desired bed category is unavailable.
6. Do not ignore clinical priority in out-patient or diagnostic queues when a patient needs earlier response.
7. Staff who find registration, unique-number or bed-management rules not followed report it the same shift to the {D('Medical Superintendent')} or the {D('Quality Coordinator')}."""

PROCEDURE_STEPS = [
f"""5.1 Written guidance for registering and admitting patients

{HOSPITAL} keeps written guidance for registration and admission covering out-patients, day-care, in-patients and emergency patients. The guidance includes unidentified patients. All patients who are assessed in the hospital are registered. Government regulations that apply to registration and admission are followed. Documentation is designed to avoid duplication — information once generated is available to departments that need it within the organisation.

Identity verification at registration is done by {D('government photo ID where available, or two identifiers stated by the patient or accompanying person')}. All admissions are authorised by a doctor. Additional documentation for foreign nationals is collected as required by applicable rules.

Patients and families are informed of the salient steps for registration and admission through {D('displays at registration and information on the hospital website')}.

General consent for treatment is obtained when the patient enters the organisation. The organisation defines the scope of that general consent and explains it to the patient and/or family. General consent does not include invasive procedures or other procedures that need specific consent under the PRE consent policy. The detailed consent method for those procedures is owned by PRE — do not duplicate that procedure here.""",

f"""5.2 Unique identification number at end of registration

At the end of the patient's first registration interaction with {HOSPITAL}, a unique identification number is generated. That number identifies the patient across the organisation and supports continuity of care. All hospital records of the patient carry this number.

Unique means a one-time assignment: a patient has only one unique number. For later out-patient or in-patient visits a visit or encounter number may be generated in addition; those numbers are linked to the unique number. Registration staff must not create a second unique number for the same person.""",

f"""5.3 Accept patients only when the required service can be provided

Registration and admission staff know the services {HOSPITAL} can provide (from the AAC.1 service directory) and whom to contact for clarification — {D('the duty doctor, the Head of the relevant department, or the Medical Superintendent')}.

Patients are accepted only if the organisation can provide the required service. In emergency, life-saving treatment is initiated before any decision about acceptance. If after stabilisation the hospital still cannot provide the needed service, AAC.3 transfer-out applies.""",

f"""5.4 Managing non-availability of beds

Written guidance addresses non-availability of beds. {HOSPITAL} maintains a current list of alternate organisations where patients may be directed when beds are unavailable.

If patients are admitted to a temporary holding area, that area has adequate infrastructure to care for them. The guidance defines how long patients may remain on temporary beds before a transfer-out decision is taken — default {D('not more than 12 hours unless the Medical Superintendent extends in writing for a named patient')}.

When a bed is not available in the desired bed category or unit, staff manage placement per the guidance and explain the financial implications to the patient and/or family before confirming the alternative category.""",

f"""5.5 Prioritise access according to clinical needs

Access to healthcare services is prioritised according to the patient's clinical needs in out-patient and diagnostic settings. Patients whose clinical problem warrants an earlier response are identified and seen sooner — for example a patient in the OPD who complains of giddiness, or a vulnerable patient attending for a diagnostic test.

All staff who handle queues and diagnostic flow are oriented to these guidelines. {HOSPITAL} uses a visual identification mechanism — {D('a coloured sticker on the file or on the patient clothing')} — so that all concerned staff can recognise priority patients. The mechanism is defined in writing and taught at induction.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable for registration and admission written guidance, bed non-availability rules and clinical-priority rules.
- Approves alternate-organisation list and temporary-holding time limits.

Registration / front-office staff
- Register all assessed patients, including unidentified patients.
- Generate the unique identification number at end of registration and never duplicate it.
- Obtain general consent at entry and explain its scope; do not take invasive-procedure consent under this policy.
- Apply clinical-priority visual identification in OPD and diagnostics.

Treating doctors
- Authorise every admission.
- Decide acceptance against available services; start life-saving treatment in emergency before acceptance decisions.

Nursing administration / ward nurses
- Receive admitted patients; escalate when temporary holding exceeds the defined time.

Medical Records
- Maintain the unique-number master index linked to visit numbers.

Quality Coordinator
- Audits registration, unique-number integrity, bed-holding and priority identification {D('quarterly')}.

Department heads
- Clarify service availability for registration staff when contacted."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Written registration and admission guidance is current and covers unidentified patients, OP/IP/day-care/emergency.
- Sample of admissions shows doctor authorisation and unique identification number on all records.
- No duplicate unique numbers in the sample; visit numbers are linked where used.
- Temporary-holding episodes stay within the defined time; financial explanation for category mismatch is documented where applicable.
- Clinical-priority visual identification is in use in OPD and diagnostics; staff orientation records exist.

Root-cause analysis is required when a duplicate unique number, an unauthorised admission, or a temporary-holding over-run recurs within six months.

This policy is reviewed {D('annually')}, and sooner when registration systems or bed capacity change."""

TRAINING_ACKNOWLEDGEMENT = f"""Registration, front-office, medical records, treating doctors and nurses who admit patients are informed of this policy at induction and {D('once a year')} after that. Training covers unidentified-patient registration, unique-number rules, general consent scope at entry, bed non-availability, and clinical-priority visual identification.

Staff acknowledgement

I have read this Registration and Admission policy of {HOSPITAL}. I will register every assessed patient, generate one unique number per patient, obtain general consent at entry within its defined scope, and apply clinical priority as trained.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. Registration in-charge and the Quality Coordinator hold signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/02"),
    version=VERSION,
    prepared_by=D("Registration In-Charge"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care (AAC), standard AAC.2.
- Internal documents of {HOSPITAL}: registration and admission written guidance; unique-number procedure; alternate-organisation list; temporary-holding and bed-category guidance; clinical-priority and visual-identification guidance; PRE informed-consent policy (cross-reference for specific consent)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: registration; front office; medical records; emergency; day-care; every ward; nursing administration; billing (bed-category financial implications).

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH Hospitals chapter)
CAPA — corrective and preventive action
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
OP / OPD — out-patient / out-patient department
PRE — Patient Rights and Education (NABH chapter)"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.2.a",
        "requirement": "The organisation uses written guidance for registering and admitting patients.",
        "steps": "Section 3; 5.1 Written guidance for registering and admitting patients; Section 4 items 1–2, 7",
        "responsible": "Medical Superintendent (approve guidance); Registration / front-office (execute); Treating doctors (authorise admission)",
        "records": [
            "Written registration and admission guidance covering OP, day-care, IP, emergency and unidentified patients.",
            "Sample registration records showing assessed patients registered and general consent obtained at entry with scope explained.",
            "Admission orders or notes showing doctor authorisation for each admission in the audit sample.",
            "Display or website evidence that salient registration/admission steps are communicated to patients and families.",
        ],
    },
    {
        "oe_code": "AAC.2.b",
        "requirement": "A unique identification number is generated at the end of the registration.",
        "steps": "Section 3; 5.2 Unique identification number at end of registration; Section 4 item 3",
        "responsible": "Registration / front-office (generate); Medical Records (master index)",
        "records": [
            "Unique-number master index showing one unique number per patient.",
            "Sample clinical records carrying the unique number across departments.",
            "Visit/encounter numbers linked to the unique number where used.",
            "Audit log of duplicate-number checks with corrections.",
        ],
    },
    {
        "oe_code": "AAC.2.c",
        "requirement": "Patients are accepted only if the organisation can provide the required service.",
        "steps": "Section 3; 5.3 Accept patients only when the required service can be provided; Section 4 item 4",
        "responsible": "Registration / front-office (screen); Treating doctors (acceptance and emergency life-saving); Department heads (clarify services)",
        "records": [
            "Current AAC.1 service directory available at registration points.",
            "Contact list for service clarification (duty doctor / department head / Medical Superintendent).",
            "Emergency records showing life-saving treatment started before acceptance decisions where applicable.",
            "Log of non-accepted non-emergency presentations with reason and advice given.",
        ],
    },
    {
        "oe_code": "AAC.2.d",
        "requirement": "The written guidance also addresses managing patients during non-availability of beds.",
        "steps": "Section 3; 5.4 Managing non-availability of beds; Section 4 item 5",
        "responsible": "Medical Superintendent (approve guidance and time limits); Nursing administration (temporary holding); Registration (alternate organisations and financial explanation)",
        "records": [
            "Written bed non-availability guidance including temporary holding, time limits and category mismatch.",
            "Current list of alternate organisations for redirection.",
            "Temporary-holding log with arrival time, decision time and outcome.",
            "Documented explanation of financial implications when desired bed category is unavailable.",
        ],
    },
    {
        "oe_code": "AAC.2.e",
        "requirement": "Access to the healthcare services in the organisation is prioritised according to the clinical needs of the patient.",
        "steps": "Section 3; 5.5 Prioritise access according to clinical needs; Section 4 item 6",
        "responsible": "Registration / front-office and diagnostic reception (apply priority); Quality Coordinator (audit orientation)",
        "records": [
            "Written clinical-priority guidelines for OPD and diagnostic services.",
            "Description of the visual identification mechanism (sticker or equivalent) and where it is placed.",
            "Staff orientation records for queue and diagnostic staff.",
            "Sample of priority patients identified and seen earlier, with visual marker noted.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.2 v2 (2026-08-20). HCO Full Accreditation, NABH Hospitals 6th Edition.
PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. OCR: policies/source/hco6_aac_ocr.txt (PDF indices 66–68).

OE COUNT: 5 (a–e). Asterisked: AAC.2.a, AAC.2.d, AAC.2.e (Tier 1). Core: AAC.2.b. AAC.2.c Commitment without asterisk (Tier 2).

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work (transfer instability owned by AAC.3). Disclaimer accreditation-only. chapter=HCO, doc_no HCO/AAC/POL/02.

BOUNDARY: General consent at entry is in AAC.2.a interpretation; specific/invasive consent method is PRE — cross-referenced, not duplicated.

FLAG: OCR label 'Commitment cc.' cleaned to AAC.2.c. No remaining unclear OE."""


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
        "prepared_by": D("Registration In-Charge"),
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "HCO Full Accreditation, 6th Edition — registration and admission.",
        "doc_no": D("HCO/AAC/POL/02"),
        "acknowledgement_note": "Registration in-charge and the Quality Coordinator hold signed acknowledgements.",
        "stop_work": "",
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.2",
    }
    emit_pre_v2(
        draft,
        "hco_aac2_v2_draft.json",
        "HCO.AAC.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
