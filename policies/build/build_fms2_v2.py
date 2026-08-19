# -*- coding: utf-8 -*-
"""FMS.2 v2 — safety of patients, families, staff and visitors.

Shape follows FMS.5 v2.2 (section list and order only). Wording is this
standard's OEs and v1 substance. Does not overwrite fms2_draft.json or
build_fms2.py. No SQL. No Supabase insert.

Disclaimer P2 names NBC 2016 as locally applied (same statute scoping as v1).
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

STANDARD_CODE = "FMS.2"
CHAPTER = "FMS"
OE_CODES = [
    "FMS.2.a", "FMS.2.b", "FMS.2.c", "FMS.2.d",
    "FMS.2.e", "FMS.2.f", "FMS.2.g",
]
POLICY_TITLE = "Safety of Patients, Families, Staff and Visitors"
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
        "description": "Same section skeleton as FMS.5 v2.2; wording rebuilt from FMS.2 OEs and v1. Not an approved master.",
    },
]

PURPOSE = f"""This policy governs how {HOSPITAL} keeps the building safe for patients, their families, staff and visitors: how patient-safety devices and infrastructure are installed and inspected; how facilities for the differently-abled are provided and kept usable; how extra-security areas are named and access is described; how facility inspection rounds are walked at least once a month; how the electrical installation is audited; how material not in use is identified and disposed of; and how hazardous materials used in the building are identified and used safely.

It is facility safety of people in the building. It is not a fire-drill script, not biomedical-waste colour code, not the equipment preventive-maintenance programme, and not the care process for matching a neonate or observing a vulnerable adult.

Editable defaults in this document are marked {D('like this')}. A hospital that adopts the default keeps the wording. A hospital that needs a different owner, interval or arrangement replaces the marked text before issue. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """A grab rail that is still in the wall, a round that actually walked the ward, and a chemical that still has its label. A register signed from the engineering office is not a round."""

SCOPE = f"""This policy applies to the buildings, grounds and occupied spaces of {HOSPITAL}, and to the people who install and inspect patient-safety fabric, keep access for the differently-abled usable, plan extra-security and access control, walk monthly facility inspection rounds, audit the electrical installation, condemn and dispose of material not in use, and identify and control hazardous materials used in the facility.

It covers: patient-safety devices and infrastructure and their periodic inspection; facilities for the differently-abled; extra-security areas and access by staff, patients and visitors; facility inspection rounds at least once a month; electrical safety audits; identification and disposal of material not in use; and identification and safe use of hazardous materials.

It does not govern planned space, drawings, wayfinding, round-the-clock water and electricity, backup testing or energy initiatives — those belong to the utilities programme. A backup-test failure found on a round is recorded here as a safety finding and handed back to that programme to fix the plant.

A broken grab-rail is this policy's infrastructure. A failed ventilator is the equipment programme. A leaking medical-gas cylinder found on a round is handed to the gas programme.

Fire detection, alarms, extinguishers and suppression are fire provisions, maintained under the fire programme. A blocked exit found on a monthly round is a finding here that the fire programme must close. Management's duty that proactive risk exists across the organisation remains that management-risk programme; this policy writes the monthly facility walk.

Laboratory result and imaging no-report rules for overdue calibrators remain those diagnostic programmes. Laboratory bench chemical hygiene remains the laboratory safety programme. This policy owns hospital-wide hazardous materials and the monthly facility walk. Building chemical stores, diesel, mercury if still present, and housekeeping chemicals are here.

Radiation and PC-PNDT signs remain the laboratory and imaging safety programme. Wayfinding is the utilities programme.

Matching, handing-over and missing-child response for a neonate, and bedside observation of a vulnerable adult, remain those care policies. This policy owns locks, cameras, door hardware and the written access description.

Blood and body-fluid spills remain the infection-control spill programme. Cytotoxic spill at preparation and administration remains that medication programme. Biomedical-waste colour, internal transport and authorisation remain the infection-control waste programme. Material not in use here is condemned furniture, obsolete non-device equipment, unused construction debris and expired non-waste stores — not the four-colour clinical waste stream.

WHO Safe Management of Wastes from Health-Care Activities is a waste framework only; colours stay the waste programme. Gudlavalleti is the disability-access framework, not a pasted accessibility-audit form. NBC 2016 is the building, access and electrical-installation framework as the local authority applied it. IS 732, IS 3043 and IS 2190 are NBC-pointed practice, not extra disclaimer statutes. Hospital Safety Index is an evaluator framework, not a mandated score.

Patient-facing expected cost is not a safety round. A safety finding that caused harm is also an incident; the round remains this policy."""

