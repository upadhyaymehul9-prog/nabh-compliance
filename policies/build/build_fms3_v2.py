# -*- coding: utf-8 -*-
"""FMS.3 v2 — medical and support-service equipment programme.

Shape follows FMS.5 v2.2 (section list and order only). Wording is this
standard's OEs and v1 substance. Does not overwrite fms3_draft.json or
build_fms3.py. No SQL. No Supabase insert.

Disclaimer P2 names the Medical Devices Rules, 2017, read with the Drugs and
Cosmetics Act, 1940 (same statute scoping as v1).
"""
from __future__ import annotations

import sys

from fms_v2_common import (
    BLANK,
    D,
    HOSPITAL,
    emit_v2,
    verify_shape,
)
from policy_build_common import make_disclaimer

STANDARD_CODE = "FMS.3"
CHAPTER = "FMS"
OE_CODES = [
    "FMS.3.a", "FMS.3.b", "FMS.3.c", "FMS.3.d",
    "FMS.3.e", "FMS.3.f", "FMS.3.g",
]
POLICY_TITLE = "Medical and Support-Service Equipment Programme"
VERSION = "2.1"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "First v2 shape pass (withdrawn: fire-cloned wording).",
    },
    {
        "version": "2.1",
        "date": "19-08-2026",
        "description": "Same section skeleton as FMS.5 v2.2; wording rebuilt from FMS.3 OEs and v1. Not an approved master.",
    },
]

PURPOSE = f"""This policy governs how {HOSPITAL} runs its programme for medical and support-service equipment: how equipment is planned against the services actually offered and the strategic plan; how it is inventoried and logged; how the documented operational and maintenance (preventive and breakdown) plan is implemented; how equipment is inspected and calibrated; how only qualified and trained people operate and maintain it; how device-related adverse events, hazard notices and recalls are monitored and complied with; and how downtime for critical-equipment breakdown is timed from the user report to inspection and corrective action.

It is the hospital-wide equipment programme. It is not the laboratory rule that a result is not issued from an overdue calibrator, not imaging quality-assurance and no-report-if-overdue, not steriliser validation as a reprocessing act, not crash-cart contents, and not building-plant utilities.

Editable defaults in this document are marked {D('like this')}. A hospital that adopts the default keeps the wording. A hospital that needs a different owner, interval or arrangement replaces the marked text before issue. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """A machine in use is on the inventory, in date, and operated by someone trained for that class. A sticker is not a maintenance record. Downtime starts when the user reports, not when the engineer arrives."""

SCOPE = f"""This policy applies to medical equipment and support-service equipment of {HOSPITAL}, whether owned, leased, loaned, consigned or outsourced, and to the people who plan, inventory, operate, maintain, inspect, calibrate, recall and record downtime for that equipment.

It covers: planning equipment against the service directory and strategic plan; inventory and logs; implementation of operational and maintenance (preventive and breakdown) plans; periodic inspection and calibration; qualified and trained operators and maintainers; monitoring of device-related adverse events, hazard notices and recalls; and monitoring of critical-equipment downtime from report to inspection and corrective action.

The defined scope of services is the service-directory programme. Equipment is planned against that directory and against strategy and budget approval. A service the directory does not provide is a recorded absence, not a copied intensive-care equipment list.

Laboratory calibration as a condition of issuing a result — no report from an overdue or failed instrument — remains that laboratory programme. This policy owns hospital-wide inventory, preventive maintenance, breakdown logs and the calibration programme as facility work. Two records, two purposes. Imaging calibration and quality-assurance tests, and that an overdue imaging device does not issue a report, remain that imaging programme. This policy owns that the imaging device is on the hospital inventory and has a maintenance and breakdown log.

Cabinet certification as a laboratory-safety condition remains that laboratory programme. Hospital-wide programme logistics sit here.

Steriliser validation, Bowie-Dick, biological indicators and recall of processed items when the sterilisation process fails remain the infection-control sterilisation programme. This policy owns the steriliser as equipment (inventory, preventive maintenance, breakdown). A failed cycle is that sterilisation programme; a failed boiler or door seal is this programme.

Crash-cart contents, seal and checklist as a resuscitation kit remain that resuscitation programme. Those kits are not this inventory counted twice; a defibrillator on the cart is still equipment here.

