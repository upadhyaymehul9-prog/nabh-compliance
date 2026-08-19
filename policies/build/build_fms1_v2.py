# -*- coding: utf-8 -*-
"""Template-test rebuild of FMS.1 as an adoptable hospital policy.

Does NOT overwrite policies/drafts/fms1_draft.json or build_fms1.py.
Writes policies/drafts/fms1_v2_draft.json only. No SQL. No Supabase insert.
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
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "Template rebuild to FMS.5 v2.2 shape. Not an approved master.",
    },
]

PURPOSE = f"""This policy governs how {HOSPITAL} plans its buildings and space, holds the drawings the occupancy actually required, directs patients and families through the site, keeps potable water and electricity available around the clock, proves that backup sources work under load, and runs named energy and environment initiatives.

It sets the standards the hospital requires of the people who plan space, operate plant and post signs. It is not a consultant drawing set, a generator-vendor manual, or a green-hospital certification application.

Editable defaults are marked {D('like this')}. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """A tap that should serve a patient and a circuit that should serve care are live at 03:00. A drawing matches the floor. A green poster is not an initiative."""

SCOPE = f"""This policy applies to the buildings and plant of {HOSPITAL} and to the people who plan space, hold drawings, post wayfinding, operate potable-water and electrical systems and their backups, and run this year's energy and environment initiatives.

It covers: space matched to the services the hospital actually offers; the controlled as-built drawing set; internal and external wayfinding; round-the-clock potable water and electricity; alternate electricity and water, tested under load; and measured energy-efficient and environment-friendly initiatives.

It does not govern patient-safety devices, monthly facility rounds, electrical-installation audits, unused-material disposal or building hazardous materials (those are the facility-safety programme). It does not govern medical-equipment PPM (the equipment programme), medical gases (the gas programme), or fire and non-fire emergency plans. A power or water failure that is declared an emergency is handed to the fire-and-non-fire programme; routine backup testing stays here. Biomedical-waste colours stay the infection-control waste programme. Patient-facing expected cost is not a facilities tariff."""

POLICY_STATEMENT = f"""A service listed in the hospital's service directory has the waiting, clinical, diagnostic, utility, storage and staff space it needs. A corridor is not a ward. A sluice is not a sterile store. A service the directory does not provide is recorded as not offered; it is not given another hospital's floor plate. Indian Public Health Standards 2022 and NBC 2016 occupancy, as the local authority applied them, are the space frameworks — not a NABH bed-count mandate.

The controlled as-built set is the set the local building and fire authority required for this occupancy under the National Building Code of India, 2016, as applied: architectural, structural, electrical single-line, plumbing/water, fire/detection (used by the fire programme), and medical-gas sheets if a piped system exists (used by the gas programme). The set is updated when the building or a major service run changes. A brochure plan is not that set.

Wayfinding gets a first-time family to the entrance, registration, toilets, emergency, lifts, wards and the way out, in {D('Gujarati and English')}. Radiation, restricted-area, pregnancy-caution and PC-PNDT notices are the laboratory and imaging safety programme. Fire-exit plans are the fire programme. Those notices are not this wayfinding.

Potable water and electricity are live at the points of use at 03:00, not only at the morning check. Essential circuits — emergency; OT, labour, ICU/HDU, nursery and blood bank if those services exist; ventilators; emergency lighting; fire detection; medical-gas plant or manifold alarms — remain energised. Potable-water quality testing uses WHO Guidelines for Drinking-water Quality, 4th edition, as the framework. Dialysis water, if dialysis is offered, uses Coulliette and Arduino as the haemodialysis-water framework; if dialysis is not offered, that is recorded as not applicable.

Backup electricity is a loaded test of the essential-circuit list — not a weekly no-load crank. Backup water is tank-to-tap movement, pump auto-start, or a tanker that can be mobilised at night. Tests run {D('monthly')}. IS 732 wiring practice and IS 3043 earthing inform how the installation should behave; they are NBC-pointed frameworks, not extra statutes in the disclaimer.

Energy and environment initiatives are named, owned, baselined and reviewed. Dhillon (2015) is the green-hospital framework, not a rating mandate and not authority to cut clinical ventilation. Biomedical-waste colours stay the infection-control waste programme."""

