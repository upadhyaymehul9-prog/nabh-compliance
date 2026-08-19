# -*- coding: utf-8 -*-
"""HIC.6 v2 — sterilisation and disinfection of instruments, equipment and devices.

Shape follows PRE.2 v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 102.
Chapter intent: PDF index 98.

HAS stop-work section. Five OEs mapped to five What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HIC.6"
CHAPTER = "HIC"
OE_CODES = ["HIC.6.a", "HIC.6.b", "HIC.6.c", "HIC.6.d", "HIC.6.e"]
POLICY_TITLE = "Sterilisation and Disinfection of Instruments, Equipment and Devices"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HIC v2 template: adoptable shape, plain English, HIC roles, five steps, stop-work for sterilisation failure.",
    },
]

STATEMENT_OF_INTENT = (
    "Infection prevention measures include sterilisation and/or disinfection of instruments, "
    "equipment and devices — adequate space and zoning, written guidance for the cycle from "
    "cleaning to issue, controlled reprocessing of single-use items, validation testing, and "
    "a recall procedure when sterilisation breakdown is identified."
)

PURPOSE = f"""This policy describes how {HOSPITAL} ensures sterilisation and/or disinfection of instruments, equipment and devices used in patient care: adequate space and zoning, the cleaning-packing-disinfection/sterilisation-storing-issue cycle, reprocessing of single-use items under written guidance, validation testing, and the recall procedure when a sterilisation breakdown is identified.

Boundaries: sterilisation/reprocessing is owned here; implant procurement and traceability stays with MOM.9. Instrument cleaning before sterilisation is part of the cycle described here; OT housekeeping stays with HIC.3.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the central sterile services department (CSSD) or sterilisation area and to all staff who handle, sterilise, store or issue instruments, equipment and devices at {HOSPITAL}.

It covers the five elements HIC.6.a–e name: space and zoning, the cleaning-to-issue cycle, reprocessing of single-use items, validation tests, and the recall procedure.

Boundaries with other policies of {HOSPITAL}:

- HIC.1 owns programme governance; this policy owns sterilisation as a component.
- HIC.2 owns clinical practices (safe injection, standard precautions) upstream of instrument use.
- HIC.3 owns support-service cleaning; this policy owns instrument decontamination.
- HIC.4 owns SSI prevention bundles that depend on sterile instruments.
- MOM.9 owns implant procurement and traceability; this policy does not cover procurement.
- FMS owns the building shell; this policy owns internal CSSD zoning requirements."""

POLICY_STATEMENT = f"""{HOSPITAL} provides adequate space and appropriate zoning for sterilisation activities. Cleaning, packing, disinfection and/or sterilisation, storing and issue of items are done per written guidance. Reprocessing of single-use instruments, equipment and devices is done only per written guidance. Validation tests for sterilisation are carried out and documented regularly. A recall procedure is implemented when a breakdown in the sterilisation system is identified.

An instrument that has failed sterilisation verification or a single-use device reprocessed against written guidance triggers the stop-work authority defined in this policy."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Using an instrument, equipment or device whose sterilisation verification (chemical indicator or biological indicator) has failed or is unreadable.
2. Reprocessing a single-use instrument, equipment or device without written guidance that specifies which items may be reprocessed, how many cycles are permitted, and what validation is required.
3. Storing sterile packs in a way that compromises pack integrity (humidity, open shelving without dust cover, stacking beyond defined limit).
4. Issuing a sterile pack past its shelf-life expiry date or with a compromised integrity indicator.
5. Bypassing the recall procedure when a sterilisation failure is identified (including late biological indicator positivity)."""

PROCEDURE_STEPS = [
f"""5.1 Space and zoning for sterilisation activities

{HOSPITAL} provides adequate space and appropriate zoning for sterilisation activities in the CSSD or designated sterilisation area:

- Three distinct zones: dirty (receiving and cleaning), clean (packing and sterilisation), and sterile (storage and issue).
- One-way workflow from dirty to clean to sterile; no reverse flow.
- Physical barriers or clear demarcation between zones.
- Adequate ventilation: {D('negative pressure in dirty zone relative to clean zone; positive pressure in sterile store relative to corridor')}.
- Pass-through hatches or autoclaves between dirty and clean zones where layout permits.
- Staff change area between dirty and clean zones; PPE requirements defined per zone.
- Environmental monitoring: temperature and humidity in sterile store maintained at {D('≤ 24 °C and ≤ 70 % RH')}.""",

f"""5.2 Cleaning, packing, disinfection/sterilisation, storing and issue