A diesel generator, UPS as building plant, pumps and potable-water plant are the utilities programme. A ventilator compressor is equipment here.

Condemned equipment is struck off this inventory then disposed of under the unused-material procedure in the facility-safety programme. Grab-rails are infrastructure, not this list.

Medical-gas plant, manifolds and piped installation are the gas programme. A flowmeter or regulator may be equipment here if this hospital inventories it as a device.

Credentialing method, when that human-resources programme is written, holds the credentialing file. This policy requires that the person who pressed the button or opened the cover was qualified and trained for that class.

Implantable-prosthesis procurement remains that medication and implant programme. A loaner drill may sit on this inventory; implant selection stays there.

Equipment downtime rates may be supplied as managerial indicators; the indicator set remains that quality-indicator programme. A device adverse event that harmed a patient is dual-entered in the incident system.

Capital for equipment may be approved with the strategic plan and budget; the programme is here.

Patient-facing expected cost is not this preventive-maintenance file.

NHM Biomedical Equipment Management and Maintenance Program (BEMMP) is the preventive-maintenance and inventory framework. It is not the Clinical Establishments Act and not Central Electricity Authority guidance. It is not a mandate to join a named NHM contract.

CDSCO Medical Devices and Diagnostics, and the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, govern regulated devices, adverse-event reporting and recalls insofar as they apply to devices this hospital uses. They do not make this hospital a manufacturer."""

POLICY_STATEMENT = f"""{HOSPITAL} plans medical and support-service equipment in accordance with its services and strategic plan.

{HOSPITAL} inventories medical and support-service equipment, including loaned, consigned and outsourced items, and maintains logs as required. An item in use that is not on the inventory is a defect.

{HOSPITAL} implements the documented operational and maintenance (preventive and breakdown) plan. A binder of manufacturer PDFs, or a sticker with no job card, is not an implemented plan. NHM BEMMP is the criticality framework, not a named-contract mandate and not the Clinical Establishments Act.

{HOSPITAL} periodically inspects and calibrates medical and support-service equipment. An overdue measuring device is withdrawn until it has passed. Laboratory and imaging no-report rules remain those diagnostic programmes.

{HOSPITAL} requires that qualified and trained personnel operate and maintain medical and support-service equipment. A nurse using an infusion pump they were never shown, or a visiting technician without a job card, is a failure of this policy.

{HOSPITAL} monitors medical-equipment and medical-device adverse events and complies with hazard notices and recalls. A letter in the quality office that never reached the user is not compliance.

{HOSPITAL} monitors downtime for critical-equipment breakdown from the user report to inspection and implementation of corrective actions. The clock does not start when the engineer arrives.

{HOSPITAL} does not treat a calibration sticker without a record, a recall letter that never reached the user, or laboratory or imaging specialty quality-assurance offered as this whole programme, as that duty."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no operational exception and no "until the vendor comes" exception.

1. Using a medical or support-service device that is not on the inventory.
2. Using a device that is overdue for inspection or calibration, that failed its last check, or that is under recall or quarantine.
3. Operating a device the person has not been trained for, or opening a cover the person is not qualified to maintain.
4. Treating a manufacturer PDF binder, a sticker, or annual maintenance bunched the week before an assessment, as implemented preventive maintenance.
5. Counting steriliser process validation (Bowie-Dick, biological indicators, recall of a failed load) as this autoclave's preventive maintenance. Validation of the load remains the infection-control sterilisation programme; a failed boiler or door seal is this programme.
6. Counting laboratory or imaging no-report-from-overdue-calibrator rules as this whole hospital programme. Those rules remain those diagnostic programmes; this programme still withdraws the device.
7. Starting the downtime clock from the engineer's arrival rather than from the user report.
8. Filing a recall against a serial number that is not on the inventory, or leaving a recalled item in the ward because "stores will collect it."
9. Treating BEMMP as the Clinical Establishments Act, as Central Electricity Authority guidance, or as a mandate to join a named NHM contract.
10. Offering a crash-cart checklist as the defibrillator's equipment file.

A person who finds an uninventoried device in use, an overdue calibrator still in service, or a recall that did not reach the ward, reports it the same shift to the {D('Biomedical In-Charge')}."""

PROCEDURE_STEPS = [
f"""5.1 Plan equipment against the services we offer

The services are the service directory. Strategy and budget approval are that management programme. This section is the equipment plan that matches those, including replacement of condemned items, and excluding equipment for a service the directory does not provide.