NON_NEGOTIABLES = f"""The following are prohibited.

1. Occupying or using a clinical area whose essential water or electricity is known to have failed, unless a compensating provision is already in place and the Medical Superintendent has accepted the residual risk in writing until restoration.
2. Treating a no-load generator crank, a UPS that has not been discharge-tested, a seized tank outlet, or a tanker memorandum with no night number, as a functioning backup test.
3. Using a brochure floor plan, or a consultant drawing never marked as-built, as the occupancy set.
4. Shutting clinical ventilation, HVAC or essential circuits to show an energy saving.
5. Offering radiation or PC-PNDT notices, or the fire-exit display, as the wayfinding system.

Anyone who sees a prohibited act stops it under the stop-work clause and reports it the same shift to the {D('Maintenance In-Charge')} or, at night, the Night Duty Officer."""

PROCEDURE_STEPS = [
f"""5.1 Space, drawings and wayfinding

The Maintenance In-Charge holds a dated record that the built space matches the service directory: waiting, clinical, diagnostic, utility, storage and staff rooms for every service actually offered. A mismatch is reported to the Medical Superintendent and is not papered over with another hospital's floor plate.

The same person holds the controlled as-built set and the update log. After a building change or a major service run, the set is updated before the floor is reoccupied. Fire sheets are the set the fire programme uses; medical-gas sheets, if piped, are the set the gas programme uses. This policy holds the master.

Wayfinding is inspected {D('monthly')} for faded, contradictory or missing signs. A visitor who cannot read the majority language is still directed: {D('pictograms at entrance, registration, emergency, toilets and exit')}. Staff on induction walk the public route once before they work a night shift.""",

f"""5.2 Round-the-clock water and electricity

Points of use for drinking, clinical wash, kitchen water as the food programme uses it, CSSD if present, and dialysis if present, deliver water when needed. A roof tank that is full on paper while the OT scrub is dry is a failure of this policy.

Essential circuits named in the policy standards stay energised. A live incoming meter with a dark theatre because changeover never closed is a failure of this policy.

The {D('Maintenance In-Charge')} watches availability, including night and holiday, and records every interruption. Restoration is the same shift unless the Medical Superintendent has accepted a dated compensating arrangement. This policy does not invent a NABH minutes-to-restore clock.

Potable-water quality tests follow WHO GDWQ 4th edition at the points and interval that edition requires for this supply. Legionella control applies to aerosolising systems this hospital actually runs (cooling towers, decorative fountains, unused dead-legs) or is recorded as not applicable if none exist.""",

f"""5.3 Alternate sources — loaded tests

When incoming electricity fails or is shed, the diesel generator, UPS/inverter for circuits that cannot wait for a start (ventilators, monitors, lights over an open table), and automatic mains-failure changeover if installed, take the essential-circuit list. The test is a loaded run of that list, with the Maintenance In-Charge present so a changeover failure is seen before a night outage. Fuel, coolant and battery condition are recorded. Frequency: {D('monthly')}. A start-only test is not this test.

When municipal or borewell water fails or is short, reserve tanks with working float valves, a second borewell if this hospital has one, a tanker contract that can deliver at night, and pumps that auto-start, move water to the points of use. The test proves tank-to-tap movement or pump auto-start. Frequency: {D('monthly')}.

A utility failure that is declared an emergency is the fire-and-non-fire programme. This section is the test before that night.""",

f"""5.4 Energy and environment initiatives

Each calendar year the Medical Superintendent names the initiatives in force, the owner, the baseline and the review date. Initiatives this hospital actually runs — measured electricity or fuel use, lighting or HVAC set-back in non-clinical hours, solar if installed, rainwater or condensate reuse if installed, reduction of single-use non-clinical materials — are recorded with a baseline and a result.

An unused rooftop array, an energy audit with no action, a single LED retrofit offered as the whole programme, or a tree-planting photograph, is not this year's initiative. Clinical ventilation is not reduced below what the services require.

Municipal waste is not mixed into the biomedical-waste stream. Colours, transport and authorisation stay the infection-control waste programme.""",
]

STOP_WORK = f"""Every person on the premises has the authority and the duty to stop an act that breaches a non-negotiable rule: occupying a dark essential circuit or a dry clinical tap without a compensating arrangement; passing a no-load crank as a backup test; shutting clinical ventilation for an energy figure; treating a brochure as the as-built set.

The person says "stop", makes the immediate safe condition they are competent to make, and reports the same shift to the {D('Maintenance In-Charge')} or the Night Duty Officer. There is no retaliation for a good-faith stop-work. A vendor who refuses to stop is required to leave the area."""

