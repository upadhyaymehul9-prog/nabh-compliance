# -*- coding: utf-8 -*-
"""Template-test rebuild of FMS.2 as an adoptable hospital policy.

Does NOT overwrite policies/drafts/fms2_draft.json or build_fms2.py.
Writes policies/drafts/fms2_v2_draft.json only. No SQL. No Supabase insert.
"""
from __future__ import annotations

import sys

from fms_v2_common import BLANK, D, HOSPITAL, emit_v2, verify_shape
from policy_build_common import make_disclaimer

STANDARD_CODE = "FMS.2"
CHAPTER = "FMS"
OE_CODES = [
    "FMS.2.a", "FMS.2.b", "FMS.2.c", "FMS.2.d", "FMS.2.e", "FMS.2.f", "FMS.2.g",
]
POLICY_TITLE = "Safety of Patients, Families, Staff and Visitors"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "Template rebuild to FMS.5 v2.2 shape. Not an approved master.",
    },
]

PURPOSE = f"""This policy governs how {HOSPITAL} keeps the building safe for patients, families, staff and visitors: patient-safety devices and infrastructure, access for the differently-abled, extra-security areas, monthly facility inspection rounds, electrical-installation audits, unused material, and building hazardous materials.

It is not a generator-load test, a medical-equipment PPM file, a medical-gas SOP, or a fire plan. A finding on a round is recorded here and closed by the programme that owns the plant, the device, the gas or the fire provision.

Editable defaults are marked {D('like this')}. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """A round is a walk. An unlabelled jerry-can is not a programme. A condemned bed does not stay in a patient bay."""

SCOPE = f"""This policy applies to the buildings, grounds and occupied spaces of {HOSPITAL} and to the people who inspect devices, keep access usable, control extra-security areas, walk monthly rounds, audit the electrical installation, condemn unused material, and identify building hazardous materials.

It covers grab rails, wet-area flooring, window restrictors, call-bell hardware and similar fabric; ramps, lifts and accessible toilets this building actually has; locks, access descriptions and CCTV if installed; facility inspection rounds at least once a month; electrical safety audits of the installation; identification and disposal of material not in use; and identification and safe use of housekeeping chemicals, water-treatment chemicals, diesel, mercury if still present, and engineering solvents.

It does not govern planned utilities and energy initiatives, medical-equipment PPM, medical gases, or fire-equipment maintenance. Fire extinguishers found missing on a round are a finding here that the fire programme must close. Laboratory bench chemical hygiene, blood and body-fluid spills, cytotoxic bench spills, and biomedical-waste colours stay those programmes. Locks and cameras are here; matching a neonate and observing a vulnerable adult stay those care policies. PESO and gas-cylinder rules, if they apply, live on the applicable-legislation register — not as this chemical list counted twice."""

POLICY_STATEMENT = f"""Patient-safety devices that prevent a foreseeable harm in the building are installed and inspected. Grab rails in toilets and wet areas, anti-skid flooring where water is expected, window restrictors on upper floors, bumper guards on trolley routes, and nurse-call hardware as fabric, are this policy. Fire detection and extinguishers are the fire programme; they appear on a round as found, blocked or missing, not as this install-and-inspect list counted twice. Bed-rail use as a falls decision stays the vulnerable-adult care policy; this policy owns that the hardware exists and is fixed.

Facilities for the differently-abled that this building actually provides — ramps or a working lift to floors used by patients, an accessible toilet, wayfinding a wheelchair user can follow — are kept usable. A single ramp to a locked side door is not that provision. Gudlavalleti (2018) and NBC 2016 access, as the local authority applied them, are the frameworks. This policy does not invent a NABH gradient or door-width for every small hospital.

Areas that need extra security are named: pharmacy stores, medical records if held on site, nursery and labour, server or plant rooms, the gas manifold, and any other area the Medical Superintendent adds. Access by staff, patients and visitors is described. A CCTV monitor that is never watched is not extra security. Matching and handing over a neonate, and bedside observation of a vulnerable adult, stay those care policies; this policy owns the locks and the door.

Facility inspection rounds walk occupied clinical and support spaces at least once a month. That interval is in the standard and is not optional. A register signed from the engineering office with no ward walk has not been held.

