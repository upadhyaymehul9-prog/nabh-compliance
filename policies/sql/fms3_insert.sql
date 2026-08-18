-- FMS.3 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 8 FMS, printed page 117
-- (PDF page index 123). TWO OEs CARRY THE ASTERISK -- FMS.3.c, f.
-- UNAPPROVED DRAFT. Do not run this insert until the owner confirms the write.


insert into public.shco_policy_masters (
  standard_code,
  chapter,
  oe_codes,
  policy_title,
  purpose,
  scope,
  policy_statement,
  procedure_steps,
  responsibility,
  references_text,
  distribution,
  abbreviations,
  disclaimer,
  oe_mapping,
  universal_facts_checklist,
  version,
  revision_history,
  status
) values (
  'FMS.3',
  'FMS',
  array['FMS.3.a', 'FMS.3.b', 'FMS.3.c', 'FMS.3.d', 'FMS.3.e', 'FMS.3.f', 'FMS.3.g'],
  $q$Medical and Support-Service Equipment Programme$q$,
  $q$This document sets out the programme of {{HOSPITAL_NAME}} for medical and support-service equipment management: how the organisation plans equipment in accordance with its services and strategic plan; how medical and support-service equipment are inventoried and logs maintained; how the documented operational and maintenance (preventive and breakdown) plan is implemented; how equipment is periodically inspected and calibrated; how qualified and trained personnel operate and maintain it; how medical-equipment and medical-device adverse events, hazard notices and recalls are monitored and complied with; and how downtime for critical equipment breakdown is monitored from reporting to inspection and corrective action.

The chapter intent is a programme for medical and utility equipment management. A sticker on a machine with no PPM record, a recall letter in quality that never reached the ward, or AAC.4.h laboratory calibration offered as the whole hospital programme, is not that intent.

This document is the hospital-wide equipment programme. It is not AAC.4.h's rule that a laboratory result is not issued from an overdue calibrator. It is not AAC.5.i's imaging AERB QA and no-report-if-overdue. It is not HIC.6 steriliser validation as a reprocessing act. It is not COP.3 crash-cart contents. It is not FMS.1 plant utilities (DG, pumps as building plant). It is not the billing ledger.$q$,
  $q$This policy applies to medical equipment and support-service equipment of {{HOSPITAL_NAME}}, whether owned, leased, loaned, consigned or outsourced, and to the people who plan, inventory, operate, maintain, inspect, calibrate, recall and record downtime for that equipment.

It covers: planning equipment against the service directory and strategic plan; inventory and logs; implementation of operational and maintenance (preventive and breakdown) plans; periodic inspection and calibration; qualified and trained operators and maintainers; monitoring of device-related adverse events, hazard notices and recalls; and monitoring of critical-equipment downtime from report to inspection and corrective action.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- AAC.1 owns the defined scope of services. Equipment is planned against that directory (and ROM.3.a strategy/budget). A service the directory does not provide is a recorded absence, not a copied ICU equipment list. HANDOFF ACCEPTED.
- AAC.4.h owns laboratory calibration/QA as a condition of issuing a result: no report from an overdue or failed instrument. THIS document owns hospital-wide inventory, PPM, breakdown logs and the calibration programme as facility work. The laboratory still does not issue a result from an overdue calibrator. Two records, two purposes. HANDOFF ACCEPTED from the AAC.4 FMS forward-ref.
- AAC.5.i owns imaging calibration and AERB quality-assurance tests, and that an overdue imaging device does not issue a report. THIS document owns that the imaging device is on the hospital inventory and has a PPM/breakdown log. AERB tests stay AAC.5. HANDOFF ACCEPTED from AAC.5.
- AAC.6 names cabinet certification as a lab-safety condition. Cabinet PPM/certification logistics sit with whoever maintains the cabinet; the safety condition remains AAC.6. Hospital-wide programme is here.
- HIC.6 owns steriliser validation, Bowie-Dick, biological indicators and recall of processed items when the sterilisation process fails. THIS document owns the steriliser as equipment (inventory, PPM, breakdown). Validation of the load remains HIC.6. Two failure modes: a failed cycle is HIC.6; a failed boiler or door seal is this programme.
- COP.3 owns crash-cart contents, seal and checklist as a resuscitation kit. Those kits are not this inventory counted twice; a defibrillator on the cart is still equipment here.
- FMS.1 owns DG, UPS as building plant, pumps and potable-water plant. A ventilator compressor is equipment here; the incoming electrical backup is FMS.1.e.
- FMS.2.f unused-material disposal strikes condemned equipment off this inventory then disposes of the carcass. FMS.2.a grab-rails are infrastructure, not this list.
- FMS.4 owns medical-gas plant, manifolds and piped installation. A flowmeter or regulator on a cylinder may be equipment here if this hospital inventories it as a device; the gas programme is FMS.4.
- HRM (undrafted) owns credentialing method. THIS document's FMS.3.e requires qualified and trained operators and maintainers; it does not write the credentialing file.
- MOM.9 owns implantable-prosthesis procurement as a medication/device-implant duty. A loaner drill may sit on this inventory; implant selection stays MOM.9.
- PSQ.2 owns managerial indicators. Equipment downtime rates may be supplied from FMS.3.g; PSQ.2 owns the indicator set. PSQ.5 owns incidents; a device adverse event that harmed a patient is dual-entered.
- ROM.3.a owns budget approval. Capital for equipment may be approved there; the programme is here. ROM.4.a may use equipment risk as an input; the PPM method is here.
- PRE.5 billing is not this document. Equipment charges on a bill stay PRE.5 patient-facing cost / accounts, not this PPM file.
- NHM Biomedical Equipment Management and Maintenance Program (BEMMP) (chapter reference 10) is the PPM/inventory framework. It is not the Clinical Establishments Act and not Central Electricity Authority guidance. It is not a mandate to join a named NHM contract.
- CDSCO Medical Devices and Diagnostics (chapter reference 8) and the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, govern regulated devices, adverse-event reporting and recalls insofar as they apply to devices this hospital uses. They do not make this hospital a manufacturer.$q$,
  $q${{HOSPITAL_NAME}} plans medical and support-service equipment in accordance with its services and strategic plan.

{{HOSPITAL_NAME}} inventories medical and support-service equipment and maintains logs as required.

{{HOSPITAL_NAME}} implements the documented operational and maintenance (preventive and breakdown) plan for medical and support-service equipment.

{{HOSPITAL_NAME}} periodically inspects and calibrates medical and support-service equipment for proper functioning.

{{HOSPITAL_NAME}} requires that qualified and trained personnel operate and maintain medical and support-service equipment.

{{HOSPITAL_NAME}} monitors medical-equipment and medical-device adverse events and complies with hazard notices and recalls.

{{HOSPITAL_NAME}} monitors downtime for critical-equipment breakdown from reporting to inspection and implementation of corrective actions.

{{HOSPITAL_NAME}} does not treat a calibration sticker without a record, a recall letter that never reached the user, or AAC.4.h/AAC.5.i specialty QA offered as this whole programme, as that duty.$q$,
  array[
    $s$1. Planning equipment against services and the strategic plan

The organisation plans for medical and support service equipment in accordance with its services and strategic plan.

The services are AAC.1. The strategic plan and budget approval are ROM.3.a. This step is the equipment plan that matches those, including replacement of condemned items (FMS.2.f) and excluding equipment for a service the directory does not provide.

How the plan is made, who signs that a new service has the equipment it needs before it is offered, and how a gap is recorded, are [Hospital to define — how medical and support-service equipment is planned against the AAC.1 directory and ROM.3.a strategy]. BEMMP (chapter reference 10) is a planning/criticality framework, not a named NHM-contract mandate. IPHS 2022 (chapter reference 18) is a planning framework, not a NABH equipment-list mandate.$s$,
    $s$2. Inventory and logs

Medical equipment and support service equipment are inventoried, and proper logs are maintained as required.

The inventory identifies each item that can harm a patient if it fails or is missing: unique identifier, location, owner department, criticality, and whether it is owned, loaned, consigned or outsourced. Logs are the running record BEMMP-style programmes keep (acceptance, PPM, breakdown, calibration due). AAC.4/AAC.5 specialty registers do not replace this hospital-wide inventory. A crash-cart checklist (COP.3) does not replace the defibrillator's equipment file.

What is on the inventory, what a log contains, and how a loaner or outsourced analyser is still listed, are [Hospital to define — the medical and support-service equipment inventory and the logs maintained]. An item in use that is not on the inventory is a defect.$s$,
    $s$3. Operational and maintenance (preventive and breakdown) plan implemented

The documented operational and maintenance (preventive and breakdown) plan for medical and support service equipment is implemented. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask to see the plan and then to see that last month's PPM and last week's breakdown actually happened. The answer must be an implemented plan, not a binder of manufacturer PDFs, not a sticker with no job card, and not HIC.6's steriliser validation offered as PPM of the autoclave.

The reason this is the programme's centre is that FMS.3.a/b are plan and list; this OE is that preventive and breakdown maintenance run. NHM BEMMP (chapter reference 10) is the Indian public-sector framework for criticality-based PPM intervals, user-level care, and workshop/vendor breakdown. It is not a mandate to outsource to a named NHM agency and not "CEA guidelines." Manufacturer instructions inform the task list; they are not a substitute for a hospital plan that names who does the work and what happens when a critical item is down (step 7). The common error is annual PPM bunched the week before assessment, or a breakdown register that records "OK" without a fault, time-to-attend or spare.

The documented operational plan (who may operate which class — step 5), the preventive plan (task, interval by criticality, who attends, what is recorded), the breakdown plan (how a user reports, who attends, cannibalisation rule, loaner rule), and proof of implementation on a sample of critical items, are [Hospital to define — the documented operational and maintenance (preventive and breakdown) plan and how implementation is evidenced]. HIC.6 remains steriliser process validation. AAC.4.h / AAC.5.i remain no-report-from-overdue-calibrator.$s$,
    $s$4. Periodic inspection and calibration

Medical and support service equipment are periodically inspected and calibrated for their proper functioning.

Inspection here is the in-service check that the item is safe to use (housing, leads, alarms, accessories). Calibration is the measurement against a traceable standard for items that measure or deliver a quantity (monitors, defibrillator energy, infusion pumps, OT table scales, laboratory instruments as inventory items). AAC.4.h still forbids issuing a laboratory result from an overdue or failed calibrator. AAC.5.i still forbids an imaging report from an overdue AERB-QA device. This step is that those due dates live on the hospital programme and that non-lab, non-imaging measuring devices are also calibrated.

Which items require calibration versus inspection-only, the interval, the traceable standard or vendor, and the rule that an overdue measuring device is withdrawn until passed, are [Hospital to define — periodic inspection and calibration: which items, interval, traceable method, and withdrawal-until-passed]. BEMMP criticality informs interval; it is not a NABH universal calendar. This step does not invent a SHCO-wide six-month calibration mandate.$s$,
    $s$5. Qualified and trained personnel operate and maintain

Qualified and trained personnel operate and maintain medical and support service equipment.

Operators are the clinical or technical users. Maintainers are biomedical/engineering or the contracted workshop. HRM (when drafted) owns the credentialing file; this OE is that the person who pressed the button or opened the cover was qualified and trained for that class. A visiting technician without a job card, or a nurse using an infusion pump they were never shown, is a failure of this OE.

Which roles may operate which class, which roles may maintain which class, and how training is recorded, are [Hospital to define — who is qualified and trained to operate and to maintain each class of medical and support-service equipment].$s$,
    $s$6. Adverse events, hazard notices and recalls

There is monitoring of medical equipment and medical devices related to adverse events, and compliance hazard notices on recalls. This step is the documented-evidence anchor of an Achievement requirement the standard asterisks. An assessor will ask what was the last device adverse event, the last manufacturer or CDSCO hazard notice, and what this hospital did. The answer must be monitoring and compliance, not a letter in the quality office that never reached the user, not PSQ.5's incident SOP offered as the whole OE, and not MOM.9's implant traceability offered as hospital-wide device recall.

The reason this is distinct is that FMS.3.c is planned maintenance; this OE is the after-market safety net. CDSCO Medical Devices and Diagnostics (chapter reference 8) and the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, are the Indian regulatory framework for device adverse events and recalls insofar as they apply to devices this hospital uses. This hospital is not a manufacturer. The common error is to file a recall against a serial number that is not on the inventory (step 2), or to leave a recalled infusion set in the ward because "stores will collect it."

How a device-related adverse event is captured (dual entry with PSQ.5 when a patient was harmed; MOM.7 when it is also a medication-delivery event), how hazard notices and recalls are received (CDSCO, manufacturer, vendor), how the inventory is searched, how affected items are quarantined and returned or destroyed, and who signs compliance, are [Hospital to define — monitoring of medical-equipment and medical-device adverse events, and compliance with hazard notices and recalls]. An empty recall log is acceptable only if the inventory search was still run when a notice named a type this hospital holds.$s$,
    $s$7. Critical-equipment downtime

Downtime for critical equipment breakdown is monitored from reporting to inspection and implementation of corrective actions.

Critical equipment is the subset of the inventory whose failure stops a defined service (ventilator, anaesthesia workstation, autoclave as equipment, imaging device, clinical analyser, blood-bank refrigerator, and others this hospital names). Downtime starts when the user reports and ends when the item is inspected and corrective action has restored it or a defined alternative is in place (loaner, diversion under AAC.2/AAC.7, recorded service pause). The failure mode is a breakdown register that records the engineer's arrival but not the hours the OT list was stopped.

Which items are critical, how reporting-to-restoration is timed, and how a corrective action is recorded, are [Hospital to define — critical-equipment list and downtime monitoring from report to inspection and corrective action]. PSQ.2 may use the rate; this document owns the clock. A diverted service remains AAC.1/AAC.2; this clock still runs.$s$,
    $s$8. Records, review and the order of operations

The equipment plan against AAC.1/ROM.3.a, the inventory and logs, implemented PPM and breakdown job cards, inspection and calibration certificates with withdrawal-until-passed, operator/maintainer training records, adverse-event and recall-compliance files, and critical-equipment downtime logs, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for the equipment-programme records] for: an inventory that includes loaners; PPM that happened rather than a sticker; calibration withdrawal that AAC.4.h/AAC.5.i still own as no-report rules; HIC.6 steriliser validation not counted as this PPM; recalls that reached the user; downtime from report not from engineer arrival; BEMMP used as framework not a named-contract mandate; and PRE.5 billing left with PRE.5.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a recall was missed, or when AAC.4, AAC.5, AAC.6, HIC.6, FMS.1, FMS.2, FMS.4, COP.3 or MOM.9 that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable that the medical and support-service equipment programme runs as this document requires.

A named biomedical or engineering lead holds the inventory, PPM, calibration, recall and downtime records as this hospital has defined those roles.

Clinical heads do not operate a device their staff are not trained for, and they do not issue a laboratory or imaging report from an overdue calibrator (AAC.4.h / AAC.5.i).

AAC.1, AAC.4, AAC.5, AAC.6, HIC.6, COP.3, FMS.1, FMS.2, FMS.4, MOM.9, ROM.3, PSQ.2, PSQ.5 and HRM (when drafted) remain the owning methods named in Scope.

The quality or accreditation coordinator audits the records at step 8.

All staff are expected to treat an uninventoried device in use, an overdue calibrator still in service, and a recall that did not reach the ward, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.3.
- Biomedical Equipment Management and Maintenance Program. National Health Mission — chapter reference 10; PPM/inventory/criticality framework, not a named-contract mandate and not Clinical Establishments Act or Central Electricity Authority guidance.
- Medical Devices and Diagnostics. Central Drugs Standard Control Organisation — chapter reference 8.
- Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940 — Indian instrument for regulated devices, adverse events and recalls insofar as they apply to devices this hospital uses; this hospital is not a manufacturer.
- Indian Public Health Standards. (2022). National Health Mission — chapter reference 18; planning framework, not a NABH equipment-list mandate.
- Internal documents of {{HOSPITAL_NAME}}: equipment plan; inventory; PPM and breakdown plan; calibration; recall file; downtime log; AAC.1, AAC.4, AAC.5; HIC.6; COP.3; FMS.1, FMS.2, FMS.4; MOM.9; ROM.3; PSQ.5.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the named biomedical or engineering lead and the quality or accreditation coordinator.

Copies issued to: department heads who operate equipment; contracted workshop if maintenance is outsourced (ROM.4.d/e remain the agreement).

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder].

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

