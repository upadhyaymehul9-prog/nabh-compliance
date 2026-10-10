# -*- coding: utf-8 -*-
"""Builds the SHCO SOP + Records for FMS.3 (Medical and Support-Service
Equipment Programme), following the approved FMS.3 master policy
(shco_policy_masters, status='approved') and the structural template in
sop_record_common.py.

FMS.3 OEs: FMS.3.a-g (7 OEs). doc_required per live shco_full_oes, queried
2026-10-10: FMS.3.c and FMS.3.f are true (Tier 1, full treatment). The
rest are Tier 2.

Source for every procedure step, reference and the division-of-
responsibility language: the approved FMS.3 master policy's
procedure_steps / references_text / responsibility columns (read directly
from shco_policy_masters on 2026-10-10). No new citation or number
introduced beyond what FMS.3 already cites: NHM BEMMP, CDSCO Medical
Devices and Diagnostics, Medical Devices Rules 2017 read with Drugs and
Cosmetics Act 1940, IPHS 2022. The master policy explicitly warns against
inventing a "SHCO-wide six-month calibration mandate" -- this SOP does not
introduce one; every interval is «Hospital to define».
"""
from __future__ import annotations

from pathlib import Path

from sop_record_common import ProcedureBlock, RecordSpec, SOPSpec, build_record, build_sop

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "FMS"

FMS3_REFS = [
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management and Safety chapter, standard FMS.3.",
    "Ministry of Health & Family Welfare, Government of India. "
    "[Biomedical Equipment Management and Maintenance "
    "Programme (BMMP)](https://mohfw.gov.in/sites/default/files/BMMP%20Technical%20Manual.pdf). PPM/inventory/criticality framework, not a named-contract "
    "mandate.",
    "Central Drugs Standard Control Organisation. "
    "[Medical Devices and Diagnostics](https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/).",
    "Government of India. (2017). [Medical Devices Rules, 2017]"
    "(https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/m_device/mdr,%202017%20(1).pdf), read with the Drugs "
    "and Cosmetics Act, 1940. Indian regulatory instrument for device adverse events "
    "and recalls insofar as they apply to devices this hospital uses; this hospital "
    "is not a manufacturer.",
    "National Health Mission. (2022). [Indian Public Health Standards]"
    "(https://nhsrcindia.org/sites/default/files/CHC%20IPHS%202022%20Guidelines%20pdf.pdf). Planning "
    "framework, not a NABH equipment-list mandate.",
]

