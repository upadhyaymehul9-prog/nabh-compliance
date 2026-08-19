# -*- coding: utf-8 -*-
"""MOM.5 v2 — medications are dispensed in a safe manner.

PDF index 84. Stop-work: do not dispense expired, recalled, or unverified high-risk medication.
Six OEs, six What-we-do subsections.
NOTE: PDF header on this page says "Medications are prescribed safely and rationally" but the
OEs are about dispensing. We use the correct summary title.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer

STANDARD_CODE = "MOM.5"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.5.a", "MOM.5.b", "MOM.5.c", "MOM.5.d", "MOM.5.e", "MOM.5.f",
]
POLICY_TITLE = "Medications Are Dispensed in a Safe Manner"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, six steps, stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Every medication is dispensed safely — correct drug, correct label, verified for high-risk "
    "orders, with recalls and near-expiry handled before they reach the patient, and returns "
    "managed properly."
)

PURPOSE = f"""This policy describes how {HOSPITAL} dispenses medications safely: safe dispensing practices, recall handling, near-expiry handling, labelling, high-risk order verification, and medication returns.

It covers MOM.5.a–f.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the Pharmacy In-Charge, pharmacy staff, nurses, the Multidisciplinary Medication Committee, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.5.a–f: safe dispensing; recall handling; near-expiry handling; labelling; high-risk order verification; and return of medications.

Boundaries with other policies of {HOSPITAL}:

- MOM.2 owns storage. MOM.3 owns prescribing. MOM.4 owns uniform order writing.
- MOM.6 owns administration. This policy ends at the point the labelled medication leaves the pharmacy or dispensing area.
- MOM.2.c owns the high-risk medication list. This policy owns the verification step for high-risk orders at dispensing."""

POLICY_STATEMENT = f"""{HOSPITAL} dispenses medications safely, with every dispensed medication labelled and every high-risk medication order verified before dispensing.

Recalled medications are removed and quarantined. Near-expiry medications are handled before they reach the patient. Medications returned to the pharmacy are assessed and re-shelved or destroyed."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. Every dispensed medication is labelled with at minimum: patient name, drug name, strength, dose, route, frequency and expiry date.
2. No expired medication is dispensed. An expired medication found at the dispensing point is quarantined immediately.
3. Recalled medications are removed from all dispensing and storage locations within {D('24 hours')} of the recall notice.
4. Every high-risk medication order is verified by a second pharmacist or a second check (four-eyes principle) before dispensing.
5. Near-expiry medications (within {D('three months')}) are flagged and dispensed first (FEFO) or returned to the supplier where possible.
6. Returned medications are assessed by the pharmacist before being re-shelved; opened, tampered or temperature-exposed returns are destroyed.

Staff who find an expired, recalled, or unverified high-risk medication at the dispensing point do not dispense it. They quarantine it and report to the {D('Pharmacy In-Charge')}."""

PROCEDURE_STEPS = [
f"""5.1 Safe dispensing

Dispensing of medications is done safely.

The pharmacist receives the prescription, verifies it meets MOM.4 requirements (authorised, legible, complete), checks the patient's allergy record (MOM.3.c), selects the correct medication, checks expiry and physical integrity, counts or measures the quantity, and labels the dispensed item.

A final check is performed before handing the medication to the patient or nurse: right patient, right drug, right strength, right quantity. For in-patients, the medication is delivered to the ward in a sealed or labelled container.""",

f"""5.2 Recall handling

Medication recalls are handled effectively.

When a recall notice is received (from the manufacturer, distributor, or regulatory authority), the Pharmacy In-Charge:

1. Identifies all affected batches in the pharmacy and satellite storage locations.
2. Removes affected stock within {D('24 hours')} and places it in the quarantine area with a recall label.
3. Notifies the Multidisciplinary Medication Committee and the Medical Superintendent.
4. Checks dispensing records to identify patients who may have received affected batches and notifies the treating doctor.
5. Documents the recall in the recall register.
6. Returns or destroys affected stock per the manufacturer's or regulator's instructions.""",

f"""5.3 Near-expiry handling

