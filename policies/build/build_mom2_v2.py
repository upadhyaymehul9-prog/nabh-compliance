# -*- coding: utf-8 -*-
"""MOM.2 v2 — medications are stored appropriately and are available where required.

PDF index 82–83. Has stop-work (expired, recalled, incorrectly stored medication).
Six OEs, six What-we-do subsections.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer

STANDARD_CODE = "MOM.2"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.2.a", "MOM.2.b", "MOM.2.c", "MOM.2.d", "MOM.2.e", "MOM.2.f",
]
POLICY_TITLE = "Medications Are Stored Appropriately and Are Available Where Required"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, six steps, stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Medications are stored safely across the organisation, including high-risk and "
    "emergency medications, so that every medication administered is fit for use and "
    "emergency medications are always available."
)

PURPOSE = f"""This policy describes how {HOSPITAL} stores medications safely, maintains inventory control, defines and stores high-risk medications including look-alike sound-alike medications, provides emergency medications uniformly, and ensures emergency medications are available and replenished promptly.

It covers MOM.2.a–f. Medication storage environment boundaries with FMS (facilities) are noted: FMS owns the building environment; this policy owns the medication-specific storage conditions.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to pharmacy staff, nurses, the Pharmacy In-Charge, treating doctors, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.2.a–f: clean and safe storage environment; inventory control; high-risk and look-alike sound-alike medications; storage of high-risk medications outside pharmacy; emergency medication list and uniform storage; and availability and replenishment.

Boundaries with other policies of {HOSPITAL}:

- FMS owns the building environment (temperature control, ventilation, lighting). This policy owns medication-specific storage conditions (refrigerator temperature logs, light-sensitive storage, controlled-substance security).
- MOM.1 owns the formulary and committee governance. This policy owns how approved medications are stored.
- MOM.5 owns dispensing. MOM.6 owns administration."""

POLICY_STATEMENT = f"""{HOSPITAL} stores medications in a clean, safe and secure environment incorporating manufacturer recommendations.

{HOSPITAL} defines a list and mechanism for high-risk medications including look-alike sound-alike medications and stores them with additional safeguards.

Emergency medications are defined, stored uniformly, available at all times, and replenished promptly when used."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. Medications are stored at the temperature, humidity and light conditions stated on the label or manufacturer's recommendation. A deviation is an incident.
2. Expired medications are never dispensed or administered. They are quarantined and disposed of per the Drugs and Cosmetics Rules, 1945.
3. Recalled medications are removed from all storage locations within {D('24 hours')} of the recall notice and quarantined.
4. High-risk medications and look-alike sound-alike medications are stored with additional alerts (tall-man lettering, colour-coded labels, separate shelves) as defined by the committee.
5. Emergency medications are checked {D('daily on each shift change')} for availability, expiry and seal integrity. A missing or expired emergency medication is replaced immediately.
6. Controlled substances (narcotics, psychotropic) are stored in a double-locked cupboard with a register; detailed requirements are in MOM.8.

Staff who find an expired, recalled, or incorrectly stored medication do not use it. They quarantine it and report to the {D('Pharmacy In-Charge')} the same shift."""

PROCEDURE_STEPS = [
f"""5.1 Clean, safe and secure storage environment

Medications are stored in a clean, safe and secure environment incorporating the manufacturer's recommendations.

The pharmacy and every satellite storage area (ward cupboard, refrigerator, night cupboard) meets: temperature within manufacturer's range (monitored {D('twice daily')} with a min-max thermometer or data logger); protection from light where the label requires it; restricted access (locked when unattended); clean shelves free of dust and spillage.

The Pharmacy In-Charge inspects satellite storage areas {D('monthly')}. Temperature excursions trigger quarantine and pharmacist assessment before the medication is returned to stock.""",

f"""5.2 Inventory control

Sound inventory control practices guide storage of medications throughout {HOSPITAL}.

First-expiry-first-out (FEFO) is the default issue method. Minimum and maximum stock levels are defined for each formulary item. The Pharmacy In-Charge runs a stock-count {D('monthly')} and reconciles against the register. Discrepancies are investigated the same day.

