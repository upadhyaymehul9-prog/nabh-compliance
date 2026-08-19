# -*- coding: utf-8 -*-
"""FMS.1 v2 — planned facilities, utilities and environment-friendly measures.

Shape follows FMS.5 v2.2 (section list and order only). Wording is this
standard's OEs and v1 substance, in plain English. Does not overwrite
fms1_draft.json or build_fms1.py. No SQL. No Supabase insert.

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
VERSION = "2.2"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "First v2 shape pass (withdrawn: fire-cloned wording).",
    },
    {
        "version": "2.1",
        "date": "19-08-2026",
        "description": "Same section skeleton as FMS.5 v2.2; wording rebuilt from FMS.1 OEs and v1.",
    },
    {
        "version": "2.2",
        "date": "19-08-2026",
        "description": "Plain-English rewrite. Same rules, facts and intervals. Not an approved master.",
    },
]

PURPOSE = f"""This policy says how {HOSPITAL} plans its rooms and plant.

It covers six jobs:

- match the built space to the services this hospital actually offers;
- keep the as-built drawings (drawings that show the building as it was actually built);
- put up signs that patients and families can follow;
- keep drinking water and electricity available day and night;
- prove that backup power and backup water work;
- run named energy-saving and environment projects this year.

This is the method for running the building and its utilities. It is not a consultant's drawing set. It is not a generator-vendor manual. It is not an application for a green-hospital certificate. It does not replace the occupancy conditions the local building authority issued for this site.

Words marked {D('like this')} are defaults a small hospital can keep. Change the marked text before issue if this hospital needs a different owner, interval or arrangement. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SAFETY_OBJECTIVE = """Drinking water and power for care must work at 3 a.m. The drawing must match the building. A green poster is not an energy project."""

SCOPE = f"""This policy applies to the buildings of {HOSPITAL}. It also applies to the people who plan space, keep drawings, put up signs, run water and electrical systems and their backups, and run this year's energy and environment projects.

It covers:

- whether rooms and facilities fit the services this hospital offers;
- as-built drawings, and updates when the building changes;
- signs inside and outside the building;
- drinking water and electricity available day and night;
- backup electricity and backup water, and the tests that prove they work;
- energy-saving and environment-friendly projects.

It does not cover grab rails, monthly safety walks, electrical-installation audits, unused items, or building chemicals. Those belong to the facility-safety policy.

It does not cover medical-equipment maintenance. It does not cover medical gases. It does not cover fire and non-fire emergency plans.

If a power or water failure is declared an emergency, the fire-and-non-fire policy takes over. Routine backup testing stays here.

The list of services this hospital offers sits in the service-directory policy. This policy checks that the built space can hold those services. If the directory does not list a service, write down that this hospital does not offer it. Do not copy another hospital's intensive-care floor layout for a service this hospital does not run.

Radiation signs, restricted-area signs, pregnancy-caution signs and Pre-Conception and Pre-Natal Diagnostic Techniques (PC-PNDT) notices belong to the laboratory and imaging safety policy. This policy covers hospital-wide direction signs. Emergency-exit plans belong to the fire policy. Those exit plans must not contradict the direction signs. They are not a substitute for the direction signs.

A diesel generator (DG), a pump, or an uninterruptible power supply (UPS — a battery backup that keeps selected circuits live while the generator starts) that is building plant belongs here. A ventilator or a steriliser belongs to the equipment policy. Checking that a steriliser cycle actually sterilised the load belongs to the infection-control sterilisation policy.

Electricity or water that feeds a piped medical-gas plant may sit on this policy's essential-circuit list. How medical gases are bought, stored and used belongs to the gas policy.

Biomedical-waste colours, transport and authorisation belong to the infection-control waste policy. Kitchen food safety belongs to that waste and food policy. What a patient is told about cost is not a facilities charge sheet.

Indian Public Health Standards (IPHS) 2022 and the National Building Code of India, 2016 (NBC 2016) are guides for space and building work, as the local authority applied them to this site. They do not set a NABH bed count, occupancy type, or sprinkler rule for every small hospital.

Coulliette and Arduino is the dialysis-water guide only if dialysis is on the service directory. If this hospital does not provide dialysis, write that down. Do not copy a reverse-osmosis (RO) plant procedure from another hospital."""