Electrical safety audits cover the installation: earthing continuity, residual-current protection on wet-area and patient-care circuits, damaged flexible cords, sockets in wet areas, panel labelling and lockability, and isolated-power or equivalent in OT if an OT exists. IS 732 and IS 3043 are NBC-pointed frameworks. A megger reading from commissioning with no subsequent audit is not this audit. A failed medical device is the equipment programme; a failed building circuit is here.

Material not in use — condemned furniture, obsolete equipment struck off the equipment inventory, unused building materials, expired non-biomedical stores — is identified, quarantined so it cannot be reused on a patient, and disposed of or sold. The four-colour clinical waste stream is not this procedure.

Hazardous materials this hospital actually holds are listed, labelled, segregated and used with the PPE and spill method for building chemical, mercury and fuel. An SDS folder in quality with an unlabelled jerry-can is not identification. Blood spills, cytotoxic bench spills, biomedical waste and laboratory bench hygiene stay those programmes. Dual entry when a spill meets two definitions."""

NON_NEGOTIABLES = f"""The following are prohibited.

1. Signing a monthly facility inspection round without walking occupied clinical space.
2. Leaving tagged or condemned unused material in a patient bay.
3. Using an unlabelled hazardous material, or treating an SDS folder as identification when the container at the point of use has no label.
4. Offering biomedical-waste colours as the unused-material procedure.
5. Blocking a ramp, accessible toilet or extra-security door, or treating unwatched CCTV as extra security.

Anyone who sees a prohibited act stops it under the stop-work clause and reports it the same shift to the {D('Maintenance In-Charge')} or, at night, the Night Duty Officer."""

PROCEDURE_STEPS = [
f"""5.1 Devices, access and extra security

The Maintenance In-Charge holds the installed-device list and inspects those devices {D('monthly')}, on the facility round. A grab rail that has pulled out of a wet-wall fixing, or a call bell that rings at the panel but not in the room, is withdrawn from reliance and repaired. Inspection from a purchase invoice is not inspection.

Differently-abled facilities this building has are walked on the same round and kept unblocked. A trolley bay on a ramp is a finding.

Extra-security areas are listed, with the access description for staff, patients and visitors. Security Supervisor holds the hardware (locks, access control, CCTV if installed) and the watch roster. A breach that meets the incident definition is also entered in the incident system.""",

f"""5.2 Monthly rounds and electrical safety audits

The {D('Maintenance In-Charge')} walks occupied clinical and support spaces at least once a month. The circuit includes wards, theatre and labour if running, stores, plant rooms and extra-security areas. Findings — blocked exit, failed grab rail, wet floor without warning, unlabelled chemical, condemned item in a corridor, open electrical panel, missing extinguisher — are recorded, owned and closed. A missed month is a defect. A finding that caused harm is also an incident.

Electrical safety audits of the installation are done {D('annually')} by a {D('competent in-house person or licensed contractor')}. Scope: earthing, residual-current protection, wet-area sockets, panel lockability, and OT isolated-power or equivalent if an OT exists. A failed earth or missing ELCB is isolated until repaired. This is not the loaded generator test and not device calibration.""",

f"""5.3 Unused material

Material not in use is identified with tag, location, date and owner. If the item is equipment, the equipment programme strikes it off the inventory before the carcass is moved. It is stored so it cannot be reused on a patient, then disposed of or sold. A tagged item still in a patient bay is a failure of this policy.

Biomedical waste stays the infection-control waste programme. WHO Safe Management of Wastes from Health-Care Activities is a waste framework only; it does not move colour-code ownership here.""",

f"""5.4 Hazardous materials

The Maintenance In-Charge holds the inventory of classes this hospital actually holds — housekeeping and water-treatment chemicals, diesel and other fuels, mercury if a column still exists, engineering solvents, bulk stores outside the laboratory bench programme — or a recorded absence for a class not held.

Every container at the point of use is labelled. PPE and the spill method for building chemical, mercury and fuel are displayed at the store. Users are named. NBC 2016 storage provisions apply as the local authority applied them.

Blood and body-fluid spills, cytotoxic preparation spills, biomedical waste and laboratory bench hygiene remain those programmes. Dual entry when a spill meets two definitions.""",
]

STOP_WORK = f"""Every person on the premises has the authority and the duty to stop an act that breaches a non-negotiable rule: a monthly round being paper-signed; a condemned bed in a patient bay; an unlabelled chemical in use; a blocked ramp or exit.

