# -*- coding: utf-8 -*-
"""Template-test rebuild of FMS.3 as an adoptable hospital policy.

Does NOT overwrite policies/drafts/fms3_draft.json or build_fms3.py.
Writes policies/drafts/fms3_v2_draft.json only. No SQL. No Supabase insert.
"""
from __future__ import annotations

import sys

from fms_v2_common import BLANK, D, HOSPITAL, emit_v2, verify_shape
from policy_build_common import make_disclaimer

STANDARD_CODE = "FMS.3"
CHAPTER = "FMS"
OE_CODES = [
    "FMS.3.a", "FMS.3.b", "FMS.3.c", "FMS.3.d", "FMS.3.e", "FMS.3.f", "FMS.3.g",
]
POLICY_TITLE = "Medical and Support-Service Equipment Programme"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "Template rebuild to FMS.5 v2.2 shape. Not an approved master.",
    },
]

PURPOSE = f"""This policy governs how {HOSPITAL} plans, inventories, maintains, inspects, calibrates, recalls and times downtime for medical and support-service equipment.

It is the hospital-wide equipment programme. It is not the laboratory rule that a result is not issued from an overdue calibrator, the imaging AERB quality-assurance file, steriliser load validation, crash-cart contents, or building-plant tests of the generator. Those programmes remain in force. This policy puts the device on an inventory, a PPM job card and a recall search.

Editable defaults are marked {D('like this')}. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """A sticker is not PPM. A recall letter that never left quality has not been complied with. An overdue measuring device is withdrawn."""

SCOPE = f"""This policy applies to medical equipment and support-service equipment of {HOSPITAL} — owned, leased, loaned, consigned or outsourced — and to the people who plan, inventory, operate, maintain, inspect, calibrate, recall and record downtime for that equipment.

It covers planning against the service directory and strategic plan; inventory and logs; implemented preventive and breakdown maintenance; periodic inspection and calibration; qualified operators and maintainers; device adverse events, hazard notices and recalls; and critical-equipment downtime from the user's report to inspection and corrective action.

A generator, pump or UPS that is building plant is the utilities programme. A grab rail is facility-safety infrastructure. Medical-gas plant is the gas programme. A flowmeter may sit on this inventory if this hospital lists it as a device; the gas programme still owns the gas path. Steriliser load validation stays the reprocessing programme; a failed boiler or door seal is here. A crash-cart checklist is the resuscitation-kit policy; the defibrillator on the cart is still equipment here. Credentialing files, when that programme is written, hold the method; this policy requires that the person who pressed the button was trained for that class. Implant selection stays the implant policy. Patient-facing equipment charges stay expected-cost, not this PPM file.

NHM Biomedical Equipment Management and Maintenance Program (BEMMP) is the criticality and PPM framework — not a named NHM-contract mandate, not the Clinical Establishments Act, and not Central Electricity Authority guidance. CDSCO and the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, govern regulated devices, adverse events and recalls insofar as they apply to devices this hospital uses. This hospital is not a manufacturer."""

POLICY_STATEMENT = f"""Equipment is planned against the services the hospital actually offers and the strategic plan. A service the directory does not provide is not given another hospital's ICU list. BEMMP criticality and IPHS 2022 are planning frameworks, not a NABH equipment catalogue.

Every item that can harm a patient if it fails or is missing is on the inventory: unique identifier, location, owner department, criticality, and whether it is owned, loaned, consigned or outsourced. Logs record acceptance, PPM, breakdown and calibration due. An item in use that is not on the inventory is a defect.

The operational and maintenance plan is implemented. Preventive tasks follow criticality and the manufacturer; breakdowns are reported by the user, attended, and closed with a fault, time-to-attend and spare — not an "OK" with no fault. A binder of manufacturer PDFs, or a sticker with no job card, is not implementation. Annual PPM bunched the week before an assessment is not this plan.

Measuring and delivering devices are inspected in service and calibrated against a traceable standard. An overdue measuring device is withdrawn until it passes. The laboratory still does not issue a result from an overdue calibrator; imaging still does not issue a report from an overdue AERB-QA device. Those no-report rules stay those programmes; the due date lives on this inventory. This policy does not invent a SHCO-wide six-month calibration calendar.

