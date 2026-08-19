# -*- coding: utf-8 -*-
"""MOM.1 v2 — multidisciplinary committee guides pharmacy services and medication management.

Shape follows PRE.1 v2 / FMS.5 v2.2 (section list and order only). Wording is built
from MOM.1 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 82.
Chapter intent: PDF index 81.

No stop-work section. Six OEs clustered into six What-we-do subsections.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer

STANDARD_CODE = "MOM.1"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.1.a", "MOM.1.b", "MOM.1.c", "MOM.1.d", "MOM.1.e", "MOM.1.f",
]
POLICY_TITLE = "Multidisciplinary Committee Guides Pharmacy Services and Medication Management"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, six steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "A multidisciplinary committee governs the formulary, pharmacy services and medication usage — "
    "so that medication decisions are clinically led, not left to ad-hoc purchasing."
)

PURPOSE = f"""This policy describes how {HOSPITAL} establishes and maintains a formulary, governs pharmacy services through a multidisciplinary committee, acquires medications inside and outside the formulary, provides medication access when the pharmacy is closed, includes implantable prostheses and medical devices in the committee's scope, and monitors clinician adherence to the formulary.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the Multidisciplinary Medication Committee (Pharmacy and Therapeutics Committee), pharmacy staff, treating doctors (prescribers), nurses, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.1.a–f: formulary development; committee governance of pharmacy services; acquisition of formulary and non-formulary medications; medication access when the pharmacy is closed; implantable prostheses and medical devices; and clinician adherence to the formulary.

Boundaries with other policies of {HOSPITAL}:

- MOM.1.e lists implantable prostheses and medical devices in the committee's scope. MOM.9 owns the detailed guidance on procurement, counselling and traceability of implants.
- Medication storage is MOM.2. Prescribing is MOM.3. Dispensing is MOM.5. Administration is MOM.6.
- Safe use of narcotics, chemotherapeutic and radioactive agents is MOM.8."""

POLICY_STATEMENT = f"""{HOSPITAL} develops and maintains a formulary appropriate for its patient population and scope of services.

{HOSPITAL} governs pharmacy services and medication usage through the Multidisciplinary Medication Committee, not by individual decision.

{HOSPITAL} follows written procedures for acquisition of formulary and non-formulary medications, access when the pharmacy is closed, and the inclusion of implantable prostheses and medical devices in the committee's oversight.

Clinicians adhere to the current formulary. Exceptions are documented through the non-formulary acquisition procedure."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. The formulary is reviewed at least {D('annually')} by the Multidisciplinary Medication Committee.
2. No medication is routinely stocked unless it appears in the approved formulary or is acquired through the non-formulary procedure.
3. The non-formulary acquisition procedure is documented and followed every time — verbal agreements are not a substitute.
4. When the pharmacy is closed, the procedure for emergency medication access is followed; medications are not taken from the pharmacy without documentation.
5. Implantable prostheses and medical devices are included in the committee's scope per MOM.1.e; detailed guidance is MOM.9.
6. Clinicians prescribe from the current formulary; off-formulary prescribing follows the documented acquisition procedure.