Cleaning, packing, disinfection and/or sterilisation, storing and the issue of items is done as per written guidance:

Cleaning:
- Pre-cleaning/soaking of instruments immediately after use in the clinical area.
- Manual and/or automated (ultrasonic/washer-disinfector) cleaning in the dirty zone.
- Visual inspection under magnification for residual soil before packing.

Packing:
- Items wrapped or placed in pouches/containers appropriate to the sterilisation method.
- Chemical indicator (Class 5 or 6 integrator) placed inside each pack.
- External chemical indicator (Class 1 process indicator) on the outside.
- Pack labelled with contents, steriliser load number, date of sterilisation, and expiry date.

Sterilisation:
- Method selected per item: steam (autoclave at {D('134 °C for 3.5 minutes or 121 °C for 15 minutes')}); dry heat; ethylene oxide; or low-temperature hydrogen peroxide plasma where available.
- Load records maintained for every cycle (time, temperature, pressure, operator).

Storing:
- Sterile packs stored in enclosed, dust-free shelving in the sterile zone.
- Stock rotation: first-in-first-out (FIFO).
- Shelf life per packaging type: {D('wrapped packs 30 days; sealed pouches 180 days; event-related where facility qualifies')}.

Issue:
- Issued only against a valid request; pack integrity and expiry verified before release.
- Transport in covered, clean containers to the point of use.""",

f"""5.3 Reprocessing of single-use instruments, equipment and devices

Reprocessing of single-use instruments, equipment and devices is done as per written guidance at {HOSPITAL}:

- A written list identifies which single-use items are approved for reprocessing by the Infection Control Committee (items not on this list are never reprocessed).
- Maximum number of reprocessing cycles per item is defined.
- Reprocessing follows the same cleaning-packing-sterilisation-validation cycle as reusable items.
- Functional testing after reprocessing (integrity, sharpness, calibration as applicable).
- Traceability: each reprocessed item is labelled with the number of cycles completed.
- The decision to reprocess is reviewed {D('annually')} by the ICC based on safety evidence and cost analysis.

Where {HOSPITAL} does not reprocess any single-use device, this is documented as a policy decision and no reprocessing list exists.""",

f"""5.4 Validation tests for sterilisation

Regular validation tests for sterilisation are carried out and documented:

- Physical monitoring: every cycle — time, temperature, pressure recorded from steriliser gauges/printout.
- Chemical indicators: every pack — Class 5/6 integrator inside; Class 1 outside.
- Biological indicators (BI): {D('weekly')} for steam sterilisers; every load for implant items; per manufacturer guidance for EtO/plasma.
- Bowie-Dick test: daily (first cycle) for pre-vacuum steam sterilisers.
- Records are maintained in the sterilisation validation log and retained for {D('3 years')}.

A failed BI or failed Bowie-Dick triggers the recall procedure (section 5.5) and the stop-work authority (section 6). Items from the affected load are not used until investigation confirms safety or the load is re-sterilised.""",

f"""5.5 Recall procedure for sterilisation breakdown

The established recall procedure is implemented when a breakdown in the sterilisation system is identified:

- Trigger: positive biological indicator, failed Bowie-Dick test, steriliser malfunction alarm, or discovery of a compromised pack after issue.
- Immediate actions: quarantine all items from the suspect load; do not use them.
- Notification: the CSSD/Sterilisation In-Charge notifies the Infection Control Officer, the OT/clinical area that received items, and the Medical Superintendent.
- Trace-back: identify all items from the affected load using load number and distribution records.
- Retrieval: items already distributed but not yet used are retrieved and quarantined.
- Items already used on patients: the Infection Control Officer assesses patient risk, initiates surveillance for infection, and documents the assessment.
- Investigation: root cause of the steriliser failure is identified; corrective action is implemented before the steriliser is returned to service.
- Re-qualification: the steriliser passes {D('three consecutive empty-chamber BIs')} before patient loads resume.
- Documentation: recall log with timeline, affected items, patient impact assessment, corrective action and re-qualification results.""",
]

STOP_WORK = f"""Do not use any instrument, equipment or device from a load whose biological indicator has returned positive, whose Bowie-Dick test has failed, or whose steriliser alarmed mid-cycle.