How the plan is made, who signs that a new service has the equipment it needs before it is offered, and how a gap is recorded, are held by the {D('Biomedical In-Charge')}. BEMMP is a planning and criticality framework, not a named NHM-contract mandate. Indian Public Health Standards 2022 are a planning framework, not a NABH equipment-list mandate.""",

f"""5.2 Inventory equipment and keep the logs

The inventory identifies each item that can harm a patient if it fails or is missing: unique identifier, location, owner department, criticality, and whether it is owned, loaned, consigned or outsourced. Logs are the running record BEMMP-style programmes keep (acceptance, preventive maintenance, breakdown, calibration due).

Laboratory and imaging specialty registers do not replace this hospital-wide inventory. A crash-cart checklist does not replace the defibrillator's equipment file.

What is on the inventory, what a log contains, and how a loaner or outsourced analyser is still listed, are held by the {D('Biomedical In-Charge')}. An item in use that is not on the inventory is a defect.""",

f"""5.3 Run preventive and breakdown maintenance

Planning and listing are 5.1 and 5.2. This section is that preventive and breakdown maintenance actually run.

NHM BEMMP is the Indian public-sector framework for criticality-based intervals, user-level care, and workshop or vendor breakdown. It is not a mandate to outsource to a named NHM agency and not "CEA guidelines." Manufacturer instructions inform the task list; they are not a substitute for a hospital plan that names who does the work and what happens when a critical item is down (5.7).

The documented operational plan (who may operate which class — 5.5), the preventive plan (task, interval by criticality, who attends, what is recorded), the breakdown plan (how a user reports, who attends, cannibalisation rule, loaner rule), and proof of implementation on a sample of critical items, are held by the {D('Biomedical In-Charge')}.

A binder of manufacturer PDFs, a sticker with no job card, or a breakdown register that records "OK" without a fault, time-to-attend or spare, is not an implemented plan. Steriliser process validation remains the infection-control sterilisation programme. Laboratory and imaging no-report rules remain those diagnostic programmes. Generator and UPS plant tests remain the utilities programme.""",

f"""5.4 Inspect and calibrate; withdraw until passed

Inspection is the in-service check that the item is safe to use (housing, leads, alarms, accessories). Calibration is the measurement against a traceable standard for items that measure or deliver a quantity (monitors, defibrillator energy, infusion pumps, operating-table scales, laboratory instruments as inventory items).

Laboratory no-report from an overdue or failed calibrator remains that laboratory programme. Imaging no-report from an overdue quality-assurance device remains that imaging programme. This section is that those due dates live on the hospital programme and that non-laboratory, non-imaging measuring devices are also calibrated.

Which items require calibration versus inspection-only, the interval, the traceable standard or vendor, and the rule that an overdue measuring device is withdrawn until passed, are held by the {D('Biomedical In-Charge')}. BEMMP criticality informs interval; it is not a NABH universal calendar. This policy does not invent a small-hospital-wide six-month calibration mandate.""",

f"""5.5 Qualify the people who operate and who maintain

Operators are the clinical or technical users. Maintainers are biomedical or engineering staff, or the contracted workshop. Credentialing method, when that human-resources programme is written, holds the credentialing file. This section is that the person who pressed the button or opened the cover was qualified and trained for that class.

A visiting technician without a job card, or a nurse using an infusion pump they were never shown, is a failure of this policy.

Which roles may operate which class, which roles may maintain which class, and how training is recorded, are held by the {D('Biomedical In-Charge')} with department heads. After hours, a breakdown is reported to the {D('named person who takes a breakdown call after hours')} — a biomedical or engineering roster, not an emergency-command title imported from the fire programme.""",

f"""5.6 Act on adverse events, hazard notices and recalls

Planned maintenance is 5.3. This section is the after-market safety net.

CDSCO Medical Devices and Diagnostics, and the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, are the Indian regulatory framework for device adverse events and recalls insofar as they apply to devices this hospital uses. This hospital is not a manufacturer.

How a device-related adverse event is captured (dual entry with the incident system when a patient was harmed; with the medication programme when it is also a medication-delivery event), how hazard notices and recalls are received (CDSCO, manufacturer, vendor), how the inventory is searched, how affected items are quarantined and returned or destroyed, and who signs compliance, are held by the {D('Biomedical In-Charge')}.

