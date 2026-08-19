# -*- coding: utf-8 -*-
"""COP.8 v2 — safe paediatric services.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 71.
No stop-work section. Six OEs clustered into six What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.8"
CHAPTER = "COP"
OE_CODES = [
    "COP.8.a", "COP.8.b", "COP.8.c", "COP.8.d", "COP.8.e", "COP.8.f",
]
POLICY_TITLE = "Safe Paediatric Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation provides safe paediatric services — age-specific competency, "
    "neonatal care aligned with guidelines, special provisions for children, "
    "growth and immunisation assessment, and measures to prevent abduction and abuse."
)

PURPOSE = f"""This policy defines how {HOSPITAL} organises and provides safe paediatric services covering neonatal care, age-specific competency, special provisions for children, nutritional/growth/developmental/immunisation assessment, and prevention of child/neonate abduction and abuse.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff caring for paediatric patients at {HOSPITAL}: paediatricians, treating doctors, nurses, and support staff in paediatric and neonatal areas.

Boundaries with other policies of {HOSPITAL}:

- AAC.3 owns initial patient assessment. This policy owns nutritional, growth, developmental and immunisation assessment specific to paediatric patients (COP.8.e).
- COP.12 owns vulnerable-patient identification generally; this policy owns paediatric-specific safety including abduction and abuse prevention.
- Services not provided by this hospital are recorded absences against the service directory, not copied SOPs."""

POLICY_STATEMENT = f"""{HOSPITAL} organises paediatric services safely, ensures neonatal care follows national/international guidelines, maintains age-specific competency among staff who care for children, makes special provisions for children, assesses nutrition/growth/development/immunisation, and prevents child/neonate abduction and abuse.

{HOSPITAL} does not import paediatric protocols from tertiary centres that exceed its service directory."""

NON_NEGOTIABLES = f"""1. A person without age-specific paediatric competency does not independently care for a paediatric patient.
2. Neonatal care does not deviate from the national/international guidelines this hospital has adopted without documented clinical justification.
3. Paediatric drug doses are weight-based; adult doses are not used for children.
4. No child or neonate is discharged to an unverified person.
5. A suspected abduction or abuse event is reported immediately to the {D('Paediatric In-Charge')} and hospital security."""

PROCEDURE_STEPS = [
f"""5.1 Organisation of paediatric services

Paediatric services at {HOSPITAL} are organised with designated paediatric areas, age-appropriate equipment, and staffing that ensures safe care. The {D('Paediatric In-Charge')} holds the operational method for organising these services.

Equipment sizing, drug formulary entries and resuscitation aids are paediatric-specific. Ward layout separates children from adult patients where the facility allows. Where separation is not possible, the documented method explains the safeguards used.""",

f"""5.2 Neonatal care aligned with guidelines

Neonatal care at {HOSPITAL} follows {D('NNF Essential Newborn Care guidelines and IAP Neonatology protocols')} or equivalent national/international guidelines adopted by this hospital.

The {D('Paediatric In-Charge')} maintains the list of adopted guidelines and reviews them {D('annually')} for currency. Deviations are documented with clinical justification in the patient record.""",

f"""5.3 Age-specific competency

All staff who care for children at {HOSPITAL} hold age-specific competency demonstrated through training, certification or supervised practice. The {D('Paediatric In-Charge')} maintains a competency matrix.

New staff complete a paediatric competency assessment before independent duty. Competency is reassessed {D('annually')}. Records are held with the training file.""",

f"""5.4 Special provisions for children

{HOSPITAL} makes special provisions for the care of children including {D('child-friendly environment, parental presence during procedures where safe, play and distraction aids, and paediatric pain assessment tools')}.

The provisions are documented and reviewed {D('annually')} by the {D('Paediatric In-Charge')} for adequacy against the patient population served.""",

f"""5.5 Nutritional, growth, developmental and immunisation assessment

Patient assessment for paediatric patients includes nutritional screening, growth charting, developmental milestones and immunisation status. AAC.3 owns initial assessment; this step owns the paediatric-specific components.

Growth is plotted on {D('WHO/IAP growth charts')}. Immunisation status is compared against {D('the National Immunisation Schedule')}. Gaps trigger a documented referral or counselling note. Developmental screening uses {D('a validated tool appropriate to age')}.""",

f"""5.6 Prevention of child/neonate abduction and abuse

{HOSPITAL} has measures to prevent child and neonate abduction and abuse. These include {D('identity-band verification at every handover, restricted access to neonatal areas, CCTV where installed, visitor-pass system, and staff training on recognising abuse signs')}.

A suspected abduction triggers {D('immediate lockdown of the ward/floor, security alert, and police notification within 30 minutes')}. Suspected abuse is reported to the {D('Paediatric In-Charge')} who activates the hospital's child-protection protocol. Records of drills and incidents are maintained.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that paediatric services are organised safely and that competency, guidelines, and prevention measures are in place.

Paediatric In-Charge
- Holds operational methods for sections 5.1–5.6.
- Maintains competency matrix, guideline list, and abduction/abuse prevention protocol.

Paediatricians and treating doctors
- Provide care with age-specific competency; document assessments per 5.5.

Nurses (paediatric and neonatal areas)
- Apply identity-band checks, growth charting, and special provisions daily.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when a paediatric safety defect recurs."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Age-specific competency records current for all paediatric staff.
- Neonatal care adherence to adopted guidelines (sample charts).
- Growth/development/immunisation assessments completed on paediatric admissions.
- Abduction-prevention drill conducted {D('every six months')}.
- Abuse-recognition training records current.