Near-expiry medications (within {D('three months')} of expiry) are flagged with a near-expiry sticker and moved to the dispensing front. Near-expiry handling details are in MOM.5.c.""",

f"""5.3 High-risk medications and look-alike sound-alike medications

{HOSPITAL} defines a list and mechanism for storage of high-risk medications including look-alike sound-alike medications.

The Multidisciplinary Medication Committee defines the high-risk medication list at least {D('annually')}. The list includes look-alike sound-alike pairs identified in this hospital's formulary.

Storage safeguards include: tall-man lettering on shelf labels; colour-coded bin cards; physical separation of look-alike pairs where feasible; alert stickers on high-risk bins. The Pharmacy In-Charge verifies safeguards are in place during {D('monthly')} inspections.""",

f"""5.4 High-risk medications outside the pharmacy

High-risk medications are stored in areas of the organisation where it is clinically necessary.

Where clinical need requires high-risk medications to be stored on a ward or in the emergency room, the committee approves the location and the list. The same safeguards (5.3) apply. The Pharmacy In-Charge audits these locations {D('monthly')}.

Quantities outside the pharmacy are limited to {D('the minimum needed for immediate clinical use')}. Replenishment follows the pharmacy requisition process.""",

f"""5.5 Emergency medication list and uniform storage

The list of emergency medications is defined and stored uniformly.

The Multidisciplinary Medication Committee defines the emergency medication list. The list is stored in every {D('crash cart / emergency tray')} in a uniform layout. Layout means the same sequence and labelling across all units.

The Pharmacy In-Charge issues a master layout diagram. Ward nurses verify the layout matches the diagram after every use and during the daily check (see 5.6).""",

f"""5.6 Availability and replenishment of emergency medications

Emergency medications are available all the time and are replenished promptly when used.

Emergency medications are checked {D('daily on each shift change')} for availability, expiry and seal integrity. A checklist is signed by the duty nurse.

When an emergency medication is used, the ward nurse requests replacement from the pharmacy immediately. The Pharmacy In-Charge replenishes within {D('one hour during pharmacy hours; within two hours via the after-hours procedure (MOM.1.d)')}. A delay beyond that limit triggers an incident report.""",
]

STOP_WORK = f"""Any staff member who finds an expired, recalled, or incorrectly stored medication (temperature excursion, broken seal, wrong location):

1. Does not dispense or administer the medication.
2. Removes it from the shelf or tray and places it in the {D('quarantine bin')} at the pharmacy or ward.
3. Labels it with the reason, date and name.
4. Reports to the Pharmacy In-Charge (or duty nurse if pharmacy is closed) the same shift.

No approval is needed to quarantine. The Pharmacy In-Charge investigates and decides disposition (return to stock after assessment, return to supplier, or destroy)."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that medication storage meets regulatory and accreditation requirements.

Multidisciplinary Medication Committee (Pharmacy and Therapeutics)
- Defines high-risk medication list, look-alike sound-alike pairs, and emergency medication list.

Pharmacy In-Charge
- Implements storage standards; inspects satellite areas; manages inventory; replenishes emergency medications.

Nurses
- Check emergency medications daily; document withdrawals; quarantine suspect medications.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks CAPA when storage lapses recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at storage conditions and records.

What is monitored each quarter:

- Temperature logs in pharmacy and satellite areas; excursion incidents.
- Inventory reconciliation records and discrepancies.
- High-risk and LASA safeguards in place during unannounced spot-check.
- Emergency medication checklist completion and replenishment times.
- Quarantine log entries and disposition records.
- Near-expiry handling and FEFO compliance.

Root-cause analysis is required when the same storage lapse recurs within six months.

This policy is reviewed {D('annually')}, and sooner when the formulary or high-risk list changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All pharmacy staff and nursing staff are trained on this policy at induction and {D('once a year')} after that. Training covers storage standards, high-risk safeguards, emergency medication checks, and the quarantine procedure.

Staff acknowledgement