A letter in the quality office that never reached the user, implant traceability offered as hospital-wide device recall, or a recalled infusion set left in the ward because "stores will collect it," is not compliance. An empty recall log is acceptable only if the inventory search was still run when a notice named a type this hospital holds.""",

f"""5.7 Time critical-equipment downtime from the user report

Critical equipment is the subset of the inventory whose failure stops a defined service (ventilator, anaesthesia workstation, autoclave as equipment, imaging device, clinical analyser, blood-bank refrigerator, and others this hospital names). Named critical list: {BLANK}.

Downtime starts when the user reports and ends when the item is inspected and corrective action has restored it or a defined alternative is in place (loaner, diversion under the admission and referral programmes, recorded service pause). The failure this clock exists to catch is a breakdown register that records the engineer's arrival but not the hours the operating list was stopped.

Which items are critical, how reporting-to-restoration is timed, and how a corrective action is recorded, are held by the {D('Biomedical In-Charge')}. Managerial indicators may use the rate; this policy owns the clock. A diverted service remains the service-directory and referral programmes; this clock still runs.""",
]

STOP_WORK = f"""A person who is about to do any of the following does not proceed:

- use a device that is not on the inventory, is overdue for inspection or calibration, failed its last check, or is under recall or quarantine;
- operate a device they have not been trained for;
- issue a laboratory or imaging report from a device this programme has withdrawn as overdue or failed — those no-report rules remain the diagnostic programmes; this stop is that the device stays out of service;
- return a recalled or quarantined item to a clinical bay.

They take the device out of the bay if they are competent to, label it withdrawn, and tell the {D('Biomedical In-Charge')} the same shift — or, if that person is not on site, the {D('named person who takes a breakdown call after hours')}.

A good-faith refusal to use an overdue or uninventoried device is not a disciplinary matter. The device is not returned to service until the Biomedical In-Charge says it has passed."""

RESPONSIBILITY = f"""These are the jobs this equipment programme needs. In a small hospital the biomedical lead may be the same person as the facilities Maintenance In-Charge; they still keep this inventory as the equipment file, not as a combined generator-and-ventilator log.

Medical Superintendent (head of the institution)
- Accountable that the medical and support-service equipment programme runs as this policy requires.

{D('Biomedical In-Charge')} (named biomedical or engineering lead)
- Holds the equipment plan, inventory, preventive-maintenance and breakdown job cards, inspection and calibration, recall file and downtime log.
- Withdraws an overdue or failed measuring device until it has passed.
- Runs the inventory search when a hazard notice or recall arrives.
- Names the {D('named person who takes a breakdown call after hours')}.

Clinical heads / department in-charges
- Do not operate a device their staff are not trained for.
- Do not issue a laboratory or imaging report from an overdue calibrator (those no-report rules remain those diagnostic programmes).
- Report a breakdown when it happens, not when it is convenient.

Quality Coordinator
- Audits the records in section 8.

Contracted workshop, if maintenance is outsourced
- Works to the job card and the breakdown clock in this policy. Outsourcing agreements remain that management-agreement programme; the technical tests remain here.

All staff who use equipment
- Report an uninventoried device in use, an overdue calibrator still in service, and a recall that did not reach the ward.

A RACI snapshot:

- Equipment plan: Biomedical In-Charge (R); Medical Superintendent (A)
- Inventory and logs: Biomedical In-Charge (R/A)
- Preventive and breakdown maintenance: Biomedical In-Charge (R/A); users report breakdowns (R)
- Inspection and calibration: Biomedical In-Charge (R/A)
- Operator and maintainer training: Biomedical In-Charge (R); department heads (C)
- Adverse events and recalls: Biomedical In-Charge (R/A); incident system (C when a patient was harmed)
- Downtime clock: user who reports (R for start); Biomedical In-Charge (A)
- Audit: Quality Coordinator (R); Medical Superintendent (A)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at the machines and the records, not at a binder.

What is monitored each quarter:

- Inventory includes loaners, consigned and outsourced items; no item in use is missing from the list.
- Preventive maintenance happened rather than a sticker; last month's job cards exist for a sample of critical items.
- Calibration withdrawal is in force; laboratory and imaging no-report rules still sit with those diagnostic programmes.
- Steriliser process validation is not counted as this autoclave's preventive maintenance.
- Recalls reached the user; inventory search was run; quarantined items are not in a clinical bay.
- Downtime is timed from the user report, not from engineer arrival.
- BEMMP is used as a framework, not as a named-contract mandate or as the Clinical Establishments Act.
- Patient-facing billing is left with the expected-cost programme.