RESPONSIBILITY = f"""Roles below are titles, not vacancies. If one person holds two titles in a small hospital, both duties still apply.

Medical Superintendent (Head of the Institution)
- Accountable that this policy is issued, resourced and followed.
- Accepts in writing any residual risk while a failed essential utility has a compensating arrangement.
- Names this year's energy and environment initiatives.

Maintenance In-Charge
- Owns space-to-scope record, controlled drawings, wayfinding inspection, availability watch, loaded backup tests, and the energy-initiative file.
- Holds NBC-as-applied occupancy drawings.

Nursing Superintendent
- Confirms clinical space still matches the services nursing actually runs.
- Ensures wayfinding is not covered by clinical notices.

Night Duty Officer
- Holds the Medical Superintendent's utility-failure authority between {D('20:00 and 08:00')}.
- Records a night interruption and does not treat a dark essential circuit as "until morning."

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring).

Department in-charges
- Report a space mismatch when a service is added or withdrawn.

A RACI snapshot:
- Space match: Maintenance In-Charge (R); Medical Superintendent (A)
- Drawings: Maintenance In-Charge (R/A)
- Wayfinding: Maintenance In-Charge (R); Nursing Superintendent (A for notices)
- Availability: Maintenance In-Charge (R); Night Duty Officer (A at night)
- Loaded tests: Maintenance In-Charge (R/A)
- Energy initiatives: named owner (R); Medical Superintendent (A)
- Stop-work: all staff (R); Maintenance In-Charge (A for restart)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at the plant and the records, not at a binder.

What is monitored each quarter:
- Space still matches the service directory; unused services are recorded as not offered.
- As-built set matches the floor; last update is dated.
- Wayfinding still directs a first-time family; it is not a radiation notice.
- Availability records cover night and holiday.
- Last loaded electricity test took the essential-circuit list; last water test moved water to a point of use.
- This year's energy file has a baseline and a result, not a poster.
- Dialysis-water method exists only if dialysis is offered.

Root-cause analysis is required when: a backup test fails under load; an essential circuit is found dark after hours; a drawing does not match the floor; or an energy action cut clinical ventilation. CAPA is dated, has an owner, and is checked at the next quarterly audit. An open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a failed loaded test or a change to the service directory."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who operate plant, post signs, or work on an occupied floor are trained against this policy at induction and {D('once a year')} thereafter. Training covers: the public route, reporting a dark circuit or dry tap, and the non-negotiable rules. Staff who may start the generator or operate changeover are named on a trained-operator list held by the Maintenance In-Charge.

Staff acknowledgement

I have read this Planned Facilities, Utilities and Environment-Friendly Measures policy of {HOSPITAL}. I will not occupy a clinical area whose essential water or electricity is known to have failed. I will not treat a no-load crank as a backup test. I will not shut clinical ventilation to show an energy saving.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/01')}
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

REFERENCES = """- National Building Code of India, 2016 (Bureau of Indian Standards), occupancy, services and as-built drawing framework as the local building and fire authority has applied it; not a universal sprinkler or bed-count mandate.
- IS 732 — wiring practice; IS 3043 — earthing (NBC-pointed frameworks, not extra disclaimer statutes).
- Guidelines for Drinking-water Quality (4th Edition). World Health Organization (2011) — potable-water quality-testing framework, not a pasted protocol.
- Coulliette, A. D., & Arduino, M. J. (2015). Hemodialysis and Water Quality. Semin Dial — dialysis-water framework only if dialysis is offered.
- Dhillon, V. S. (2015). Green Hospital and Climate Change. J Clin Diagn Res — energy-efficiency framework, not a named rating mandate.
- Indian Public Health Standards (2022). National Health Mission — space-planning framework, not a NABH bed-count mandate.
- NABH Standards for Small Healthcare Organisations, 3rd Edition, Chapter 8, standard FMS.1 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- Internal: service directory; as-built set; wayfinding; availability and backup-test records; energy-initiative file; facility-safety, equipment, gas and fire programmes; infection-control waste programme."""

DISTRIBUTION = f"""Controlled master: office of the Medical Superintendent, {HOSPITAL}, with a working copy held by the Maintenance In-Charge and the Quality Coordinator.