Only named, trained people operate or maintain each class. A visiting technician without a job card, or a nurse using an infusion pump they were never shown, is a failure of this policy.

Device-related adverse events are captured. Hazard notices and recalls from CDSCO, the manufacturer or the vendor are searched against the inventory; affected items are quarantined and returned or destroyed. A letter in quality that never reached the ward has not been complied with. Harm to a patient is also an incident.

Critical equipment — the subset whose failure stops a defined service (ventilator, anaesthesia workstation, autoclave as equipment, imaging device, clinical analyser, blood-bank refrigerator, and others named here) — has downtime timed from the user's report, not from the engineer's arrival, until inspection and corrective action restore it or a defined alternative is in place."""

NON_NEGOTIABLES = f"""The following are prohibited.

1. Using a medical or support-service device on a patient that is not on the inventory.
2. Leaving an overdue measuring device in service.
3. Filing a hazard notice or recall in quality without searching the inventory and quarantining affected serial numbers.
4. Counting a sticker, a manufacturer PDF, or PPM bunched for assessment week, as implemented maintenance.
5. Operating or opening a device the person has not been trained and named for.

Anyone who sees a prohibited act stops it under the stop-work clause and reports it the same shift to the {D('Maintenance In-Charge')} or, at night, the Night Duty Officer."""

PROCEDURE_STEPS = [
f"""5.1 Plan and inventory

The Maintenance In-Charge (biomedical for this policy) holds the equipment plan against the service directory and the strategic plan, including replacement of condemned items. A new service is not offered until the Medical Superintendent has signed that the equipment it needs is present or a dated gap is accepted.

The inventory includes loaners and outsourced analysers. Each item has a unique identifier, location, owner, criticality and tenure. Logs: acceptance, PPM, breakdown, calibration due. Crash-cart checklists do not replace the defibrillator file.""",

f"""5.2 PPM, breakdown, inspection and calibration

Preventive maintenance runs to the criticality and manufacturer task list. The user reports a breakdown; the attender records fault, time-to-attend and spare; cannibalisation and loaner rules are written. Sample job cards show last month's PPM and last week's breakdown actually happened.

In-service inspection covers housing, leads, alarms and accessories. Calibration against a traceable standard covers monitors, defibrillator energy, infusion pumps, OT table scales, and laboratory or imaging instruments as inventory items. Overdue measuring devices are withdrawn until passed. Steriliser load validation stays the reprocessing programme; a failed door seal is this job card.""",

f"""5.3 Qualified operators and maintainers

The Maintenance In-Charge holds the trained-operator list and the maintainer list by class. Clinical heads do not let untrained staff press the button. Visiting technicians work only against a job card. Training is recorded at induction, on a new class, and {D('once a year')}.""",

f"""5.4 Adverse events, recalls and critical downtime

A device-related adverse event is recorded here. If a patient was harmed it is also an incident; if it is also a medication-delivery event it is dual-entered with that programme.

Hazard notices and recalls are received, the inventory is searched, and affected items are quarantined and returned or destroyed. An empty recall log is acceptable only if the search was still run when a notice named a type this hospital holds.

Critical equipment is listed. Downtime starts when the user reports and ends when inspection and corrective action restore the item or a defined alternative (loaner, diversion, recorded pause) is in place. The clock does not start at engineer arrival.""",
]

STOP_WORK = f"""Every person has the authority and the duty to stop an act that breaches a non-negotiable rule: an uninventoried device in use; an overdue measuring device still on a patient; a recalled item left in the ward; an untrained person at a critical device.

The person says "stop", withdraws the device from use if they are competent to, and reports the same shift to the {D('Maintenance In-Charge')} or the Night Duty Officer. There is no retaliation for a good-faith stop-work."""

RESPONSIBILITY = f"""Roles below are titles, not vacancies.

Medical Superintendent
- Accountable that this programme is issued and resourced.
- Signs that a new service has the equipment it needs.

Maintenance In-Charge (biomedical for this policy)
- Owns the plan, inventory, PPM, calibration, recall search and downtime clock.

Nursing Superintendent
- Ensures ward devices in use are on the inventory and that overdue items are not borrowed back into service.

Night Duty Officer
- Receives a night breakdown report; the downtime clock starts then.