Near-expiry medications are handled effectively.

Medications within {D('three months')} of expiry are flagged with a near-expiry sticker and moved to the dispensing front (FEFO).

The Pharmacy In-Charge reviews near-expiry stock {D('monthly')} and arranges return to supplier, transfer to another facility, or planned consumption where clinically appropriate. Medications that reach expiry are quarantined per MOM.2 and not dispensed.""",

f"""5.4 Labelling of dispensed medications

Dispensed medications are labelled.

Every dispensed medication carries a label with: patient name, drug name (generic and brand where applicable), strength, dose, route of administration, frequency or time of administration, and expiry date. For in-patient unit-dose dispensing, each unit is labelled.

Labels are printed or written legibly. The pharmacist verifies the label against the prescription before release.""",

f"""5.5 High-risk medication order verification

High-risk medication orders are verified before dispensing.

Every medication on the high-risk list (MOM.2.c) requires a second verification before dispensing. The dispensing pharmacist prepares the medication; a second pharmacist (or, where only one pharmacist is on duty, a {D('senior nurse trained in medication verification')}) independently checks drug name, strength, dose, patient identity and expiry.

The verification is documented with the verifier's initials, date and time on the prescription or dispensing log.""",

f"""5.6 Return of medications to the pharmacy

Return of medications to the pharmacy is addressed.

Medications returned from wards or patients are received by the pharmacist, who assesses: packaging integrity, storage conditions (was temperature maintained?), expiry date, and whether the medication was opened or tampered with.

Medications that pass assessment are re-shelved with a return sticker noting the date. Medications that fail are destroyed per the {D('Drugs and Cosmetics Rules, 1945 disposal procedure')}. The return is documented in the return register.""",
]