SOP = SOPSpec(
    sop_no="SOP-FMS.3",
    title="Medical and Support-Service Equipment Programme",
    standard_code_range="FMS.3.a-g",
    what_is_this_for=(
        "This SOP tells biomedical, engineering, clinical and quality staff, in one "
        "place, how this hospital plans, inventories, maintains, calibrates, staffs, "
        "monitors for recalls, and tracks downtime of every piece of medical and "
        "support-service equipment it runs. If you operate a device, maintain one, "
        "sign off a PPM job card, or hold the inventory, this SOP is for you."
    ),
    worked_example=(
        "A ward nurse reports an infusion pump alarming erratically at 11pm. This "
        "SOP is what tells them which log to report it in, who attends, whether a "
        "loaner is available while it is down, and that the downtime clock runs from "
        "the report, not from when the engineer happens to arrive."
    ),
    why_nabh_asks=(
        "NABH requires equipment planning matched to services, an inventory with "
        "logs, an implemented maintenance plan (Core, asterisked), periodic "
        "inspection and calibration, qualified operators and maintainers, monitoring "
        "of adverse events and recalls (Achievement, asterisked), and downtime "
        "tracking for critical equipment."
    ),
    purpose=(
        "To define how «Hospital Name» plans, inventories, maintains, calibrates, "
        "staffs, and monitors recalls and downtime for every piece of medical and "
        "support-service equipment it runs, matched to the services in the AAC.1 "
        "directory and the ROM.3.a strategic plan."
    ),
    scope=(
        "Applies to every medical and support-service equipment item at "
        "{{HOSPITAL_NAME}}, owned, loaned, consigned or outsourced. It does not "
        "cover steriliser process validation (HIC.6), laboratory/imaging calibration "
        "no-report rules (AAC.4.h, AAC.5.i), implant traceability (MOM.9), or the "
        "crash-cart checklist (COP.3) -- those remain their own documents and are "
        "only pointed to here where this SOP's steps hand work to them."
    ),
    responsibilities=[
        ("Head of the Institution",
         "Is accountable that the medical and support-service equipment programme "
         "runs as this SOP requires."),
        ("Named Biomedical/Engineering Lead",
         "Holds the inventory, PPM, calibration, recall and downtime records."),
        ("Clinical Heads",
         "Do not let staff operate a device they are not trained for, and do not "
         "issue a laboratory or imaging report from an overdue calibrator (AAC.4.h, "
         "AAC.5.i)."),
        ("Quality/Accreditation Coordinator",
         "Audits a sample of the records this SOP produces, at «Hospital to define» "
         "frequency."),
        ("All Staff",
         "Treat an uninventoried device in use, an overdue calibrator still in "
         "service, or a recall that did not reach the ward, as defects to report."),
    ],
    blocks=[
        ProcedureBlock(
            heading="4.1 Planning equipment against services and the strategic plan (FMS.3.a)",
            why_it_matters=(
                "Equipment bought without reference to the AAC.1 service directory "
                "or the ROM.3.a strategic plan is how a hospital ends up with "
                "devices for services it doesn't run, and no plan for the ones it "
                "does -- this step is the match between the two."
            ),
            steps=[
                "1. The organisation plans for medical and support-service equipment "
                "in accordance with its services (AAC.1) and strategic plan and "
                "budget approval (ROM.3.a), including replacement of condemned items "
                "(FMS.2.f).",
                "2. «Hospital to define how medical and support-service equipment is "
                "planned against the AAC.1 directory and ROM.3.a strategy» -- who "
                "signs that a new service has the equipment it needs before it is "
                "offered, and how a gap is recorded.",
                "3. Equipment for a service the AAC.1 directory does not list is not "
                "planned under this step.",
            ],
            technical_sources=[
                "Ministry of Health & Family Welfare, Government of India. [Biomedical Equipment Management and "
                "Maintenance Programme (BMMP)](https://mohfw.gov.in/sites/default/files/BMMP%20Technical%20Manual.pdf).",
                "National Health Mission. (2022). [Indian Public Health Standards](https://nhsrcindia.org/sites/default/files/CHC%20IPHS%202022%20Guidelines%20pdf.pdf).",
            ],
        ),
        ProcedureBlock(
            heading="4.2 Inventory and logs (FMS.3.b)",
            why_it_matters=(
                "A device in clinical use that is not on the inventory cannot be "
                "maintained, calibrated or recalled against -- this step is what "
                "makes every other step in this SOP possible."
            ),
            steps=[
                "1. Medical equipment and support-service equipment are inventoried, "
                "and proper logs are maintained, identifying each item that can harm "
                "a patient if it fails or is missing: unique identifier, location, "
                "owner department, criticality, and whether it is owned, loaned, "
                "consigned or outsourced.",
                "2. Logs are the running record (acceptance, PPM, breakdown, "
                "calibration due) -- AAC.4/AAC.5 specialty registers do not replace "
                "this hospital-wide inventory, and a crash-cart checklist (COP.3) "
                "does not replace the defibrillator's own equipment file.",
                "3. «Hospital to define what is on the inventory, what a log "
                "contains, and how a loaner or outsourced analyser is still listed» "
                "-- an item in use that is not on the inventory is a defect.",
            ],
        ),
        ProcedureBlock(
            heading="4.3 Operational and maintenance (preventive and breakdown) plan implemented (FMS.3.c, Core, ASTERISKED)",
            why_it_matters=(
                "This is the programme's centre and the chapter's first documented-"
                "evidence anchor -- an assessor asks to see the plan, then to see "
                "that last month's PPM and last week's breakdown actually happened. "
                "A binder of manufacturer PDFs or a sticker with no job card is not "
                "an implemented plan."
            ),
            steps=[
                "1. The documented operational and maintenance (preventive and "
                "breakdown) plan for medical and support-service equipment is "
                "implemented -- not merely written.",
                "2. BEMMP is the Indian public-sector framework for criticality-"
                "based PPM intervals, user-level care, and workshop/vendor "
                "breakdown; it is not a mandate to outsource to a named NHM agency. "
                "Manufacturer instructions inform the task list; they do not "
                "substitute for a hospital plan naming who does the work.",
                "3. «Hospital to define the documented operational and maintenance "
                "(preventive and breakdown) plan and how implementation is "
                "evidenced» -- the operational plan (who may operate which class), "
                "the preventive plan (task, interval by criticality, who attends, "
                "what is recorded), the breakdown plan (how a user reports, who "
                "attends, cannibalisation rule, loaner rule), and proof of "
                "implementation on a sample of critical items.",
                "4. HIC.6 remains steriliser process validation; AAC.4.h and AAC.5.i "
                "remain the no-report-from-overdue-calibrator rules -- this step "
                "does not restate either.",
            ],
            technical_sources=[
                "Ministry of Health & Family Welfare, Government of India. [Biomedical Equipment Management and "
                "Maintenance Programme (BMMP)](https://mohfw.gov.in/sites/default/files/BMMP%20Technical%20Manual.pdf).",
            ],
        ),
        ProcedureBlock(
            heading="4.4 Periodic inspection and calibration (FMS.3.d)",
            why_it_matters=(
                "Inspection confirms a device is safe to use; calibration confirms "
                "it measures correctly against a traceable standard -- confusing the "
                "two means a device can look safe while silently measuring wrong."
            ),
            steps=[
                "1. Inspection is the in-service check that the item is safe to use "
                "(housing, leads, alarms, accessories). Calibration is the "
                "measurement against a traceable standard for items that measure or "
                "deliver a quantity (monitors, defibrillator energy, infusion pumps, "
                "OT table scales, laboratory instruments as inventory items).",
                "2. AAC.4.h still forbids issuing a laboratory result from an "
                "overdue or failed calibrator; AAC.5.i still forbids an imaging "
                "report from an overdue AERB-QA device -- this step is that those "
                "due dates live on the hospital programme, and that non-lab, non-"
                "imaging measuring devices are also calibrated.",
                "3. «Hospital to define which items require calibration versus "
                "inspection-only, the interval, the traceable standard or vendor, "
                "and the rule that an overdue measuring device is withdrawn until "
                "passed» -- BEMMP criticality informs interval; it is not a NABH "
                "universal calendar, and this step does not invent a SHCO-wide six-"
                "month calibration mandate.",
            ],
        ),
        ProcedureBlock(
            heading="4.5 Qualified and trained personnel operate and maintain (FMS.3.e)",
            why_it_matters=(
                "A visiting technician without a job card, or a nurse using an "
                "infusion pump they were never shown, is this step failing -- the "
                "device being present and working is not enough if the person "
                "touching it was never qualified to."
            ),
            steps=[
                "1. Qualified and trained personnel operate and maintain medical and "
                "support-service equipment. Operators are the clinical or technical "
                "users; maintainers are biomedical/engineering or the contracted "
                "workshop.",
                "2. HRM (when drafted) owns the credentialing file; this step is "
                "that the person who pressed the button or opened the cover was "
                "qualified and trained for that class.",
                "3. «Hospital to define which roles may operate which class, which "
                "roles may maintain which class, and how training is recorded».",
            ],
        ),
        ProcedureBlock(
            heading="4.6 Adverse events, hazard notices and recalls (FMS.3.f, Achievement, ASTERISKED)",
            why_it_matters=(
                "This is the chapter's second documented-evidence anchor -- an "
                "assessor asks what was the last device adverse event, the last "
                "manufacturer or CDSCO hazard notice, and what this hospital did "
                "about it. A letter in the quality office that never reached the "
                "user is not monitoring."
            ),
            steps=[
                "1. There is monitoring of medical equipment and medical devices "
                "related to adverse events, and compliance with hazard notices on "
                "recalls -- this is the after-market safety net, distinct from "
                "FMS.3.c's planned maintenance.",
                "2. CDSCO Medical Devices and Diagnostics, and the Medical Devices "
                "Rules 2017 read with the Drugs and Cosmetics Act 1940, are the "
                "Indian regulatory framework for device adverse events and recalls "
                "insofar as they apply to devices this hospital uses -- this "
                "hospital is not a manufacturer.",
                "3. «Hospital to define how a device-related adverse event is "
                "captured (dual entry with PSQ.5 when a patient was harmed; MOM.7 "
                "when it is also a medication-delivery event), how hazard notices "
                "and recalls are received, how the inventory is searched, how "
                "affected items are quarantined and returned or destroyed, and who "
                "signs compliance».",
                "4. A recall filed against a serial number that is not on the "
                "inventory, or a recalled infusion set left in the ward because "
                "\"stores will collect it\", is a failure of this step. An empty "
                "recall log is acceptable only if the inventory search was still "
                "run when a notice named a type this hospital holds.",
            ],
            technical_sources=[
                "Central Drugs Standard Control Organisation. [Medical Devices and "
                "Diagnostics](https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/).",
                "Government of India. (2017). [Medical Devices Rules, 2017](https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/m_device/mdr,%202017%20(1).pdf), read with "
                "the Drugs and Cosmetics Act, 1940.",
            ],
        ),
        ProcedureBlock(
            heading="4.7 Critical-equipment downtime (FMS.3.g)",
            why_it_matters=(
                "A breakdown register that records the engineer's arrival but not "
                "the hours the OT list was stopped is not downtime monitoring -- the "
                "clock that matters is the one that runs from when the user reported "
                "the failure, not from when someone finally showed up."
            ),
            steps=[
                "1. Downtime for critical equipment breakdown is monitored from "
                "reporting to inspection and implementation of corrective actions. "
                "Critical equipment is the subset of the inventory whose failure "
                "stops a defined service (ventilator, anaesthesia workstation, "
                "autoclave as equipment, imaging device, clinical analyser, blood-"
                "bank refrigerator, and others this hospital names).",
                "2. Downtime starts when the user reports and ends when the item is "
                "inspected and corrective action has restored it, or a defined "
                "alternative is in place (loaner, diversion under AAC.2/AAC.7, "
                "recorded service pause).",
                "3. «Hospital to define the critical-equipment list and downtime "
                "monitoring from report to inspection and corrective action». PSQ.2 "
                "may use the downtime rate as an indicator; this document owns the "
                "clock. A diverted service remains AAC.1/AAC.2 -- this clock still "
                "runs while it is diverted.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-7 (see the FMS.3 Records folder).",
    related_documents=[
        "Policy — Medical and Support-Service Equipment Programme (FMS.3)",
        "Hospital's Service Directory (AAC.1)",
        "Hospital's Strategic Plan and Budget Approval (ROM.3.a)",
        "Hospital's Steriliser Process Validation SOP (HIC.6)",
        "Hospital's Laboratory and Imaging Calibration No-Report Rules (AAC.4.h, AAC.5.i)",
        "Hospital's Implant Traceability SOP (MOM.9)",
        "Hospital's Crash-Cart Checklist (COP.3)",
    ],
    verified_sources=FMS3_REFS,
    review_text=(
        "This policy is reviewed at «Hospital to define the review interval for "
        "this policy», and sooner when a recall was missed, or when AAC.4, AAC.5, "
        "AAC.6, HIC.6, FMS.1, FMS.2, FMS.4, COP.3 or MOM.9 that this document hands "
        "work to are revised."
    ),
)


RECORDS = [
    RecordSpec(
        oe_code="FMS.3.a",
        oe_requirement="The organisation plans for medical and support service equipment in accordance with its services and strategic plan.",
        record_title="FMS.3 Record 1 — Equipment-planning-to-service-directory alignment record",
        what_is_this=(
            "A record showing new or replacement equipment was planned against the "
            "AAC.1 service directory and the ROM.3.a strategic plan, not acquired "
            "ad hoc."
        ),
        real_example=(
            "A new day-care service is approved; this record shows the required "
            "equipment was planned and in place before the service was offered to "
            "patients."
        ),
        why_nabh_asks=(
            "NABH requires equipment planning in accordance with services and the "
            "strategic plan -- a Commitment requirement checked against the match "
            "between the two, not a budget line alone."
        ),
        how_to_fill=[
            ("Date", "Date the equipment plan was made or reviewed."),
            ("Service (per AAC.1)", "Named service the equipment supports."),
            ("Equipment Planned", "What equipment was planned, including any FMS.2.f condemned-item replacement."),
            ("Signed Off Before Service Offered? (Y/N)", "Whether equipment was in place before the service went live."),
            ("Gap Recorded (If Any)", "Any gap found and how it was addressed."),
            ("Confirmed By", "Named biomedical/engineering lead."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.3.",
        ],
        column_headers=["Date", "Service (per AAC.1)", "Equipment Planned",
                         "Signed Off Before Service Offered? (Y/N)", "Gap Recorded (If Any)", "Confirmed By"],
        worked_example_row=["05/01/2026", "Day-care procedure unit", "Procedure trolley, pulse oximeter, recovery monitor",
                             "Y", "None", "Biomedical Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.3.b",
        oe_requirement="Medical equipment and support service equipment are inventoried, and proper logs are maintained as required.",
        record_title="FMS.3 Record 2 — Medical and support-service equipment inventory",
        what_is_this=(
            "The hospital-wide inventory of every item that can harm a patient if "
            "it fails or is missing -- unique identifier, location, owner "
            "department, criticality, and ownership status."
        ),
        real_example=(
            "A consigned analyser in the laboratory is listed on the inventory with "
            "its consignment status, even though the hospital does not own it "
            "outright."
        ),
        why_nabh_asks=(
            "NABH requires equipment to be inventoried with proper logs maintained "
            "-- a Commitment requirement checked against whether every in-use item "
            "is actually on the list, owned, loaned or outsourced alike."
        ),
        how_to_fill=[
            ("Unique Identifier", "Asset tag or serial number."),
            ("Item/Description", "What the equipment is."),
            ("Location/Owner Department", "Where it is and which department owns it."),
            ("Criticality", "Hospital-defined criticality rating."),
            ("Ownership Status", "Owned / loaned / consigned / outsourced."),
            ("Confirmed By", "Named biomedical/engineering lead."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.3.",
        ],
        column_headers=["Unique Identifier", "Item/Description", "Location/Owner Department",
                         "Criticality", "Ownership Status", "Confirmed By"],
        worked_example_row=["BME-0231", "Patient monitor", "ICU",
                             "Critical", "Owned", "Biomedical Lead «Name»"],
        extra_blank_rows=11,
    ),
    RecordSpec(
        oe_code="FMS.3.c",
        oe_requirement="The documented operational and maintenance (preventive and breakdown) plan for medical and support service equipment is implemented.",
        record_title="FMS.3 Record 3 — PPM and breakdown job-card log",
        what_is_this=(
            "A log of preventive maintenance (PPM) and breakdown job cards actually "
            "carried out -- not a binder of manufacturer PDFs or a sticker with no "
            "job card. The chapter's first asterisked, documented-evidence record."
        ),
        real_example=(
            "A ventilator's quarterly PPM is carried out on schedule, with the job "
            "card showing the technician, tasks performed and result; a separate "
            "breakdown of the same ventilator two weeks later is logged with fault, "
            "time-to-attend and spare used."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- a Core requirement where the organisation "
            "must show the maintenance plan was actually implemented, not merely "
            "written."
        ),
        how_to_fill=[
            ("Date", "Date of the PPM task or breakdown report."),
            ("Equipment (Unique Identifier)", "Which inventoried item."),
            ("Type", "PPM (preventive) or breakdown."),
            ("Task/Fault", "What was done (PPM) or what failed (breakdown)."),
            ("Time-to-Attend / Spare Used", "For breakdown: how long until attended, and any spare/loaner used."),
            ("Confirmed By", "Named technician or biomedical lead."),
        ],
        verified_sources=[
            "Ministry of Health & Family Welfare, Government of India. [Biomedical Equipment Management and "
            "Maintenance Programme (BMMP)](https://mohfw.gov.in/sites/default/files/BMMP%20Technical%20Manual.pdf).",
        ],
        column_headers=["Date", "Equipment (Unique Identifier)", "Type", "Task/Fault",
                         "Time-to-Attend / Spare Used", "Confirmed By"],
        worked_example_row=["10/03/2026", "BME-0115 (Ventilator)", "PPM",
                             "Quarterly PPM: filter, calibration check, alarm test — pass", "N/A",
                             "Biomedical Technician «Name»"],
        extra_blank_rows=11,
    ),
    RecordSpec(
        oe_code="FMS.3.d",
        oe_requirement="Medical and support service equipment are periodically inspected and calibrated for their proper functioning.",
        record_title="FMS.3 Record 4 — Inspection and calibration certificate log",
        what_is_this=(
            "A log of inspection (safe-to-use checks) and calibration (traceable "
            "measurement accuracy) results, with any overdue measuring device "
            "withdrawn from service until it passes."
        ),
        real_example=(
            "An infusion pump's annual calibration finds it reading 4% high; the "
            "pump is withdrawn from service the same day and only returned after "
            "re-calibration passes."
        ),
        why_nabh_asks=(
            "NABH requires periodic inspection and calibration for proper "
            "functioning -- a Commitment requirement checked against the withdrawal-"
            "until-passed rule for a failed or overdue measuring device."
        ),
        how_to_fill=[
            ("Date", "Date of inspection or calibration."),
            ("Equipment (Unique Identifier)", "Which inventoried item."),
            ("Inspection or Calibration", "Which type was performed."),
            ("Result", "Pass, fail, or reading against traceable standard."),
            ("Withdrawn Until Passed? (Y/N)", "Whether a failed/overdue item was withdrawn from service."),
            ("Confirmed By", "Named biomedical lead or vendor."),
        ],
        verified_sources=[
            "Ministry of Health & Family Welfare, Government of India. [Biomedical Equipment Management and "
            "Maintenance Programme (BMMP)](https://mohfw.gov.in/sites/default/files/BMMP%20Technical%20Manual.pdf).",
        ],
        column_headers=["Date", "Equipment (Unique Identifier)", "Inspection or Calibration",
                         "Result", "Withdrawn Until Passed? (Y/N)", "Confirmed By"],
        worked_example_row=["18/03/2026", "BME-0098 (Infusion pump)", "Calibration",
                             "Reading 4% high against traceable standard — fail", "Y, withdrawn same day",
                             "Biomedical Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.3.e",
        oe_requirement="Qualified and trained personnel operate and maintain medical and support service equipment.",
        record_title="FMS.3 Record 5 — Operator and maintainer training record",
        what_is_this=(
            "A record of which staff are qualified and trained to operate or "
            "maintain each class of equipment, so a device is never handled by "
            "someone who was never shown how."
        ),
        real_example=(
            "A ward nurse is trained on the new infusion-pump model before it "
            "replaces the old one on her ward, with the training dated and signed "
            "off."
        ),
        why_nabh_asks=(
            "NABH requires qualified and trained personnel to operate and maintain "
            "equipment -- a Commitment requirement checked against an actual "
            "training record, not an assumption of competence."
        ),
        how_to_fill=[
            ("Staff Name/Role", "Who was trained."),
            ("Equipment Class", "Which class of equipment they are trained on."),
            ("Operate or Maintain", "Whether this is operator or maintainer training."),
            ("Date Trained", "Date training was completed."),
            ("Trainer", "Who provided the training."),
            ("Confirmed By", "Named biomedical lead or department head."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.3.",
        ],
        column_headers=["Staff Name/Role", "Equipment Class", "Operate or Maintain",
                         "Date Trained", "Trainer", "Confirmed By"],
        worked_example_row=["Staff Nurse «Name», ICU", "Infusion pump (new model)", "Operate",
                             "22/03/2026", "Biomedical Technician «Name»", "ICU In-Charge «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.3.f",
        oe_requirement="There is monitoring of medical equipment and medical devices related to adverse events, and compliance hazard notices on recalls.",
        record_title="FMS.3 Record 6 — Adverse event and recall-compliance log",
        what_is_this=(
            "A log of device-related adverse events, manufacturer/CDSCO hazard "
            "notices and recalls, with the inventory search, quarantine and "
            "compliance sign-off for each. The chapter's second asterisked, "
            "documented-evidence record."
        ),
        real_example=(
            "A manufacturer recall notice for a specific infusion-set batch is "
            "received; the inventory is searched, two affected sets are found in "
            "stores, quarantined the same day, and returned to the vendor."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- an Achievement requirement where the "
            "organisation must show hazard notices and recalls actually reached "
            "the user and were acted on, not filed in the quality office."
        ),
        how_to_fill=[
            ("Date", "Date the adverse event or hazard notice/recall was received."),
            ("Source", "CDSCO, manufacturer, vendor, or internal report."),
            ("Device/Batch Affected", "What the notice concerns."),
            ("Inventory Searched? (Y/N)", "Whether the inventory was checked for affected items."),
            ("Quarantined/Returned/Destroyed", "Action taken on any affected items found."),
            ("Compliance Signed By", "Named person who signed compliance."),
        ],
        verified_sources=[
            "Central Drugs Standard Control Organisation. [Medical Devices and "
            "Diagnostics](https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/).",
            "Government of India. (2017). [Medical Devices Rules, 2017](https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2022/m_device/mdr,%202017%20(1).pdf), read with "
            "the Drugs and Cosmetics Act, 1940.",
        ],
        column_headers=["Date", "Source", "Device/Batch Affected", "Inventory Searched? (Y/N)",
                         "Quarantined/Returned/Destroyed", "Compliance Signed By"],
        worked_example_row=["02/04/2026", "Manufacturer recall notice", "Infusion-set batch #IS-2291", "Y",
                             "2 units found in stores, quarantined and returned to vendor",
                             "Biomedical Lead «Name»"],
        extra_blank_rows=9,
    ),
    RecordSpec(
        oe_code="FMS.3.g",
        oe_requirement="Downtime for critical equipment breakdown is monitored from reporting to inspection and implementation of corrective actions.",
        record_title="FMS.3 Record 7 — Critical-equipment downtime log",
        what_is_this=(
            "A log timing critical-equipment breakdown from the moment a user "
            "reports it to inspection and corrective action, including any loaner "
            "or service diversion used in the meantime."
        ),
        real_example=(
            "An anaesthesia workstation fails at 9am; the downtime clock starts "
            "then, a loaner unit is in place by 11am, and the fault is corrected "
            "and the original unit restored by 3pm the next day."
        ),
        why_nabh_asks=(
            "NABH requires critical-equipment downtime to be monitored from "
            "reporting to corrective action -- a Commitment requirement checked "
            "against the clock starting at the report, not at the engineer's "
            "arrival."
        ),
        how_to_fill=[
            ("Equipment (Unique Identifier)", "Which critical item broke down."),
            ("Date/Time Reported", "When the user reported the failure."),
            ("Alternative in Place (If Any)", "Loaner, diversion under AAC.2/AAC.7, or recorded service pause."),
            ("Date/Time Restored", "When corrective action restored the item or service."),
            ("Corrective Action", "What was done to fix the fault."),
            ("Confirmed By", "Named biomedical lead."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.3.",
        ],
        column_headers=["Equipment (Unique Identifier)", "Date/Time Reported",
                         "Alternative in Place (If Any)", "Date/Time Restored",
                         "Corrective Action", "Confirmed By"],
        worked_example_row=["BME-0077 (Anaesthesia workstation)", "15/04/2026 09:00",
                             "Loaner unit from 11:00", "16/04/2026 15:00",
                             "Faulty flow sensor replaced", "Biomedical Lead «Name»"],
    ),
]


def main() -> None:
    sop_path = OUT_ROOT / "SOP_FMS.3.a_to_g_medical_support_equipment_programme.docx"
    build_sop(SOP, sop_path)
    print(f"built {sop_path}")

    manifest_entries = [{
        "file": sop_path.name,
        "document_type": "sop",
        "standard_code": "FMS.3",
        "title": "Medical and Support-Service Equipment Programme",
    }]

    for idx, rec in enumerate(RECORDS, start=1):
        fname = f"FMS.3_Record_{idx:02d}_{rec.record_title.split('—')[-1].strip().lower().replace(' ', '_').replace(',', '')[:60]}.docx"
        rec_path = OUT_ROOT / "Records" / fname
        build_record(rec, rec_path)
        print(f"built {rec_path}")
        manifest_entries.append({
            "file": f"Records/{fname}",
            "document_type": "record",
            "standard_code": "FMS.3",
            "record_index": idx,
            "title": rec.record_title.split("—")[-1].strip(),
        })

    import json
    manifest_path = OUT_ROOT / "manifest.json"
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing = [e for e in existing if e["standard_code"] != "FMS.3"]
    else:
        existing = []
    existing.extend(manifest_entries)
    manifest_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"updated {manifest_path} ({len(manifest_entries)} FMS.3 entries)")


if __name__ == "__main__":
    main()