Quality Coordinator
- Audits this policy {D('quarterly')}.

Department in-charges
- Do not operate a class their staff are not trained for.
- Do not issue a laboratory or imaging report from an overdue calibrator (those no-report rules stay those programmes).

A RACI snapshot:
- Plan and inventory: Maintenance In-Charge (R/A)
- PPM and breakdown: Maintenance In-Charge (R/A); user reports (R)
- Calibration withdrawal: Maintenance In-Charge (R); department in-charge (A for not using the item)
- Recall: Maintenance In-Charge (R/A)
- Downtime clock: Maintenance In-Charge (R); Night Duty Officer (A at night for the start time)
- Stop-work: all staff (R); Maintenance In-Charge (A for restart)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored:
- Inventory includes loaners; no device in use off the list.
- PPM job cards for a sample of critical items, dated when due, not bunched.
- Overdue measuring devices withdrawn; laboratory and imaging no-report rules still those programmes.
- Recall file shows inventory search and quarantine.
- Downtime from user report, not engineer arrival.
- Trained-operator list current.

Root-cause analysis is required when: a device in use is not on the inventory; a recall did not reach the serial numbers held; an overdue measuring device is found in service; a critical item's PPM was missed. CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a missed recall."""

TRAINING_ACKNOWLEDGEMENT = f"""Operators and maintainers are trained against this policy at induction, before using a new class, and {D('once a year')} thereafter.

Staff acknowledgement

I have read this Medical and Support-Service Equipment Programme of {HOSPITAL}. I will not use a device that is not on the inventory. I will not use an overdue measuring device. I will not operate a class I am not named for.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/03')}
Issue number: {D('01')}
Version: 2.0 (template test — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}
Number of pages: as printed

Prepared by (designation): {D('Maintenance In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = """- Biomedical Equipment Management and Maintenance Program. National Health Mission — PPM, inventory and criticality framework; not a named-contract mandate and not Clinical Establishments Act or Central Electricity Authority guidance.
- Medical Devices and Diagnostics. Central Drugs Standard Control Organisation.
- Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940 — regulated devices, adverse events and recalls insofar as they apply to devices this hospital uses; this hospital is not a manufacturer.
- Indian Public Health Standards (2022). National Health Mission — planning framework, not a NABH equipment-list mandate.
- NABH Standards for Small Healthcare Organisations, 3rd Edition, Chapter 8, standard FMS.3 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- Internal: equipment plan; inventory; PPM and breakdown plan; calibration; recall file; downtime log; service directory; laboratory, imaging, reprocessing, crash-cart, utilities, facility-safety and gas programmes; incident system."""

DISTRIBUTION = f"""Controlled master: office of the Medical Superintendent, {HOSPITAL}, with a working copy held by the Maintenance In-Charge and the Quality Coordinator.

Issued to: Nursing Superintendent, department in-charges who operate equipment, contracted workshop if maintenance is outsourced.