POLICY_STATEMENT = f"""{HOSPITAL} installs patient-safety devices and infrastructure across the organisation and inspects them periodically. Fabric that prevents a foreseeable harm in the building — grab rails, wet-area flooring, window restrictors, call-bell hardware, bed-rail hardware as furniture — exists and works. Fire extinguishers are not this install-and-inspect programme counted twice.

{HOSPITAL} has facilities for the differently-abled and keeps them usable. A single ramp to a locked side door is not that provision.

{HOSPITAL} identifies areas that need extra security and describes access to different areas by staff, patients and visitors, with the hardware that enforces it. A camera that is never watched is not extra security. Matching a neonate and observing a vulnerable adult remain those care policies.

{HOSPITAL} walks facility inspection rounds to ensure safety at least once a month. That interval is in the requirement and is not optional. A register signed from the engineering office with no ward walk is not a round.

{HOSPITAL} conducts electrical safety audits of the facility: earthing, residual-current protection, wet-area sockets, panel lockability. This is not the utilities programme's loaded generator test and not the equipment programme's device calibration.

{HOSPITAL} identifies material not in use and disposes of it so it cannot be reused on a patient. Biomedical-waste colours are not that procedure.

{HOSPITAL} identifies hazardous materials it actually holds and uses them safely, with labels, segregation, PPE and a spill method for building chemicals, fuels and mercury if still present. Blood spills, cytotoxic bench spills, laboratory bench hygiene and biomedical-waste colours remain those other programmes.

{HOSPITAL} does not treat a monthly register signed without a walk, biomedical-waste colours offered as unused-material disposal, or a chemical store with no identification, as that duty."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no operational exception and no "until the vendor comes" exception.

1. Signing the monthly facility inspection round from the engineering office, or on the last day of the month, without walking occupied clinical and support spaces.
2. Missing a calendar month. At least once a month is the floor.
3. Inspecting patient-safety fabric from a purchase invoice. A grab rail that has pulled out of a wet-wall fixing, or a call bell that rings at the panel but not in the room, is a failed device.
4. Blocking a ramp, accessible toilet, or other differently-abled facility with a trolley bay, stores or a parked vehicle.
5. Treating a camera that is never watched, or a lock whose key is on an open hook, as extra security.
6. Absorbing neonatal matching, missing-child response, or bedside observation of a vulnerable adult into this hardware description. Those remain the care policies.
7. Offering the four-colour biomedical-waste stream as identification and disposal of material not in use.
8. Leaving a condemned item in a patient bay, or putting a condemned bed or device back into clinical use.
9. Leaving a hazardous-material container unlabelled at the point of use, or keeping an SDS folder in quality while the jerry-can has no label.
10. Counting a blood or body-fluid spill, a cytotoxic bench spill, laboratory bench chemical hygiene, or biomedical-waste colours as this building hazardous-material list.
11. Leaving a failed earth, a missing residual-current device on a wet-area or patient-care circuit, or an unlocked live panel, in service. Isolation until repaired.
12. Treating the Hospital Safety Index as a mandated score this hospital must achieve.

A person who finds a blocked exit, an unlabelled chemical, a condemned bed in a patient bay, or a monthly register with no walk, reports it the same shift to the {D('Maintenance In-Charge')}."""

