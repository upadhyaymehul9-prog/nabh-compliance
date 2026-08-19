# -*- coding: utf-8 -*-
"""FMS.1 v2 — planned facilities, utilities and environment-friendly measures.

Shape follows FMS.5 v2.2 (section list and order only). Wording is this
standard's OEs and v1 substance. Does not overwrite fms1_draft.json or
build_fms1.py. No SQL. No Supabase insert.

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

STANDARD_CODE = "FMS.1"
CHAPTER = "FMS"
OE_CODES = ["FMS.1.a", "FMS.1.b", "FMS.1.c", "FMS.1.d", "FMS.1.e", "FMS.1.f"]
POLICY_TITLE = "Planned Facilities, Utilities and Environment-Friendly Measures"
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
        "description": "Same section skeleton as FMS.5 v2.2; wording rebuilt from FMS.1 OEs and v1. Not an approved master.",
    },
]

PURPOSE = f"""This policy governs how {HOSPITAL} matches built space to the services it actually offers, holds the as-built drawings the occupancy required, posts wayfinding patients and families can follow, keeps potable water and electricity available round the clock, proves that alternate electricity and water work under load, and runs named energy-efficient and environment-friendly initiatives.

It is the planned-operation method for the building and its utilities. It is not a consultant drawing set, a generator-vendor manual, a green-hospital certification application, or a substitute for the occupancy conditions the local building authority issued for this site.

Editable defaults in this document are marked {D('like this')}. A hospital that adopts the default keeps the wording. A hospital that needs a different owner, interval or arrangement replaces the marked text before issue. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """A tap that should serve a patient and a circuit that should serve care are live at 03:00. A drawing matches the floor. A green poster is not an initiative."""

SCOPE = f"""This policy applies to the physical facilities of {HOSPITAL} and to the people who plan space, hold drawings, post wayfinding, operate potable-water and electrical systems and their backups, and run this year's energy and environment initiatives.

It covers: appropriateness of facilities and space to the defined scope of services; as-built and updated drawings; internal and external sign postings; round-the-clock potable water and electricity; alternate electricity and water sources and the tests that prove they work; and energy-efficient / environment-friendly initiatives.

It does not govern patient-safety devices, monthly facility inspection rounds, electrical-installation audits, unused-material disposal, or building hazardous materials — those belong to the facility-safety programme. It does not govern medical-equipment preventive maintenance, medical gases, or fire and non-fire emergency plans. A power or water failure that is declared an emergency is handed to the fire-and-non-fire programme; routine backup testing stays here.

The defined scope of services is the service-directory programme. This policy owns that the built space can hold those services. A service the directory does not provide is a recorded absence, not another hospital's floor plate.

Radiation, restricted-area, pregnancy-caution and PC-PNDT notices are the laboratory and imaging safety programme. This policy owns hospital-wide wayfinding. Emergency-exit display is the fire programme; those sheets must be consistent with wayfinding but are not this posting counted twice.

A diesel generator, pump or UPS that is building plant is this policy. A ventilator or steriliser is the equipment programme. Steriliser validation as a reprocessing act stays the infection-control sterilisation programme.

Piped medical-gas plant electricity or water may be essential circuits here; the gas programme remains the gas programme.

Biomedical-waste colour, transport and authorisation stay the infection-control waste programme. Kitchen food-safety stays that waste/food programme. Patient-facing expected cost is not a facilities tariff.

Indian Public Health Standards 2022 and the National Building Code of India, 2016, are space and building-code frameworks as the local authority applied them. They are not a NABH bed-count, occupancy-subdivision or sprinkler mandate for every small hospital.

Coulliette and Arduino is the dialysis-water framework only if dialysis is in the service directory. If dialysis is not provided, that is a recorded absence, not a copied reverse-osmosis SOP."""