Available to all staff at the {D('Nursing Station policy folder')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

On revision, every displayed copy is withdrawn the same day. One dated superseded copy is retained by the Quality Coordinator."""

ABBREVIATIONS = """BEMMP — Biomedical Equipment Management and Maintenance Program (National Health Mission)
CDSCO — Central Drugs Standard Control Organisation
PPM — planned preventive maintenance
AERB — Atomic Energy Regulatory Board (imaging quality assurance remains the imaging programme)
CAPA — corrective and preventive action
RCA — root-cause analysis

Night Duty Officer — the senior doctor or senior nurse holding emergency command overnight
Maintenance In-Charge — the person accountable for the equipment programme under this policy (biomedical)"""

STATUTE_CLAUSE = (
    "the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, "
    "insofar as they govern medical devices this hospital uses, including adverse-event "
    "reporting and recalls"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "FMS.3.a",
        "requirement": "The organisation plans for medical and support service equipment in accordance with its services and strategic plan.",
        "steps": "Section 3; 5.1 Plan and inventory",
        "responsible": "Medical Superintendent (accountable); Maintenance In-Charge (plan)",
        "records": [
            "Equipment plan matched to the service directory and strategic plan.",
            "Signed gap or go-ahead before a new service is offered.",
            "Recorded absences for services not offered.",
        ],
    },
    {
        "oe_code": "FMS.3.b",
        "requirement": "Medical equipment and support service equipment are inventoried, and proper logs are maintained as required.",
        "steps": "Section 3; 5.1 Plan and inventory",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Inventory including loaners and outsourced items.",
            "Logs: acceptance, PPM, breakdown, calibration due.",
            "Unique identifier, location, owner and criticality for each item.",
        ],
    },
    {
        "oe_code": "FMS.3.c",
        "requirement": "The documented operational and maintenance (preventive and breakdown) plan for medical and support service equipment is implemented.",
        "steps": "Section 3; 5.2 PPM, breakdown, inspection and calibration",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Written PPM and breakdown plan (criticality, who attends, how a user reports).",
            "Job cards showing last month's PPM and last week's breakdown actually happened.",
            "Cannibalisation and loaner rules as written.",
        ],
    },
    {
        "oe_code": "FMS.3.d",
        "requirement": "Medical and support service equipment are periodically inspected and calibrated for their proper functioning.",
        "steps": "Section 3; 5.2 PPM, breakdown, inspection and calibration",
        "responsible": "Maintenance In-Charge",
        "records": [
            "In-service inspection records.",
            "Calibration certificates against a traceable standard.",
            "Withdrawal-until-passed for overdue measuring devices.",
        ],
    },
    {
        "oe_code": "FMS.3.e",
        "requirement": "Qualified and trained personnel operate and maintain medical and support service equipment.",
        "steps": "Section 3; 5.3 Qualified operators and maintainers",
        "responsible": "Maintenance In-Charge; department in-charges",
        "records": [
            "Trained-operator list by class.",
            "Maintainer list and visiting-technician job cards.",
            "Annual refresher recorded for each named operator.",
        ],
    },
    {
        "oe_code": "FMS.3.f",
        "requirement": "There is monitoring of medical equipment and medical devices related to adverse events, and compliance hazard notices on recalls.",
        "steps": "Section 3; 5.4 Adverse events, recalls and critical downtime",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Device adverse-event records (incident dual-entry if a patient was harmed).",
            "Hazard-notice and recall file: inventory search, quarantine, return or destruction.",
            "Signed compliance that the ward received the quarantine instruction.",
        ],
    },
    {
        "oe_code": "FMS.3.g",
        "requirement": "Downtime for critical equipment breakdown is monitored from reporting to inspection and implementation of corrective actions.",
        "steps": "Section 3; 5.4 Adverse events, recalls and critical downtime",
        "responsible": "Maintenance In-Charge; Night Duty Officer (night start time)",
        "records": [
            "Critical-equipment list.",
            "Downtime logs from user report to inspection and corrective action.",
            "Defined alternative (loaner, diversion or pause) when the item is not restored.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.3 v2 to the FMS.5 v2.2 shape.

Technical substance retained from v1: BEMMP as framework not NHM-contract/CEA/CEA-Act;
MDR 2017 + D&C 1940 in P2 because recalls; CDSCO chapter ref 8; IPHS planning
framework; AAC.4.h/AAC.5.i no-report rules stay those programmes; HIC.6 steriliser
validation vs equipment split; COP.3 crash-cart vs defibrillator file; downtime
from user report; no invented six-month calibration calendar.

Four 5.x subsections, five non-negotiables. Stop-work included. No SQL. Draft.
"""


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
        "definitions": SAFETY_OBJECTIVE,
        "exceptions": NON_NEGOTIABLES,
        "monitoring_audit": MONITORING_AUDIT,
        "training_competency": TRAINING_ACKNOWLEDGEMENT,
        "resources_required": DOCUMENT_CONTROL,
        "template_test": "fms_v2_adoptable_shape",
        "doc_no": "«FMS/POL/03»",
        "subtitle": "Standards for inventory, implemented PPM, recalls and downtime.",
        "footer_label": "Equipment programme",
        "acknowledgement_note": "The Nursing Superintendent holds signed acknowledgements with the induction record. Operators of each class are named on the trained-operator list.",
    }
    md = verify_shape(
        draft,
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    emit_v2(draft, "fms3_v2_draft.json", "FMS.3_v2_preview.md", md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
