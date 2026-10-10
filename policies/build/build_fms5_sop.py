# -*- coding: utf-8 -*-
"""Builds the SHCO SOP + Records for FMS.5 (Fire and Non-Fire Emergencies),
following the approved FMS.5 master policy (shco_policy_masters,
status='approved') and the structural template in sop_record_common.py.

FMS.5 OEs: FMS.5.a-e (5 OEs). doc_required per live shco_full_oes, queried
2026-10-10: FMS.5.a and FMS.5.d are true (Tier 1, full treatment). The
rest are Tier 2.

Source for every procedure step, reference and the division-of-
responsibility language: the approved FMS.5 master policy's
procedure_steps / references_text / responsibility columns (read directly
from shco_policy_masters on 2026-10-10). No new citation or number
introduced beyond what FMS.5 already cites: NBC 2016 (+ IS 2190 as
NBC-pointed extinguisher practice), NDMA Hospital Safety Guidelines 2016,
WHO Hospital Safety Index 2015. FMS.5.c's "mock drills at least twice a
year" is the OE's own non-optional wording -- like FMS.2.d's monthly
round, it is stated plainly, NOT wrapped in guillemets as a hospital
example.
"""
from __future__ import annotations

from pathlib import Path

from sop_record_common import ProcedureBlock, RecordSpec, SOPSpec, build_record, build_sop

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "FMS"

FMS5_REFS = [
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management and Safety chapter, standard FMS.5.",
    "Bureau of Indian Standards. (2016). [National Building Code of India, 2016]"
    "(https://bis.gov.in/others/national-building-code/). "
    "Fire and life-safety framework as the local fire authority has applied it to "
    "this occupancy; not a universal sprinkler or occupancy-subdivision mandate. "
    "IS 2190 is NBC-pointed portable-extinguisher practice, not an extra statute.",
    "National Disaster Management Authority. (2016). [National Disaster Management "
    "Guidelines: Hospital Safety](https://nhsrcindia.org/sites/default/files/2021-05/Guidelines-Hospital-Safety.pdf). Non-fire and hospital-continuity framework, not "
    "an Act of Parliament.",
    "World Health Organization. (2015). [Hospital Safety Index: Guide for Evaluators]"
    "(https://www.who.int/publications/i/item/9789241548984) "
    "(2nd ed.). Evaluator framework, not a mandated score.",
]