Any non-conformity is a finding. The Biomedical In-Charge owns the corrective action. Root-cause analysis is required when: a device in use is not on the inventory; an overdue measuring device was found in service; a recall did not reach the serial numbers this hospital holds; downtime was timed from engineer arrival; or a person operated a device they were not trained for.

Corrective and preventive action is dated, has an owner, and is checked at the next quarterly audit. An open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a missed recall, a critical-equipment failure that stopped a defined service, or a change to the service directory that should have changed the equipment plan."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who operate or maintain a class of medical or support-service equipment are trained against this policy at induction, before first unsupervised use of that class, and {D('once a year')} thereafter. Training covers: reporting a breakdown; not using an uninventoried, overdue, failed or recalled device; the downtime clock starting at the user report; and the split that laboratory and imaging no-report rules and steriliser validation remain those other programmes. Maintainers are named on a trained-maintainer list held by the Biomedical In-Charge.

Staff acknowledgement

I have read this Medical and Support-Service Equipment Programme policy of {HOSPITAL}. I will not use a device that is not on the inventory, is overdue, has failed, or is under recall. I will not operate a class I have not been trained for. I will report a breakdown when it happens.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/03')}
Issue number: {D('01')}
Version: 2.1 (template test — standard-specific wording; not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}
Number of pages: as printed

