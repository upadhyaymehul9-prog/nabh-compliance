# -*- coding: utf-8 -*-
"""Builds the SHCO SOP + Records for FMS.2 (Safety of Patients, Families,
Staff and Visitors), following the approved FMS.2 master policy
(shco_policy_masters, status='approved') and the structural template in
sop_record_common.py.

FMS.2 OEs: FMS.2.a-g (7 OEs). doc_required (asterisk) per live
shco_full_oes, queried 2026-10-10: FMS.2.f and FMS.2.g are true (Tier 1,
full treatment). FMS.2.a-e are Tier 2 under the two-tier depth standing
rule.

Source for every procedure step, reference and the division-of-
responsibility language: the approved FMS.2 master policy's
procedure_steps / references_text / responsibility columns (read directly
from shco_policy_masters on 2026-10-10). No new citation or number is
introduced beyond what FMS.2 already cites: NBC 2016 (+ IS 732/IS 3043/
IS 2190 as NBC-pointed practice), Gudlavalleti (2018), WHO Safe Management
of Wastes (2014), WHO Hospital Safety Index (2015), Aggarwal et al. (2010),
Health Facilities Management (2015). The "at least once a month" in
FMS.2.d (4.4 below) is the OE's own wording, not an invented example --
the master policy explicitly states it is a Core, non-hospital-optional
floor, so it is NOT wrapped in guillemets here either.
"""
from __future__ import annotations

from pathlib import Path

from sop_record_common import ProcedureBlock, RecordSpec, SOPSpec, build_record, build_sop

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "FMS"

FMS2_REFS = [
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management and Safety chapter, standard FMS.2.",
    "Bureau of Indian Standards. (2016). [National Building Code of India, 2016]"
    "(https://bis.gov.in/others/national-building-code/). "
    "Building, access and electrical-installation framework as the local authority "
    "has applied it; IS 732, IS 3043 and IS 2190 are NBC-pointed practice, not extra "
    "statutes.",
    "Gudlavalleti, V. S. (2018). [Challenges in Accessing Health Care for People with "
    "Disability in the South Asian Context: A Review](https://www.mdpi.com/1660-4601/15/11/2366). International Journal of "
    "Environmental Research and Public Health, 15(11), 2366. Disability-access "
    "framework.",
    "World Health Organization. (2014). [Safe Management of Wastes from Health-Care "
    "Activities](https://www.who.int/publications-detail-redirect/9789241548564) (2nd ed.). Waste framework only; BMW colour-coding and SPCB handover "
    "remain HIC.3.",
    "World Health Organization. (2015). [Hospital Safety Index: Guide for Evaluators]"
    "(https://www.who.int/publications/i/item/9789241548984) "
    "(2nd ed.). Evaluator framework, not a mandated score.",
    "Aggarwal, R., Mytton, O. T., Derbrew, M., Hananel, D., Heydenburg, M., Issenberg, "
    "B., MacAulay, C., Mancini, M. E., Morimoto, T., Soper, N., Ziv, A., & Reznick, R. "
    "(2010). [Training and simulation for patient safety](https://qualitysafety.bmj.com/content/19/Suppl_2/i34). Quality and Safety in Health "
    "Care, 19(Suppl 2), i34-i43. Infrastructure-and-safety framework.",
    "American Society for Health Care Engineering. (2015). "
    "[Infrastructures to improve patient safety]"
    "(https://www.hfmmagazine.com/articles/1827-infrastructures-to-improve-patient-safety). "
    "Health Facilities Management. Framework reference only.",
]

