# -*- coding: utf-8 -*-
"""AAC.2 v2 — registration, admission and transfer.

Shape follows PRE v2 adoptable-policy shape. Wording from AAC.2 OEs (NABH SHCO
3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 56–57.
Stop-work section 6. Disclaimer P2 accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, emit_pre_v2

STANDARD_CODE = "AAC.2"
CHAPTER = "AAC"
OE_CODES = ["AAC.2.a", "AAC.2.b", "AAC.2.c", "AAC.2.d", "AAC.2.e", "AAC.2.f"]
POLICY_TITLE = "Registration, Admission and Transfer"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "AAC v2 template: plain English, AAC roles, six steps, stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation has a well-defined registration, admission and transfer process — "
    "so that every patient is identified, accepted appropriately, and moved safely."
)

PURPOSE = f"""This policy says how {HOSPITAL} registers and admits patients, generates a unique identification number, accepts only patients it can serve, manages non-availability of beds, prioritises access by clinical need, and handles transfer-in, transfer-out and referral.

The chapter intent is that registration, admission and transfer are orderly, safe and clinically driven.

This policy owns registration, admission and transfer. PRE owns patient information and consent. AAC.3 owns assessment and care plan. AAC.7 owns continuity and handover during care. AAC.8 owns discharge.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to registration, front-office, nursing, treating doctors, the Medical Superintendent and the Quality Coordinator at {HOSPITAL}.

It covers the six elements AAC.2.a–f: registration and admission mechanism, unique identification, acceptance criteria, bed-management when beds are unavailable, clinical prioritisation, and transfer-in / transfer-out / referral.

Boundaries:

- PRE owns patient information at registration (PRE.1) and consent (PRE.3). This policy owns the registration and admission process itself.
- AAC.7 owns clinical handover communication. This policy owns the transfer logistics (criteria, documentation, transport).
- AAC.3 owns initial assessment and care plan. This policy owns that a patient is accepted only if the required service can be provided.
- PSQ.2 owns quality indicators. Registration turnaround and bed-occupancy data feed PSQ.2."""

POLICY_STATEMENT = f"""{HOSPITAL} registers and admits patients through a defined mechanism. A unique identification number is generated at the end of registration. Patients are accepted only if the organisation can provide the required service. When beds are unavailable there is a documented management plan. Access is prioritised according to clinical need. Transfer-in, transfer-out and referral are done appropriately.

{HOSPITAL} does not admit beyond capacity without a management plan, and does not transfer an unstable patient without transfer criteria met."""

NON_NEGOTIABLES = f"""1. Do not admit a patient when the required service is not available and no documented management plan exists.
2. Do not register a patient without generating a unique identification number by the end of registration.
3. Do not transfer an unstable patient without documented transfer criteria being met and the receiving facility confirming acceptance.
4. Do not bypass clinical prioritisation by admitting on a first-come basis when a more urgent patient is waiting.
5. Staff who see a registration or transfer rule broken report it the same shift to the {D('Registration In-Charge')} or the {D('Medical Superintendent')}."""

STOP_WORK = f"""Do not transfer an unstable patient without transfer criteria met — stabilise first, document the clinical state, confirm the receiving facility can accept, and ensure appropriate transport.

Do not admit beyond capacity without a documented management plan — activate the plan (section 5.4) before accepting another patient when beds are full.

Stop-work applies to the transfer or the admission, not to emergency stabilisation.

The person responsible tells the {D('Medical Superintendent')} or {D('Registration In-Charge')} the same shift. Refusing to transfer an unstable patient or to admit without a plan is not a disciplinary matter."""

PROCEDURE_STEPS = [
f"""5.1 Registration and admission mechanism

{HOSPITAL} registers every patient who presents for care. Registration captures {D('name, age, sex, address, contact number, next of kin, and presenting complaint')} in the {D('hospital information system or registration register')}.

Admission follows registration when the treating doctor determines the patient needs in-patient care. The admission process records the admitting doctor, date and time of admission, bed/ward allocation, and provisional diagnosis.

Registration and admission are available during {D('all working hours; emergency registration is available 24 hours')}.""",

f"""5.2 Unique identification number

A unique identification number is generated at the end of registration for every patient. The number is {D('system-generated and non-repeating')}. It appears on every document, request form and report associated with the patient during that episode and any future episode.

No two patients share the same number. When a returning patient is identified, the existing number is retrieved.""",

f"""5.3 Acceptance criteria

Patients are accepted only if {HOSPITAL} can provide the required service. The treating doctor or the doctor on duty confirms that the service, diagnostic capability and treatment capability exist before admission.

When the required service is not available, the patient is informed, stabilised if necessary, and referred or transferred under section 5.6. A record is made of the reason for non-acceptance and the referral destination.""",

f"""5.4 Management of non-availability of beds

{HOSPITAL} has a documented plan for managing patients when beds are not available. The plan includes:

- {D('use of extra beds in designated overflow areas')};
- {D('prioritised discharge review to free beds')};
- {D('transfer to a partner facility with confirmed bed availability')};
- communication to the patient and family about the situation and expected wait.

The {D('Registration In-Charge')} activates the plan when occupancy reaches {D('90 per cent')} or when the last bed in a ward is allocated. The Medical Superintendent is informed the same shift.""",

f"""5.5 Clinical prioritisation of access

Access to healthcare services is prioritised according to the clinical needs of the patient. The treating doctor or triage nurse assigns priority based on clinical urgency — {D('emergency, urgent, routine')}.

Emergency patients are seen and stabilised first regardless of registration status. Registration is completed after stabilisation. The prioritisation method is displayed at {D('the emergency entrance and the registration counter')}.""",

f"""5.6 Transfer-in, transfer-out and referral