POLICY_STATEMENT = f"""{HOSPITAL} matches waiting rooms, clinical rooms, diagnostic rooms, utility rooms, stores and staff rooms to the services it actually runs. A corridor is not a ward. A sluice is not a sterile store. If the service directory does not list a service, record that it is not offered.

{HOSPITAL} keeps the as-built drawing set the local building and fire authority required for this occupancy under NBC 2016, as applied to this site. The set is updated when the building or a major service run changes. A brochure floor plan is not that set. A consultant drawing that was never marked as-built is not that set.

{HOSPITAL} puts up direction signs inside and outside so a family visiting for the first time can find the entrance, registration, toilets, emergency, lifts, wards and the way out. Signs are in {D('Gujarati and English')}. Radiation and PC-PNDT notices are not these direction signs. Fire-exit plans are not these direction signs.

{HOSPITAL} keeps drinking water and electricity available day and night at the taps and circuits that serve patients and care. This includes night and holidays. A morning check is not enough.

{HOSPITAL} provides backup electricity and backup water for a failure or shortage. It tests that they actually work {D('monthly')}. The electricity test is a loaded run of the essential-circuit list (the generator takes the real hospital load, not just a start with no load). The water test is water moving from tank to tap, or a pump that starts on its own. A sealed tanker letter with no night phone number is not a backup test.

{HOSPITAL} runs named energy-saving and environment-friendly projects. Each project has an owner, a starting figure (baseline), and a result. Dhillon (2015) is the green-hospital guide. It is not a rating this hospital must hold. It does not allow cutting clinical ventilation below what the services need.

{HOSPITAL} does not treat these as meeting this policy: a generator that is started but never takes the essential-circuit load; a drawing that does not match the building; a green-hospital poster with no measured project."""

NON_NEGOTIABLES = f"""These acts are banned. There is no operational exception. "Until the vendor comes" is not an exception.

1. Using a corridor as a ward, or a sluice as a sterile store. Copying another hospital's floor layout for a service this hospital's directory does not list.
2. Using a brochure floor plan, or a consultant drawing never marked as-built, as the official occupancy drawing set.
3. Using a newly altered floor before the official as-built drawings have been updated for that change.
4. Using radiation, restricted-area, pregnancy-caution or PC-PNDT notices, or the fire-exit display, as the hospital's direction-sign system.
5. Treating a morning check as proof that water and power work all day and night. A tap that should serve patients, and a circuit that should serve care, must be live at night and on a holiday.
6. Taking drinking water or clinical-wash water from a tap that failed its last quality test, or from a tap labelled not safe to drink (non-potable).
7. Treating any of these as a working backup test: starting the generator with no hospital load; a UPS whose batteries have not been discharge-tested; a tank outlet that will not open; a tanker letter with no night phone number.
8. Signing a backup-test sheet for a generator that did not take the essential-circuit list, or for a water backup that did not move water to a tap or point of use.
9. Switching off clinical ventilation, heating, ventilation and air-conditioning (HVAC), or essential circuits in order to show an energy saving.
10. Treating any of these as this year's energy project: a green-hospital poster; one LED lighting change offered as the whole programme; unused solar panels on the roof; an energy audit that led to no action; a tree-planting photograph.
11. Using biomedical-waste colours, transport or authorisation as an environment-friendly measure. That waste stream stays with the infection-control waste policy.

If you find a dry clinical tap, a dark essential circuit, a drawing that does not match the floor, or a backup test being signed without load, report it the same shift to the {D('Maintenance In-Charge')}. If that person is not on site, report it to the {D('named person on the after-hours facilities roster')}."""