Issued to: Nursing Superintendent, Night Duty Officer folder, department in-charges whose space must match the service directory.

Available to all staff at the {D('Nursing Station policy folder')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

On revision, every displayed copy is withdrawn the same day. One dated superseded copy is retained by the Quality Coordinator."""

ABBREVIATIONS = """NBC — National Building Code of India, 2016
DG — diesel generator
UPS — uninterruptible power supply
IPHS — Indian Public Health Standards
GDWQ — WHO Guidelines for Drinking-water Quality
MGPS — medical gas pipeline system
RO — reverse osmosis
CAPA — corrective and preventive action
RCA — root-cause analysis

Night Duty Officer — the senior doctor or senior nurse holding emergency command overnight
Maintenance In-Charge — the person accountable for drawings, plant and backup tests under this policy"""

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
        "steps": "Section 3; 5.1 Space, drawings and wayfinding",
        "responsible": "Medical Superintendent (accountable); Maintenance In-Charge (space record)",
        "records": [
            "Dated space-to-scope record against the service directory.",
            "Recorded absences for services not offered.",
            "Report of a mismatch to the Medical Superintendent.",
        ],
    },
    {
        "oe_code": "FMS.1.b",
        "requirement": "As-built and updated drawings are maintained as per statutory requirements.",
        "steps": "Section 3; 5.1 Space, drawings and wayfinding",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Controlled as-built set the occupancy actually required.",
            "Update log after a building or major-service change.",
            "Fire and medical-gas sheets issued as working copies, not second masters.",
        ],
    },
    {
        "oe_code": "FMS.1.c",
        "requirement": "There are internal and external sign postings in the organisation in a manner understood by the patient, families and community.",
        "steps": "Section 3; 5.1 Space, drawings and wayfinding",
        "responsible": "Maintenance In-Charge (signs); Nursing Superintendent (notices not covering them)",
        "records": [
            "Monthly wayfinding inspection.",
            "Induction record that staff walked the public route before a first night shift.",
            "Languages and pictograms as issued.",
        ],
    },
    {
        "oe_code": "FMS.1.d",
        "requirement": "Potable water and electricity are available round the clock.",
        "steps": "Section 3; 5.2 Round-the-clock water and electricity",
        "responsible": "Maintenance In-Charge; Night Duty Officer (night interruptions)",
        "records": [
            "Availability records covering night and holiday.",
            "Essential-circuit list actually energised.",
            "WHO GDWQ quality-test records at the defined points.",
            "Dialysis-water method, or a recorded not-applicable if dialysis is not offered.",
        ],
    },
    {
        "oe_code": "FMS.1.e",
        "requirement": "Alternate sources for electricity and water are provided as a backup for any failure/shortage and their functioning is tested at a predefined frequency.",
        "steps": "Section 3; 5.3 Alternate sources — loaded tests",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Named alternate electricity and water sources.",
            "Loaded essential-circuit test records at the defined frequency.",
            "Tank-to-tap or pump auto-start records.",
            "Fuel, coolant and battery condition recorded with each electricity test.",
        ],
    },
    {
        "oe_code": "FMS.1.f",
        "requirement": "The organisation takes initiatives towards an energy-efficient and environment friendly hospital.",
        "steps": "Section 3; 5.4 Energy and environment initiatives",
        "responsible": "Medical Superintendent (accountable); named owner of each initiative",
        "records": [
            "This year's named initiatives, owner, baseline and review date.",
            "Measured result against the baseline.",
            "Record that clinical ventilation was not cut to show a saving.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.1 v2 to the FMS.5 v2.2 shape.

Technical substance retained from v1: NBC 2016 as-applied; WHO GDWQ 4th edition;
Coulliette & Arduino only if dialysis exists; Dhillon 2015 as framework not a
rating; IPHS 2022 space framework; IS 732/IS 3043 NBC-pointed not P2; loaded
test not no-load crank; energy initiative not a poster; BMW colours stay HIC.3.

Length: four 5.x subsections, five non-negotiables. Stop-work included
(failed essential utility; no-load crank as a pass; cutting clinical ventilation).
Disclaimer P2 NBC 2016 as locally applied. No SQL. Status remains draft.
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
        "acknowledgement_note": "The Nursing Superintendent holds signed acknowledgements with the induction record. Staff who start the generator or operate changeover are named on the trained-operator list.",
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