PROCEDURE_STEPS = [
f"""5.1 Install and inspect patient-safety fabric

Patient-safety devices and infrastructure are the fabric that prevents a foreseeable harm in the building: grab rails in toilets and wet areas, anti-skid flooring where water is expected, window restrictors on upper floors, bumper guards on trolley routes, nurse-call or emergency-bell infrastructure as hardware, bed-rail hardware as furniture, and similar devices this hospital actually runs.

Bedside observation that uses a call bell, and the decision to raise a bed rail as a falls or restraint act, remain those care policies. This section owns that the bell exists and works, and that the rail as furniture is still attached.

Fire detection, alarms, extinguishers and suppression are fire provisions, inspected under the fire programme. They may be listed on a monthly round as found, blocked or failed; they are not this install-and-inspect programme counted twice.

NBC 2016 and the chapter's patient-safety infrastructure frameworks (Aggarwal et al.; Health Facilities Management) inform what this hospital installs; they are not a pasted device catalogue.

The {D('Maintenance In-Charge')} holds the installed-device list and inspects {D('monthly')}. A grab rail that pulled out of a wet-wall fixing, or an inspection done from a purchase invoice, is a failure of this policy.""",

f"""5.2 Provide facilities for the differently-abled and keep them usable

Gudlavalleti is the South-Asian disability-access framework in the chapter bibliography. This section is the facilities this hospital actually provides: ramps or a working lift to the floors it uses for patients, an accessible toilet, wayfinding a wheelchair user can follow (consistent with the utilities programme's signs), and the other provisions this hospital has defined for the disabilities it can reasonably accommodate in this building.

A single ramp to a locked side door is not this provision. NBC 2016 access provisions apply insofar as the local authority applied them to this occupancy. This policy does not invent a NABH gradient or door-width figure for every small hospital.

Which facilities are in place, how they are kept usable (not blocked by a trolley bay), and how a failure is recorded, are held by the {D('Maintenance In-Charge')}. Facilities provided: {BLANK}.""",

f"""5.3 Identify extra-security areas and describe who may enter

Extra-security areas typically include pharmacy stores, medical records if held on site, nursery and labour as the neonatal care policy uses them, server or plant rooms, the gas manifold, and any other area this hospital has named. Named extra-security areas: {BLANK}.

Matching and handing over a neonate, and the missing-child response, remain the neonatal care policy. Bedside observation of a vulnerable adult remains that care policy. This section owns locks, access-control hardware, cameras if installed, and the written description of who may enter which area.

A camera that is never watched is not extra security. Who may enter, as staff, patients and visitors, and the hardware that enforces it, are held by the {D('named security or administration lead')}. A breach that is also an incident is dual-entered in the incident system.""",

f"""5.4 Walk the facility inspection round every month

Facility inspection rounds to ensure safety are conducted at least once a month. That interval is in the requirement and is not hospital-optional.

The round is a walk of occupied clinical and support spaces that can find a blocked exit, a failed grab rail, a wet floor without warning, a chemical container without a label, a condemned item still in a corridor, an electrical panel left open, or a fire extinguisher missing (handed to the fire programme). The failure this walk exists to catch is a register signed on the last day of the month from the engineering office with no ward walk, or a round that only inspects the director's corridor.

Who walks: {D('Maintenance In-Charge with a clinical staff member from the area')}. The circuit: {BLANK}. A finding is recorded and closed; overdue closures are visible to the Medical Superintendent. The management-risk programme may use these as risk inputs; this remains the facility method. A missed month is a defect. A finding that is also an incident is dual-entered in the incident system.""",

f"""5.5 Audit the electrical installation

This is not the utilities programme's loaded generator test and not the equipment programme's calibration of a medical device. It is an audit of the electrical installation as a facility: earthing continuity, residual-current / earth-leakage protection on wet-area and patient-care circuits, overload and discrimination, damaged flexible cords, socket outlets in wet areas, panel labelling and lockability, and isolated-power or equivalent provision in the operating theatre if this hospital runs one.

NBC 2016 is the building-code hook. IS 732 (wiring practice) and IS 3043 (earthing) are NBC-pointed frameworks, not extra disclaimer statutes. Central Electricity Authority electrical-supply regulations are not a numbered FMS chapter reference and are not imported into the disclaimer; the hospital's applicable-legislation register remains that legislation programme if that instrument actually applies to this occupancy.

The failure this audit exists to catch is a megger reading filed once at commissioning with no subsequent audit, or an audit that never enters the operating theatre because "biomedical owns it." Who audits: {D('in-house competent person or licensed contractor')}. Interval: {D('annually')}. A failed earth or a missing residual-current device is isolated until repaired. A failed medical device is still the equipment programme; a failed building circuit is this audit.""",

f"""5.6 Identify and dispose of material not in use

Material not in use is condemned furniture, obsolete equipment that the equipment programme has struck off the inventory, unused building materials, and expired non-waste general stores. It is not the four-colour biomedical-waste stream. WHO Safe Management of Wastes from Health-Care Activities is a waste framework; it does not move biomedical-waste ownership here.

How material not in use is identified: tag, location, date, owner. Who authorises condemnation: {D('Maintenance In-Charge')}, including equipment-programme strike-off when the item is equipment. It is stored so it cannot be reused on a patient, then disposed of or sold.

A locked store-room with no identification step, a sale-to-scrap handshake with no tag, or a condemned ventilator left in a ward bay "until biomedical collects it," is not this procedure. A tagged item that is still in a patient bay is a failure of this policy.""",

f"""5.7 Identify hazardous materials and use them safely

The chapter intent is that the organisation safely manages hazardous materials. Laboratory bench chemical hygiene and laboratory fire pointing at the fire programme remain those programmes. Blood and body-fluid spills remain the infection-control spill programme. Cytotoxic preparation and administration spills remain that medication programme. Biomedical waste remains the waste programme.

This section is the facility list: housekeeping chemicals, water-treatment chemicals, diesel and other fuels, mercury if a sphygmomanometer or thermometer stock still exists, engineering solvents, and laboratory bulk stores that sit outside the bench programme. Dual entry when a spill meets two definitions.

The inventory is of classes this hospital actually holds, or a recorded absence for a class it does not hold. Labels and segregation are on the container at the point of use, not only in an SDS folder in quality. PPE and the spill method for chemical, mercury and fuel are distinct from blood spill and cytotoxic bench spill. Who may use which material is named.

NBC 2016 storage provisions apply as the local authority applied them. Explosives and cylinder rules, if they apply, live on the applicable-legislation register and in the gas programme; they are not this chemical list counted twice.

An SDS folder with no label on the jerry-can, or a mercury spill kit that was never opened because "we went digital" while a mercury column still sits in a drawer, is a failure of this policy.""",
]

