# -*- coding: utf-8 -*-
"""COP.1 v2 — uniform care to patients.

Shape follows PRE.1 v2 (section list and order only). Wording from COP.1 OEs
(NABH SHCO 3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed page 67 / PDF index 67.

No stop-work. Disclaimer accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.1"
CHAPTER = "COP"
OE_CODES = ["COP.1.a", "COP.1.b", "COP.1.c", "COP.1.d", "COP.1.e"]
POLICY_TITLE = "Uniform Care to Patients"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: plain English, COP roles, five OEs, no stop-work, accreditation-only disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "Uniform care to patients is provided in all settings of the organization and is "
    "guided by written guidance, and the applicable laws and regulations — not a set of "
    "guidelines that sits in the quality office while wards run on habit."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides uniform care to patients across all settings, guided by written guidance and applicable laws and regulations.

It covers five elements: a uniform process for patient identification using at least two identifiers; care in consonance with applicable laws and regulations; adoption of evidence-based clinical practice guidelines or clinical protocols; uniform care delivery for a given clinical condition across settings; and safe and secure telemedicine where provided.

The chapter intent is that care is uniform across settings and guided by written documents, not by individual habit or ward tradition.

This policy owns the uniformity of care delivery. AAC.2 owns registration, admission and transfer processes. AAC.3 owns the care plan as a clinical document. PRE.3 owns informed consent method.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every clinical setting at {HOSPITAL} — out-patient, in-patient, emergency, day care and any satellite or extension clinic — and to every staff member who delivers or supports patient care: treating doctors, nurses, registration staff, the {D('Quality Coordinator')}, and the Medical Superintendent.

It covers the five elements COP.1.a–e name. It does not cover the registration or admission process (AAC.2), the individual care plan (AAC.3), or the consent method (PRE.3).

Boundaries with other policies of {HOSPITAL}:

- AAC.2 owns the registration, admission, transfer and discharge process. This policy owns that care delivered in those settings is uniform.
- AAC.3 owns the care plan as a clinical document. This policy owns that care plans follow adopted clinical practice guidelines.
- PRE.3 owns the consent method. This policy owns that uniform processes apply before care begins, including patient identification.
- COP.2 owns emergency clinical care. This policy owns that emergency care is as uniform as elective care for the same clinical condition.
- If telemedicine is not provided, record that as a written absence. Do not copy a telemedicine SOP from another hospital."""

POLICY_STATEMENT = f"""{HOSPITAL} uses a uniform process for patient identification that uses at least two identifiers — {D('patient name and unique registration number')} — in every setting. A bed number is not an identifier.

{HOSPITAL} provides care in consonance with applicable laws and regulations. Staff are made aware of those laws and regulations relevant to their work.

{HOSPITAL} adopts evidence-based clinical practice guidelines and clinical protocols to guide uniform patient care. Guidelines are reviewed {D('annually')} and updated when evidence changes. A guideline that is adopted but never read by the staff who use it is not adopted.

When similar care is provided in more than one setting — for example, wound dressing in out-patient and in-patient — the care delivered for a given clinical condition is uniform. A patient with the same condition receives the same standard of care regardless of the setting.

{HOSPITAL} provides telemedicine safely and securely based on written guidance, where telemedicine is on the service directory. If telemedicine is not provided, that is recorded as a written absence.

{HOSPITAL} does not treat any of these as meeting this policy: a patient identified by bed number alone; a clinical guideline that no clinician has read; or care that differs for the same clinical condition depending on the ward."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no ward convenience exception.

1. Identifying a patient by bed number alone or by a single identifier. At least two identifiers must be used every time.
2. Delivering care that violates an applicable law or regulation the hospital is bound by, or treating ignorance of an applicable law as a defence.
3. Adopting a clinical practice guideline on paper while staff who deliver the care have never read or been trained on it.
4. Delivering materially different care for the same clinical condition in two settings without a documented clinical reason.
5. Providing telemedicine without written guidance covering privacy, consent, prescribing limits and documentation, or copying a telemedicine SOP from another hospital for a service this hospital does not run.

Staff who see one of these acts report it the same shift to the {D('Quality Coordinator')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Patient identification using two identifiers

Every patient is identified using at least two identifiers before any care, treatment, medication or investigation. The identifiers are {D('patient name and unique registration number')}. A bed number is never an identifier.

Identification is verified at registration, before medication administration, before specimen collection, before any procedure, and before transfer. Wristbands or identification labels are used for in-patients, and their accuracy is checked at each handover.

The {D('Quality Coordinator')} holds the written identification process and trains staff {D('at induction and annually')}.""",