SOP = SOPSpec(
    sop_no="SOP-FMS.2",
    title="Safety of Patients, Families, Staff and Visitors",
    standard_code_range="FMS.2.a-g",
    what_is_this_for=(
        "This SOP tells facilities, security, engineering and quality staff, in one "
        "place, how this hospital keeps the building itself safe: the grab rails and "
        "call bells that actually work, access for the differently-abled, which areas "
        "need extra security, the monthly walk that finds what a register alone "
        "cannot, the electrical audit that is not just a DG test, how condemned items "
        "actually leave the clinical floor, and how hazardous materials are tracked "
        "and used safely. If you walk a round, hold a key, sign off an audit, or tag "
        "a condemned bed, this SOP is for you."
    ),
    worked_example=(
        "A monthly facility round finds a grab rail pulled out of a wet-wall fixing "
        "in a ground-floor toilet. This SOP is what tells the rounding staff member "
        "which record to log it in, who closes the finding, and by when -- rather "
        "than the defect sitting unaddressed until the next round finds it again."
    ),
    why_nabh_asks=(
        "NABH requires patient-safety devices and infrastructure, facilities for the "
        "differently-abled, a description of extra-security areas and access, a "
        "monthly facility safety round (a Core, non-negotiable interval), electrical "
        "safety audits, a procedure for identifying and disposing of material not in "
        "use, and identification and safe use of hazardous materials -- the last two "
        "being the chapter's asterisked, documented-evidence elements."
    ),
    purpose=(
        "To define how «Hospital Name» keeps patients, families, staff and visitors "
        "safe from the building itself: installed safety devices, access for the "
        "differently-abled, extra-security areas, the monthly facility round, "
        "electrical safety audits, disposal of material not in use, and the safe "
        "identification and use of hazardous materials."
    ),
    scope=(
        "Applies to every area of {{HOSPITAL_NAME}} that patients, families, staff or "
        "visitors use. It does not cover fire detection, alarms, extinguishers or "
        "suppression (FMS.5), medical-device calibration (FMS.3), biomedical-waste "
        "colour coding and transport (HIC.3), blood/body-fluid spill response (HIC.2), "
        "cytotoxic spill response (MOM.8), or laboratory bench chemical hygiene "
        "(AAC.6) -- those remain their own documents and are only pointed to here "
        "where this SOP's steps hand work to them."
    ),
    responsibilities=[
        ("Head of the Institution",
         "Is accountable that the facility operates so that patients, families, "
         "staff and visitors are safe as this SOP requires."),
        ("Named Facilities/Engineering Lead",
         "Holds device inspections, monthly rounds, electrical audits, unused-"
         "material records and the hazardous-material inventory."),
        ("Security/Administration",
         "Holds the extra-security and access description, where this is not the "
         "facilities lead."),
        ("Quality/Accreditation Coordinator",
         "Audits a sample of the records this SOP produces, at «Hospital to define» "
         "frequency, flagging a mismatch rather than filing it."),
        ("All Staff",
         "Treat a blocked exit, an unlabelled chemical, a condemned bed left in a "
         "patient bay, or a monthly register with no actual walk, as defects to "
         "report, not someone else's problem."),
    ],
    blocks=[
        ProcedureBlock(
            heading="4.1 Patient-safety devices and infrastructure, installed and inspected (FMS.2.a)",
            why_it_matters=(
                "A grab rail that pulled out of a wet-wall fixing, or a call bell "
                "that rings at the panel but not in the room, is the failure this "
                "step exists to catch -- not the absence of the device, but a device "
                "that looks installed and does not actually work."
            ),
            steps=[
                "1. Patient-safety devices and infrastructure installed across the "
                "organisation include grab rails in toilets and wet areas, anti-skid "
                "flooring where water is expected, window restrictors on upper floors, "
                "bumper guards on trolley routes, nurse-call/emergency-bell hardware, "
                "and bed-rail hardware -- the devices this hospital actually runs.",
                "2. Fire detection, alarms, extinguishers and suppression are FMS.5 "
                "provisions, inspected under FMS.5.d; they are listed on the monthly "
                "round (4.4 below) as found/blocked/failed, not counted twice as this "
                "OE's own install-and-inspect programme.",
                "3. «Hospital to define which patient-safety devices and infrastructure "
                "are installed, and the inspection interval and method» -- an inspection "
                "that tests the device, not one read off a purchase invoice.",
                "4. COP.12 owns the clinical decision to use a bed rail or a call bell "
                "at the bedside; this step owns that the hardware exists and works.",
            ],
            technical_sources=[
                "Bureau of Indian Standards. (2016). [National Building Code of India, 2016](https://bis.gov.in/others/national-building-code/).",
                "Aggarwal, R., et al. (2010). [Training and simulation for patient safety](https://qualitysafety.bmj.com/content/19/Suppl_2/i34). "
                "Quality and Safety in Health Care, 19(Suppl 2), i34-i43.",
                "American Society for Health Care Engineering. (2015). [Infrastructures to improve patient safety](https://www.hfmmagazine.com/articles/1827-infrastructures-to-improve-patient-safety). Health Facilities "
                "Management.",
            ],
        ),
        ProcedureBlock(
            heading="4.2 Facilities for the differently-abled (FMS.2.b)",
            why_it_matters=(
                "A single ramp to a locked side door is not this OE -- a wheelchair "
                "user needs to actually reach the floors and services this hospital "
                "treats, not just the building's front step."
            ),
            steps=[
                "1. «Hospital to define facilities for the differently-abled and how "
                "they are kept usable» -- ramps or a working lift to the floors this "
                "hospital uses for patients, an accessible toilet, and wayfinding a "
                "wheelchair user can follow (consistent with FMS.1.c).",
                "2. Facilities are kept usable, not blocked by a trolley bay or storage "
                "-- a facility that exists on paper but is obstructed in practice fails "
                "this step.",
                "3. NBC 2016 access provisions apply insofar as the local authority "
                "applied them to this building's occupancy; this step does not invent a "
                "universal door-width or gradient figure for every SHCO.",
            ],
            technical_sources=[
                "Gudlavalleti, V. S. (2018). [Challenges in Accessing Health Care for "
                "People with Disability in the South Asian Context: A Review](https://www.mdpi.com/1660-4601/15/11/2366). "
                "International Journal of Environmental Research and Public Health, "
                "15(11), 2366.",
                "Bureau of Indian Standards. (2016). [National Building Code of India, 2016](https://bis.gov.in/others/national-building-code/).",
            ],
        ),
        ProcedureBlock(
            heading="4.3 Extra security and access to areas (FMS.2.c)",
            why_it_matters=(
                "A CCTV monitor that is never watched is not extra security -- this "
                "step is about areas actually being harder to enter without "
                "authorisation, not a camera pointed at an unwatched screen."
            ),
            steps=[
                "1. Extra-security areas typically include pharmacy stores, medical-"
                "records if held on site, nursery/labour (as COP.8 uses them), server "
                "or plant rooms, and the medical-gas manifold (FMS.4) -- plus any other "
                "area this hospital has named.",
                "2. «Hospital to define extra-security areas, access by staff, patients "
                "and visitors, and the hardware that enforces it» -- locks, access-"
                "control hardware, CCTV if installed, and a written access description.",
                "3. COP.8.f owns the care process of matching and handing over a "
                "neonate and the missing-child response; COP.12.b owns bedside "
                "observation of a vulnerable adult -- this step owns the locks, access "
                "control and written description, not those care processes.",
                "4. A breach that is also an incident is dual-entered in PSQ.5.",
            ],
        ),
        ProcedureBlock(
            heading="4.4 Facility inspection rounds at least once a month (FMS.2.d, Core)",
            why_it_matters=(
                "A register signed on the last day of the month from the engineering "
                "office, with no ward walk, is the failure this step exists to catch "
                "-- the round only counts if clinical and support spaces were actually "
                "walked."
            ),
            steps=[
                "1. Facility inspection rounds to ensure safety are conducted at least "
                "once a month. That interval is set by the objective element itself "
                "and is not hospital-optional.",
                "2. The round is a walk of occupied clinical and support spaces that "
                "can find a blocked exit, a failed grab rail, a wet floor without "
                "warning, an unlabelled chemical container, a condemned item still in "
                "a corridor (4.6 below), or an open electrical panel (4.5 below); a "
                "fire extinguisher missing is handed to FMS.5.",
                "3. «Hospital to define who conducts the monthly round, the circuit, "
                "and how findings are closed» -- a round that only inspects the "
                "director's corridor does not satisfy this step.",
                "4. A missed month is treated as a defect, not a gap to be filled "
                "retroactively. A finding that is also an incident is dual-entered in "
                "PSQ.5; ROM.4.a may use round findings as risk inputs without this "
                "step ceasing to be the facility method of record.",
            ],
        ),
        ProcedureBlock(
            heading="4.5 Electrical safety audits of the facility (FMS.2.e)",
            why_it_matters=(
                "A megger reading filed once at commissioning, with no audit since, "
                "is not an electrical safety programme -- this step is a recurring "
                "audit of the building's electrical installation, not a one-time "
                "commissioning record."
            ),
            steps=[
                "1. This is not the FMS.1.e loaded DG test and not FMS.3's calibration "
                "of a medical device -- it is an audit of the electrical installation "
                "as a facility: earthing continuity, residual-current/earth-leakage "
                "protection on wet-area and patient-care circuits, overload and "
                "discrimination, damaged flexible cords, socket outlets in wet areas, "
                "panel labelling and lockability, and isolated-power provision in the "
                "OT where this hospital runs one.",
                "2. «Hospital to define the electrical safety audit scope, competence "
                "of the auditor, interval, and the isolation-until-repaired rule» -- "
                "who audits (in-house competent person or licensed contractor), and how "
                "a failed earth or a missing ELCB is isolated until it is repaired.",
                "3. A failed medical device remains FMS.3's concern; a failed building "
                "circuit is this audit's concern.",
            ],
            technical_sources=[
                "Bureau of Indian Standards. (2016). [National Building Code of India, "
                "2016](https://bis.gov.in/others/national-building-code/) (as the framework pointing to IS 732 wiring practice and IS 3043 "
                "earthing).",
            ],
        ),
        ProcedureBlock(
            heading="4.6 Identification and disposal of material not in use (FMS.2.f, Commitment, ASTERISKED)",
            why_it_matters=(
                "A condemned ventilator left in a ward bay \"until biomedical "
                "collects it\", with no identification tag, is the failure this step "
                "exists to catch. This is the first of the chapter's two documented-"
                "evidence anchors -- an assessor will ask how a condemned bed, an "
                "obsolete monitor, or construction debris actually leaves the "
                "clinical floor."
            ),
            steps=[
                "1. There is a procedure which addresses the identification and "
                "disposal of material(s) not in use in the organisation -- condemned "
                "furniture, obsolete equipment that FMS.3 has struck off the "
                "inventory, unused building materials, and expired non-BMW general "
                "stores.",
                "2. This is distinct from HIC.3's biomedical-waste stream: HIC.3 owns "
                "colour, internal transport, SPCB and common-facility handover. This "
                "step is material not in use, not the four-colour clinical waste "
                "stream pointed at as the answer.",
                "3. «Hospital to define the procedure that identifies and disposes of "
                "material not in use, including the HIC.3 split» -- how material is "
                "identified (tag, location, date, owner), who authorises condemnation "
                "including FMS.3 strike-off when the item is equipment, how it is "
                "stored so it cannot be reused on a patient, and how it is disposed of "
                "or sold.",
                "4. A tagged item still sitting in a patient bay is a failure of this "
                "OE, not a work-in-progress.",
            ],
            technical_sources=[
                "World Health Organization. (2014). [Safe Management of Wastes from "
                "Health-Care Activities](https://www.who.int/publications-detail-redirect/9789241548564) (2nd ed.). Waste framework only; BMW colour-"
                "coding and SPCB handover remain HIC.3.",
            ],
        ),
        ProcedureBlock(
            heading="4.7 Hazardous materials identified and used safely (FMS.2.g, Core, ASTERISKED)",
            why_it_matters=(
                "A safety data sheet folder in quality, with no label on the actual "
                "jerry-can, is not identification. This is the chapter's second "
                "documented-evidence anchor -- an assessor will ask for the list, the "
                "location, the label, the PPE and the spill method for chemicals this "
                "hospital actually holds."
            ),
            steps=[
                "1. Hazardous materials are identified and used safely within the "
                "organisation -- the facility-wide list: housekeeping chemicals, "
                "water-treatment chemicals, diesel and other fuels, mercury if a "
                "sphygmomanometer or thermometer stock still exists, engineering "
                "solvents, and laboratory bulk stores that sit outside the bench "
                "programme.",
                "2. This is not HIC.2's blood/body-fluid spill SOP, not MOM.8's "
                "cytotoxic bench spill SOP, not HIC.3's BMW colours, and not AAC.6's "
                "laboratory chemical-hygiene programme counted as the whole hospital "
                "list -- dual entry applies when a spill meets two definitions.",
                "3. «Hospital to define the identification and safe use of hazardous "
                "materials, including spill method for building chemicals and "
                "mercury» -- the inventory of hazardous materials this hospital "
                "actually holds (or a recorded absence for a class it does not hold), "
                "labelling and segregation, PPE, and who may use which material.",
                "4. NBC 2016 storage provisions apply as the local authority applied "
                "them; PESO/explosives rules for gas cylinders remain FMS.4, not this "
                "chemical list counted twice.",
            ],
            technical_sources=[
                "Bureau of Indian Standards. (2016). [National Building Code of India, 2016](https://bis.gov.in/others/national-building-code/).",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-7 (see the FMS.2 Records folder).",
    related_documents=[
        "Policy — Safety of Patients, Families, Staff and Visitors (FMS.2)",
        "Hospital's Facility Management and Fire Safety Programme (FMS.5)",
        "Hospital's Medical and Support-Service Equipment Programme (FMS.3)",
        "Hospital's Support-Services Infection-Control Policy (HIC.3)",
        "Hospital's Blood/Body-Fluid Spill SOP (HIC.2)",
        "Hospital's Cytotoxic Handling SOP (MOM.8)",
        "Hospital's Laboratory Safety Programme (AAC.6)",
    ],
    verified_sources=FMS2_REFS,
    review_text=(
        "This policy is reviewed at «Hospital to define the review interval for this "
        "policy», and sooner when a monthly round was missed, or when FMS.1, FMS.3, "
        "FMS.4, FMS.5, HIC.2, HIC.3, AAC.6, COP.8 or COP.12 that this document hands "
        "work to are revised."
    ),
)


RECORDS = [
    RecordSpec(
        oe_code="FMS.2.a",
        oe_requirement="Patient-safety devices and infrastructure are installed across the organisation and inspected periodically.",
        record_title="FMS.2 Record 1 — Patient-safety device inspection record",
        what_is_this=(
            "A log proving patient-safety devices (grab rails, anti-skid flooring, "
            "window restrictors, bumper guards, call-bell hardware) were actually "
            "inspected and found working, not read off a purchase invoice."
        ),
        real_example=(
            "A ground-floor toilet grab rail is found loose during inspection; this "
            "record shows it was found, logged and refixed, not left until the next "
            "round."
        ),
        why_nabh_asks=(
            "NABH requires patient-safety devices and infrastructure to be installed "
            "and inspected periodically -- a Core requirement checked against actual "
            "device function, not a purchase record."
        ),
        how_to_fill=[
            ("Date of Inspection", "Date the device was inspected."),
            ("Device/Area", "Grab rail, anti-skid flooring, window restrictor, bumper guard, call bell, etc., and location."),
            ("Working? (Y/N)", "Whether the device actually functions as inspected."),
            ("Defect Found", "What was found wrong, if anything."),
            ("Action Taken", "What was done to fix a defect, and by when."),
            ("Confirmed By", "Named facilities lead who inspected."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.2.",
        ],
        column_headers=["Date of Inspection", "Device/Area", "Working? (Y/N)",
                         "Defect Found", "Action Taken", "Confirmed By"],
        worked_example_row=["03/04/2026", "Grab rail, ground-floor patient toilet", "N",
                             "Rail loose at wet-wall fixing", "Refixed same day, re-tested",
                             "Facilities Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.2.b",
        oe_requirement="The organisation has facilities for the differently-abled.",
        record_title="FMS.2 Record 2 — Differently-abled facility usability record",
        what_is_this=(
            "A record confirming facilities for the differently-abled (ramps, lift "
            "access, accessible toilet, wayfinding) are present and kept usable, not "
            "blocked by storage or a trolley bay."
        ),
        real_example=(
            "A monthly check finds the accessible toilet door was being used to "
            "store cleaning equipment; this record shows it was found and cleared the "
            "same day."
        ),
        why_nabh_asks=(
            "NABH requires the organisation to have facilities for the differently-"
            "abled -- a Commitment requirement checked against whether the facility "
            "is actually usable, not merely present."
        ),
        how_to_fill=[
            ("Date of Check", "Date the facility was checked."),
            ("Facility", "Ramp, lift, accessible toilet, wayfinding signage, etc."),
            ("Usable? (Y/N)", "Whether it is accessible and unobstructed right now."),
            ("Obstruction/Defect Found", "What was blocking or preventing use, if anything."),
            ("Action Taken", "What was done to restore usability."),
            ("Confirmed By", "Named facilities lead."),
        ],
        verified_sources=[
            "Gudlavalleti, V. S. (2018). [Challenges in Accessing Health Care for "
            "People with Disability in the South Asian Context: A Review](https://www.mdpi.com/1660-4601/15/11/2366). "
            "International Journal of Environmental Research and Public Health, "
            "15(11), 2366.",
        ],
        column_headers=["Date of Check", "Facility", "Usable? (Y/N)",
                         "Obstruction/Defect Found", "Action Taken", "Confirmed By"],
        worked_example_row=["03/04/2026", "Accessible toilet, ground floor", "N",
                             "Cleaning equipment stored inside, door partly blocked",
                             "Cleared same day; storage relocated", "Facilities Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.2.c",
        oe_requirement=(
            "Operational planning identifies areas which need to have extra security "
            "and describes access to different areas in the hospital by staff, "
            "patients, and visitors."
        ),
        record_title="FMS.2 Record 3 — Extra-security area and access register",
        what_is_this=(
            "A register of areas this hospital has named as needing extra security "
            "(pharmacy store, medical-records, server/plant rooms, gas manifold, "
            "nursery/labour), the access-control hardware in place, and who may "
            "enter."
        ),
        real_example=(
            "The pharmacy store is listed with its lock type, the named staff "
            "authorised to hold a key, and the date access was last reviewed."
        ),
        why_nabh_asks=(
            "NABH requires operational planning to identify extra-security areas "
            "and describe access by staff, patients and visitors -- an Achievement "
            "requirement checked against a written, working description, not an "
            "unwatched camera."
        ),
        how_to_fill=[
            ("Area", "Named extra-security area (pharmacy store, medical-records, server room, gas manifold, nursery/labour, etc.)."),
            ("Access Control", "Lock, access-control hardware, CCTV, or other measure in place."),
            ("Who May Enter", "Staff categories/roles authorised, and how patient/visitor access is restricted."),
            ("Last Reviewed", "Date access arrangements were last confirmed current."),
            ("Breach Recorded? (Y/N)", "Whether any unauthorised access occurred since last review (dual-entered in PSQ.5 if an incident)."),
            ("Confirmed By", "Named security or facilities lead."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.2.",
        ],
        column_headers=["Area", "Access Control", "Who May Enter", "Last Reviewed",
                         "Breach Recorded? (Y/N)", "Confirmed By"],
        worked_example_row=["Pharmacy store", "Keyed lock, key register",
                             "Pharmacist and pharmacy assistant only", "01/04/2026", "N",
                             "Security Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.2.d",
        oe_requirement="Facility inspection rounds to ensure safety are conducted at least once a month.",
        record_title="FMS.2 Record 4 — Monthly facility safety round report",
        what_is_this=(
            "A report of each monthly walk-round of occupied clinical and support "
            "spaces, showing the circuit actually walked and every finding closed "
            "out -- not a register signed from the engineering office."
        ),
        real_example=(
            "The April round walks every ward, OT corridor and the main pharmacy; "
            "it finds one blocked fire exit in the physiotherapy corridor, logs it, "
            "and records it closed two days later."
        ),
        why_nabh_asks=(
            "NABH requires facility inspection rounds at least once a month -- a "
            "Core, non-negotiable interval set by the objective element itself, not "
            "hospital-defined."
        ),
        how_to_fill=[
            ("Month/Date of Round", "The month covered and the date the round was walked."),
            ("Areas Walked (Circuit)", "Every clinical/support area actually covered, not just the office corridor."),
            ("Findings", "Each defect found: blocked exit, failed rail, wet floor, unlabelled chemical, condemned item, open panel, etc."),
            ("Closed? (Y/N) and Date", "Whether and when each finding was closed."),
            ("Dual-Entered in PSQ.5? (Y/N)", "Whether any finding was also an incident."),
            ("Confirmed By", "Named round owner."),
        ],
        verified_sources=[
            "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
            "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
            "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management "
            "and Safety chapter, standard FMS.2.",
        ],
        column_headers=["Month/Date of Round", "Areas Walked (Circuit)", "Findings",
                         "Closed? (Y/N) and Date", "Dual-Entered in PSQ.5? (Y/N)", "Confirmed By"],
        worked_example_row=["April 2026, walked 04/04/2026",
                             "All wards, OT corridor, main pharmacy, emergency department",
                             "Blocked fire exit, physiotherapy corridor (storage trolley)",
                             "Y, closed 06/04/2026", "N", "Facilities Lead «Name»"],
        extra_blank_rows=11,
    ),
    RecordSpec(
        oe_code="FMS.2.e",
        oe_requirement="Organisation conducts electrical safety audits for the facility.",
        record_title="FMS.2 Record 5 — Electrical safety audit report",
        what_is_this=(
            "A report of the electrical installation audit (earthing, residual-"
            "current protection, wet-area sockets, panel lockability) and any "
            "isolation-until-repaired action, separate from FMS.1.e's DG load test "
            "and FMS.3's device calibration."
        ),
        real_example=(
            "An annual audit finds a missing ELCB on a wet-area circuit in the "
            "physiotherapy department; the circuit is isolated the same day until "
            "the ELCB is fitted and re-tested."
        ),
        why_nabh_asks=(
            "NABH requires the organisation to conduct electrical safety audits for "
            "the facility -- an Achievement requirement checked against a recurring "
            "audit, not a one-time commissioning record."
        ),
        how_to_fill=[
            ("Date of Audit", "Date the electrical safety audit was conducted."),
            ("Auditor", "Named competent person or licensed contractor."),
            ("Scope Covered", "Earthing, residual-current protection, wet-area sockets, panel labelling/lockability, isolated-power (OT), etc."),
            ("Fault Found", "Any fault found, e.g. missing ELCB, damaged cord, unlabelled panel."),
            ("Isolated Until Repaired? (Y/N) and Date Repaired", "Whether the faulty circuit was isolated, and when it was fixed."),
            ("Confirmed By", "Named facilities lead."),
        ],
        verified_sources=[
            "Bureau of Indian Standards. (2016). [National Building Code of India, "
            "2016](https://bis.gov.in/others/national-building-code/) (as the framework pointing to IS 732 wiring practice and IS 3043 "
            "earthing).",
        ],
        column_headers=["Date of Audit", "Auditor", "Scope Covered", "Fault Found",
                         "Isolated Until Repaired? (Y/N) and Date Repaired", "Confirmed By"],
        worked_example_row=["15/03/2026", "Licensed electrical contractor «Name»",
                             "Earthing, RCD/ELCB, wet-area sockets, panel lockability",
                             "Missing ELCB, physiotherapy wet-area circuit",
                             "Y, isolated 15/03/2026; repaired and re-tested 17/03/2026",
                             "Facilities Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.2.f",
        oe_requirement="There is a procedure which addresses the identification and disposal of material(s) not in use in the organisation.",
        record_title="FMS.2 Record 6 — Material-not-in-use identification and disposal log",
        what_is_this=(
            "A log of condemned furniture, obsolete equipment struck off by FMS.3, "
            "unused building materials and expired non-BMW stores -- how each was "
            "tagged, condemned, quarantined and finally disposed of or sold. The "
            "chapter's first asterisked, documented-evidence record."
        ),
        real_example=(
            "An obsolete patient monitor is struck off the FMS.3 equipment "
            "inventory, tagged the same day, moved to the condemned store so it "
            "cannot be reused on a patient, and sold for scrap six weeks later."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- a Commitment requirement where the "
            "organisation must show material not in use is actually identified and "
            "disposed of, not left in a patient bay or confused with HIC.3's "
            "biomedical-waste stream."
        ),
        how_to_fill=[
            ("Date Identified", "Date the item was identified as not in use."),
            ("Item", "What the item is (bed, monitor, construction debris, expired non-BMW stock, etc.)."),
            ("Tag/Location/Owner", "Tag reference, where it is quarantined, and who authorised condemnation (FMS.3 strike-off if equipment)."),
            ("Quarantined So It Cannot Be Reused? (Y/N)", "Whether it is physically removed from where a patient could be given it."),
            ("Disposal/Sale Date and Method", "How and when it finally left the hospital."),
            ("Confirmed By", "Named facilities lead."),
        ],
        verified_sources=[
            "World Health Organization. (2014). [Safe Management of Wastes from "
            "Health-Care Activities](https://www.who.int/publications-detail-redirect/9789241548564) (2nd ed.). Waste framework only; BMW colour-"
            "coding and SPCB handover remain HIC.3.",
        ],
        column_headers=["Date Identified", "Item", "Tag/Location/Owner",
                         "Quarantined So It Cannot Be Reused? (Y/N)",
                         "Disposal/Sale Date and Method", "Confirmed By"],
        worked_example_row=["10/02/2026", "Patient monitor, obsolete model (FMS.3 struck off)",
                             "Tag #C-0042, condemned store, authorised by Facilities Lead",
                             "Y", "24/03/2026, sold for scrap via approved vendor",
                             "Facilities Lead «Name»"],
        extra_blank_rows=9,
    ),
    RecordSpec(
        oe_code="FMS.2.g",
        oe_requirement="Hazardous materials are identified and used safely within the organisation.",
        record_title="FMS.2 Record 7 — Hazardous-material inventory and safe-use record",
        what_is_this=(
            "The facility-wide inventory of hazardous materials this hospital "
            "actually holds (housekeeping chemicals, fuels, mercury if present, "
            "engineering solvents, bulk stores) with labelling, segregation, PPE "
            "and the spill method -- the chapter's second asterisked, documented-"
            "evidence record."
        ),
        real_example=(
            "A 20-litre diesel drum in the generator room is listed with its label, "
            "storage segregation, required PPE, and the spill-containment method, "
            "distinct from HIC.2's blood-spill SOP and MOM.8's cytotoxic-spill SOP."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- a Core requirement where the organisation "
            "must show hazardous materials are identified and used safely at the "
            "point of use, not filed as a safety data sheet nobody has attached to "
            "the actual container."
        ),
        how_to_fill=[
            ("Material", "Named hazardous material (housekeeping chemical, fuel, mercury, solvent, etc.), or recorded absence of a class not held."),
            ("Location", "Where it is stored/used."),
            ("Labelled and Segregated? (Y/N)", "Whether the actual container is labelled and correctly segregated."),
            ("PPE Required", "PPE specified for safe use."),
            ("Spill Method Reference", "This hospital's building-chemical/mercury/fuel spill method (not HIC.2 blood, MOM.8 cytotoxic, or HIC.3 BMW)."),
            ("Confirmed By", "Named facilities lead."),
        ],
        verified_sources=[
            "Bureau of Indian Standards. (2016). [National Building Code of India, 2016](https://bis.gov.in/others/national-building-code/).",
        ],
        column_headers=["Material", "Location", "Labelled and Segregated? (Y/N)",
                         "PPE Required", "Spill Method Reference", "Confirmed By"],
        worked_example_row=["Diesel (generator fuel)", "Generator room, 20-litre drum, bunded storage",
                             "Y", "Gloves, eye protection",
                             "Facility hazardous-materials spill procedure, s.3 (fuel)",
                             "Facilities Lead «Name»"],
    ),
]


def main() -> None:
    sop_path = OUT_ROOT / "SOP_FMS.2.a_to_g_patient_family_staff_visitor_safety.docx"
    build_sop(SOP, sop_path)
    print(f"built {sop_path}")

    manifest_entries = [{
        "file": sop_path.name,
        "document_type": "sop",
        "standard_code": "FMS.2",
        "title": "Safety of Patients, Families, Staff and Visitors",
    }]

    for idx, rec in enumerate(RECORDS, start=1):
        fname = f"FMS.2_Record_{idx:02d}_{rec.record_title.split('—')[-1].strip().lower().replace(' ', '_').replace(',', '')[:60]}.docx"
        rec_path = OUT_ROOT / "Records" / fname
        build_record(rec, rec_path)
        print(f"built {rec_path}")
        manifest_entries.append({
            "file": f"Records/{fname}",
            "document_type": "record",
            "standard_code": "FMS.2",
            "record_index": idx,
            "title": rec.record_title.split("—")[-1].strip(),
        })

    import json
    manifest_path = OUT_ROOT / "manifest.json"
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing = [e for e in existing if e["standard_code"] != "FMS.2"]
    else:
        existing = []
    existing.extend(manifest_entries)
    manifest_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"updated {manifest_path} ({len(manifest_entries)} FMS.2 entries)")


if __name__ == "__main__":
    main()