POLICY_STATEMENT = f"""{HOSPITAL} matches waiting, clinical, diagnostic, utility, storage and staff space to the services it actually runs. A corridor is not a ward. A sluice is not a sterile store. A service the directory does not provide is recorded as not offered.

{HOSPITAL} holds the as-built drawing set the local building and fire authority required for this occupancy under the National Building Code of India, 2016, as applied, and updates that set when the building or a major service run changes. A brochure plan, or a consultant drawing never marked as-built, is not that set.

{HOSPITAL} posts internal and external wayfinding a first-time family can follow to the entrance, registration, toilets, emergency, lifts, wards and the way out, in {D('Gujarati and English')}. Radiation and PC-PNDT notices are not this wayfinding. Fire-exit plans are not this wayfinding.

{HOSPITAL} keeps potable water and electricity available round the clock at the points of use that serve patients and care, including night and holiday, not only at the morning check.

{HOSPITAL} provides alternate electricity and water for failure or shortage, and tests that they actually work at {D('monthly')} frequency: a loaded run of the essential-circuit list, not a no-load crank; tank-to-tap movement or pump auto-start, not a sealed tanker memorandum with no night number.

{HOSPITAL} takes named energy-efficient and environment-friendly initiatives with an owner, a baseline and a result. Dhillon (2015) is the green-hospital framework, not a rating mandate and not authority to cut clinical ventilation below what the services require.

{HOSPITAL} does not treat a generator that is cranked but never takes essential-circuit load, a drawing that does not match the built floor, or a green-hospital poster with no measured initiative, as that duty."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no operational exception and no "until the vendor comes" exception.

1. Using a corridor as a ward, a sluice as a sterile store, or another hospital's floor plate for a service this hospital's directory does not provide.
2. Using a brochure floor plan, or a consultant drawing never marked as-built, as the occupancy set.
3. Occupying a newly altered floor before the controlled as-built set has been updated for that change.
4. Offering radiation, restricted-area, pregnancy-caution or PC-PNDT notices, or the fire-exit display, as the wayfinding system.
5. Treating a morning check as round-the-clock availability. A tap that should serve patients and a circuit that should serve care must be live at night and on a holiday.
6. Drawing drinking or clinical-wash water from a tap that failed its last quality test, or from a point labelled non-potable.
7. Treating a no-load generator crank, a UPS that has not been discharge-tested, a seized tank outlet, or a tanker memorandum with no night number, as a functioning backup test.
8. Signing a backup-test sheet for a generator that did not take the essential-circuit list, or for a water backup that did not move water to a point of use.
9. Shutting clinical ventilation, HVAC or essential circuits to show an energy saving.
10. Offering a green-hospital poster, a single LED retrofit as the whole programme, an unused rooftop array, an energy audit that produced no action, or a tree-planting photograph, as this year's initiative.
11. Rewriting biomedical-waste colours, transport or authorisation as an environment-friendly measure. That waste stream stays the infection-control waste programme.

A person who finds a dry clinical tap, a dark essential circuit, a drawing that does not match the floor, or a backup test being signed without load, reports it the same shift to the {D('Maintenance In-Charge')}. If that person is not on site, the report goes to the {D('named person on the after-hours facilities roster')}."""