STOP_WORK = f"""Any pharmacist or nurse who finds an expired, recalled, or unverified high-risk medication about to be dispensed:

1. Does not dispense the medication.
2. Quarantines the item and labels it with the reason, date and name.
3. Reports to the Pharmacy In-Charge the same shift.
4. For a recalled medication, follows the recall procedure (5.2).

No approval is needed to stop dispensing. Patient safety overrides throughput."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for safe dispensing standards.

Multidisciplinary Medication Committee (Pharmacy and Therapeutics)
- Reviews dispensing incidents, recall trends and near-expiry data.

Pharmacy In-Charge
- Implements safe dispensing, recall handling, near-expiry management, labelling standards and return assessment.

Pharmacy staff
- Dispense, label, verify high-risk orders and assess returns.

Nurses
- Verify dispensed medication against the order before administration; return unused medications properly.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks CAPA when dispensing lapses recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at dispensing records and processes.

What is monitored each quarter:

- Sample dispensed medications checked for correct labelling.
- High-risk medication verification documentation.
- Recall register completeness and timeliness.
- Near-expiry stock review and actions taken.
- Return register and disposition records.
- Dispensing-error and near-miss reports.

Root-cause analysis is required when the same dispensing lapse recurs within six months.

This policy is reviewed {D('annually')}, and sooner when the formulary or high-risk list changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All pharmacy staff and nursing staff are trained on this policy at induction and {D('once a year')} after that. Training covers safe dispensing, labelling, high-risk verification, recall handling, and the return procedure.

Staff acknowledgement

I have read this Medications Are Dispensed in a Safe Manner policy of {HOSPITAL}. I will dispense safely, label correctly, verify high-risk orders, and never dispense expired or recalled medication.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Pharmacy In-Charge holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/05",
    version=VERSION,
    prepared_by=D("Pharmacy In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.5.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945 — dispensing, labelling and recall requirements.
- Internal documents of {HOSPITAL}: high-risk medication list (MOM.2.c); dispensing log; recall register; return register; near-expiry review records."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Pharmacy In-Charge and the Quality Coordinator.

Copies issued to: pharmacy; every in-patient ward; out-patient dispensary; emergency room.

The current version is available to all staff at the {D('pharmacy counter policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
FEFO — first expiry, first out
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, "
    "insofar as dispensing is performed by licensed personnel and recalled or expired "
    "medications are withdrawn"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.5.a",
        "requirement": "Dispensing of medications is done safely.",
        "steps": "Statement of intent; Section 3; 5.1 Safe dispensing",
        "responsible": "Pharmacy staff (dispense); Pharmacy In-Charge (oversee)",
        "records": [
            "Dispensing log with patient name, drug, quantity, date and pharmacist initials.",
            "Sample dispensing records verified against prescriptions.",
            "Quarterly audit sample of dispensing accuracy.",
        ],
    },
    {
        "oe_code": "MOM.5.b",
        "requirement": "Medication recalls are handled effectively.",
        "steps": "Section 4 item 3; 5.2 Recall handling",
        "responsible": "Pharmacy In-Charge (coordinate recall); committee (review)",
        "records": [
            "Recall register with batch numbers, dates, quantities and disposition.",
            "Evidence of removal within the defined time limit.",
            "Notification records to treating doctors for affected patients.",
            "Committee review of recall trends.",
        ],
    },
    {
        "oe_code": "MOM.5.c",
        "requirement": "Near-expiry medications are handled effectively.",
        "steps": "Section 4 item 5; 5.3 Near-expiry handling",
        "responsible": "Pharmacy In-Charge (review and action); pharmacy staff (flag and FEFO)",
        "records": [
            "Monthly near-expiry review records with actions taken.",
            "Near-expiry sticker evidence on flagged stock.",
            "Disposal or return-to-supplier records for expired items.",
        ],
    },
    {
        "oe_code": "MOM.5.d",
        "requirement": "Dispensed medications are labelled.",
        "steps": "Section 3; Section 4 item 1; 5.4 Labelling of dispensed medications",
        "responsible": "Pharmacy staff (label); Pharmacy In-Charge (verify standards)",
        "records": [
            "Sample dispensed medications or photographs showing correct labelling.",
            "Label-verification records against prescriptions.",
            "Quarterly audit sample of labelling accuracy.",
        ],
    },
    {
        "oe_code": "MOM.5.e",
        "requirement": "High-risk medication orders are verified before dispensing.",
        "steps": "Section 4 item 4; 5.5 High-risk medication order verification",
        "responsible": "Dispensing pharmacist (prepare); second verifier (check)",
        "records": [
            "Verification documentation with verifier initials, date and time.",
            "High-risk dispensing log.",
            "Quarterly audit sample of high-risk verification compliance.",
        ],
    },
    {
        "oe_code": "MOM.5.f",
        "requirement": "Return of medications to the pharmacy is addressed.",
        "steps": "5.6 Return of medications to the pharmacy",
        "responsible": "Pharmacist (assess returns); nurses (return properly)",
        "records": [
            "Return register with date, drug, reason, assessment outcome and disposition.",
            "Destruction records for medications that failed assessment.",
            "Quarterly audit of return-register completeness.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.5 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header (summary) "Medications are dispensed in a safe manner." MOM.5.a–f PDF index 84. MOM.5.a, MOM.5.b, MOM.5.c, MOM.5.d, MOM.5.f asterisked. MOM.5.d and MOM.5.e Core.

SHAPE: Six What-we-do subsections (5.1–5.6). Stop-work yes (do not dispense expired/recalled/unverified high-risk). Disclaimer names Drugs and Cosmetics Act 1940. MOM roles only."""


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
        "subtitle": "Safe dispensing, labelling, recall handling and high-risk verification.",
        "doc_no": "MOM/POL/05",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom5_v2_draft.json",
        "MOM.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