Do not reprocess any single-use device that is not on the written approved-for-reprocessing list, or that has exceeded its maximum reprocessing cycles.

When either situation is identified:
1. Quarantine all items from the affected load (or the non-approved device).
2. Notify the CSSD/Sterilisation In-Charge and the Infection Control Officer immediately.
3. Do not release items for patient use until the recall procedure (section 5.5) is complete and the steriliser is re-qualified.

No disciplinary action follows from invoking stop-work for a genuine sterilisation concern. Any staff member — CSSD technician, OT nurse, or clinician — has the authority to refuse a suspect instrument."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for CSSD resources, space, equipment and recall authority.

Infection Control Officer
- Oversees sterilisation validation, recall investigations and reprocessing policy.

CSSD / Sterilisation In-Charge
- Manages day-to-day sterilisation operations, load records, BI testing and recall execution.

Infection Control Nurse
- Audits CSSD practices, monitors chemical/biological indicator compliance.

Infection Control Committee
- Approves the reprocessing list, reviews recall reports, validates corrective actions.

OT and clinical area nurses
- Verify pack integrity and expiry before use; report suspect packs immediately.

Quality Coordinator
- Audits this policy {D('quarterly')}; tracks CAPA closure."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit reviews:

- CSSD zoning compliance and environmental monitoring records.
- Load records completeness (physical monitoring data for every cycle).
- Chemical indicator placement and reading compliance (every pack).
- Biological indicator testing frequency and results.
- Reprocessing list currency and cycle-count labelling compliance.
- Recall log entries and re-qualification records.
- Stop-work invocations and their outcomes.

Root-cause analysis is required when a biological indicator returns positive, or when a pack with a failed indicator reaches a clinical area.

This policy is reviewed {D('annually')}, and sooner when new sterilisation equipment is installed or after a recall event."""

TRAINING_ACKNOWLEDGEMENT = f"""All CSSD staff, OT nurses and clinical staff who handle sterile instruments are trained on this policy at induction and {D('once a year')} after that. Training covers zoning, the sterilisation cycle, indicator reading, reprocessing rules, and the stop-work/recall procedure.

Staff acknowledgement

I have read this Sterilisation and Disinfection policy of {HOSPITAL}. I understand the sterilisation cycle, validation requirements, stop-work authority and recall procedure.


Name: ___________________________    Designation: ___________________________