f"""5.2 Care in consonance with applicable laws and regulations

{HOSPITAL} identifies the laws and regulations applicable to the care it provides. Staff are made aware of those that are relevant to their work. The Medical Superintendent holds a register of applicable laws and regulations and reviews it {D('annually')}.

When a law or regulation changes, staff are informed and trained before the change takes effect. Care delivered during the transition period follows the later of the old or new requirement, whichever is stricter.

This policy does not import every statute into a checklist. It requires that applicable laws are known and followed.""",

f"""5.3 Evidence-based clinical practice guidelines and protocols

{HOSPITAL} adopts evidence-based clinical practice guidelines and clinical protocols to guide uniform patient care. Guidelines are selected by the {D('Medical Superintendent in consultation with treating doctors')}, adopted formally, and made available to the staff who use them.

Adopted guidelines are reviewed {D('annually')} and updated when evidence changes. A guideline review that finds no change records that finding. A guideline that is never read by the staff who deliver the care it covers is not an adopted guideline.

Clinical protocols derived from guidelines are written in a form the treating team can follow at the bedside. They are not a photocopy of a textbook chapter.""",

f"""5.4 Uniform care across settings

When similar care is provided in more than one setting — for example, wound dressing in out-patient and in-patient, or nebulisation in emergency and ward — the care delivered for a given clinical condition is uniform. A patient receives the same standard of care regardless of the setting.

The {D('Quality Coordinator')} audits at least {D('two clinical conditions quarterly')} that are delivered in more than one setting and records whether the care was uniform. Differences that have a documented clinical reason are accepted. Differences that exist only because the ward has a different habit are findings.

Clinical heads confirm at least {D('annually')} that care protocols for conditions treated in their setting are aligned with the hospital-adopted guidelines.""",

f"""5.5 Telemedicine — safe and secure provision

If telemedicine is on the service directory, {HOSPITAL} provides it safely and securely based on written guidance. The guidance covers: patient identification using the same two-identifier process; informed consent for the telemedicine consultation; privacy and data security; prescribing limits as applicable regulations allow; documentation of the consultation in the patient record; and escalation to an in-person visit when the telemedicine consultation is insufficient.

The {D('Medical Superintendent')} holds the written telemedicine guidance and reviews it {D('annually')}.

If telemedicine is not provided, record that as a written absence. Do not copy a telemedicine SOP from another hospital for a service this hospital does not run.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that care is uniform across settings, guided by written guidance and applicable laws.
- Holds the register of applicable laws and regulations.
- Approves adopted clinical practice guidelines.

Treating doctors
- Follow adopted clinical practice guidelines and protocols.
- Identify patients using two identifiers before every care act.
- Provide telemedicine within written guidance where it is offered.

Nurses
- Verify patient identification at each handover and before medication, specimen collection or procedure.
- Follow adopted clinical protocols at the bedside.

{D('Quality Coordinator')}
- Holds the written patient identification process.
- Audits uniform care across settings {D('quarterly')}.
- Tracks CAPA when care differs for the same clinical condition without a documented clinical reason.

Registration staff
- Assign and verify the two identifiers at registration."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at records and at the floor.

What is monitored each quarter:

- Patient identification using two identifiers before care, medication, specimen collection and procedures.
- Applicable laws and regulations register is current and staff are aware.
- Adopted clinical practice guidelines are available to and read by the staff who use them.
- At least two clinical conditions delivered in more than one setting are audited for uniformity.
- Telemedicine written guidance is current where telemedicine is provided, or recorded absence where it is not.

Root-cause analysis is required when the same identification failure or the same non-uniform care finding recurs twice within six months.

This policy is reviewed {D('annually')}, and sooner when a clinical practice guideline is updated, an applicable law changes, or a new service is added to the directory."""