Prepared by (designation): {D('Biomedical In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Critical-equipment list location: {BLANK}
After-hours breakdown roster: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.3 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- Biomedical Equipment Management and Maintenance Program. National Health Mission — preventive-maintenance, inventory and criticality framework, not a named-contract mandate and not Clinical Establishments Act or Central Electricity Authority guidance.
- Medical Devices and Diagnostics. Central Drugs Standard Control Organisation.
- Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940 — Indian instrument for regulated devices, adverse events and recalls insofar as they apply to devices this hospital uses; this hospital is not a manufacturer.
- Indian Public Health Standards. (2022). National Health Mission — planning framework, not a NABH equipment-list mandate.
- Internal documents of this hospital: equipment plan; inventory; preventive-maintenance and breakdown plan; calibration; recall file; downtime log; service directory; laboratory and imaging no-report rules; steriliser validation programme; crash-cart programme; utilities, unused-material and gas programmes; incident system."""

DISTRIBUTION = f"""Controlled master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('Biomedical In-Charge')} and the Quality Coordinator.

Copies issued to: department heads who operate equipment; contracted workshop if maintenance is outsourced.

The current version is available to all staff at the {D('biomedical / engineering office policy file')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

Superseded versions are withdrawn from all points of use on issue of a revision. One dated copy of each is retained by the Quality Coordinator."""

ABBREVIATIONS = """BEMMP — Biomedical Equipment Management and Maintenance Program (National Health Mission)
CDSCO — Central Drugs Standard Control Organisation
PPM — planned preventive maintenance
AERB — Atomic Energy Regulatory Board (imaging quality-assurance remains the imaging programme)
NHM — National Health Mission
CAPA — corrective and preventive action
RCA — root-cause analysis
UPS — uninterruptible power supply (building plant remains the utilities programme)
AMC — annual maintenance contract"""

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
        "steps": "Section 3; 5.1 Plan equipment against the services we offer",
        "responsible": "Medical Superintendent (accountable); Biomedical In-Charge (plan)",
        "records": [
            "Equipment plan matched to the service directory and the strategic plan.",
            "Recorded absences for unused services.",
            "Sign-off that a new service has the equipment it needs before it is offered.",
        ],
    },
    {
        "oe_code": "FMS.3.b",
        "requirement": "Medical equipment and support service equipment are inventoried, and proper logs are maintained as required.",
        "steps": "Section 3; 5.2 Inventory equipment and keep the logs",
        "responsible": "Biomedical In-Charge",
        "records": [
            "Inventory including owned, loaned, consigned and outsourced items (unique identifier, location, department, criticality).",
            "Logs: acceptance, preventive maintenance, breakdown, calibration due.",
            "Record that crash-cart checklists and laboratory or imaging specialty registers do not replace this inventory.",
        ],
    },
    {
        "oe_code": "FMS.3.c",
        "requirement": "The documented operational and maintenance (preventive and breakdown) plan for medical and support service equipment is implemented.",
        "steps": "Section 3; 5.3 Run preventive and breakdown maintenance",
        "responsible": "Biomedical In-Charge",
        "records": [
            "Written operational and maintenance (preventive and breakdown) plan, with criticality-based tasks and who attends.",
            "Job cards showing last month's preventive maintenance and last week's breakdown actually happened.",
            "User-report method, cannibalisation rule and loaner rule.",
            "Record that BEMMP is used as a framework, not as a named NHM-contract mandate.",
            "Record that steriliser process validation remains the infection-control sterilisation programme.",
        ],
    },
    {
        "oe_code": "FMS.3.d",
        "requirement": "Medical and support service equipment are periodically inspected and calibrated for their proper functioning.",
        "steps": "Section 3; 5.4 Inspect and calibrate; withdraw until passed",
        "responsible": "Biomedical In-Charge; laboratory and imaging no-report rules remain those programmes",
        "records": [
            "Inspection and calibration records.",
            "Withdrawal-until-passed for overdue measuring devices.",
            "Traceable standard or vendor for items that measure or deliver a quantity.",
        ],
    },
    {
        "oe_code": "FMS.3.e",
        "requirement": "Qualified and trained personnel operate and maintain medical and support service equipment.",
        "steps": "Section 3; 5.5 Qualify the people who operate and who maintain",
        "responsible": "Biomedical In-Charge with department heads",
        "records": [
            "Role-to-class training records for operators.",
            "Trained-maintainer list.",
            "After-hours breakdown roster.",
        ],
    },
    {
        "oe_code": "FMS.3.f",
        "requirement": "There is monitoring of medical equipment and medical devices related to adverse events, and compliance hazard notices on recalls.",
        "steps": "Section 3; 5.6 Act on adverse events, hazard notices and recalls",
        "responsible": "Biomedical In-Charge; incident system when a patient was harmed",
        "records": [
            "Device adverse-event records, dual-entered with the incident system when a patient was harmed.",
            "Hazard-notice and recall-compliance files showing inventory search, quarantine and return or destruction.",
            "Record that this hospital is not treated as a manufacturer under the Medical Devices Rules, 2017.",
        ],
    },
    {
        "oe_code": "FMS.3.g",
        "requirement": "Downtime for critical equipment breakdown is monitored from reporting to inspection and implementation of corrective actions.",
        "steps": "Section 3; 5.7 Time critical-equipment downtime from the user report",
        "responsible": "Biomedical In-Charge; user who reports (clock start)",
        "records": [
            "Named critical-equipment list.",
            "Downtime logs timed from user report to inspection and corrective action or defined alternative.",
            "Loaner, diversion or service-pause record where restoration was not same-shift.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.3 v2.1 uses the FMS.5 v2.2 section skeleton.
Wording is this standard's seven OEs and v1 substance. Fire-cloned stop-work,
Night Duty Officer as emergency command, Floor Fire Warden, and "roles are
titles not vacancies" do not appear. Biomedical In-Charge is the lead, with
a note that a small hospital may use the same person as the facilities lead.

Technical substance retained from v1: BEMMP is not CEA or Clinical
Establishments Act; Medical Devices Rules 2017 + Drugs and Cosmetics Act
1940 in P2; laboratory and imaging no-report rules stay those programmes;
steriliser validation stays HIC.6; downtime from user report not engineer
arrival.

Length follows the seven OEs (seven 5.x subsections). Stop-work is the
genuine do-not-proceed acts for uninventoried, overdue, failed, recalled or
unqualified use. Disclaimer P2 MDR 2017 + D&C 1940. No SQL. Status remains
draft.
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
        "subtitle": "Standards for the hospital-wide medical and support-service equipment programme.",
        "footer_label": "Medical and support-service equipment",
        "prepared_by": "«Biomedical In-Charge»",
        "acknowledgement_note": "The Biomedical In-Charge holds signed acknowledgements of operators and maintainers with the induction record. Maintainers are named on the trained-maintainer list.",
        "control_extra_rows": [
            ["Critical-equipment list", "«________»", "After-hours breakdown roster", "«________»"],
        ],
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