Staff who see a breach report it the same shift to the {D('Pharmacy In-Charge')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Formulary development and maintenance

The Multidisciplinary Medication Committee develops, updates and implements a list of medications appropriate for the patients and the scope of clinical services at {HOSPITAL}.

The formulary is reviewed at least {D('annually')} and whenever a new clinical service is added or a drug-safety alert warrants a change. The committee records additions, deletions and the clinical rationale.

The formulary is available to all prescribers at {D('the pharmacy counter and, if the hospital keeps an intranet, on the staff intranet')}.""",

f"""5.2 Committee governance of pharmacy services

Pharmacy services and medication usage are implemented following written guidance through the Multidisciplinary Medication Committee.

The committee meets at least {D('quarterly')} and includes at a minimum: {D('Medical Superintendent (or delegate), a treating doctor, the Pharmacy In-Charge, and a nursing representative')}. Minutes are kept and include decisions, action items and deadlines.

The committee reviews medication-usage data, adverse drug reactions, medication errors and near-miss trends reported under MOM.7, and recommends changes to formulary, storage, prescribing or dispensing practices.""",

f"""5.3 Acquisition of formulary and non-formulary medications

{HOSPITAL} adheres to the procedure for the acquisition of formulary medications and medications not listed in the formulary.

Formulary medications are procured through the pharmacy from {D('approved suppliers licensed under the Drugs and Cosmetics Act, 1940')}. The Pharmacy In-Charge maintains supplier records and verifies batch, expiry and storage conditions on receipt.

Non-formulary medications are acquired only with a written request from the prescribing doctor, reviewed and approved by {D('the Pharmacy In-Charge or a committee member')}, and documented in the non-formulary register. Emergency non-formulary requests follow the same documentation but may be approved retrospectively within {D('24 hours')}.""",

f"""5.4 Medication access when the pharmacy is closed

There is a procedure to obtain medication when the pharmacy is closed.

{HOSPITAL} maintains {D('a night cupboard / emergency medication stock on each in-patient floor')} accessible to the duty nurse. The stock list is defined by the committee and matches MOM.2.e (emergency medications).

The duty nurse documents every withdrawal against the patient's name and medication order. The Pharmacy In-Charge reconciles withdrawals the next working day. Missing or unreconciled items trigger an incident report under MOM.7.""",

f"""5.5 Implantable prostheses and medical devices

Implantable prostheses and medical devices are used in accordance with laid-down criteria and are within the committee's scope.

The committee defines which implantable prostheses and medical devices are approved for use at {HOSPITAL}. Criteria include clinical indication, supplier qualification, batch traceability and cost disclosure.

Detailed guidance on procurement, patient and family counselling, and traceability of implants is in MOM.9. This step ensures the committee has oversight; MOM.9 owns the operational detail.""",

f"""5.6 Clinician adherence to the formulary

Clinicians adhere to the current formulary.

Prescribers are expected to prescribe from the current formulary. The Pharmacy In-Charge flags off-formulary prescriptions to the prescriber and records them.

The committee reviews adherence data {D('quarterly')} and takes action where off-formulary prescribing is frequent or unjustified. Action may include education, formulary revision, or restriction.""",
]

STOP_WORK = ""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for committee constitution and that pharmacy services follow written guidance.

Multidisciplinary Medication Committee (Pharmacy and Therapeutics)
- Develops and maintains the formulary; governs pharmacy services and medication usage; reviews adherence, incidents and trends.

Pharmacy In-Charge
- Implements committee decisions; manages formulary stock, non-formulary acquisition and after-hours reconciliation.

Treating doctors (prescribers)
- Prescribe from the current formulary; follow non-formulary acquisition procedure when needed.

Nurses
- Follow the after-hours medication access procedure; document withdrawals.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Tracks CAPA when committee decisions are not implemented."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at committee records and pharmacy operations.

What is monitored each quarter:

- Formulary currency: last review date, additions or deletions and rationale.
- Committee meeting minutes and attendance.
- Non-formulary acquisition register: completeness of documentation.
- After-hours withdrawal reconciliation and any unreconciled items.
- Implant list maintained under committee oversight (MOM.9 detail).
- Formulary adherence data and committee action on off-formulary prescribing.

Root-cause analysis is required when the same lapse recurs within six months.

This policy is reviewed {D('annually')}, and sooner when MOM.2–MOM.9 or the scope of clinical services changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All pharmacy staff, prescribers and nursing staff are trained on this policy at induction and {D('once a year')} after that. Training covers the formulary, non-formulary procedure, after-hours access, and reporting.

Staff acknowledgement