TRAINING_ACKNOWLEDGEMENT = f"""All clinical and registration staff are trained on this policy at induction and {D('once a year')} after that. Training covers the two-identifier rule, adopted clinical practice guidelines, uniform care across settings, and telemedicine guidance where applicable.

Staff acknowledgement

I have read this Uniform Care to Patients policy of {HOSPITAL}. I will identify every patient using at least two identifiers. I will follow adopted clinical practice guidelines. I will deliver uniform care for a given clinical condition regardless of the setting.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/01"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.1.
- Telemedicine Practice Guidelines (2020), Board of Governors, Medical Council of India — telemedicine guidance where telemedicine is on the service directory; not pasted as a protocol.
- Internal documents of {HOSPITAL}: patient identification process; adopted clinical practice guidelines and clinical protocols; register of applicable laws and regulations; telemedicine written guidance where provided; service directory."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every clinical department; registration; nursing administration; emergency department.

The current version is available to all staff at the {D('quality office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations
SOP — standard operating procedure"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.1.a",
        "requirement": "The organization has a uniform process for identification of patients and at a minimum, uses two identifiers.",
        "steps": "Section 3; 5.1 Patient identification using two identifiers",
        "responsible": "Quality Coordinator (process owner); nurses (verify); registration staff (assign)",
        "records": [
            "Written patient identification process naming the two identifiers.",
            "Wristband or identification label records for in-patients.",
            "Quarterly audit sample of identification before care, medication, specimen and procedure.",
            "Training records at induction and annually.",
        ],
    },
    {
        "oe_code": "COP.1.b",
        "requirement": "Care shall be provided in consonance with applicable laws and regulations.",
        "steps": "Section 3; 5.2 Care in consonance with applicable laws and regulations",
        "responsible": "Medical Superintendent (register and accountability); all clinical staff (compliance)",
        "records": [
            "Register of applicable laws and regulations reviewed annually.",
            "Staff awareness records when a law or regulation changes.",
            "Training records for applicable laws relevant to each role.",
        ],
    },
    {
        "oe_code": "COP.1.c",
        "requirement": "The organization adopts evidence-based clinical practice guidelines and/or clinical protocols to guide uniform patient care.",
        "steps": "Section 3; 5.3 Evidence-based clinical practice guidelines and protocols",
        "responsible": "Medical Superintendent (approve adoption); treating doctors (follow); Quality Coordinator (audit)",
        "records": [
            "List of adopted clinical practice guidelines with adoption date and review date.",
            "Evidence that staff who deliver the care have read the guideline.",
            "Annual review record for each adopted guideline.",
            "Bedside clinical protocols derived from guidelines.",
        ],
    },
    {
        "oe_code": "COP.1.d",
        "requirement": "Care delivery is uniform for a given clinical condition when similar care is provided in more than one setting.",
        "steps": "Section 3; 5.4 Uniform care across settings; Section 4 item 4",
        "responsible": "Quality Coordinator (audit); clinical heads (confirm alignment); treating doctors and nurses (deliver)",
        "records": [
            "Quarterly audit of at least two clinical conditions delivered in more than one setting.",
            "Record of whether care was uniform or a documented clinical reason for difference.",
            "Clinical heads' annual confirmation that protocols are aligned with hospital-adopted guidelines.",
            "CAPA records where non-uniform care was found without clinical justification.",
        ],
    },
    {
        "oe_code": "COP.1.e",
        "requirement": "Telemedicine facility is provided safely and securely based on written guidance.",
        "steps": "Section 3; 5.5 Telemedicine — safe and secure provision",
        "responsible": "Medical Superintendent (written guidance owner); treating doctors (follow guidance)",
        "records": [
            "Written telemedicine guidance covering identification, consent, privacy, prescribing limits, documentation and escalation.",
            "Annual review record of telemedicine guidance.",
            "Written absence record if telemedicine is not on the service directory.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.1 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Uniform care to patients is provided in all settings of the organization and is guided by written guidance, and the applicable laws and regulations." COP.1.a–e PDF page 67. COP.1.d asterisked (Commitment). COP.1.e asterisked (Excellence). COP.1.a Commitment, COP.1.b Achievement, COP.1.c Core.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. COP roles only."""


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
        "subtitle": "Uniform care guided by written guidance across all settings.",
        "doc_no": D("COP/POL/01"),
    }
    emit_pre_v2(
        draft,
        "cop1_v2_draft.json",
        "COP.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