PROCEDURE_STEPS = [
f"""5.1 Match built space to the services we offer

The defined scope of services is the service directory. This section is the built match: waiting, clinical, diagnostic, utility, storage and staff spaces this hospital actually runs can physically hold those services.

How appropriateness is judged — against that directory and, as frameworks, Indian Public Health Standards 2022 and NBC 2016 occupancy as the local authority applied it — is held by the {D('Maintenance In-Charge')} as a dated space-to-scope record. A mismatch is reported to the Medical Superintendent. A service the directory does not provide is a recorded absence, not a copied intensive-care floor plate.

When a service is added or withdrawn, the space record is updated before the service is offered or the room is re-used. Clinical heads confirm that the space still matches the services they actually run.""",

f"""5.2 Hold the as-built drawings and update them

NBC 2016 is the Indian building-code framework the local building and fire authority typically uses for occupancy, means of egress and services drawings. This hospital holds the as-built set that occupancy and that authority actually required.

The controlled set includes, as this occupancy required: architectural; structural; electrical single-line; plumbing and water; fire and detection sheets the fire programme will use; and medical-gas sheets the gas programme will use if a piped system exists. Those other programmes use working copies. This policy holds the master.

The {D('Maintenance In-Charge')} updates the set when the building or a major service run changes, before the altered floor is reoccupied. A brochure floor plan is not this set.""",

f"""5.3 Post internal and external wayfinding

Wayfinding is how a first-time family finds the entrance, registration, toilets, emergency, lifts, wards and the way out, in language they actually read. Languages and scripts on the public route are {D('Gujarati and English')}. A visitor who cannot read the majority language is still directed by {D('pictograms at entrance, registration, emergency, toilets and exit')}.

Radiation, restricted-area, pregnancy-caution and PC-PNDT notices are not this system. Fire-exit plans are the fire programme; they must not contradict these signs.

The {D('Maintenance In-Charge')} inspects faded, contradictory or missing signs {D('monthly')}. Department in-charges do not cover a public sign with a clinical notice.""",

f"""5.4 Keep potable water and electricity available round the clock

Availability is the duty: a tap that should serve patients and a circuit that should serve care are live at 03:00, not only at the morning check.

Potable water. Points of use this hospital has defined for drinking, clinical wash, kitchen (as the food programme uses water, not as this document rewriting that programme), CSSD if present, and dialysis if present, actually deliver water when needed. A roof tank that is full on paper while the operating-theatre scrub is dry because a valve is shut is a failure of this policy.

Quality testing is not a second NABH interval invented here. WHO Guidelines for Drinking-water Quality, 4th edition, is the framework for which parameters are tested, at which points, and how often. Local values: parameters {BLANK}; sample points {BLANK}; interval {D('as WHO GDWQ 4th edition requires for this supply')}. Dialysis water, if dialysis is in the service directory, uses Coulliette and Arduino as the haemodialysis-water framework; if dialysis is not provided, that is a recorded absence, not a copied reverse-osmosis SOP. Legionella control for aerosolising systems this hospital actually runs (cooling towers, decorative fountains, unused dead-legs) is {D('the written stagnant-water and Legionella control for systems this hospital actually runs')}, or a recorded absence if none of those systems exist.

Electricity. Essential clinical and life-safety circuits — at minimum the areas this hospital actually runs that cannot wait for restoration: emergency; operating theatre, labour, intensive or high-dependency care, nursery and blood bank if those services exist; ventilators and their compressors; emergency lighting; fire detection; and medical-gas plant or manifold alarms — remain energised. A live incoming meter with a dark theatre because a changeover never closed is a failure of this policy.

The {D('Maintenance In-Charge')} watches availability, including night and holiday. An interruption is recorded the same shift. Restoration is the same shift unless the Medical Superintendent has accepted a dated compensating arrangement. This policy does not invent a NABH minutes-to-restore clock. After hours, the {D('named person on the after-hours facilities roster')} is who a night nurse calls when a tap is dry or an essential circuit is dark.""",

f"""5.5 Test backup electricity and water so they actually work

When incoming electricity fails or is shed, the backup that will carry the essential circuits named in 5.4 is: the diesel generator; UPS or inverter for circuits that cannot tolerate a start delay (ventilators, monitors, lights over an open table); and any automatic mains-failure changeover this hospital has installed. The failure this test exists to catch is a weekly no-load crank that proves the starter motor, not that the set will take theatre, intensive care and emergency lighting together, or a UPS whose batteries have not been discharge-tested. A start-only test is not a functioning test.

How the loaded test is done: essential-circuit load, not the workshop socket; the {D('Maintenance In-Charge')} present so a changeover failure is seen before a night outage; fuel, coolant and battery condition recorded. Frequency: {D('monthly')}. IS 732 wiring practice and IS 3043 earthing inform how the installation should behave; they are NBC-pointed frameworks, not extra statutes in the disclaimer. Central Electricity Authority electrical-supply regulations are not a numbered FMS chapter reference and are not imported here.

When municipal or borewell water fails or is short, the backup that actually moves water to the points of use in 5.4 is: reserve tanks with working float valves; a second borewell if this hospital has one; a tanker contract that can deliver at night; and pumps that auto-start. A sealed tanker memorandum with no night number, or a tank whose outlet valve has seized, is not backup. The test proves tank-to-tap movement, pump auto-start, or tanker mobilisation. Frequency: {D('monthly')}.

A utility failure that is declared an emergency is handed to the fire-and-non-fire programme. This section is the test before that night.""",

f"""5.6 Take this year's energy and environment initiatives

Round-the-clock availability and backup testing are 5.4 and 5.5. This section is that the organisation takes initiatives toward using less energy and harming the environment less, while still meeting those availability duties.

Dhillon, V. S. (2015), Green Hospital and Climate Change, is the chapter's green-hospital framework. It is not a mandate to hold a named green-building rating, not a pasted energy-audit form, and not authority to reduce clinical ventilation below what this hospital's services require.

Each calendar year the Medical Superintendent names the initiatives in force, the owner, the baseline and the review date. Initiatives this hospital actually runs — measured electricity or fuel use, lighting or HVAC set-back in non-clinical hours, solar if installed, rainwater or condensate reuse if installed, segregation of municipal waste from the biomedical stream, reduction of single-use non-clinical materials — are recorded with a baseline and a result.

An unused rooftop solar array, an energy audit that produced no action, a single LED retrofit offered as the whole programme, or a tree-planting photograph, is not this year's initiative. Clinical ventilation is not reduced below what the services require. Biomedical-waste colour, transport and authorisation stay the infection-control waste programme; environment-friendly hospital here is not a second waste SOP.""",
]

