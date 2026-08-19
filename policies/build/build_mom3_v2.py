# -*- coding: utf-8 -*-
"""MOM.3 v2 — medications are prescribed safely and rationally.

PDF index 83. No stop-work. Eight OEs, eight What-we-do subsections.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer

STANDARD_CODE = "MOM.3"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.3.a", "MOM.3.b", "MOM.3.c", "MOM.3.d",
    "MOM.3.e", "MOM.3.f", "MOM.3.g", "MOM.3.h",
]
POLICY_TITLE = "Medications Are Prescribed Safely and Rationally"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, eight steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Prescribing is safe and rational — guided by good practices, minimum prescription "
    "requirements, allergy checks, decision support, safe verbal orders, audit and medication reconciliation."
)

PURPOSE = f"""This policy describes how {HOSPITAL} ensures safe and rational prescribing: good practice guidelines, minimum prescription requirements, allergy and adverse-reaction checks, clinical decision support, verbal orders, prescription audit, corrective action, and medication reconciliation at transition points.

It covers MOM.3.a–h.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to treating doctors (prescribers), the Pharmacy In-Charge, nurses, the Multidisciplinary Medication Committee, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.3.a–h: rational prescribing guidelines; minimum prescription requirements; allergy ascertainment; clinical decision support; verbal orders; prescription audit; corrective and preventive action; and medication reconciliation at transition points.

Boundaries with other policies of {HOSPITAL}:

- MOM.1 owns the formulary. MOM.4 owns uniform order writing. MOM.5 owns dispensing. MOM.6 owns administration.
- MOM.7 owns monitoring after administration, near-miss and adverse-drug-reaction reporting. Audit findings under MOM.3.f–g that relate to adverse events feed into MOM.7.
- PSQ.5 owns the general incident reporting system; medication-related audit findings cross-reference PSQ.5 where applicable."""

POLICY_STATEMENT = f"""{HOSPITAL} requires that every prescription is rational, complete, and checked for allergies and previous adverse drug reactions before the medication is dispensed.

{HOSPITAL} provides clinical decision support to assist prescribers. Verbal orders are handled safely. Prescription audit drives corrective and preventive action. Medication reconciliation occurs at every transition point."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. Every prescription meets the minimum requirements defined in MOM.3.b before it is dispensed.
2. Drug allergies and previous adverse drug reactions are ascertained and documented before prescribing.
3. Verbal orders are used only when the prescriber cannot write or enter the order; they are read back and documented within {D('24 hours')}.
4. Off-formulary prescribing follows MOM.1.c.
5. Prescription audit is conducted at least {D('quarterly')} and findings are acted upon.
6. Medication reconciliation is performed at admission, transfer and discharge.