SOP = SOPSpec(
    sop_no="SOP-FMS.5",
    title="Fire and Non-Fire Emergencies",
    standard_code_range="FMS.5.a-e",
    what_is_this_for=(
        "This SOP tells fire wardens, facilities, clinical heads and quality "
        "staff, in one place, how this hospital detects, abates and contains fire "
        "and the non-fire emergencies it has named; how the exit plan is "
        "documented and displayed; how mock drills meet the twice-a-year floor; "
        "how fire equipment is maintained; and how essential services continue "
        "when a ward, OT or plant is lost. If you are a fire warden, hold the "
        "drill file, or run an AAC.1 service, this SOP is for you."
    ),
    worked_example=(
        "A smoke detector trips at 3am in a ward corridor. This SOP is what tells "
        "the night-duty lead who to notify, how the exit plan evacuates that "
        "ward's dependent patients, and which record logs the event -- not an "
        "improvised response because the plan was never actually drilled at "
        "night."
    ),
    why_nabh_asks=(
        "NABH requires plans and provisions for early detection, abatement and "
        "containment of fire and non-fire emergencies (Core, asterisked), a "
        "documented and displayed exit plan, mock drills at least twice a year "
        "(a Commitment, non-optional interval), a maintenance plan for fire-"
        "related equipment and infrastructure (Commitment, asterisked), and a "
        "service continuity plan."
    ),
    purpose=(
        "To define how «Hospital Name» detects, abates and contains fire and "
        "non-fire emergencies; documents and displays its exit plan; runs mock "
        "drills meeting the twice-a-year floor; maintains fire-related equipment "
        "and infrastructure; and continues essential services when a ward, OT or "
        "plant is lost."
    ),
    scope=(
        "Applies to every occupied area of {{HOSPITAL_NAME}} and every non-fire "
        "emergency this occupancy actually faces, per the plans named below. It "
        "does not cover laboratory bench chemical hygiene (AAC.6), medical-gas "
        "leak handling at source (FMS.4), electrical backup testing (FMS.1.e), or "
        "outsourced-service quality monitoring (ROM.4.e) -- those remain their "
        "own documents and are only pointed to here where this SOP's steps hand "
        "work to them."
    ),
    responsibilities=[
        ("Head of the Institution",
         "Is accountable that fire and non-fire emergency plans exist and are "
         "provisioned as this SOP requires."),
        ("Named Fire/Facilities Lead",
         "Holds the plans, exit display, drill records and fire-equipment "
         "maintenance."),
        ("Fire Wardens and Night-Duty Leads",
         "Execute the exit plan."),
        ("Clinical Heads",
         "Execute continuity for the AAC.1 services they run."),
        ("Quality/Accreditation Coordinator",
         "Audits a sample of the records this SOP produces, at «Hospital to "
         "define» frequency."),
        ("All Staff",
         "Treat a blocked exit, a discharged extinguisher left in place, a fire "
         "door wedged open, or a year with fewer than two drills, as defects to "
         "report."),
    ],
    blocks=[
        ProcedureBlock(
            heading="4.1 Plans and provisions for early detection, abatement and containment (FMS.5.a, Core, ASTERISKED)",
            why_it_matters=(
                "This is the chapter's first documented-evidence anchor -- an "
                "assessor asks what detects a fire at 3am, what abates it before "
                "the stair is lost, and what contains it so a ward outside the "
                "compartment can continue. A municipal fire NOC is not a plan; it "
                "is a certificate that a plan was once inspected."
            ),
            steps=[
                "1. The organisation has plans and provisions for early "
                "detection, abatement and containment of fire and non-fire "
                "emergencies -- detection (smoke/heat/manual call points as the "
                "local fire NOC required), abatement (extinguishers to IS 2190 "
                "as NBC-pointed practice; hose reels/hydrant/sprinkler only if "
                "the occupancy required them -- no sprinkler mandate is invented "
                "for every SHCO), containment (fire doors, shutters, compartments "
                "as built and as the FMS.1.b drawings show).",
                "2. NDMA Hospital Safety Guidelines 2016 is the non-fire "
                "framework: what is detected (an earthquake, a flood, a bomb "
                "threat, a gas leak from FMS.4), what abates it, what contains it "
                "so the rest of the hospital is not abandoned without a "
                "decision.",
                "3. «Hospital to define the fire plan (detection, abatement, "
                "containment, who is fire warden, how a dependent patient is "
                "moved without rewriting COP.8/COP.12), the non-fire plans for "
                "events this occupancy actually faces, and the provisions "
                "installed». An event this occupancy does not face -- for "
                "example a basement flood in a single-storey building with no "
                "basement -- is a recorded absence, not a gap.",
                "4. AAC.6's laboratory fire sentence is not this hospital plan on "
                "its own -- AAC.6 lab fire uses this plan, it does not replace "
                "it.",
            ],
            technical_sources=[
                "Bureau of Indian Standards. (2016). [National Building Code of "
                "India, 2016](https://bis.gov.in/others/national-building-code/).",
                "National Disaster Management Authority. (2016). [National "
                "Disaster Management Guidelines: Hospital Safety](https://nhsrcindia.org/sites/default/files/2021-05/Guidelines-Hospital-Safety.pdf).",
            ],
        ),
        ProcedureBlock(
            heading="4.2 Documented and displayed exit plan (FMS.5.b)",
            why_it_matters=(
                "A framed plan in the board room, or an exit arrow pointing at a "
                "locked grilled window, is not this OE -- the plan only counts if "
                "a first-time family and a night nurse can actually find and "
                "follow it."
            ),
            steps=[
                "1. The organisation has a documented and displayed exit plan in "
                "case of fire and non-fire emergencies -- documented (how each "
                "occupied floor leaves, assembly point, who sweeps) and displayed "
                "where it can actually be seen, consistent with FMS.1.c "
                "wayfinding and not confused with AAC.6.e radiation signs.",
                "2. «Hospital to define how the exit plan is documented, where "
                "it is displayed, and how a change in a fire door or a ward move "
                "updates the display». The FMS.1.b drawings are the controlled "
                "set this display must match.",
            ],
        ),
        ProcedureBlock(
            heading="4.3 Mock drills at least twice a year (FMS.5.c, Commitment)",
            why_it_matters=(
                "Two tabletop minutes in the quality office, or a drill "
                "photograph of day-shift administration while the OT continues "
                "unaware, is not a drill -- this step only counts when the "
                "people who would actually be on duty are the ones who respond."
            ),
            steps=[
                "1. Mock drills are held at least twice a year. That interval is "
                "set by the objective element itself and is not hospital-"
                "optional.",
                "2. A drill tests detection-to-evacuation (or shelter-in-place "
                "if that is the plan for a named non-fire event) with the people "
                "who would actually be on duty, including a night or weekend "
                "sample over the year, and includes a dependent-patient move.",
                "3. Fire and non-fire need not be eight separate events; they "
                "need to cover, across the year, fire and at least one named "
                "non-fire emergency.",
                "4. «Hospital to define how drills are scheduled so the floor "
                "of twice a year is met, who observes, how a failed objective is "
                "recorded and re-drilled, and how HRM.3 (when drafted) uses these "
                "as the plans staff are trained to». A drill that harmed someone "
                "is also a PSQ.5 incident.",
            ],
        ),
        ProcedureBlock(
            heading="4.4 Maintenance plan for fire-related equipment and infrastructure (FMS.5.d, Commitment, ASTERISKED)",
            why_it_matters=(
                "This is the chapter's second documented-evidence anchor -- a "
                "plan to contain fire fails the moment the door closer is "
                "disconnected and the extinguisher gauge sits in the red. A "
                "vendor contract with no job card is not a maintenance plan."
            ),
            steps=[
                "1. There is a maintenance plan for fire-related equipment and "
                "infrastructure -- detectors, alarms, extinguishers, hose reels, "
                "fire doors, emergency lighting, and any pump or sprinkler this "
                "occupancy actually has.",
                "2. IS 2190 is the NBC-pointed framework for portable "
                "extinguishers (monthly visual and periodic maintenance as that "
                "standard's practice -- the local interval is hospital-defined, "
                "not a NABH monthly-extinguisher mandate invented on top of "
                "FMS.2.d's monthly round). Detectors and panels follow the "
                "installer's and NBC-as-applied inspection.",
                "3. FMS.2.d's monthly round may find fire doors or lighting "
                "failed; this plan is what repairs them -- not a second round, a "
                "repair programme.",
                "4. «Hospital to define which fire-related equipment and "
                "infrastructure this occupancy actually has, the maintenance "
                "task and interval for each class, who attends (in-house or "
                "AMC), and the rule that a failed detector zone or a discharged "
                "extinguisher is replaced or isolated with a compensating "
                "provision until restored». An AMC that cannot show last month's "
                "extinguisher visual and last alarm test is not this OE.",
            ],
            technical_sources=[
                "Bureau of Indian Standards. (2016). National Building Code of "
                "India, 2016 (IS 2190 portable-extinguisher practice).",
            ],
        ),
        ProcedureBlock(
            heading="4.5 Service continuity plan (FMS.5.e, Achievement)",
            why_it_matters=(
                "\"Patients will be shifted to a nearby hospital\" with no named "
                "hospital, no who-calls, and no list of who cannot be moved "
                "without an oxygen reserve, is not a continuity plan -- it is a "
                "sentence that sounds like one."
            ),
            steps=[
                "1. The organisation has a service continuity plan in case of "
                "fire and non-fire emergencies -- how defined AAC.1 services "
                "continue, pause, divert (AAC.2) or move internally (AAC.7) "
                "when a ward, OT or plant is lost.",
                "2. This is not FMS.1.e's DG test, though that test is a "
                "precondition, and it is not ROM.4.e's outsourced-quality "
                "monitoring. NDMA Hospital Safety 2016 is the framework for "
                "keeping essential hospital functions running.",
                "3. «Hospital to define how each essential service continues or "
                "is paused, the named receiving arrangement if diversion is the "
                "plan, how medical-gas and electrical backups (FMS.4.c / "
                "FMS.1.e) are used in that hour, and who declares continuity "
                "versus full evacuation». AAC.1 unused services are not given a "
                "continuity annex.",
            ],
            technical_sources=[
                "National Disaster Management Authority. (2016). [National "
                "Disaster Management Guidelines: Hospital Safety](https://nhsrcindia.org/sites/default/files/2021-05/Guidelines-Hospital-Safety.pdf).",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the FMS.5 Records folder).",
    related_documents=[
        "Policy — Fire and Non-Fire Emergencies (FMS.5)",
        "Hospital's As-Built Drawing Set (FMS.1.b)",
        "Hospital's Monthly Facility Safety Round (FMS.2.d)",
        "Hospital's Medical Gases, Vacuum and Compressed Air SOP (FMS.4)",
        "Hospital's Laboratory Safety Programme (AAC.6)",
        "Hospital's Service Directory (AAC.1)",
    ],
    verified_sources=FMS5_REFS,
    review_text=(
        "This policy is reviewed at «Hospital to define the review interval for "
        "this policy», and sooner when a drill failed or a fire-door closer was "
        "found disconnected, or when FMS.1, FMS.2, FMS.4, AAC.6 or ROM.4 that "
        "this document hands work to are revised."
    ),
)


RECORDS = [
    RecordSpec(
        oe_code="FMS.5.a",
        oe_requirement="The organisation has plans and provisions for early detection, abatement and containment of the fire, and non-fire emergencies.",
        record_title="FMS.5 Record 1 — Fire and non-fire detection, abatement and containment provisions record",
        what_is_this=(
            "A record of the installed provisions (detectors, extinguishers, "
            "fire doors, compartments) against the fire and named non-fire plans, "
            "showing provisions actually exist in the building. The chapter's "
            "first asterisked, documented-evidence record."
        ),
        real_example=(
            "The ground-floor ward's smoke detectors, two CO2 extinguishers and "
            "self-closing fire door are each confirmed present and matching the "
            "fire plan for that compartment."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- a Core requirement where the organisation "
            "must show plans and provisions exist in the building, not just in a "
            "municipal NOC or a copied NBC paragraph."
        ),
        how_to_fill=[
            ("Date of Check", "Date the provision was confirmed."),
            ("Area/Compartment", "Where the provision is located."),
            ("Provision Type", "Detection / abatement / containment, and the specific item."),
            ("Present and Matches Plan? (Y/N)", "Whether the provision is installed as the plan requires."),
            ("Fire or Named Non-Fire Event", "Which hazard this provision addresses."),
            ("Confirmed By", "Named fire/facilities lead."),
        ],
        verified_sources=[
            "Bureau of Indian Standards. (2016). [National Building Code of India, 2016](https://bis.gov.in/others/national-building-code/).",
        ],
        column_headers=["Date of Check", "Area/Compartment", "Provision Type",
                         "Present and Matches Plan? (Y/N)", "Fire or Named Non-Fire Event", "Confirmed By"],
        worked_example_row=["04/03/2026", "Ground-floor ward A", "Detection (smoke detector) + abatement (2x CO2 extinguisher) + containment (self-closing fire door)",
                             "Y", "Fire", "Fire Lead «Name»"],
        extra_blank_rows=9,
    ),
    RecordSpec(
        oe_code="FMS.5.b",
        oe_requirement="The organisation has a documented and displayed exit plan in case of fire and non-fire emergencies.",
        record_title="FMS.5 Record 2 — Exit plan display inspection record",
        what_is_this=(
            "A record confirming the exit plan is actually displayed, legible, "
            "and matches the current FMS.1.b drawings -- not framed in the board "
            "room or pointing at a locked window."
        ),
        real_example=(
            "A routine inspection finds the exit plan display on the second "
            "floor is still showing the layout before a corridor was partitioned; "
            "this record shows it was found and corrected."
        ),
        why_nabh_asks=(
            "NABH requires a documented and displayed exit plan -- a Commitment "
            "requirement checked against whether the display actually matches "
            "the building as it is now."
        ),
        how_to_fill=[
            ("Date of Inspection", "Date the display was inspected."),
            ("Location", "Where the exit plan is displayed."),
            ("Matches Current FMS.1.b Drawings? (Y/N)", "Whether the display reflects the current as-built layout."),
            ("Legible/Accessible? (Y/N)", "Whether it can actually be seen and read."),
            ("Action Taken", "What was done to correct a defect."),
            ("Confirmed By", "Named fire/facilities lead."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.5.",
        ],
        column_headers=["Date of Inspection", "Location", "Matches Current FMS.1.b Drawings? (Y/N)",
                         "Legible/Accessible? (Y/N)", "Action Taken", "Confirmed By"],
        worked_example_row=["10/03/2026", "Second floor, corridor junction", "N (pre-partition layout)",
                             "Y", "Display updated to match current drawings", "Fire Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.5.c",
        oe_requirement="Mock drills are held at least twice a year.",
        record_title="FMS.5 Record 3 — Mock drill record",
        what_is_this=(
            "A record of each mock drill, showing detection-to-evacuation (or "
            "shelter-in-place) was tested with the actual on-duty staff, "
            "including a dependent-patient move, meeting the twice-a-year floor "
            "across fire and at least one named non-fire event."
        ),
        real_example=(
            "A night-shift fire drill in April moves a bed-bound ICU patient "
            "through the evacuation route; observed failures (a delayed door "
            "release) are logged and re-drilled in June."
        ),
        why_nabh_asks=(
            "NABH requires mock drills at least twice a year -- a Commitment, "
            "non-optional interval checked against drills with real on-duty "
            "staff, not a tabletop exercise."
        ),
        how_to_fill=[
            ("Date of Drill", "Date the drill was conducted."),
            ("Fire or Named Non-Fire Event", "Which hazard the drill tested."),
            ("Shift/Staff Involved", "Day, night or weekend; which staff actually responded."),
            ("Dependent-Patient Move Included? (Y/N)", "Whether a dependent-patient move was part of the drill."),
            ("Observed Failures and Re-Drill", "Any failure found, and the re-drill date if applicable."),
            ("Observed By", "Named observer."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.5.",
        ],
        column_headers=["Date of Drill", "Fire or Named Non-Fire Event", "Shift/Staff Involved",
                         "Dependent-Patient Move Included? (Y/N)", "Observed Failures and Re-Drill", "Observed By"],
        worked_example_row=["15/04/2026", "Fire", "Night shift, ICU and Ward A",
                             "Y, bed-bound patient moved via evacuation route",
                             "Delayed fire-door release (3 sec); re-drilled 10/06/2026, passed",
                             "Quality Coordinator «Name»"],
        extra_blank_rows=9,
    ),
    RecordSpec(
        oe_code="FMS.5.d",
        oe_requirement="There is a maintenance plan for fire-related equipment and infrastructure.",
        record_title="FMS.5 Record 4 — Fire-equipment and infrastructure maintenance job-card log",
        what_is_this=(
            "A log of maintenance job cards for detectors, alarms, extinguishers, "
            "hose reels, fire doors and emergency lighting -- not a vendor "
            "contract with no job card. The chapter's second asterisked, "
            "documented-evidence record."
        ),
        real_example=(
            "A monthly visual check of corridor extinguishers finds one gauge in "
            "the red; it is replaced the same day and the replacement logged."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- a Commitment requirement where the "
            "organisation must show fire equipment and infrastructure were "
            "actually maintained, not covered by an AMC that never produces a "
            "job card."
        ),
        how_to_fill=[
            ("Date", "Date of the maintenance task."),
            ("Equipment/Infrastructure", "Detector, alarm, extinguisher, hose reel, fire door, emergency lighting, pump, etc."),
            ("Task", "Visual check, functional test, service, repair, replacement."),
            ("Result", "Pass, fail, or finding (e.g. discharged extinguisher, disconnected door closer)."),
            ("Isolated/Compensating Provision Until Restored? (Y/N)", "Whether a failed item was isolated or compensated for until fixed."),
            ("Confirmed By", "Named in-house or AMC attendee."),
        ],
        verified_sources=[
            "Bureau of Indian Standards. (2016). [National Building Code of India, "
            "2016](https://bis.gov.in/others/national-building-code/) (IS 2190 portable-extinguisher practice).",
        ],
        column_headers=["Date", "Equipment/Infrastructure", "Task", "Result",
                         "Isolated/Compensating Provision Until Restored? (Y/N)", "Confirmed By"],
        worked_example_row=["01/03/2026", "CO2 extinguisher, corridor outside ICU", "Monthly visual check",
                             "Fail — gauge in red", "Y, replaced same day with spare unit",
                             "Fire Lead «Name»"],
        extra_blank_rows=9,
    ),
    RecordSpec(
        oe_code="FMS.5.e",
        oe_requirement="The organisation has a service continuity plan in case of fire and non-fire emergencies.",
        record_title="FMS.5 Record 5 — Service continuity plan activation record",
        what_is_this=(
            "A record of how each essential AAC.1 service would continue, pause "
            "or divert if lost to fire or a named non-fire event, and any actual "
            "activation of that plan -- naming the receiving arrangement, not a "
            "vague reference to 'a nearby hospital'."
        ),
        real_example=(
            "A planned fire-door maintenance outage requires the OT list to "
            "pause for two hours; the continuity plan's named decision-maker "
            "authorises the pause and the resumption is logged."
        ),
        why_nabh_asks=(
            "NABH requires a service continuity plan for fire and non-fire "
            "emergencies -- an Achievement requirement checked against a plan "
            "that names who decides, what continues, and where patients go if "
            "diversion is needed."
        ),
        how_to_fill=[
            ("Service (per AAC.1)", "Named essential service covered by this continuity entry."),
            ("Continue/Pause/Divert Plan", "How the service continues, pauses, or diverts (naming the receiving arrangement if diversion)."),
            ("Backup Dependency", "Which FMS.4.c/FMS.1.e backup this plan depends on, if any."),
            ("Decision-Maker", "Who declares continuity versus full evacuation."),
            ("Activated? (Y/N) and Date", "Whether this plan was actually activated, and when."),
            ("Confirmed By", "Named clinical head or fire/facilities lead."),
        ],
        verified_sources=[
            "National Disaster Management Authority. (2016). [National Disaster "
            "Management Guidelines: Hospital Safety](https://nhsrcindia.org/sites/default/files/2021-05/Guidelines-Hospital-Safety.pdf).",
        ],
        column_headers=["Service (per AAC.1)", "Continue/Pause/Divert Plan", "Backup Dependency",
                         "Decision-Maker", "Activated? (Y/N) and Date", "Confirmed By"],
        worked_example_row=["General Surgery (OT list)", "Pause for planned fire-door maintenance outage",
                             "None (planned, non-emergency pause)", "OT In-Charge «Name»",
                             "Y, 20/03/2026, resumed same day", "OT In-Charge «Name»"],
    ),
]


def main() -> None:
    sop_path = OUT_ROOT / "SOP_FMS.5.a_to_e_fire_non_fire_emergencies.docx"
    build_sop(SOP, sop_path)
    print(f"built {sop_path}")

    manifest_entries = [{
        "file": sop_path.name,
        "document_type": "sop",
        "standard_code": "FMS.5",
        "title": "Fire and Non-Fire Emergencies",
    }]

    for idx, rec in enumerate(RECORDS, start=1):
        fname = f"FMS.5_Record_{idx:02d}_{rec.record_title.split('—')[-1].strip().lower().replace(' ', '_').replace(',', '').replace('/', '-')[:60]}.docx"
        rec_path = OUT_ROOT / "Records" / fname
        build_record(rec, rec_path)
        print(f"built {rec_path}")
        manifest_entries.append({
            "file": f"Records/{fname}",
            "document_type": "record",
            "standard_code": "FMS.5",
            "record_index": idx,
            "title": rec.record_title.split("—")[-1].strip(),
        })

    import json
    manifest_path = OUT_ROOT / "manifest.json"
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing = [e for e in existing if e["standard_code"] != "FMS.5"]
    else:
        existing = []
    existing.extend(manifest_entries)
    manifest_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"updated {manifest_path} ({len(manifest_entries)} FMS.5 entries)")


if __name__ == "__main__":
    main()
