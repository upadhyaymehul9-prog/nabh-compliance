# -*- coding: utf-8 -*-
"""Builds the SHCO SOP + Records for FMS.1 (Planned Facilities, Utilities
and Environment-Friendly Measures), following the approved FMS.1 master
policy (shco_policy_masters, status='approved') and the structural template
in sop_record_common.py (itself verified against SOP_COP.13.*).

FMS.1 OEs: FMS.1.a-f (6 OEs). doc_required (asterisk) per live
shco_full_oes, queried 2026-10-10: only FMS.1.f is true. FMS.1.a-e are
Tier 2 under the two-tier depth standing rule; FMS.1.f gets full treatment.

Source for every procedure step, reference and the division-of-responsibility
language: the approved FMS.1 master policy's procedure_steps / references_text
/ responsibility columns (read directly from shco_policy_masters on
2026-10-10, not re-derived from the NABH PDF by this script) -- the SOP is a
staff-facing restatement of what the hospital's own approved policy already
says, which is the same relationship SOP_COP.13 has to the approved COP.13
master. No new citation is introduced here beyond what FMS.1 already cites:
NBC 2016, WHO GDWQ 4th ed., Coulliette & Arduino (2015), Dhillon (2015),
IPHS 2022.
"""
from __future__ import annotations

from pathlib import Path

from sop_record_common import ProcedureBlock, RecordSpec, SOPSpec, build_record, build_sop

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "FMS"

FMS1_REFS = [
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). NABH SHCO Accreditation "
    "Programme page. Facility Management and Safety chapter, standard FMS.1.",
    "Bureau of Indian Standards. (2016). National Building Code of India, 2016. "
    "Occupancy, means-of-egress and services-drawing framework as applied by the "
    "local building and fire authority; not a universal mandate.",
    "World Health Organization. (2011). Guidelines for Drinking-water Quality (4th ed.). "
    "Potable-water quality-testing framework, not a pasted protocol or a NABH interval.",
    "Coulliette, A. D., & Arduino, M. J. (2015). Hemodialysis and water quality. "
    "Seminars in Dialysis, 26(4), 427-438. Dialysis-water framework, used only where "
    "dialysis is a service this hospital provides.",
    "Dhillon, V. S. (2015). Green hospital and climate change: Their interrelationship "
    "and the way forward. Journal of Clinical and Diagnostic Research. Energy-efficiency "
    "framework, not a named green-building rating mandate.",
    "National Health Mission. (2022). Indian Public Health Standards. Space-planning "
    "framework, not a NABH bed-count mandate.",
]