STOP_WORK = f"""A person who is about to do any of the following does not proceed:

- put a condemned bed, device or other tagged unused item back into a patient bay or into clinical use;
- pour, mix or store a chemical from an unlabelled container;
- restore a circuit that failed an electrical-safety audit — failed earth, missing residual-current device on a wet-area or patient-care circuit, unlocked live panel — until it has been repaired;
- sign the monthly round sheet without having walked the occupied clinical areas on the circuit.

They tag and quarantine the condemned item, cap and set aside the unlabelled container, leave the failed circuit isolated, or leave the round sheet unsigned, and tell the {D('Maintenance In-Charge')} the same shift.

A good-faith refusal to sign a round that was not walked is not a disciplinary matter. The month is not recorded as inspected until the walk happened."""

RESPONSIBILITY = f"""These are the jobs this facility-safety policy needs. In a small hospital the facilities lead may also hold the utilities file; they still walk this round as a safety walk, not as a generator test.

Medical Superintendent (head of the institution)
- Accountable that the facility operates so that patients, families, staff and visitors are safe as this policy requires.
- Sees overdue round closures.

{D('Maintenance In-Charge')} (named facilities or engineering lead)
- Holds device inspections, the monthly round, electrical-audit follow-up, unused-material records and the hazardous-material inventory.
- Isolates a failed building circuit until repaired.
- Authorises condemnation of material not in use.

{D('named security or administration lead')}
- Holds the extra-security list, the access description, and the hardware that enforces it, where that is not the engineering lead.

Quality Coordinator
- Audits the records in section 8.

Department in-charges
- Keep ramps, accessible toilets and extra-security doors unblocked in their area.
- Report a failed grab rail, call bell, unlabelled chemical or condemned item still in a bay.

All staff
- Report a blocked exit, an unlabelled chemical, a condemned bed in a patient bay, and a monthly register with no walk.

A RACI snapshot:

- Patient-safety fabric: Maintenance In-Charge (R/A)
- Differently-abled facilities: Maintenance In-Charge (R/A)
- Extra-security and access: named security or administration lead (R); Medical Superintendent (A)
- Monthly round: Maintenance In-Charge (R); Medical Superintendent (A)
- Electrical-installation audit: named competent auditor (R); Maintenance In-Charge (A for isolation-until-repaired)
- Unused material: Maintenance In-Charge (R/A); equipment programme (C for strike-off)
- Hazardous materials: Maintenance In-Charge (R/A)
- Audit: Quality Coordinator (R); Medical Superintendent (A)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at the fabric and the records, not at a binder.

What is monitored each quarter:

- Inspections that touched devices rather than invoices; grab rails, call bells and wet-area flooring still in place.
- Differently-abled facilities still unblocked.
- Extra-security list still matches the hardware; cameras, if installed, are watched as described.
- Monthly rounds that walked clinical areas at least once a month rather than a signed register. A missed month is a finding.
- Electrical audits of the building, not the utilities programme's generator tests counted twice; isolation-until-repaired still in force for a failed earth.
- Unused-material procedure that is not biomedical-waste colours; no condemned item in a patient bay.
- Hazardous-material identification on the container at the point of use, not an SDS folder offered as the whole list. Blood, cytotoxic, laboratory-bench and waste programmes left as those documents.
- Fire equipment left with the fire programme except as a round finding.
- Care-process matching and observation left with those care policies.

Any non-conformity is a finding. The Maintenance In-Charge owns corrective action for fabric, rounds, unused material and building chemicals. The named security or administration lead owns corrective action for extra-security hardware. Root-cause analysis is required when: a month was missed; a condemned item is found in a patient bay; an unlabelled chemical is found at the point of use; a failed earth was left in service; or a round was signed without a walk.

Corrective and preventive action is dated, has an owner, and is checked at the next quarterly audit. An open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a missed month, a hazardous-material spill in a building store, or a change to extra-security areas."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who walk monthly rounds, inspect devices, handle building chemicals, condemn unused material, or hold extra-security access are trained against this policy at induction and {D('once a year')} thereafter. Training covers: the monthly walk; not signing a round that was not walked; tagging unused material so it cannot be reused on a patient; labelling chemicals at the point of use; isolation of a failed building circuit; and the split that biomedical-waste colours, blood spills, cytotoxic bench spills and laboratory bench hygiene remain those other programmes.

Staff acknowledgement

I have read this Safety of Patients, Families, Staff and Visitors policy of {HOSPITAL}. I will not sign a monthly round I did not walk. I will not put a condemned item back into a patient bay. I will not use an unlabelled chemical.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/02')}
Issue number: {D('01')}
Version: 2.1 (template test — standard-specific wording; not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}
Number of pages: as printed

Prepared by (designation): {D('Maintenance In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Monthly-round circuit (areas): {BLANK}
Named extra-security areas: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.2 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- National Building Code of India, 2016. Bureau of Indian Standards — building, access and electrical-installation framework as the local authority has applied it; IS 732, IS 3043 and IS 2190 are NBC-pointed practice, not extra disclaimer statutes.
- Gudlavalleti, V. (2018). Challenges in Accessing Health Care for People with Disability in the South Asian Context: A Review. Int J Environ Res Public Health, 15(11), 2366 — disability-access framework.
- Safe Management of Wastes from Health-Care Activities (2nd ed.). World Health Organization (2014) — waste framework only; biomedical-waste colour and authorisation remain the infection-control waste programme.
- Hospital safety index: guide for evaluators – 2nd ed. World Health Organization (2015) — evaluator framework, not a mandated score.
- Aggarwal, R., et al. (2010). Technology as applied to patient safety: an overview. Qual Saf Health Care, 19(Suppl 2), i3-i8 — infrastructure framework.
- Infrastructures to improve patient safety. Health Facilities Management (2015) — framework.
- Internal documents of this hospital: monthly round form; electrical audit; unused-material procedure; hazardous-material inventory; utilities, equipment, gas and fire programmes; infection-control spill and waste programmes; laboratory safety programme; neonatal and vulnerable-adult care policies; incident system."""