Department / area: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The CSSD/Sterilisation In-Charge holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="HIC/POL/06",
    version=VERSION,
    prepared_by=D("CSSD/Sterilisation In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — HIC chapter, standard HIC.6.
- WHO Decontamination and Reprocessing of Medical Devices for Health-care Facilities (2016).
- CDC/HICPAC Guideline for Disinfection and Sterilization in Healthcare Facilities (2008, updated 2019).
- IS/ISO 17665 (steam sterilisation) and IS/ISO 11135 (EtO sterilisation) — applicable Indian Standards.
- Internal documents of {HOSPITAL}: CSSD SOP, reprocessing list, sterilisation validation log, recall protocol, load record template."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Infection Control Officer and the Quality Coordinator.

Copies issued to: CSSD, OT, labour room, minor OT/procedure rooms, emergency, nursing administration.

The current version is available to all staff at the {D('infection control manual / staff intranet')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """BI — biological indicator
CAPA — corrective and preventive action
CSSD — central sterile services department
EtO — ethylene oxide
FMS — Facility Management and Safety (NABH SHCO chapter)
HIC — Hospital Infection Prevention and Control (NABH SHCO chapter)
ICC — Infection Control Committee
MOM — Management of Medication (NABH SHCO chapter)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
OT — operation theatre
PPE — personal protective equipment
RH — relative humidity
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HIC.6.a",
        "requirement": "The organisation provides adequate space and appropriate zoning for sterilisation activities.",
        "steps": "Section 3; 5.1 Space and zoning for sterilisation activities",
        "responsible": "Medical Superintendent (provide space); CSSD/Sterilisation In-Charge (maintain zoning); FMS (building shell)",
        "records": [
            "CSSD layout diagram showing three zones and one-way workflow.",
            "Environmental monitoring records (temperature, humidity in sterile store).",
            "Staff change and PPE compliance records per zone.",
            "Zoning compliance audit results.",
        ],
    },
    {
        "oe_code": "HIC.6.b",
        "requirement": "Cleaning, packing, disinfection and/or sterilisation, storing and the issue of items is done as per the written guidance.",
        "steps": "Section 3; 5.2 Cleaning, packing, disinfection/sterilisation, storing and issue; Section 4 items 3, 4",
        "responsible": "CSSD/Sterilisation In-Charge (manage cycle); CSSD technicians (execute); Infection Control Nurse (audit)",
        "records": [
            "Written SOP for each stage (cleaning, packing, sterilisation, storing, issue).",
            "Load records for every sterilisation cycle (time, temperature, pressure, operator).",
            "Chemical indicator reading log (Class 1 and Class 5/6 per pack).",
            "Stock rotation and shelf-life expiry tracking records.",
            "Issue register with pack integrity and expiry verification.",
        ],
    },
    {
        "oe_code": "HIC.6.c",
        "requirement": "Reprocessing of single-use instruments, equipment and devices are done as per written guidance.",
        "steps": "Section 3; 5.3 Reprocessing of single-use instruments; Section 4 item 2; Section 6 (stop-work)",
        "responsible": "Infection Control Committee (approve list); CSSD/Sterilisation In-Charge (execute reprocessing); Infection Control Officer (oversee)",
        "records": [
            "Written approved-for-reprocessing list with maximum cycle counts per item.",
            "Reprocessing log showing item, cycle number, validation result and functional test.",
            "Annual ICC review minutes for the reprocessing decision.",
            "Policy statement where no single-use reprocessing is conducted.",
        ],
    },
    {
        "oe_code": "HIC.6.d",
        "requirement": "Regular validation tests for sterilisation are carried out and documented.",
        "steps": "Section 3; 5.4 Validation tests for sterilisation; Section 4 item 1; Section 6 (stop-work)",
        "responsible": "CSSD/Sterilisation In-Charge (perform tests); Infection Control Officer (review results); Infection Control Nurse (audit frequency)",
        "records": [
            "Biological indicator test log with results and incubation times.",
            "Bowie-Dick test records (daily first cycle for pre-vacuum sterilisers).",
            "Physical monitoring printouts/gauge readings for every cycle.",
            "Sterilisation validation log retained for the defined period.",
        ],
    },
    {
        "oe_code": "HIC.6.e",
        "requirement": "The established recall procedure is implemented when a breakdown in the sterilisation system is identified.",
        "steps": "Section 3; 5.5 Recall procedure for sterilisation breakdown; Section 4 item 5; Section 6 (stop-work)",
        "responsible": "CSSD/Sterilisation In-Charge (execute recall); Infection Control Officer (investigate and assess patient risk); Medical Superintendent (authorise re-qualification)",
        "records": [
            "Recall log with trigger, timeline, affected items, distribution trace-back and patient impact assessment.",
            "Quarantine records for affected load items.",
            "Root-cause investigation and corrective action report.",
            "Re-qualification records (consecutive BI passes before resuming patient loads).",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HIC.6 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Infection prevention measures include sterilisation and/or disinfection of instruments, equipment and devices." HIC.6.a–e PDF index 102. Four asterisked OEs: HIC.6.b, HIC.6.c, HIC.6.d, HIC.6.e (all Commitment). Stop-work YES (sterilisation failure → quarantine, do not use).

SHAPE: Five What-we-do subsections (5.1–5.5). Stop-work section present. Disclaimer accreditation-only. HIC roles."""


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
        "template_test": "hic_v2_adoptable_shape",
        "subtitle": "Sterilisation, disinfection, validation and recall of instruments and devices.",
        "doc_no": "HIC/POL/06",
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "hic6_v2_draft.json",
        "HIC.6_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