I have read this Multidisciplinary Committee Guides Pharmacy Services and Medication Management policy of {HOSPITAL}. I will prescribe from the formulary, follow acquisition procedures and report breaches.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Pharmacy In-Charge holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/01",
    version=VERSION,
    prepared_by=D("Pharmacy In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.1.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945 — formulary and licensed pharmacy requirements.
- Pharmacy Act, 1948 — registered pharmacist requirement.
- Internal documents of {HOSPITAL}: formulary; non-formulary acquisition register; after-hours withdrawal log; committee meeting minutes; MOM.9 implant guidance."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Pharmacy In-Charge and the Quality Coordinator.

Copies issued to: pharmacy; every in-patient ward (after-hours procedure extract); out-patient dispensary; committee members.

The current version is available to all staff at the {D('pharmacy counter policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, "
    "insofar as the organisation maintains a formulary and acquires medications "
    "through a licensed pharmacy, and the Pharmacy Act, 1948, insofar as pharmacy "
    "services are provided by registered pharmacists"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.1.a",
        "requirement": "The organisation develops, updates and implements a list of medications appropriate for the patients and as per the scope of the organisation's clinical services.",
        "steps": "Statement of intent; Section 3; 5.1 Formulary development and maintenance",
        "responsible": "Multidisciplinary Medication Committee (develop); Pharmacy In-Charge (implement)",
        "records": [
            "Current approved formulary with date of last review.",
            "Committee minutes recording additions, deletions and clinical rationale.",
            "Evidence the formulary is available to all prescribers.",
        ],
    },
    {
        "oe_code": "MOM.1.b",
        "requirement": "Pharmacy services and medication usage are implemented following written guidance through a multidisciplinary committee.",
        "steps": "Statement of intent; Section 3; 5.2 Committee governance of pharmacy services",
        "responsible": "Multidisciplinary Medication Committee (govern); Medical Superintendent (constitute)",
        "records": [
            "Committee constitution and terms of reference.",
            "Quarterly meeting minutes with attendance, decisions, action items and deadlines.",
            "Written guidance documents the committee has issued or endorsed.",
            "Review of medication-usage data and adverse-event trends.",
        ],
    },
    {
        "oe_code": "MOM.1.c",
        "requirement": "The organisation adheres to the procedure for the acquisition of formulary medications and medications not listed in the formulary.",
        "steps": "Section 3; Section 4 items 2–3; 5.3 Acquisition of formulary and non-formulary medications",
        "responsible": "Pharmacy In-Charge (procure and verify); prescriber (non-formulary request); committee member (approve)",
        "records": [
            "Supplier records with licence verification.",
            "Goods-receipt register with batch, expiry and storage check.",
            "Non-formulary acquisition register with prescriber request and approval.",
            "Retrospective approval records for emergency non-formulary requests.",
        ],
    },
    {
        "oe_code": "MOM.1.d",
        "requirement": "There is a procedure to obtain medication when the pharmacy is closed.",
        "steps": "Section 4 item 4; 5.4 Medication access when the pharmacy is closed",
        "responsible": "Duty nurse (withdraw and document); Pharmacy In-Charge (reconcile next working day)",
        "records": [
            "Written after-hours medication access procedure.",
            "Night-cupboard stock list defined by the committee.",
            "Withdrawal log with patient name and medication order reference.",
            "Next-day reconciliation records and incident reports for discrepancies.",
        ],
    },
    {
        "oe_code": "MOM.1.e",
        "requirement": "Implantable prosthesis and medical devices are used in accordance with laid down criteria.",
        "steps": "Section 3; 5.5 Implantable prostheses and medical devices; MOM.9 (detail)",
        "responsible": "Multidisciplinary Medication Committee (criteria and oversight); MOM.9 (operational detail)",
        "records": [
            "Committee-approved list of implantable prostheses and medical devices.",
            "Criteria for approval including clinical indication and supplier qualification.",
            "Cross-reference to MOM.9 for procurement, counselling and traceability.",
        ],
    },
    {
        "oe_code": "MOM.1.f",
        "requirement": "The clinicians adhere to the current formulary.",
        "steps": "Section 3; Section 4 item 6; 5.6 Clinician adherence to the formulary",
        "responsible": "Prescribers (adhere); Pharmacy In-Charge (flag); committee (review)",
        "records": [
            "Off-formulary prescription log maintained by pharmacy.",
            "Quarterly adherence data presented to the committee.",
            "Committee action records where off-formulary prescribing was frequent or unjustified.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.1 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Multidisciplinary committee guides pharmacy services and management of medication." MOM.1.a–f PDF index 82. MOM.1.b and MOM.1.c asterisked. MOM.1.f is Excellence level.

SHAPE: Six What-we-do subsections (5.1–5.6). No stop-work. Disclaimer names Drugs and Cosmetics Act 1940 and Pharmacy Act 1948. MOM roles only."""


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
        "template_test": "mom_v2_adoptable_shape",
        "subtitle": "Formulary, committee governance and medication acquisition.",
        "doc_no": "MOM/POL/01",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom1_v2_draft.json",
        "MOM.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