Transfer-in: a patient transferred from another facility is received with documentation, assessed on arrival, and entered in the register with a unique identification number.

Transfer-out / referral: a patient is transferred out or referred when {HOSPITAL} cannot provide the required service, when the patient requests transfer, or when a higher level of care is needed. Before transfer:

- the patient is stabilised;
- the receiving facility confirms it can accept;
- a transfer summary including diagnosis, treatment given, reason for transfer and clinical status at transfer is sent with the patient;
- appropriate transport is arranged — {D('hospital ambulance or documented alternative')};
- the patient or family gives informed consent for the transfer (consent method stays with PRE.3).

Transfer documentation is filed in the patient record.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that registration, admission and transfer processes are defined, resourced and followed.

Registration / front-office In-Charge
- Manages day-to-day registration, unique ID generation and bed-management plan activation.

Treating doctors
- Confirm acceptance criteria, assign clinical priority, and authorise transfers.

Nurses
- Support triage, admission documentation, transfer stabilisation and handover.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when a registration or transfer defect recurs."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Every registration has a unique identification number generated at the end of registration.
- Acceptance decisions are documented with service-availability confirmation.
- Bed-management plan exists and was activated when required.
- Clinical prioritisation evidence in emergency and admission records.
- Transfer-out documentation: stabilisation, receiving confirmation, transfer summary, transport, consent.
- Transfer-in documentation: arrival assessment, unique ID, records received.

Root-cause analysis is required when the same registration or transfer defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when services, capacity or referral pathways change."""

TRAINING_ACKNOWLEDGEMENT = f"""All registration, nursing and medical staff are trained on this policy at induction and {D('once a year')} after that. Training covers registration, unique ID, acceptance criteria, bed-management plan, clinical prioritisation and transfer process.

Staff acknowledgement

I have read this Registration, Admission and Transfer policy of {HOSPITAL}. I will follow the registration, acceptance, prioritisation and transfer processes described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('AAC/POL/02')}
Issue number: {D('01')}
Version: {VERSION} (AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Registration In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.2.
- Internal documents of {HOSPITAL}: registration process; admission process; bed-management plan; transfer protocols; referral pathways; clinical prioritisation method."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: registration; emergency; every in-patient ward; nursing administration; treating doctors.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 2)
CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PRE — Patient Rights and Education (NABH SHCO chapter 4)
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.2.a",
        "requirement": "The organization has a mechanism for registering and admitting patients.",
        "steps": "Section 3; 5.1 Registration and admission mechanism; Section 4 items 1, 2",
        "responsible": "Registration In-Charge (manage); Medical Superintendent (accountable)",
        "records": [
            "Written registration and admission process.",
            "Registration register or hospital information system entries.",
            "Admission records with admitting doctor, date, time, bed and provisional diagnosis.",
        ],
    },
    {
        "oe_code": "AAC.2.b",
        "requirement": "A unique identification number is generated at the end of registration.",
        "steps": "Section 3; 5.2 Unique identification number; Section 4 item 2",
        "responsible": "Registration staff (generate); Registration In-Charge (system integrity)",
        "records": [
            "Unique identification number on every patient registration.",
            "System or register showing non-repeating number assignment.",
            "Sample patient documents bearing the unique number.",
        ],
    },
    {
        "oe_code": "AAC.2.c",
        "requirement": "Patients are accepted only if the organization can provide the required service.",
        "steps": "Section 3; 5.3 Acceptance criteria; Section 4 item 1",
        "responsible": "Treating doctor (confirm service availability); Registration In-Charge (record)",
        "records": [
            "Record of service-availability confirmation before admission.",
            "Non-acceptance log with reason and referral destination.",
            "Quarterly audit sample of acceptance decisions.",
        ],
    },
    {
        "oe_code": "AAC.2.d",
        "requirement": "The organization has a mechanism to address management of patients during non-availability of beds.",
        "steps": "Section 3; 5.4 Management of non-availability of beds; Section 4 item 1",
        "responsible": "Registration In-Charge (activate plan); Medical Superintendent (informed)",
        "records": [
            "Documented bed-management plan.",
            "Activation log showing when the plan was triggered.",
            "Communication records to patients and families during bed shortage.",
        ],
    },
    {
        "oe_code": "AAC.2.e",
        "requirement": "Access to the healthcare services in the organization is prioritized according to the clinical needs of the patient.",
        "steps": "Section 3; 5.5 Clinical prioritisation of access; Section 4 item 4",
        "responsible": "Treating doctor or triage nurse (assign priority); Registration In-Charge (process)",
        "records": [
            "Written clinical prioritisation method.",
            "Emergency and admission records showing priority assigned.",
            "Display of prioritisation method at emergency entrance and registration.",
        ],
    },
    {
        "oe_code": "AAC.2.f",
        "requirement": "Transfer-in and transfer-out / referral of patients to the organization is done appropriately.",
        "steps": "Section 3; 5.6 Transfer-in, transfer-out and referral; Section 4 item 3",
        "responsible": "Treating doctor (authorise); nurses (stabilise and handover); Registration In-Charge (documentation)",
        "records": [
            "Transfer-out checklist: stabilisation, receiving confirmation, transfer summary, transport, consent.",
            "Transfer-in records: arrival assessment, unique ID, documents received.",
            "Referral log with reason and destination.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """AAC.2 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. AAC.2.a, AAC.2.d, AAC.2.e, AAC.2.f asterisked. Stop-work section 6. P2: accreditation-only. Six OEs, six What-we-do subsections."""


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
        "subtitle": "Registration, admission and transfer of patients.",
        "doc_no": D("AAC/POL/02"),
    }
    emit_pre_v2(
        draft,
        "aac2_v2_draft.json",
        "AAC.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