I have read this Medications Are Stored Appropriately policy of {HOSPITAL}. I will follow storage standards, check emergency medications, and quarantine suspect stock.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Pharmacy In-Charge holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/02",
    version=VERSION,
    prepared_by=D("Pharmacy In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.2.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945 — labelling, storage and expiry requirements.
- Internal documents of {HOSPITAL}: formulary; high-risk medication list; LASA list; emergency medication list and layout diagram; temperature logs; inventory registers."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Pharmacy In-Charge and the Quality Coordinator.

Copies issued to: pharmacy; every in-patient ward; emergency room; operation theatre; ICU where it exists.

The current version is available to all staff at the {D('pharmacy counter policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
FEFO — first expiry, first out
LASA — look-alike sound-alike
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, "
    "insofar as medications are stored in accordance with labelling, temperature "
    "and security requirements"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.2.a",
        "requirement": "Medications are stored in a clean, safe and secure environment; and incorporating the manufacturer's recommendation(s).",
        "steps": "Section 3; Section 4 items 1–2; 5.1 Clean, safe and secure storage environment",
        "responsible": "Pharmacy In-Charge (implement and inspect); nurses (satellite areas)",
        "records": [
            "Temperature logs for pharmacy and each satellite storage area.",
            "Monthly inspection records of satellite areas.",
            "Temperature-excursion incident reports and disposition.",
        ],
    },
    {
        "oe_code": "MOM.2.b",
        "requirement": "Sound inventory control practices guide storage of the medications throughout the organisation.",
        "steps": "5.2 Inventory control",
        "responsible": "Pharmacy In-Charge (stock counts and reconciliation)",
        "records": [
            "Monthly stock-count records with reconciliation.",
            "Discrepancy investigation records.",
            "Near-expiry flagging and FEFO compliance evidence.",
        ],
    },
    {
        "oe_code": "MOM.2.c",
        "requirement": "The organisation defines a list and mechanism for storage of high-risk medication(s) including look-alike sound-alike medications.",
        "steps": "Section 3; Section 4 item 4; 5.3 High-risk medications and look-alike sound-alike medications",
        "responsible": "Multidisciplinary Medication Committee (define list); Pharmacy In-Charge (implement safeguards)",
        "records": [
            "Committee-approved high-risk medication list with LASA pairs.",
            "Photographic or inspection evidence of tall-man lettering, colour-coded labels and physical separation.",
            "Monthly inspection records verifying safeguards.",
            "Annual review record of the list by the committee.",
        ],
    },
    {
        "oe_code": "MOM.2.d",
        "requirement": "High-risk medications are stored in areas of the organisation where it is clinically necessary.",
        "steps": "5.4 High-risk medications outside the pharmacy",
        "responsible": "Committee (approve location and list); Pharmacy In-Charge (audit monthly)",
        "records": [
            "Committee approval for each location storing high-risk medications outside pharmacy.",
            "List of high-risk medications approved for each location.",
            "Monthly audit records of those locations.",
        ],
    },
    {
        "oe_code": "MOM.2.e",
        "requirement": "The list of emergency medications is defined and is stored uniformly.",
        "steps": "Section 3; Section 4 item 5; 5.5 Emergency medication list and uniform storage",
        "responsible": "Multidisciplinary Medication Committee (define); Pharmacy In-Charge (layout diagram); ward nurses (verify)",
        "records": [
            "Committee-approved emergency medication list.",
            "Master layout diagram issued by the Pharmacy In-Charge.",
            "Photographic or inspection evidence that all locations match the diagram.",
        ],
    },
    {
        "oe_code": "MOM.2.f",
        "requirement": "Emergency medications are available all the time and are replenished promptly when used.",
        "steps": "Section 4 item 5; 5.6 Availability and replenishment of emergency medications",
        "responsible": "Duty nurse (daily check); Pharmacy In-Charge (replenish); ward nurse (request)",
        "records": [
            "Daily shift-change checklist for each emergency medication location.",
            "Replenishment records with time-stamp.",
            "Incident reports when replenishment exceeded the time limit.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.2 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Medications are stored appropriately and are available where required." MOM.2.a–f PDF indices 82–83. MOM.2.c and MOM.2.e asterisked.

SHAPE: Six What-we-do subsections (5.1–5.6). Stop-work yes (quarantine expired/recalled/incorrectly stored). Disclaimer names Drugs and Cosmetics Act 1940. MOM roles only."""


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
        "subtitle": "Safe storage, high-risk safeguards and emergency medication availability.",
        "doc_no": "MOM/POL/02",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom2_v2_draft.json",
        "MOM.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