DISTRIBUTION = f"""Controlled master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('Maintenance In-Charge')} and the Quality Coordinator.

Copies issued to: staff who walk monthly rounds; the named security or administration lead where extra-security areas are defined; department heads whose areas are on the circuit.

The current version is available to all staff at the {D('engineering office policy file')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

Superseded versions are withdrawn from all points of use on issue of a revision. One dated copy of each is retained by the Quality Coordinator."""

ABBREVIATIONS = """NBC — National Building Code of India, 2016
ELCB — earth-leakage circuit breaker
RCCB — residual-current circuit breaker
CCTV — closed-circuit television
SDS — safety data sheet
PPE — personal protective equipment
CAPA — corrective and preventive action
RCA — root-cause analysis
WHO — World Health Organization
IS — Indian Standard"""

STATUTE_CLAUSE = (
    "the National Building Code of India, 2016, insofar as the local building and fire "
    "authority has applied it to this facility for occupancy, access and electrical-installation safety"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "FMS.2.a",
        "requirement": "Patient-safety devices and infrastructure are installed across the organisation and inspected periodically.",
        "steps": "Section 3; 5.1 Install and inspect patient-safety fabric",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Installed-device list (grab rails, wet-area flooring, window restrictors, call-bell hardware, bed-rail furniture).",
            "Periodic inspection records that touched the device, not a purchase invoice.",
            "Record that fire extinguishers and detection remain the fire programme except as a round finding.",
        ],
    },
    {
        "oe_code": "FMS.2.b",
        "requirement": "The organisation has facilities for the differently-abled.",
        "steps": "Section 3; 5.2 Provide facilities for the differently-abled and keep them usable",
        "responsible": "Maintenance In-Charge",
        "records": [
            "List of facilities actually provided (ramp or lift, accessible toilet, and others defined for this building).",
            "Record that they are kept unblocked.",
            "Failure and restoration record when a facility is blocked or unusable.",
        ],
    },
    {
        "oe_code": "FMS.2.c",
        "requirement": "Operational planning identifies areas which need to have extra security and describes access to different areas in the hospital by staff, patients, and visitors.",
        "steps": "Section 3; 5.3 Identify extra-security areas and describe who may enter",
        "responsible": "Named security or administration lead; Medical Superintendent (accountable)",
        "records": [
            "Extra-security area list.",
            "Written access description for staff, patients and visitors, with the hardware that enforces it.",
            "Incident-file entry for a breach that is also an incident.",
        ],
    },
    {
        "oe_code": "FMS.2.d",
        "requirement": "Facility inspection rounds to ensure safety are conducted at least once a month.",
        "steps": "Section 3; 5.4 Walk the facility inspection round every month",
        "responsible": "Maintenance In-Charge (walk); Medical Superintendent (overdue closures)",
        "records": [
            "Monthly round reports showing a walk of occupied clinical and support spaces.",
            "Closed findings, including those handed to the utilities, equipment, gas or fire programme.",
            "Record of a missed month as a defect.",
            "Incident dual-entry where a finding caused harm.",
        ],
    },
    {
        "oe_code": "FMS.2.e",
        "requirement": "Organisation conducts electrical safety audits for the facility.",
        "steps": "Section 3; 5.5 Audit the electrical installation",
        "responsible": "Named competent auditor; Maintenance In-Charge (isolation until repaired)",
        "records": [
            "Electrical safety audit reports covering earthing, residual-current protection, wet-area sockets and panel lockability.",
            "Isolation-until-repaired records for a failed earth or missing residual-current device.",
            "Competence of the auditor (in-house or licensed contractor) and the defined interval.",
        ],
    },
    {
        "oe_code": "FMS.2.f",
        "requirement": "There is a procedure which addresses the identification and disposal of material(s) not in use in the organisation.",
        "steps": "Section 3; 5.6 Identify and dispose of material not in use",
        "responsible": "Maintenance In-Charge; equipment programme for strike-off when the item is equipment",
        "records": [
            "Written unused-material procedure (tag, location, date, owner, condemnation, quarantine, disposal or sale).",
            "Sample tagged items that left the clinical floor.",
            "Equipment-programme strike-off when the item is equipment.",
            "Record that biomedical-waste colours remain the infection-control waste programme.",
        ],
    },
    {
        "oe_code": "FMS.2.g",
        "requirement": "Hazardous materials are identified and used safely within the organisation.",
        "steps": "Section 3; 5.7 Identify hazardous materials and use them safely",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Hazardous-material inventory of classes this hospital actually holds, with recorded absences for classes not held.",
            "Labels and segregation at the point of use.",
            "PPE and spill method for building chemical, mercury and fuel, distinct from blood and cytotoxic bench spills.",
            "Induction or briefing of staff who may use which material.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.2 v2.1 uses the FMS.5 v2.2 section skeleton.
Wording is this standard's seven OEs and v1 substance. Fire-cloned stop-work,
Night Duty Officer as emergency command, Floor Fire Warden, and "roles are
titles not vacancies" do not appear.

Technical substance retained from v1: monthly round floor is in the
requirement; unused material is not biomedical waste; building hazmat is not
blood, cytotoxic or lab-bench; matching and observation stay care policies;
Gudlavalleti; Hospital Safety Index is not a mandated score; NBC 2016 as
applied; IS 732/3043/2190 NBC-pointed not P2.

Length follows the seven OEs (seven 5.x subsections). Stop-work is the
genuine do-not-proceed acts for condemned reuse, unlabelled chemical, failed
circuit left live, and an unwalked round. Disclaimer P2 NBC 2016 as locally
applied. No SQL. Status remains draft.
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
        "subtitle": "Standards for facility safety of people in the building.",
        "footer_label": "Facility safety of patients, staff and visitors",
        "prepared_by": "«Maintenance In-Charge»",
        "acknowledgement_note": "The Maintenance In-Charge holds signed acknowledgements of staff who walk rounds, handle building chemicals, or condemn unused material, with the induction record.",
        "control_extra_rows": [
            ["Monthly-round circuit", "«________»", "Extra-security areas", "«________»"],
        ],
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