Staff who see a breach report it the same shift to the {D('Pharmacy In-Charge')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Rational prescribing guidelines

Medication prescription is in consonance with good practices and guidelines for the rational prescription of medications.

{HOSPITAL} adopts {D('the WHO Guide to Good Prescribing and the National List of Essential Medicines as reference frameworks')}. The Multidisciplinary Medication Committee reviews prescribing patterns {D('quarterly')} against these guidelines.

Prescribers are expected to prescribe by generic name where the formulary permits and to avoid unnecessary polypharmacy.""",

f"""5.2 Minimum prescription requirements

{HOSPITAL} adheres to the determined minimum requirements of a prescription.

Every prescription includes: patient name; unique identification number; date; prescriber name, signature and registration number; drug name (generic preferred); strength; dose; route; frequency or timing; duration; and quantity where relevant. Incomplete prescriptions are returned to the prescriber before dispensing.

The Pharmacy In-Charge verifies minimum requirements at the point of dispensing.""",

f"""5.3 Allergy and adverse-drug-reaction check

Drug allergies and previous adverse drug reactions are ascertained before prescribing.

At first contact (registration or admission), the nurse or doctor asks the patient about known drug allergies and previous adverse drug reactions. The response is documented in the {D('allergy section of the medical record and on the allergy band or alert sticker')}.

Prescribers check the allergy record before every new prescription. The pharmacy system (manual or electronic) flags known allergies at dispensing.""",

f"""5.4 Clinical decision support

{HOSPITAL} has a mechanism to assist the clinician in prescribing appropriate medication.

Decision support includes: {D('the current formulary with indications and dosing guidance; drug-interaction references available at the pharmacy counter; and allergy alerts')}. Where the hospital uses an electronic prescribing system, automated interaction and allergy alerts are enabled.

The Multidisciplinary Medication Committee reviews the adequacy of decision support {D('annually')}.""",

f"""5.5 Verbal orders

Implementation of verbal orders ensures safe medication management practices.

Verbal orders are permitted only when the prescriber cannot write or electronically enter the order (for example during a procedure or emergency). The receiver (nurse or pharmacist) writes the order, reads it back including drug name, dose, route and frequency, and obtains confirmation. The prescriber countersigns within {D('24 hours')}.

Verbal orders are documented in the same location as written orders (see MOM.4.b).""",

f"""5.6 Prescription audit

Audit of medication orders and prescriptions is carried out to check for safe and rational prescription of medications.

The Quality Coordinator or a pharmacist conducts a prescription audit at least {D('quarterly')}. The audit sample is {D('at least 30 prescriptions per quarter')} drawn from in-patient, out-patient and emergency.

The audit checks: minimum requirements (5.2); allergy documentation; rational prescribing markers (generic name, polypharmacy, off-formulary use); verbal-order compliance; and reconciliation at transitions.""",

f"""5.7 Corrective and preventive action from audit

Corrective and preventive action is taken based on the audit, where appropriate.

The Quality Coordinator presents audit findings to the Multidisciplinary Medication Committee. The committee decides corrective and preventive action: education, formulary change, system redesign, or individual feedback.

Actions are tracked to closure. Root-cause analysis is required when the same prescribing defect recurs within six months. Findings that relate to adverse events also feed into MOM.7 and PSQ.5.""",

f"""5.8 Medication reconciliation at transition points

Reconciliation of medications occurs at transition points of patient care.

At admission, the nurse or pharmacist documents the patient's current medication list (home medications, over-the-counter, and herbal). The treating doctor reconciles this list with the new prescription and documents any intentional changes or discontinuations.

At internal transfer and at discharge, reconciliation is repeated. The discharge summary (AAC.8) includes the reconciled medication list with clear instructions for the patient.""",
]

STOP_WORK = ""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for safe and rational prescribing across the organisation.

Multidisciplinary Medication Committee (Pharmacy and Therapeutics)
- Reviews prescribing patterns and audit findings; decides corrective action; maintains decision-support resources.

Treating doctors (prescribers)
- Prescribe rationally, check allergies, follow minimum requirements and verbal-order rules.

Pharmacy In-Charge
- Verifies minimum prescription requirements at dispensing; conducts or supports prescription audit; provides decision-support resources.

Nurses
- Ascertain allergies at first contact; receive and document verbal orders safely; perform medication reconciliation.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Tracks CAPA and presents findings to the committee."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at prescriptions and reconciliation records.

What is monitored each quarter:

- Prescription audit results: minimum requirements, allergy documentation, rational prescribing markers.
- Verbal-order compliance: read-back documented, countersigned within time limit.
- Medication reconciliation at admission, transfer and discharge.
- CAPA closure from previous audit findings.
- Decision-support adequacy review (annual).

Root-cause analysis is required when the same prescribing defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when the formulary or prescribing guidelines change."""

TRAINING_ACKNOWLEDGEMENT = f"""All prescribers, pharmacy staff and nursing staff are trained on this policy at induction and {D('once a year')} after that. Training covers rational prescribing, minimum requirements, allergy checks, verbal orders, audit and reconciliation.

Staff acknowledgement

I have read this Medications Are Prescribed Safely and Rationally policy of {HOSPITAL}. I will follow prescribing standards, check allergies, and participate in audit.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Pharmacy In-Charge holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/03",
    version=VERSION,
    prepared_by=D("Pharmacy In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.3.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945 — prescription requirements.
- WHO Guide to Good Prescribing — rational prescribing framework.
- Internal documents of {HOSPITAL}: formulary (MOM.1); prescription audit reports; allergy documentation; medication reconciliation forms; MOM.7 adverse-event reports."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Pharmacy In-Charge and the Quality Coordinator.

Copies issued to: pharmacy; every in-patient ward; out-patient clinics; emergency room; nursing administration.

The current version is available to all staff at the {D('pharmacy counter policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 5)
CAPA — corrective and preventive action
LASA — look-alike sound-alike
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 3)
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

STATUTE_CLAUSE = (
    "the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, "
    "insofar as prescriptions meet minimum legal requirements"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.3.a",
        "requirement": "Medication prescription is in consonance with good practices/guidelines for the rational prescription of medications.",
        "steps": "Statement of intent; Section 3; 5.1 Rational prescribing guidelines",
        "responsible": "Prescribers (prescribe rationally); committee (review patterns)",
        "records": [
            "Adopted prescribing guidelines or framework reference.",
            "Committee review of prescribing patterns (quarterly).",
            "Generic-name prescribing and polypharmacy monitoring data.",
        ],
    },
    {
        "oe_code": "MOM.3.b",
        "requirement": "The organisation adheres to the determined minimum requirements of a prescription.",
        "steps": "Section 3; Section 4 item 1; 5.2 Minimum prescription requirements",
        "responsible": "Prescribers (write complete prescriptions); Pharmacy In-Charge (verify at dispensing)",
        "records": [
            "Defined list of minimum prescription requirements.",
            "Sample prescriptions verified at dispensing.",
            "Returned-prescription log for incomplete prescriptions.",
            "Quarterly audit sample checking minimum requirements.",
        ],
    },
    {
        "oe_code": "MOM.3.c",
        "requirement": "Drug allergies and previous adverse drug reactions are ascertained before prescribing.",
        "steps": "Section 3; Section 4 item 2; 5.3 Allergy and adverse-drug-reaction check",
        "responsible": "Nurses (ascertain at first contact); prescribers (check before prescribing); pharmacy (flag at dispensing)",
        "records": [
            "Allergy documentation in medical records.",
            "Allergy band or alert sticker evidence.",
            "Pharmacy allergy-flag records.",
        ],
    },
    {
        "oe_code": "MOM.3.d",
        "requirement": "The organisation has a mechanism to assist the clinician in prescribing appropriate medication.",
        "steps": "5.4 Clinical decision support",
        "responsible": "Pharmacy In-Charge (provide resources); committee (review adequacy annually)",
        "records": [
            "Decision-support resources available at the pharmacy counter.",
            "Drug-interaction reference availability evidence.",
            "Annual review record by the committee.",
        ],
    },
    {
        "oe_code": "MOM.3.e",
        "requirement": "Implementation of verbal orders ensures safe medication management practices.",
        "steps": "Section 4 item 3; 5.5 Verbal orders",
        "responsible": "Prescribers (countersign); nurses or pharmacists (receive, read back, document)",
        "records": [
            "Verbal-order entries with read-back documentation.",
            "Countersignature within the defined time limit.",
            "Audit sample of verbal-order compliance.",
        ],
    },
    {
        "oe_code": "MOM.3.f",
        "requirement": "Audit of medication orders/prescription is carried out to check for safe and rational prescription of medications.",
        "steps": "5.6 Prescription audit",
        "responsible": "Quality Coordinator or pharmacist (conduct audit); committee (review findings)",
        "records": [
            "Quarterly prescription audit reports with sample size and findings.",
            "Audit criteria checklist.",
            "Committee meeting minutes reviewing audit findings.",
        ],
    },
    {
        "oe_code": "MOM.3.g",
        "requirement": "Corrective and/or preventive action(s) is taken based on the audit, where appropriate.",
        "steps": "5.7 Corrective and preventive action from audit",
        "responsible": "Committee (decide CAPA); Quality Coordinator (track closure)",
        "records": [
            "CAPA log linked to audit findings.",
            "Root-cause analysis records for recurring defects.",
            "Closure evidence for each action item.",
        ],
    },
    {
        "oe_code": "MOM.3.h",
        "requirement": "Reconciliation of medications occurs at transition points of patient care.",
        "steps": "Section 3; Section 4 item 6; 5.8 Medication reconciliation at transition points",
        "responsible": "Nurses or pharmacist (document home medications); treating doctor (reconcile); AAC.8 (discharge summary)",
        "records": [
            "Medication reconciliation form at admission.",
            "Reconciliation entries at internal transfer.",
            "Discharge summary with reconciled medication list.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.3 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Medications are prescribed safely and rationally." MOM.3.a–h PDF index 83. MOM.3.a, MOM.3.b, MOM.3.e asterisked. MOM.3.d Excellence. MOM.3.f–g Achievement.

SHAPE: Eight What-we-do subsections (5.1–5.8). No stop-work. Disclaimer names Drugs and Cosmetics Act 1940. MOM roles only."""


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
        "subtitle": "Rational prescribing, allergy checks, verbal orders, audit and reconciliation.",
        "doc_no": "MOM/POL/03",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom3_v2_draft.json",
        "MOM.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