STOP_WORK = f"""A person who is about to do any of the following does not proceed:

- draw drinking or clinical-wash water from a tap that failed its last quality test, or from a point labelled non-potable;
- occupy or continue a procedure in a clinical room whose essential circuit is known dark, unless a compensating UPS or generator supply is already carrying that circuit;
- sign a backup-test sheet for a generator that did not take the essential-circuit list, or for a water backup that did not move water to a point of use;
- shut clinical ventilation or an essential circuit to produce an energy figure.

They isolate the tap or room if they are competent to, leave the test unsigned, and tell the {D('Maintenance In-Charge')} the same shift — or, if that person is not on site, the {D('named person on the after-hours facilities roster')}.

A good-faith refusal to sign a test that did not take load is not a disciplinary matter. The test is not recorded as passed until a loaded run has been seen."""

RESPONSIBILITY = f"""These are the jobs this utilities policy needs. In a small hospital one person may also hold the biomedical or gas-plant lead; they still keep this file as the facilities file, not as a combined fire-and-utilities binder.

Medical Superintendent (head of the institution)
- Accountable that facilities operate as this policy requires.
- Accepts in writing any residual risk while a failed essential utility has a compensating arrangement.
- Names this year's energy and environment initiatives and the owner of each.

{D('Maintenance In-Charge')} (named facilities or engineering lead)
- Holds the space-to-scope record, the controlled as-built set and update log, wayfinding inspection, availability watch, loaded backup tests, and the energy-initiative file.
- Runs the loaded electricity test and the water-movement test.
- Names the {D('named person on the after-hours facilities roster')} who takes a dry-tap or dark-circuit call when the Maintenance In-Charge is not on site.

Clinical heads / department in-charges
- Confirm that space still matches the services they actually run.
- Report a mismatch when a service is added or withdrawn.
- Do not cover public wayfinding with a clinical notice.

Quality Coordinator
- Audits the records in section 8.

Staff who operate plant
- Named on the trained-operator list before they start the generator or operate changeover.
- Do not sign a test they did not see take load.

All staff
- Report a dark essential circuit, a dry clinical tap, a drawing that does not match the floor, or a green poster with no initiative.

A RACI snapshot:

- Space match: Maintenance In-Charge (R); Medical Superintendent (A); clinical heads (C)
- Drawings: Maintenance In-Charge (R/A)
- Wayfinding: Maintenance In-Charge (R/A)
- Availability watch: Maintenance In-Charge (R); after-hours facilities roster (R when the lead is off site); Medical Superintendent (A)
- Loaded backup tests: Maintenance In-Charge (R/A)
- Energy initiatives: named owner (R); Medical Superintendent (A)
- Audit: Quality Coordinator (R); Medical Superintendent (A)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at the plant and the records, not at a binder.

What is monitored each quarter:

- Space still matches the service directory; unused services are recorded as not offered, not given another hospital's floor plate.
- As-built set matches the built hospital and the occupancy the authority actually required; last update is dated.
- Wayfinding still directs a first-time family; it is not a radiation notice or a fire-exit display counted twice.
- Availability records cover night and holiday, not only a morning check.
- Last loaded electricity test took the essential-circuit list; last water test moved water to a point of use. A no-load crank is a finding.
- This year's energy file has a named owner, a baseline and a result, not a poster. Clinical ventilation was not cut to show a saving.
- Dialysis-water method exists only if dialysis is in the service directory.
- Biomedical-waste colours were left with the infection-control waste programme.

Any non-conformity is a finding. The Maintenance In-Charge owns the corrective action for plant, drawings and tests. The named initiative owner owns the corrective action for an energy file with no result. Root-cause analysis is required when: a backup test fails under load; an essential circuit is found dark after hours; a clinical tap is found dry after hours; a drawing does not match the floor; or an energy action cut clinical ventilation.

Corrective and preventive action is dated, has an owner, and is checked at the next quarterly audit. An open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a failed loaded test, a change to the service directory, or a building or major-service change that should have updated the as-built set."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who operate plant, post signs, or whose department space must match the service directory are trained against this policy at induction and {D('once a year')} thereafter. Training covers: reporting a dark circuit or dry tap; the public wayfinding route; not signing a backup test that did not take load; and the non-negotiable rules. Staff who may start the generator or operate changeover are named on a trained-operator list held by the Maintenance In-Charge.

Staff acknowledgement

I have read this Planned Facilities, Utilities and Environment-Friendly Measures policy of {HOSPITAL}. I will not draw drinking or clinical-wash water from a failed or non-potable tap. I will not sign a backup-test sheet for a generator that did not take the essential-circuit list. I will not shut clinical ventilation to show an energy saving.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/01')}
Issue number: {D('01')}
Version: 2.1 (template test — standard-specific wording; not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}
Number of pages: as printed

Prepared by (designation): {D('Maintenance In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Dialysis in the service directory: {D('no — recorded absence')} / {BLANK} if yes
After-hours facilities roster (name or role): {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.1 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- National Building Code of India, 2016. Bureau of Indian Standards — occupancy, services and as-built drawing framework as the local building and fire authority has applied it to this facility; not a universal sprinkler or bed-count mandate.
- IS 732 — wiring practice; IS 3043 — earthing (NBC-pointed frameworks, not extra disclaimer statutes).
- Guidelines for Drinking-water Quality (4th Edition). World Health Organization (2011) — potable-water quality-testing framework, not a pasted protocol or a NABH interval.
- Coulliette, A. D., & Arduino, M. J. (2015). Hemodialysis and Water Quality. Semin Dial, 26(4), 427-438 — dialysis-water framework only if dialysis is in the service directory.
- Dhillon, V. S. (2015). Green Hospital and Climate Change: Their Interrelationship and the Way Forward. JOURNAL OF CLINICAL AND DIAGNOSTIC RESEARCH — energy-efficiency framework, not a named rating mandate.
- Indian Public Health Standards. (2022). National Health Mission — space-planning framework, not a NABH bed-count mandate.
- Internal documents of this hospital: service directory; as-built drawing set; wayfinding; potable-water and electrical records; backup-test records; energy-initiative file; facility-safety, equipment, medical-gas and fire programmes; infection-control waste programme."""