FMS — Facility Management and Safety (SHCO 3rd Edition Chapter 8)
BEMMP — Biomedical Equipment Management and Maintenance Program (NHM)
CDSCO — Central Drugs Standard Control Organisation
PPM — planned preventive maintenance
AERB — Atomic Energy Regulatory Board (imaging QA remains AAC.5)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, insofar as they govern medical devices this hospital uses, including adverse-event reporting and recalls. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "FMS.3.a", "requirement": "The organisation plans for medical and support service equipment in accordance with its services and strategic plan.", "steps": "Steps 1, 8", "evidence": "The equipment plan matched to AAC.1 and ROM.3.a; recorded absences for unused services; BEMMP/IPHS as frameworks not mandates; the audit sample at step 8", "responsible": "Named biomedical lead holds the plan; AAC.1 and ROM.3.a remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "FMS.3.b", "requirement": "Medical equipment and support service equipment are inventoried, and proper logs are maintained as required.", "steps": "Steps 2, 8", "evidence": "The inventory including loaners/outsourced items and the logs (acceptance, PPM, breakdown, calibration due); split from COP.3 crash-cart checklists and AAC.4/AAC.5 specialty registers; the audit sample at step 8", "responsible": "Named biomedical lead holds the inventory; quality or accreditation coordinator audits"}, {"oe_code": "FMS.3.c", "requirement": "The documented operational and maintenance (preventive and breakdown) plan for medical and support service equipment is implemented.", "steps": "Steps 3, 8", "evidence": "The written operational and maintenance (preventive and breakdown) plan showing criticality-based PPM tasks, who attends, how a user reports a breakdown, and sample job cards that show last month's PPM and last week's breakdown actually happened rather than a binder of manufacturer PDFs or a sticker with no job card; the recorded use of NHM BEMMP (chapter reference 10) as a criticality/PPM framework not a named NHM-contract mandate and not Clinical Establishments Act or Central Electricity Authority guidance; the recorded splits that HIC.6 remains steriliser process validation, AAC.4.h/AAC.5.i remain no-report-from-overdue-calibrator, and FMS.1.e remains DG/UPS plant tests; induction of users who report breakdowns; the location of the plan; the audit sample at step 8 of a critical item whose PPM was done when due", "responsible": "Named biomedical lead implements PPM and breakdown; HIC.6/AAC.4/AAC.5/FMS.1 remain those methods; quality or accreditation coordinator audits"}, {"oe_code": "FMS.3.d", "requirement": "Medical and support service equipment are periodically inspected and calibrated for their proper functioning.", "steps": "Steps 4, 8", "evidence": "Inspection and calibration records with withdrawal-until-passed for overdue measuring devices; AAC.4.h/AAC.5.i still owning no-report rules; BEMMP informing interval not a NABH universal calendar; the audit sample at step 8", "responsible": "Named biomedical lead; laboratory/imaging no-report rules remain AAC.4/AAC.5; quality or accreditation coordinator audits"}, {"oe_code": "FMS.3.e", "requirement": "Qualified and trained personnel operate and maintain medical and support service equipment.", "steps": "Steps 5, 8", "evidence": "Role-to-class training records for operators and maintainers; HRM flagged as future credentialing file; the audit sample at step 8", "responsible": "Named biomedical lead with department heads; HRM when drafted holds credentialing method; quality or accreditation coordinator audits"}, {"oe_code": "FMS.3.f", "requirement": "There is monitoring of medical equipment and medical devices related to adverse events, and compliance hazard notices on recalls.", "steps": "Steps 6, 2, 8", "evidence": "Device adverse-event records dual-entered with PSQ.5 when a patient was harmed; hazard-notice and recall-compliance files showing inventory search, quarantine and return or destruction rather than a letter that never left quality; the recorded use of CDSCO (chapter reference 8) and the Medical Devices Rules, 2017 read with the Drugs and Cosmetics Act, 1940 as the regulatory framework insofar as they apply, and that this hospital is not a manufacturer; the recorded split that MOM.9 remains implant traceability and PSQ.5 remains the incident SOP; induction of users who receive a quarantine instruction; the location of the recall file; the audit sample at step 8 of a notice that reached the serial numbers on the inventory", "responsible": "Named biomedical lead runs recall search and quarantine; PSQ.5/MOM.9 remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "FMS.3.g", "requirement": "Downtime for critical equipment breakdown is monitored from reporting to inspection and implementation of corrective actions.", "steps": "Steps 7, 3, 8", "evidence": "Critical-equipment list and downtime logs from user report to inspection and corrective action rather than from engineer arrival; PSQ.2 may use the rate; the audit sample at step 8", "responsible": "Named biomedical lead times downtime; PSQ.2 remains the indicator set; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. FMS.3 standard text and all seven OEs were read from the official SHCO 3rd Edition PDF, Chapter 8, printed page 117 (PDF page index 123). OE-page header: "The organisation has a programme for medical and support service equipment management." Summary on printed page 115: "medical equipment and support services management." PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Commitment, b Commitment, c Core, d Commitment, e Commitment, f Achievement, g Achievement.
   TWO OEs CARRY THE ASTERISK -- FMS.3.c and FMS.3.f. a, b, d, e, g are unasterisked (Tier 2). FMS.3.c is Core and Tier 1 because it is asterisked. d is technical T2 (calibration).
   Asterisks verified 2026-08-18 against the page and scripts/shco_oe_asterisks.json.