PROCEDURE_STEPS = [
f"""5.1 Match built space to the services we offer

The list of services this hospital offers sits in the service directory. This section checks the built match. Waiting rooms, clinical rooms, diagnostic rooms, utility rooms, stores and staff rooms must be able to hold the services this hospital actually runs.

The {D('Maintenance In-Charge')} keeps a dated record that compares space to the service directory. Indian Public Health Standards 2022 and NBC 2016 occupancy, as the local authority applied them, are guides for that judgement. They are not a NABH bed-count rule.

Report a mismatch to the Medical Superintendent. If the directory does not list a service, write down that this hospital does not offer it. Do not copy another hospital's intensive-care floor layout.

When a service is added or stopped, update the space record before the service is offered or the room is used for something else. Clinical heads confirm that the space still matches the services they actually run.""",

f"""5.2 Hold the as-built drawings and update them

NBC 2016 is the Indian building-code guide the local building and fire authority usually uses for occupancy, escape routes and services drawings. This hospital holds the as-built set that occupancy and that authority actually required.

The official set includes, as this occupancy required: architectural drawings; structural drawings; electrical single-line drawings; plumbing and water drawings; fire and detection sheets the fire policy will use; and medical-gas sheets the gas policy will use if a piped system exists. Those other policies use working copies. This policy holds the master set.

The {D('Maintenance In-Charge')} updates the set when the building or a major service run changes. Update it before people use the altered floor again. A brochure floor plan is not this set.""",

f"""5.3 Post internal and external wayfinding

Wayfinding means direction signs. A family visiting for the first time should be able to find the entrance, registration, toilets, emergency, lifts, wards and the way out, in a language they can read. Languages on the public route are {D('Gujarati and English')}. A visitor who cannot read the majority language is still directed by {D('pictograms at entrance, registration, emergency, toilets and exit')}.

Radiation, restricted-area, pregnancy-caution and PC-PNDT notices are not this sign system. Fire-exit plans belong to the fire policy. They must not contradict these signs.

The {D('Maintenance In-Charge')} checks faded, contradictory or missing signs {D('monthly')}. Department in-charges must not cover a public sign with a clinical notice.""",

f"""5.4 Keep potable water and electricity available round the clock

Potable water means water that is safe to drink. Availability means a tap that should serve patients, and a circuit that should serve care, work at 3 a.m. A morning check is not enough.

Drinking water, clinical-wash water, kitchen water (as the food policy uses it — this policy does not rewrite that policy), the central sterile supply department (CSSD) if present, and dialysis if present, must actually deliver water when needed. A roof tank that is full on paper while the operating-theatre scrub is dry because a valve is shut is a failure of this policy.

Water-quality testing is not a second NABH timetable invented here. The World Health Organization (WHO) Guidelines for Drinking-water Quality, 4th edition (GDWQ), is the guide for which tests are done, at which taps, and how often. Local values: parameters {BLANK}; sample points {BLANK}; interval {D('as WHO GDWQ 4th edition requires for this supply')}.

If dialysis is on the service directory, dialysis water follows Coulliette and Arduino as the haemodialysis-water guide. If dialysis is not provided, write that down. Do not copy an RO-plant procedure.

Legionella (a bacterium that can grow in warm standing water) control applies to spray systems this hospital actually runs, such as cooling towers, decorative fountains, or unused dead-end pipes. The method is {D('the written stagnant-water and Legionella control for systems this hospital actually runs')}. If none of those systems exist, write that down.

Essential clinical and life-safety circuits must stay live. At minimum this covers the areas this hospital actually runs that cannot wait for power to return: emergency; operating theatre, labour, intensive or high-dependency care, nursery and blood bank if those services exist; ventilators and their compressors; emergency lighting; fire detection; and medical-gas plant or manifold alarms. A live incoming meter with a dark theatre because a changeover never closed is a failure of this policy.

The {D('Maintenance In-Charge')} watches availability, including night and holiday. Record an interruption the same shift. Restore it the same shift unless the Medical Superintendent has accepted a dated temporary arrangement. This policy does not invent a NABH minutes-to-restore clock.

After hours, a night nurse calls the {D('named person on the after-hours facilities roster')} when a tap is dry or an essential circuit is dark.""",

f"""5.5 Test backup electricity and water so they actually work

When incoming electricity fails or is cut, backup must carry the essential circuits named in 5.4. Backup is: the diesel generator; UPS or inverter for circuits that cannot wait for the generator to start (ventilators, monitors, lights over an open table); and any automatic mains-failure changeover this hospital has installed.

The test that matters is a loaded test. The generator takes the real essential-circuit list, not a start with no hospital load. A weekly no-load start only proves the starter motor. It does not prove the set will take theatre, intensive care and emergency lighting together. A UPS whose batteries have not been discharge-tested is not a working backup. Starting the engine only is not a working test.

How the loaded test is done: use the essential-circuit load, not the workshop socket. The {D('Maintenance In-Charge')} is present so a changeover failure is seen before a night outage. Record fuel, coolant and battery condition. Frequency: {D('monthly')}.

Indian Standard (IS) 732 (wiring practice) and IS 3043 (earthing) are NBC-pointed guides for how the installation should behave. They are not extra laws in the disclaimer. Central Electricity Authority electrical-supply regulations are not a numbered FMS chapter reference. They are not imported into this policy.

When municipal or borewell water fails or is short, backup must actually move water to the points of use in 5.4. Backup is: reserve tanks with working float valves; a second borewell if this hospital has one; a tanker contract that can deliver at night; and pumps that start on their own. A sealed tanker letter with no night number is not backup. A tank whose outlet valve will not open is not backup.

The water test proves tank-to-tap movement, pump auto-start, or tanker call-out. Frequency: {D('monthly')}.

If a utility failure is declared an emergency, the fire-and-non-fire policy takes over. This section is the test done before that night.""",

f"""5.6 Take this year's energy and environment initiatives

Keeping water and power available, and testing backups, are sections 5.4 and 5.5. This section is separate. The hospital must run projects that use less energy and harm the environment less, without breaking those availability duties.

Dhillon, V. S. (2015), Green Hospital and Climate Change, is this chapter's green-hospital guide. It is not a requirement to hold a named green-building rating. It is not a pasted energy-audit form. It does not allow reducing clinical ventilation below what this hospital's services need.

Each calendar year the Medical Superintendent names the projects in force, the owner, the starting figure and the review date. Record projects this hospital actually runs, with a starting figure and a result. Examples: measured electricity or fuel use; lighting or HVAC set-back in non-clinical hours; solar if installed; rainwater or condensate reuse if installed; keeping ordinary municipal waste out of the biomedical-waste stream; reducing single-use non-clinical materials.

None of these counts as this year's project: unused solar panels on the roof; an energy audit that led to no action; one LED lighting change offered as the whole programme; a tree-planting photograph. Do not reduce clinical ventilation below what the services need.

Biomedical-waste colour, transport and authorisation stay with the infection-control waste policy. An environment-friendly hospital here is not a second waste procedure.""",
]