Root-cause analysis is required when a paediatric safety event recurs within six months.

This policy is reviewed {D('annually')}, and sooner when adopted guidelines or the service directory change."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff caring for children are trained on this policy at induction and {D('once a year')} after that. Training covers age-specific competency requirements, neonatal guidelines, growth/immunisation assessment, and abduction/abuse prevention.

Staff acknowledgement

I have read this Safe Paediatric Services policy of {HOSPITAL}. I will provide paediatric care in accordance with the standards and prevention measures described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Paediatric In-Charge holds signed acknowledgements with the training file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/08"),
    version=VERSION,
    prepared_by=D("Paediatric In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.8.
- National Neonatology Forum (NNF), Essential Newborn Care guidelines — adopted edition.
- Indian Academy of Pediatrics (IAP), Neonatology protocols — adopted edition.
- WHO Child Growth Standards (2006) — growth charting reference.
- National Immunisation Schedule, Government of India — current edition.
- Internal documents of {HOSPITAL}: competency matrix, adopted guideline list, abduction/abuse prevention protocol, growth charts, immunisation gap referral pathway."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Paediatric In-Charge and Quality Coordinator.

Copies issued to: paediatric ward; neonatal area; nursing station (paediatric); emergency (paediatric section); OPD (paediatric).

The current version is available to all staff at the {D('policy file in the paediatric ward')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}."""

ABBREVIATIONS = """CAPA — corrective and preventive action
IAP — Indian Academy of Pediatrics
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NNF — National Neonatology Forum
OE — objective element
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.8.a",
        "requirement": "Paediatric services are organised and provided safely.",
        "steps": "Section 3; 5.1 Organisation of paediatric services; Section 4 items 1–5",
        "responsible": "Paediatric In-Charge (method); Medical Superintendent (accountable)",
        "records": [
            "Documented method for organising paediatric services including staffing, equipment and layout.",
            "Paediatric equipment inventory with sizing verification.",
            "Staffing roster showing paediatric-competent coverage.",
            "Annual review record of service organisation.",
        ],
    },
    {
        "oe_code": "COP.8.b",
        "requirement": "Neonatal care is in consonance with the national/international guidelines.",
        "steps": "Section 3; 5.2 Neonatal care aligned with guidelines",
        "responsible": "Paediatric In-Charge (guideline adoption and review); paediatricians (adherence)",
        "records": [
            "List of adopted national/international neonatal guidelines with edition and adoption date.",
            "Annual review record confirming guidelines are current.",
            "Sample neonatal charts showing adherence to adopted protocol.",
            "Documented deviations with clinical justification where applicable.",
        ],
    },
    {
        "oe_code": "COP.8.c",
        "requirement": "Those who care for children have age-specific competency.",
        "steps": "Section 3; 5.3 Age-specific competency; Section 4 item 1",
        "responsible": "Paediatric In-Charge (competency matrix); HR/training coordinator (records)",
        "records": [
            "Competency matrix for all staff caring for children.",
            "Initial competency assessment records for new staff.",
            "Annual reassessment records.",
        ],
    },
    {
        "oe_code": "COP.8.d",
        "requirement": "Provisions are made for special care of children.",
        "steps": "Section 3; 5.4 Special provisions for children",
        "responsible": "Paediatric In-Charge (provisions); nurses (daily application)",
        "records": [
            "Documented special provisions for children with annual adequacy review.",
            "Evidence of child-friendly environment and paediatric pain tools in use.",
            "Quarterly audit sample showing provisions applied.",
        ],
    },
    {
        "oe_code": "COP.8.e",
        "requirement": "Patient assessment includes nutritional, growth, developmental and immunisation assessment.",
        "steps": "Section 3; 5.5 Nutritional, growth, developmental and immunisation assessment",
        "responsible": "Treating doctors and nurses (assess); Paediatric In-Charge (tools and method)",
        "records": [
            "Growth charts plotted for paediatric admissions.",
            "Developmental screening records using validated tool.",
            "Immunisation status documented with gap referrals where indicated.",
            "Nutritional screening records for paediatric patients.",
        ],
    },
    {
        "oe_code": "COP.8.f",
        "requirement": "The organization has measures in place to prevent child/neonate abduction and abuse.",
        "steps": "Section 3; 5.6 Prevention of child/neonate abduction and abuse; Section 4 items 4–5",
        "responsible": "Paediatric In-Charge (protocol); security staff (execution); nurses (identity-band checks)",
        "records": [
            "Documented abduction-prevention protocol with access-control measures.",
            "Abuse-recognition training records for all paediatric staff.",
            "Drill records conducted at defined frequency.",
            "Incident log for suspected abduction or abuse events with actions taken.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.8 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Organization provides safe paediatric services." COP.8.a–f PDF index 71. Asterisked OEs: a, b, f. All Commitment level.

SHAPE: Six What-we-do subsections (5.1–5.6). No stop-work. Disclaimer accreditation-only. COP paediatric roles."""


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
        "subtitle": "Safe paediatric and neonatal care.",
        "doc_no": D("COP/POL/08"),
    }
    emit_pre_v2(
        draft,
        "cop8_v2_draft.json",
        "COP.8_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