TIERING UNDER THE STANDING RULE
1. TWO OF SEVEN OEs ARE TIER 1. Tier 1: c, f -- steps 3 and 6 carry the reasoning. Tier 2: a, b, d, e, g, with d/g given named failure modes and BEMMP/CDSCO frameworks. Shallower T1-style reasoning on those five is a DECISION UNDER THE STANDING RULE.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-18) of FMS.3.c/f against AAC.4.h, AAC.5.i, HIC.6, PSQ.5, MOM.9.
   Hospital-wide PPM vs lab/imaging no-report-if-overdue -- HANDOFF ACCEPTED. Stated in Scope and steps 3-4.
   Steriliser as equipment vs HIC.6 process validation -- HANDOFF ACCEPTED.
   Device adverse events vs PSQ.5 incidents vs MOM.9 implants -- dual entry; methods stay there.
3. FORWARD REFERENCES LANDED: AAC hospital-wide equipment programme vs lab/imaging calibration -- this document is that programme; AAC.4.h/AAC.5.i keep no-report rules. ROM.4 facility equipment risk -- method here. PRE.5 billing -- not absorbed. HRM credentialing -- flagged.
4. T2 QUICK CHECK: FMS.3.a vs AAC.1/ROM.3.a -- flagged. FMS.3.b vs COP.3 crash-cart -- flagged. FMS.3.e vs HRM -- flagged. FMS.3.g vs PSQ.2 -- flagged. FMS.1 plant vs this equipment -- flagged. FMS.2.f condemnation -- flagged.