STOP_WORK = f"""Do not go ahead if you are about to do any of the following:

- take drinking water or clinical-wash water from a tap that failed its last quality test, or from a tap labelled not safe to drink;
- occupy a clinical room, or continue a procedure there, when its essential circuit is known to be dark, unless a UPS or generator supply is already carrying that circuit;
- sign a backup-test sheet for a generator that did not take the essential-circuit list, or for a water backup that did not move water to a tap;
- switch off clinical ventilation or an essential circuit to produce an energy figure.

If you can do so safely, isolate the tap or room. Leave the test unsigned. Tell the {D('Maintenance In-Charge')} the same shift. If that person is not on site, tell the {D('named person on the after-hours facilities roster')}.

Refusing in good faith to sign a test that did not take load is not a disciplinary matter. Do not record the test as passed until a loaded run has been seen."""

RESPONSIBILITY = f"""These are the jobs this utilities policy needs. In a small hospital one person may also be the biomedical or gas-plant lead. They still keep this file as the facilities file. Do not merge it into a combined fire-and-utilities binder.

RACI in the snapshot below means: R = does the work; A = accountable (the person who must make sure it is done); C = consulted.

Medical Superintendent (head of the institution)
- Accountable that facilities operate as this policy requires.
- Accepts in writing any remaining risk while a failed essential utility has a temporary arrangement.
- Names this year's energy and environment projects and the owner of each.

{D('Maintenance In-Charge')} (named facilities or engineering lead)
- Holds the space-to-services record, the official as-built set and update log, direction-sign checks, availability watch, loaded backup tests, and the energy-project file.
- Runs the loaded electricity test and the water-movement test.
- Names the {D('named person on the after-hours facilities roster')} who takes a dry-tap or dark-circuit call when the Maintenance In-Charge is not on site.

Clinical heads / department in-charges
- Confirm that space still matches the services they actually run.
- Report a mismatch when a service is added or stopped.
- Do not cover public direction signs with a clinical notice.

Quality Coordinator
- Audits the records in section 8.

Staff who operate plant
- Must be named on the trained-operator list before they start the generator or operate changeover.
- Do not sign a test they did not see take load.

All staff
- Report a dark essential circuit, a dry clinical tap, a drawing that does not match the floor, or a green poster with no project.

A RACI snapshot:

- Space match: Maintenance In-Charge (R); Medical Superintendent (A); clinical heads (C)
- Drawings: Maintenance In-Charge (R/A)
- Direction signs: Maintenance In-Charge (R/A)
- Availability watch: Maintenance In-Charge (R); after-hours facilities roster (R when the lead is off site); Medical Superintendent (A)
- Loaded backup tests: Maintenance In-Charge (R/A)
- Energy projects: named owner (R); Medical Superintendent (A)
- Audit: Quality Coordinator (R); Medical Superintendent (A)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')} (four times a year). The audit looks at the plant and the records. Looking only at a binder is not enough.

What is checked each quarter:

- Space still matches the service directory. Services not offered are written down as not offered. They are not given another hospital's floor layout.
- The as-built set matches the built hospital and the occupancy the authority actually required. The last update is dated.
- Direction signs still help a family visiting for the first time. They are not a radiation notice or a fire-exit display used as a substitute.
- Availability records cover night and holiday, not only a morning check.
- The last loaded electricity test took the essential-circuit list. The last water test moved water to a point of use. A no-load generator start is a finding.
- This year's energy file has a named owner, a starting figure and a result, not a poster. Clinical ventilation was not cut to show a saving.
- A dialysis-water method exists only if dialysis is on the service directory.
- Biomedical-waste colours were left with the infection-control waste policy.

Any failure to meet this policy is a finding. The Maintenance In-Charge owns the corrective action for plant, drawings and tests. The named project owner owns the corrective action for an energy file with no result.

Root-cause analysis (RCA — finding why something went wrong, not only what went wrong) is required when: a backup test fails under load; an essential circuit is found dark after hours; a clinical tap is found dry after hours; a drawing does not match the floor; or an energy action cut clinical ventilation.

Corrective and preventive action (CAPA — the fix and the step that stops it happening again) is dated, has an owner, and is checked at the next quarterly audit. An open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')} (once a year), and sooner after a failed loaded test, a change to the service directory, or a building or major-service change that should have updated the as-built set."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who operate plant, put up signs, or whose department space must match the service directory are trained on this policy at induction and {D('once a year')} after that. Training covers: reporting a dark circuit or dry tap; the public direction-sign route; not signing a backup test that did not take load; and the banned acts. Staff who may start the generator or operate changeover are named on a trained-operator list held by the Maintenance In-Charge.

Staff acknowledgement

I have read this Planned Facilities, Utilities and Environment-Friendly Measures policy of {HOSPITAL}. I will not take drinking or clinical-wash water from a failed or non-potable tap. I will not sign a backup-test sheet for a generator that did not take the essential-circuit list. I will not switch off clinical ventilation to show an energy saving.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/01')}
Issue number: {D('01')}
Version: 2.2 (template test — plain English; not an approved master)
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

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.1 (this policy is written so those requirements are met in day-to-day work; it is not a commentary on the standard).
- National Building Code of India, 2016. Bureau of Indian Standards — occupancy, services and as-built drawing guide as the local building and fire authority has applied it to this facility; not a universal sprinkler or bed-count rule.
- IS 732 — wiring practice; IS 3043 — earthing (NBC-pointed guides, not extra disclaimer statutes).
- Guidelines for Drinking-water Quality (4th Edition). World Health Organization (2011) — drinking-water quality-testing guide, not a pasted protocol or a NABH interval.
- Coulliette, A. D., & Arduino, M. J. (2015). Hemodialysis and Water Quality. Semin Dial, 26(4), 427-438 — dialysis-water guide only if dialysis is on the service directory.
- Dhillon, V. S. (2015). Green Hospital and Climate Change: Their Interrelationship and the Way Forward. JOURNAL OF CLINICAL AND DIAGNOSTIC RESEARCH — energy-efficiency guide, not a named rating this hospital must hold.
- Indian Public Health Standards. (2022). National Health Mission — space-planning guide, not a NABH bed-count rule.
- Internal documents of this hospital: service directory; as-built drawing set; direction signs; drinking-water and electrical records; backup-test records; energy-project file; facility-safety, equipment, medical-gas and fire policies; infection-control waste policy."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('Maintenance In-Charge')} and the Quality Coordinator.

Copies issued to: engineering and facilities staff who operate utilities and backups; department heads whose space must match the service directory.

The current version is available to all staff at the {D('engineering office policy file')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use. The Quality Coordinator keeps one dated copy of each old version."""