SOP = SOPSpec(
    sop_no="SOP-FMS.1",
    title="Planned Facilities, Utilities and Environment-Friendly Measures",
    standard_code_range="FMS.1.a-f",
    what_is_this_for=(
        "This SOP tells facilities, engineering, clinical and quality staff, in one "
        "place, how this hospital keeps its built space matched to what it actually "
        "treats; keeps potable water and electricity live around the clock, including "
        "at night; proves its backup sources actually carry load rather than just "
        "crank once a week; and records real energy and environment initiatives "
        "instead of a green-hospital poster. If you hold drawings, watch utilities, "
        "run a backup test, or own the energy file, this SOP is for you."
    ),
    worked_example=(
        "A night-shift engineer finds the OT scrub sink dry at 2am. This SOP is what "
        "tells them which record to check (the potable-water availability log), what "
        "counts as a failure of this standard (a dry point of use regardless of what "
        "the roof tank shows on paper), and which alternate source should have carried "
        "it -- and that the alternate source's last loaded test, not just its last "
        "no-load crank, is what proves it should have worked."
    ),
    why_nabh_asks=(
        "NABH requires that facilities match the services actually provided, that "
        "potable water and electricity are available round the clock (a Core "
        "requirement), that backup sources exist and are tested at a predefined "
        "frequency, and that the organisation takes real initiatives toward an "
        "energy-efficient and environment-friendly hospital (the chapter's asterisked, "
        "documented-evidence element)."
    ),
    purpose=(
        "To define how «Hospital Name» keeps its physical facilities, drawings, "
        "wayfinding, potable water, electricity and their backups matched to the "
        "services it actually runs, available round the clock, and genuinely tested "
        "-- and how it records real initiatives toward an energy-efficient and "
        "environment-friendly hospital, rather than a certificate on a wall."
    ),
    scope=(
        "Applies to every area of {{HOSPITAL_NAME}} that depends on built space, "
        "potable water or electricity: clinical, diagnostic, utility, storage and "
        "staff areas alike. It does not cover medical and support-service equipment "
        "(FMS.3), medical gases (FMS.4), fire and non-fire emergency response (FMS.5), "
        "radiation/PC-PNDT signage (AAC.6.e), or biomedical-waste colour coding and "
        "transport (HIC.3) -- those remain their own documents and are only pointed "
        "to here where this SOP's steps hand work to them."
    ),
    responsibilities=[
        ("Head of the Institution", "Is accountable that facilities operate as this SOP requires."),
        ("Named Facilities/Engineering Lead",
         "Holds drawings, utility availability and quality-test records, loaded backup-test "
         "records, and the energy-initiative file."),
        ("Clinical Heads",
         "Confirm that built space still matches the services their department actually runs "
         "against the AAC.1 service directory."),
        ("Quality/Accreditation Coordinator",
         "Audits a sample of the records this SOP produces, at the frequency «Hospital to "
         "define» sets, and flags a mismatch rather than filing it."),
        ("All Staff",
         "Treat a dark essential circuit, a dry clinical tap, a drawing that does not match "
         "the floor, or a green poster with no initiative behind it, as defects to report, "
         "not as someone else's problem."),
    ],
    blocks=[
        ProcedureBlock(
            heading="4.1 Facilities and space provisions appropriate to the scope of services (FMS.1.a)",
            why_it_matters=(
                "A floor plate copied from another hospital, or a corridor pressed into "
                "service as a ward, is the failure this step exists to catch -- not the "
                "absence of a plan, but a plan that no longer matches what is actually "
                "treated here."
            ),
            steps=[
                "1. The AAC.1 service directory is the single source of what this hospital "
                "actually provides; this step is the built match to it -- waiting, clinical, "
                "diagnostic, utility, storage and staff space that can physically hold those "
                "services without using a sluice as a sterile store or a corridor as a ward.",
                "2. «Hospital to define how facilities and space are shown to be appropriate "
                "to the defined scope of services», using IPHS 2022 and NBC 2016 occupancy as "
                "frameworks, not bed-count mandates.",
                "3. A service the AAC.1 directory does not list is a recorded absence here, "
                "not a gap to be explained away.",
                "4. Who records a mismatch, and what happens when a service is added to or "
                "withdrawn from the directory, follows the same «Hospital to define» process "
                "as step 2.",
            ],
            technical_sources=[
                "National Health Mission. (2022). Indian Public Health Standards.",
                "Bureau of Indian Standards. (2016). National Building Code of India, 2016.",
            ],
        ),
        ProcedureBlock(
            heading="4.2 As-built and updated drawings maintained per statutory requirements (FMS.1.b)",
            why_it_matters=(
                "A consultant's drawing that was never marked as-built, or a brochure "
                "floor plan, is not this OE -- a building or fire authority inspecting "
                "this hospital needs the set that matches what was actually built and "
                "last changed."
            ),
            steps=[
                "1. The controlled as-built set covers architectural, structural, electrical "
                "single-line, plumbing/water, fire/detection (used by FMS.5) and medical-gas "
                "(used by FMS.4 where a piped system exists) drawings.",
                "2. «Hospital to define the as-built and updated drawings maintained as "
                "statutory and occupancy requirements require», using NBC 2016 as the local "
                "building-and-fire-authority framework.",
                "3. The set is updated whenever the building or a major service run changes "
                "-- an update log, not a one-time filing, is what this step produces.",
                "4. Named facilities lead holds the controlled set; FMS.4 and FMS.5 are users "
                "of specific sheets, not second masters of this record.",
            ],
            technical_sources=[
                "Bureau of Indian Standards. (2016). National Building Code of India, 2016.",
            ],
        ),
        ProcedureBlock(
            heading="4.3 Internal and external sign postings understood by patients, families and the community (FMS.1.c)",
            why_it_matters=(
                "A first-time family that cannot find the entrance, registration, "
                "toilets, lifts, wards or exit -- in a language they actually read -- "
                "is the failure this step exists to catch. A sign nobody can read is a "
                "sign that was never posted."
            ),
            steps=[
                "1. «Hospital to define internal and external sign postings in a manner "
                "understood by patients, families and the community» -- including which "
                "languages and scripts this hospital's actual patient population needs.",
                "2. Wayfinding is inspected for faded, missing or contradictory signs at "
                "the audit interval set in step 7 of this SOP.",
                "3. AAC.6.e radiation/PC-PNDT signage and FMS.5.b emergency exit displays "
                "are separate documents; this step must be consistent with both but does "
                "not duplicate or replace either.",
            ],
        ),
        ProcedureBlock(
            heading="4.4 Potable water and electricity available round the clock (FMS.1.d, Core)",
            why_it_matters=(
                "A roof tank that is full on paper while the OT scrub is dry because a "
                "valve is shut, or a live incoming meter while a theatre is dark because "
                "a changeover never closed, is this OE failing -- availability is judged "
                "at 3am, not only at the morning check."
            ),
            steps=[
                "1. Points of use for drinking, clinical wash, kitchen (owned by HIC.3, "
                "used here only as a utility point), CSSD (if present) and dialysis (if "
                "present) must actually deliver water on demand, day and night.",
                "2. «Hospital to define potable-water quality-testing parameters, sample "
                "points and interval», using WHO GDWQ 4th edition as the testing framework "
                "-- never as a pasted protocol or an invented NABH interval.",
                "3. Dialysis water, only where dialysis is in the AAC.1 directory, follows "
                "«Hospital to define» using Coulliette & Arduino (2015) as the haemodialysis-"
                "water framework; where dialysis is not provided, that is a recorded absence.",
                "4. Essential clinical and life-safety circuits -- at minimum emergency, OT, "
                "labour, ICU/HDU, nursery and blood bank where present, ventilators and their "
                "compressors, emergency lighting, fire detection (FMS.5), and medical-gas "
                "plant/manifold alarms (FMS.4) -- remain energised at all times.",
                "5. «Hospital to define how round-the-clock availability is watched, "
                "recorded and restored», covering night and holiday coverage, not only "
                "daytime checks.",
            ],
            technical_sources=[
                "World Health Organization. (2011). Guidelines for Drinking-water Quality (4th ed.).",
                "Coulliette, A. D., & Arduino, M. J. (2015). Hemodialysis and water quality. "
                "Seminars in Dialysis, 26(4), 427-438.",
            ],
        ),
        ProcedureBlock(
            heading="4.5 Alternate sources for electricity and water, tested at a predefined frequency (FMS.1.e)",
            why_it_matters=(
                "A weekly no-load crank proves the starter motor, not that the "
                "generator will carry theatre, ICU and emergency lighting together -- "
                "and a sealed tanker contract with no night number is not a backup. "
                "A start-only test is not a functioning test."
            ),
            steps=[
                "1. Alternate electricity is the source that carries the essential "
                "circuits named in step 4 above when incoming supply fails or is shed: "
                "diesel generator, UPS/inverter for circuits that cannot tolerate a start "
                "delay, and any automatic mains-failure changeover installed.",
                "2. «Hospital to define the alternate-electricity source, essential-circuit "
                "list, loaded-test method and predefined test frequency» -- a loaded test "
                "under the essential-circuit load, not the workshop socket, with someone "
                "present to see a changeover failure before it becomes a night outage.",
                "3. Alternate water is the source that actually moves water to points of "
                "use when the municipal or borewell supply fails: reserve tanks with "
                "working float valves, a second borewell if available, a tanker contract "
                "that can deliver at night, and pumps that auto-start.",
                "4. «Hospital to define the alternate-water source, the test that proves "
                "water actually moves, and the predefined test frequency» -- a tank-to-tap "
                "movement or pump auto-start record, not a sealed MoU.",
                "5. A utility failure that becomes a declared emergency is handed to FMS.5; "
                "this step is the test that happens before that night, not the emergency "
                "response itself.",
            ],
            technical_sources=[
                "Bureau of Indian Standards. (2016). National Building Code of India, 2016 "
                "(as the framework pointing to IS 732 wiring practice and IS 3043 earthing).",
            ],
        ),
        ProcedureBlock(
            heading="4.6 Energy-efficient and environment-friendly initiatives (FMS.1.f, Excellence, ASTERISKED)",
            why_it_matters=(
                "This is the chapter's documented-evidence anchor -- an assessor will ask "
                "what was actually done, what it measured, and what changed. A filed "
                "electricity bill, a tree-planting photograph, or a single LED retrofit "
                "offered as the whole programme, is not an initiative with a result. "
                "Equally, shutting HVAC in clinical areas in the name of efficiency is not "
                "this OE -- it is FMS.1.d availability failing."
            ),
            steps=[
                "1. «Hospital to define the energy-efficient and environment-friendly "
                "initiatives this hospital actually runs this year», each with a named "
                "owner, a baseline, and a recorded result -- not a poster.",
                "2. Dhillon (2015) is this chapter's green-hospital framework. It is not a "
                "mandate to hold a named green-building rating, not a pasted energy-audit "
                "form, and not authority to reduce clinical ventilation below what the "
                "hospital's services require.",
                "3. Eligible initiatives include measured electricity or fuel use, lighting "
                "or HVAC set-back in non-clinical hours, solar if installed, rainwater or "
                "condensate reuse if installed, segregation of municipal (non-biomedical) "
                "waste, and reduction of single-use non-clinical materials.",
                "4. HIC.3 remains the sole owner of biomedical-waste colour coding, "
                "transport and SPCB compliance -- this step does not restate or duplicate "
                "that SOP.",
                "5. An unused rooftop solar array, or an energy audit that produced no "
                "action, does not satisfy this step. A baseline that changed a measured "
                "result is what the audit at step 7 of this SOP looks for.",
            ],
            technical_sources=[
                "Dhillon, V. S. (2015). Green hospital and climate change: Their "
                "interrelationship and the way forward. Journal of Clinical and "
                "Diagnostic Research.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the FMS.1 Records folder).",
    related_documents=[
        "Policy — Planned Facilities, Utilities and Environment-Friendly Measures (FMS.1)",
        "Hospital's Service Directory (AAC.1)",
        "Hospital's Radiation/PC-PNDT Signage Policy (AAC.6.e)",
        "Hospital's Medical and Support-Service Equipment Programme (FMS.3)",
        "Hospital's Medical Gases, Vacuum and Compressed Air SOP (FMS.4)",
        "Hospital's Fire and Non-Fire Emergencies SOP (FMS.5)",
        "Hospital's Support-Services Infection-Control Policy (HIC.3)",
    ],
    verified_sources=FMS1_REFS,
    review_text=(
        "This SOP is reviewed annually, or sooner if a loaded backup test fails, if "
        "the AAC.1 service directory changes, or if AAC.1, AAC.6, FMS.3, FMS.4, FMS.5 "
        "or HIC.3 that this SOP hands work to are revised."
    ),
)


RECORDS = [
    RecordSpec(
        oe_code="FMS.1.a",
        oe_requirement="Facilities and space provisions are appropriate to the scope of services.",
        record_title="FMS.1 Record 1 — Space-to-service-directory alignment record",
        what_is_this=(
            "A record proving the hospital's built space -- waiting, clinical, "
            "diagnostic, utility, storage and staff areas -- actually matches the "
            "services listed in the AAC.1 service directory, not a floor plate copied "
            "from another hospital."
        ),
        real_example=(
            "This hospital's AAC.1 directory lists general medicine, general surgery "
            "and a 10-bed ICU; this record shows each of those services has matching "
            "built space, and that no service is claimed on the directory without a "
            "physical area to deliver it."
        ),
        why_nabh_asks=(
            "NABH requires facilities and space provisions to be appropriate to the "
            "scope of services -- a Commitment requirement, checked against what is "
            "actually treated, not what is advertised."
        ),
        how_to_fill=[
            ("Date of Review", "Date this record was last confirmed."),
            ("Service (per AAC.1)", "Named service from the current AAC.1 directory."),
            ("Matching Built Space", "The actual area(s) that deliver this service."),
            ("Mismatch Found? (Y/N)", "Whether the built space does not match the directory."),
            ("Action If Mismatch", "What was done, or AAC.1 was corrected instead."),
            ("Confirmed By", "Named person holding this record."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). Facility Management "
            "and Safety chapter, standard FMS.1.",
        ],
        column_headers=["Date of Review", "Service (per AAC.1)", "Matching Built Space",
                         "Mismatch Found? (Y/N)", "Action If Mismatch", "Confirmed By"],
        worked_example_row=["01/04/2026", "General Surgery", "OT suite, surgical ward, pre-op bay",
                             "N", "N/A", "Facilities Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.1.b",
        oe_requirement="As-built and updated drawings are maintained as per statutory requirements.",
        record_title="FMS.1 Record 2 — As-built drawing set and update log",
        what_is_this=(
            "A log of the controlled as-built drawing set (architectural, structural, "
            "electrical, plumbing, fire/detection, medical-gas) and every update made "
            "to it after a building or major-service change."
        ),
        real_example=(
            "This hospital adds a new MRI suite; this record shows the architectural "
            "and electrical single-line drawings were updated to as-built status within "
            "the hospital's own defined timeframe after commissioning, not left as the "
            "original consultant drawing."
        ),
        why_nabh_asks=(
            "NABH requires as-built and updated drawings to be maintained as per "
            "statutory requirements -- a Commitment requirement that a brochure floor "
            "plan or an un-updated consultant drawing does not satisfy."
        ),
        how_to_fill=[
            ("Date of Change", "Date the building or service change occurred."),
            ("Drawing Type", "Architectural / structural / electrical / plumbing / fire / medical-gas."),
            ("Change Described", "What changed in the building or service."),
            ("Updated to As-Built? (Y/N)", "Whether the controlled set now reflects the change."),
            ("Date Drawing Updated", "When the as-built update was completed."),
            ("Confirmed By", "Named facilities lead holding the controlled set."),
        ],
        verified_sources=[
            "Bureau of Indian Standards. (2016). National Building Code of India, 2016.",
        ],
        column_headers=["Date of Change", "Drawing Type", "Change Described",
                         "Updated to As-Built? (Y/N)", "Date Drawing Updated", "Confirmed By"],
        worked_example_row=["15/02/2026", "Electrical single-line", "New MRI suite added, dedicated circuit",
                             "Y", "28/02/2026", "Facilities Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.1.c",
        oe_requirement=(
            "There are internal and external sign postings in the organisation in a "
            "manner understood by the patient, families and community."
        ),
        record_title="FMS.1 Record 3 — Wayfinding and signage inspection record",
        what_is_this=(
            "An inspection log confirming internal and external signage is present, "
            "legible, consistent and in the language(s) this hospital's own patient "
            "population actually needs."
        ),
        real_example=(
            "A routine inspection finds the emergency-department sign near the main "
            "gate has faded; this record shows it was found, in which language, and "
            "when it was replaced."
        ),
        why_nabh_asks=(
            "NABH requires signage patients, families and the community can actually "
            "understand -- a Core requirement for safe wayfinding, separate from "
            "radiation/PC-PNDT notices (AAC.6.e) or emergency exit plans (FMS.5.b)."
        ),
        how_to_fill=[
            ("Date of Inspection", "Date signage was inspected."),
            ("Area/Sign Inspected", "Entrance, registration, toilets, lifts, wards, emergency, exit, etc."),
            ("Legible and Understood? (Y/N)", "Whether the sign is legible and in a language the "
             "community reads."),
            ("Defect Found", "Faded, missing, contradictory, or wrong-language sign, if any."),
            ("Action Taken", "What was done to fix a defect."),
            ("Confirmed By", "Named person who inspected."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). Facility Management "
            "and Safety chapter, standard FMS.1.",
        ],
        column_headers=["Date of Inspection", "Area/Sign Inspected", "Legible and Understood? (Y/N)",
                         "Defect Found", "Action Taken", "Confirmed By"],
        worked_example_row=["05/03/2026", "Main gate → Emergency department sign", "N",
                             "Faded lettering, hard to read at night", "Replaced with reflective signage",
                             "Facilities Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.1.d",
        oe_requirement="Potable water and electricity are available round the clock.",
        record_title="FMS.1 Record 4 — Potable water and electricity round-the-clock availability and quality-test record",
        what_is_this=(
            "A record showing potable water and electricity were actually available "
            "at every point of use, including at night, plus the periodic water-"
            "quality test results against the hospital's own defined parameters."
        ),
        real_example=(
            "A night-round check at 2am confirms the OT scrub sink and the ICU "
            "emergency circuit are both live; a quarterly water sample from the "
            "dialysis unit comes back within the hospital's defined limits."
        ),
        why_nabh_asks=(
            "NABH requires potable water and electricity to be available round the "
            "clock -- a Core requirement checked against actual availability, not a "
            "morning-only inspection."
        ),
        how_to_fill=[
            ("Date/Time of Check", "Including at least one night or holiday check per cycle."),
            ("Point of Use/Circuit", "Drinking, clinical wash, CSSD, dialysis, OT, ICU, emergency, etc."),
            ("Available? (Y/N)", "Whether water/electricity was live at that point."),
            ("Water Quality Result (if tested)", "Parameter(s) tested and result against hospital's "
             "defined limits, using WHO GDWQ as framework."),
            ("Interruption/Failure Recorded", "Any interruption found, and restoration time."),
            ("Confirmed By", "Named engineering lead."),
        ],
        verified_sources=[
            "World Health Organization. (2011). Guidelines for Drinking-water Quality (4th ed.).",
            "Coulliette, A. D., & Arduino, M. J. (2015). Hemodialysis and water quality. "
            "Seminars in Dialysis, 26(4), 427-438.",
        ],
        column_headers=["Date/Time of Check", "Point of Use/Circuit", "Available? (Y/N)",
                         "Water Quality Result (if tested)", "Interruption/Failure Recorded", "Confirmed By"],
        worked_example_row=["10/04/2026 02:15", "OT scrub sink + ICU emergency circuit", "Y",
                             "N/A (not a test cycle date)", "None", "Engineering Lead «Name»"],
        extra_blank_rows=9,
    ),
    RecordSpec(
        oe_code="FMS.1.e",
        oe_requirement=(
            "Alternate sources for electricity and water are provided as a backup for "
            "any failure/shortage and their functioning is tested at a predefined "
            "frequency."
        ),
        record_title="FMS.1 Record 5 — Alternate source loaded backup-test record",
        what_is_this=(
            "A record of loaded backup tests -- generator/UPS carrying the essential "
            "circuit load, and alternate water actually moving tank-to-tap -- not a "
            "no-load crank or a sealed tanker contract nobody has called."
        ),
        real_example=(
            "The monthly generator test is run with the OT, ICU and emergency "
            "lighting circuits on load for 30 minutes, not just started and left "
            "idling; the result, fuel level and any fault are logged."
        ),
        why_nabh_asks=(
            "NABH requires alternate electricity and water sources to be tested at a "
            "predefined frequency -- a Commitment requirement that a start-only test "
            "does not satisfy."
        ),
        how_to_fill=[
            ("Date of Test", "Date the loaded test was run."),
            ("Source Tested", "Generator / UPS / reserve tank / second borewell / tanker."),
            ("Test Type", "Loaded (essential-circuit load) or tank-to-tap water movement."),
            ("Result (Pass/Fail)", "Whether the source carried the load or moved water as required."),
            ("Fault/Observation", "Any fault found, e.g. changeover delay, low battery, seized valve."),
            ("Confirmed By", "Named engineering lead present at the test."),
        ],
        verified_sources=[
            "Bureau of Indian Standards. (2016). National Building Code of India, 2016.",
        ],
        column_headers=["Date of Test", "Source Tested", "Test Type", "Result (Pass/Fail)",
                         "Fault/Observation", "Confirmed By"],
        worked_example_row=["12/04/2026", "Diesel generator", "Loaded (OT+ICU+emergency lighting, 30 min)",
                             "Pass", "None", "Engineering Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.1.f",
        oe_requirement=(
            "The organisation takes initiatives towards an energy-efficient and "
            "environment friendly hospital."
        ),
        record_title="FMS.1 Record 6 — Energy-efficient and environment-friendly initiative record",
        what_is_this=(
            "A record of this hospital's actual energy-efficiency and environment-"
            "friendly initiatives, each with a named owner, a baseline, and a measured "
            "result -- the chapter's asterisked, documented-evidence element, not a "
            "poster or a single retrofit claimed as the whole programme."
        ),
        real_example=(
            "This hospital set back non-clinical-area HVAC by 2 degrees outside "
            "working hours; baseline monthly electricity use and post-initiative use "
            "are both logged, with the named facilities lead who owns the initiative."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- an Excellence requirement where the "
            "organisation must show real initiatives with a measured baseline and "
            "result, not a certificate or a photograph."
        ),
        how_to_fill=[
            ("Initiative", "The specific energy or environment initiative run this year."),
            ("Named Owner", "Person accountable for this initiative."),
            ("Baseline", "Measured starting point (e.g. monthly kWh, water litres, waste volume)."),
            ("Result", "Measured outcome after the initiative, with the comparison period."),
            ("Review Date", "When this initiative was last reviewed for continuation."),
            ("Confirmed By", "Quality/Accreditation Coordinator or named owner."),
        ],
        verified_sources=[
            "Dhillon, V. S. (2015). Green hospital and climate change: Their "
            "interrelationship and the way forward. Journal of Clinical and "
            "Diagnostic Research.",
        ],
        column_headers=["Initiative", "Named Owner", "Baseline", "Result", "Review Date", "Confirmed By"],
        worked_example_row=["Non-clinical HVAC set-back (2°C, outside working hours)",
                             "Facilities Lead «Name»", "4,200 kWh/month (Jan 2026)",
                             "3,780 kWh/month (Mar 2026), 10% reduction", "01/04/2026",
                             "Quality Coordinator «Name»"],
    ),
]


def main() -> None:
    sop_path = OUT_ROOT / "SOP_FMS.1.a_to_f_planned_facilities_utilities_environment.docx"
    build_sop(SOP, sop_path)
    print(f"built {sop_path}")

    manifest_entries = [{
        "file": sop_path.name,
        "document_type": "sop",
        "standard_code": "FMS.1",
        "title": "Planned Facilities, Utilities and Environment-Friendly Measures",
    }]

    for idx, rec in enumerate(RECORDS, start=1):
        fname = f"FMS.1_Record_{idx:02d}_{rec.record_title.split('—')[-1].strip().lower().replace(' ', '_').replace(',', '')[:60]}.docx"
        rec_path = OUT_ROOT / "Records" / fname
        build_record(rec, rec_path)
        print(f"built {rec_path}")
        manifest_entries.append({
            "file": f"Records/{fname}",
            "document_type": "record",
            "standard_code": "FMS.1",
            "record_index": idx,
            "title": rec.record_title.split("—")[-1].strip(),
        })

    import json
    manifest_path = OUT_ROOT / "manifest.json"
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing = [e for e in existing if e["standard_code"] != "FMS.1"]
    else:
        existing = []
    existing.extend(manifest_entries)
    manifest_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"updated {manifest_path} ({len(manifest_entries)} FMS.1 entries)")


if __name__ == "__main__":
    main()