STATUTORY AND EXTERNAL FACTS
5. P2 names Medical Devices Rules, 2017 read with Drugs and Cosmetics Act 1940 because FMS.3.f engages CDSCO chapter reference 8. BMW/FSS/CPA/CEA 2010/MHCA are not in P2. BEMMP is not an Act and is not mislabelled CEA or Clinical Establishments Act.
6. No invented NABH calibration calendar. Intervals are hospital-defined using BEMMP criticality as framework.

EDITORIAL POSITIONS TAKEN
7. Owner's "CEA guidelines for biomedical equipment" mapped to NHM BEMMP (chapter reference 10), not Central Electricity Authority and not Clinical Establishments Act.
8. AAC.4.h / AAC.5.i remain the no-report rules; this owns the hospital programme those due dates sit on.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
9. P1/P3/P4 shared. P2 names MDR 2017 / D&C Act 1940 for devices this hospital uses.

DELIBERATELY NOT INCLUDED
- Laboratory result-issue rule (AAC.4.h). Imaging AERB QA (AAC.5.i). Steriliser load validation (HIC.6). Crash-cart kit (COP.3).
- Billing. BMW. Fire plan. Medical-gas SOP.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 12 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 10 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 12; a search for "Hospital to define" without brackets finds all 12, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: equipment-planning method; inventory and logs; PPM/breakdown plan and evidence of implementation; inspection/calibration classes/interval/withdrawal; operator/maintainer qualifications; adverse-event and recall method; critical list and downtime clock; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "18-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