ABBREVIATIONS = """NBC — National Building Code of India, 2016
DG — diesel generator
UPS — uninterruptible power supply
IPHS — Indian Public Health Standards
GDWQ — WHO Guidelines for Drinking-water Quality
WHO — World Health Organization
PC-PNDT — Pre-Conception and Pre-Natal Diagnostic Techniques
MGPS — medical gas pipeline system
RO — reverse osmosis
CSSD — central sterile supply department
CAPA — corrective and preventive action
RCA — root-cause analysis
HVAC — heating, ventilation and air-conditioning
RACI — Responsible, Accountable, Consulted, Informed
IS — Indian Standard"""

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
            "Dated record comparing rooms to the service directory.",
            "Written note that a service is not offered, where it is not on the directory.",
            "Report of a mismatch to the Medical Superintendent.",
            "Update of the space record when a service is added or stopped.",
        ],
    },
    {
        "oe_code": "FMS.1.b",
        "requirement": "As-built and updated drawings are maintained as per statutory requirements.",
        "steps": "Section 3; 5.2 Hold the as-built drawings and update them",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Official as-built drawing set the occupancy actually required.",
            "Update log after a building or major-service change.",
            "Working copies of fire sheets given to the fire policy, and of medical-gas sheets to the gas policy if piped, without creating a second master set.",
        ],
    },
    {
        "oe_code": "FMS.1.c",
        "requirement": "There are internal and external sign postings in the organisation in a manner understood by the patient, families and community.",
        "steps": "Section 3; 5.3 Post internal and external wayfinding",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Languages and pictograms as issued.",
            "Monthly check of faded, contradictory or missing direction signs.",
            "Note that radiation / PC-PNDT notices and the fire-exit display are not counted as these direction signs.",
        ],
    },
    {
        "oe_code": "FMS.1.d",
        "requirement": "Potable water and electricity are available round the clock.",
        "steps": "Section 3; 5.4 Keep potable water and electricity available round the clock",
        "responsible": "Maintenance In-Charge; after-hours facilities roster when the lead is off site",
        "records": [
            "Availability records covering night and holiday.",
            "Essential-circuit list that is actually kept live.",
            "WHO GDWQ quality-test records at the defined parameters, points and interval.",
            "Dialysis-water method, or a written note that dialysis is not on the service directory.",
            "Legionella / stagnant-water control for systems actually run, or a written note that none exist.",
            "After-hours facilities roster.",
        ],
    },
    {
        "oe_code": "FMS.1.e",
        "requirement": "Alternate sources for electricity and water are provided as a backup for any failure/shortage and their functioning is tested at a predefined frequency.",
        "steps": "Section 3; 5.5 Test backup electricity and water so they actually work",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Named backup electricity and water sources.",
            "Loaded essential-circuit test records at the set frequency, with fuel, coolant and battery condition.",
            "Tank-to-tap, pump auto-start, or tanker call-out records at the set frequency.",
            "Trained-operator list for generator start and changeover.",
        ],
    },
    {
        "oe_code": "FMS.1.f",
        "requirement": "The organisation takes initiatives towards an energy-efficient and environment friendly hospital.",
        "steps": "Section 3; 5.6 Take this year's energy and environment initiatives",
        "responsible": "Medical Superintendent (accountable); named owner of each initiative",
        "records": [
            "This year's named projects, owner, starting figure and review date.",
            "Measured result against the starting figure.",
            "Note that clinical ventilation was not cut to show a saving.",
            "Note that biomedical-waste colours remain with the infection-control waste policy.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.1 v2.2 is a plain-English rewrite of v2.1.
Same rules, facts, intervals and statute scoping. No SQL. Status remains draft.
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
        "subtitle": "How this hospital plans space, keeps water and power working, and runs energy projects.",
        "footer_label": "Planned facilities and utilities",
        "prepared_by": "«Maintenance In-Charge»",
        "acknowledgement_note": "The Maintenance In-Charge keeps signed acknowledgements of plant operators and department heads with the induction record. Staff who start the generator or operate changeover are named on the trained-operator list.",
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