The person says "stop", makes the immediate safe condition they are competent to make (remove the trolley from the ramp, take the unlabelled jerry-can out of use), and reports the same shift to the {D('Maintenance In-Charge')} or the Night Duty Officer. There is no retaliation for a good-faith stop-work."""

RESPONSIBILITY = f"""Roles below are titles, not vacancies.

Medical Superintendent
- Accountable that this policy is issued and followed.
- Names extra-security areas not already listed.

Maintenance In-Charge
- Owns device inspection, monthly rounds, electrical-audit file, unused-material procedure and the hazardous-material inventory.

Nursing Superintendent
- Keeps clinical areas walkable on the monthly round; does not park trolleys on ramps or in exits.

Security Supervisor
- Owns extra-security hardware and the watch roster.

Night Duty Officer
- Receives a night finding and does not leave a blocked exit or unlabelled chemical until morning.

Quality Coordinator
- Audits this policy {D('quarterly')}.

A RACI snapshot:
- Device inspection: Maintenance In-Charge (R/A)
- Monthly round: Maintenance In-Charge (R); Medical Superintendent (A)
- Electrical audit: competent auditor (R); Maintenance In-Charge (A)
- Unused material: Maintenance In-Charge (R/A); equipment programme strikes devices off inventory
- Hazardous materials: Maintenance In-Charge (R/A)
- Extra security: Security Supervisor (R); Medical Superintendent (A)
- Stop-work: all staff (R); Maintenance In-Charge (A for restart)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored:
- Device inspections that touched fabric, not invoices.
- Monthly rounds that walked clinical areas; no missed month.
- Electrical audit of the installation, not a generator-load test counted twice; isolation-until-repaired closed.
- Unused-material tags that left the clinical floor; not biomedical-waste colours.
- Hazardous-material labels at the point of use, not only an SDS folder.
- Extra-security watch actually rostered.

Root-cause analysis is required when: a month is missed; a condemned item is found in a patient bay on two successive rounds; an unlabelled chemical is found in use; a grab rail fails in service. CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a missed month."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who walk rounds, handle building chemicals, or work on an occupied floor are trained against this policy at induction and {D('once a year')} thereafter.

Staff acknowledgement

I have read this Safety of Patients, Families, Staff and Visitors policy of {HOSPITAL}. I will not sign a round I did not walk. I will not leave unused material in a patient bay. I will not use an unlabelled chemical.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/02')}
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

REFERENCES = """- National Building Code of India, 2016 (Bureau of Indian Standards), building, access and electrical-installation framework as the local authority has applied it. IS 732, IS 3043 and IS 2190 are NBC-pointed practice, not extra disclaimer statutes.
- Gudlavalleti, V. (2018). Challenges in Accessing Health Care for People with Disability in the South Asian Context. Int J Environ Res Public Health — disability-access framework.
- Safe Management of Wastes from Health-Care Activities (2nd ed.). World Health Organization (2014) — waste framework only; biomedical-waste colour and authorisation remain the infection-control waste programme.
- Hospital safety index: guide for evaluators – 2nd ed. World Health Organization (2015) — evaluator framework, not a mandated score.
- Aggarwal, R., et al. (2010). Technology as applied to patient safety: an overview. Qual Saf Health Care — infrastructure framework.
- NABH Standards for Small Healthcare Organisations, 3rd Edition, Chapter 8, standard FMS.2 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- Internal: monthly round form; electrical audit; unused-material procedure; hazardous-material inventory; utilities, equipment, gas and fire programmes; incident system."""

DISTRIBUTION = f"""Controlled master: office of the Medical Superintendent, {HOSPITAL}, with a working copy held by the Maintenance In-Charge and the Quality Coordinator.

Issued to: Security Supervisor, Nursing Superintendent, staff who walk the monthly round, department in-charges on the circuit.

Available to all staff at the {D('Nursing Station policy folder')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

On revision, every displayed copy is withdrawn the same day. One dated superseded copy is retained by the Quality Coordinator."""

ABBREVIATIONS = """NBC — National Building Code of India, 2016
ELCB — earth-leakage circuit breaker
RCCB — residual-current circuit breaker
CCTV — closed-circuit television
SDS — safety data sheet
CAPA — corrective and preventive action
RCA — root-cause analysis

Night Duty Officer — the senior doctor or senior nurse holding emergency command overnight
Maintenance In-Charge — the person accountable for rounds, devices and building hazardous materials under this policy
Security Supervisor — the person accountable for extra-security hardware and the watch roster"""