DISTRIBUTION = f"""Controlled master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('Maintenance In-Charge')} and the Quality Coordinator.

Copies issued to: engineering and facilities staff who operate utilities and backups; department heads whose space must match the service directory.

The current version is available to all staff at the {D('engineering office policy file')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

Superseded versions are withdrawn from all points of use on issue of a revision. One dated copy of each is retained by the Quality Coordinator."""

ABBREVIATIONS = """NBC — National Building Code of India, 2016
DG — diesel generator
UPS — uninterruptible power supply
IPHS — Indian Public Health Standards
GDWQ — WHO Guidelines for Drinking-water Quality
WHO — World Health Organization
MGPS — medical gas pipeline system
RO — reverse osmosis
CSSD — central sterile supply department
CAPA — corrective and preventive action
RCA — root-cause analysis
HVAC — heating, ventilation and air-conditioning"""

STATUTE_CLAUSE = (
    "the National Building Code of India, 2016, insofar as the local building and fire "
    "authority has applied it to this facility through occupancy, building permission and "
    "as-built drawing requirements"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "FMS.1.a",
        "requirement": "Facilities and space provisions are appropriate to the scope of services.",
        "steps": "Section 3; 5.1 Match built space to the services we offer",
        "responsible": "Medical Superintendent (accountable); Maintenance In-Charge (space record); clinical heads (confirm)",
        "records": [
            "Dated space-to-scope record against the service directory.",
            "Recorded absences for services not offered.",
            "Report of a mismatch to the Medical Superintendent.",
            "Update of the space record when a service is added or withdrawn.",
        ],
    },
    {
        "oe_code": "FMS.1.b",
        "requirement": "As-built and updated drawings are maintained as per statutory requirements.",
        "steps": "Section 3; 5.2 Hold the as-built drawings and update them",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Controlled as-built set the occupancy actually required.",
            "Update log after a building or major-service change.",
            "Working copies of fire sheets issued to the fire programme, and of medical-gas sheets to the gas programme if piped, without creating a second master.",
        ],
    },
    {
        "oe_code": "FMS.1.c",
        "requirement": "There are internal and external sign postings in the organisation in a manner understood by the patient, families and community.",
        "steps": "Section 3; 5.3 Post internal and external wayfinding",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Languages and pictograms as issued.",
            "Monthly wayfinding inspection for faded, contradictory or missing signs.",
            "Record that radiation / PC-PNDT notices and fire-exit display are not counted as this posting.",
        ],
    },
    {
        "oe_code": "FMS.1.d",
        "requirement": "Potable water and electricity are available round the clock.",
        "steps": "Section 3; 5.4 Keep potable water and electricity available round the clock",
        "responsible": "Maintenance In-Charge; after-hours facilities roster when the lead is off site",
        "records": [
            "Availability records covering night and holiday.",
            "Essential-circuit list actually energised.",
            "WHO GDWQ quality-test records at the defined parameters, points and interval.",
            "Dialysis-water method, or a recorded absence if dialysis is not in the service directory.",
            "Legionella / stagnant-water control for systems actually run, or a recorded absence if none exist.",
            "After-hours facilities roster.",
        ],
    },
    {
        "oe_code": "FMS.1.e",
        "requirement": "Alternate sources for electricity and water are provided as a backup for any failure/shortage and their functioning is tested at a predefined frequency.",
        "steps": "Section 3; 5.5 Test backup electricity and water so they actually work",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Named alternate electricity and water sources.",
            "Loaded essential-circuit test records at the predefined frequency, with fuel, coolant and battery condition.",
            "Tank-to-tap, pump auto-start, or tanker-mobilisation records at the predefined frequency.",
            "Trained-operator list for generator start and changeover.",
        ],
    },
    {
        "oe_code": "FMS.1.f",
        "requirement": "The organisation takes initiatives towards an energy-efficient and environment friendly hospital.",
        "steps": "Section 3; 5.6 Take this year's energy and environment initiatives",
        "responsible": "Medical Superintendent (accountable); named owner of each initiative",
        "records": [
            "This year's named initiatives, owner, baseline and review date.",
            "Measured result against the baseline.",
            "Record that clinical ventilation was not cut to show a saving.",
            "Record that biomedical-waste colours remain the infection-control waste programme.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.1 v2.1 uses the FMS.5 v2.2 section skeleton.
Wording is this standard's six OEs and v1 substance. Fire-cloned stop-work,
Night Duty Officer as emergency command, Floor Fire Warden, and "roles are
titles not vacancies" do not appear.

Technical substance retained from v1: NBC 2016 as-applied; WHO GDWQ 4th
edition; Coulliette & Arduino only if dialysis exists; Dhillon 2015 as
framework not a rating; IPHS 2022 space framework; IS 732/IS 3043 NBC-pointed
not P2; loaded test not no-load crank; energy initiative not a poster; BMW
colours stay HIC.3.

Length follows the six OEs (six 5.x subsections). Stop-work is the genuine
do-not-proceed acts for a failed tap, a dark essential circuit, an unsigned
unloaded test, and cutting clinical ventilation. Disclaimer P2 NBC 2016 as
locally applied. No SQL. Status remains draft.
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
        "doc_no": "«FMS/POL/01»",
        "subtitle": "Standards for planned space, utilities and measured energy initiatives.",
        "footer_label": "Planned facilities and utilities",
        "prepared_by": "«Maintenance In-Charge»",
        "acknowledgement_note": "The Maintenance In-Charge holds signed acknowledgements of plant operators and department heads with the induction record. Staff who start the generator or operate changeover are named on the trained-operator list.",
        "control_extra_rows": [
            ["Dialysis in directory", "«no — recorded absence»", "After-hours facilities roster", "«________»"],
        ],
    }
    md = verify_shape(
        draft,
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    emit_v2(draft, "fms1_v2_draft.json", "FMS.1_v2_preview.md", md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