STATUTE_CLAUSE = (
    "the National Building Code of India, 2016, insofar as the local building and fire "
    "authority has applied it to this facility for occupancy, access and electrical-installation safety"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "FMS.2.a",
        "requirement": "Patient-safety devices and infrastructure are installed across the organisation and inspected periodically.",
        "steps": "Section 3; 5.1 Devices, access and extra security",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Installed-device list.",
            "Monthly inspection records of fabric (grab rails, wet-area flooring, window restrictors, call-bell hardware).",
            "Repair or withdrawal record for a failed device.",
        ],
    },
    {
        "oe_code": "FMS.2.b",
        "requirement": "The organisation has facilities for the differently-abled.",
        "steps": "Section 3; 5.1 Devices, access and extra security",
        "responsible": "Maintenance In-Charge",
        "records": [
            "List of facilities this building actually provides.",
            "Monthly round findings that ramps and accessible toilets were unblocked.",
            "Record that a ramp to a locked side door is not counted as the provision.",
        ],
    },
    {
        "oe_code": "FMS.2.c",
        "requirement": "Operational planning identifies areas which need to have extra security and describes access to different areas in the hospital by staff, patients, and visitors.",
        "steps": "Section 3; 5.1 Devices, access and extra security",
        "responsible": "Security Supervisor; Medical Superintendent (names the areas)",
        "records": [
            "Extra-security area list and access description.",
            "Watch roster for CCTV or door control if installed.",
            "Incident-file entry for a breach that met the incident definition.",
        ],
    },
    {
        "oe_code": "FMS.2.d",
        "requirement": "Facility inspection rounds to ensure safety are conducted at least once a month.",
        "steps": "Section 3; 5.2 Monthly rounds and electrical safety audits",
        "responsible": "Maintenance In-Charge (walks); Medical Superintendent (accountable)",
        "records": [
            "Monthly round reports showing a walk of clinical areas.",
            "Closed findings with owner and date.",
            "Record of a missed month treated as a defect.",
        ],
    },
    {
        "oe_code": "FMS.2.e",
        "requirement": "Organisation conducts electrical safety audits for the facility.",
        "steps": "Section 3; 5.2 Monthly rounds and electrical safety audits",
        "responsible": "Maintenance In-Charge; named competent auditor",
        "records": [
            "Electrical safety audit report at the defined interval.",
            "Isolation-until-repaired records for a failed earth or missing ELCB.",
            "Competence of the auditor (in-house or licensed contractor).",
        ],
    },
    {
        "oe_code": "FMS.2.f",
        "requirement": "There is a procedure which addresses the identification and disposal of material(s) not in use in the organisation.",
        "steps": "Section 3; 5.3 Unused material",
        "responsible": "Maintenance In-Charge; equipment programme strikes devices off inventory",
        "records": [
            "Identification tags (location, date, owner).",
            "Equipment strike-off before a device carcass is moved.",
            "Quarantine and disposal or sale record.",
        ],
    },
    {
        "oe_code": "FMS.2.g",
        "requirement": "Hazardous materials are identified and used safely within the organisation.",
        "steps": "Section 3; 5.4 Hazardous materials",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Inventory of classes actually held, or recorded absences.",
            "Labels at the point of use; PPE and spill method at the store.",
            "Named users.",
            "Spill record or drill for building chemical, mercury or fuel.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.2 v2 to the FMS.5 v2.2 shape.

Technical substance retained from v1: monthly interval is in the OE; NBC 2016
as-applied; IS 732/IS 3043 NBC-pointed not CEA-in-P2; Gudlavalleti; WHO waste
framework with BMW staying HIC.3; unused material is not BMW; building hazmat
is not blood/cytotoxic/lab-bench; COP matching/observation stay care policies;
Hospital safety index is not a mandated score.

Four 5.x subsections, five non-negotiables. Stop-work included. P2 NBC 2016.
No SQL. Status remains draft.
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
        "doc_no": "«FMS/POL/02»",
        "subtitle": "Standards for a walkable, labelled, electrically sound building.",
        "footer_label": "Facility safety",
        "acknowledgement_note": "The Nursing Superintendent holds signed acknowledgements with the induction record.",
    }
    md = verify_shape(
        draft,
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    emit_v2(draft, "fms2_v2_draft.json", "FMS.2_v2_preview.md", md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
