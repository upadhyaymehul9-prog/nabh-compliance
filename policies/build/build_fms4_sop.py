# -*- coding: utf-8 -*-
"""Builds the SHCO SOP + Records for FMS.4 (Medical Gases, Vacuum and
Compressed Air), following the approved FMS.4 master policy
(shco_policy_masters, status='approved') and the structural template in
sop_record_common.py.

FMS.4 OEs: FMS.4.a-d (4 OEs). doc_required per live shco_full_oes, queried
2026-10-10: FMS.4.a and FMS.4.d are true (Tier 1, full treatment). FMS.4.b
and FMS.4.c are Core but unasterisked (Tier 2).

Source for every procedure step, reference and the division-of-
responsibility language: the approved FMS.4 master policy's
procedure_steps / references_text / responsibility columns (read directly
from shco_policy_masters on 2026-10-10). No new citation or number
introduced beyond what FMS.4 already cites: BCGA, BS EN 12021:2014, HTM
Medical Gas Pipeline Systems, ISO 10524-1/2/3, NFPA Medical Gas and Vacuum
Systems Handbook, NFPA Medical Gas Cylinder Storage, Sarangi et al. (2018),
BOC Handle medical gases safely. The master policy is explicit that FMS.4.d
is a recorded absence (not an invented pipeline SOP) for a hospital with no
piped MGPS -- this SOP preserves that instruction rather than assuming a
piped system exists.
"""
from __future__ import annotations

from pathlib import Path

from sop_record_common import ProcedureBlock, RecordSpec, SOPSpec, build_record, build_sop

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "FMS"

FMS4_REFS = [
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). Facility Management and Safety chapter, standard FMS.4.",
    "British Compressed Gases Association. [Medical Gases guidance notes]"
    "(https://bcga.co.uk/pubcat/guidance-notes/). Handling framework.",
    "British Standards Institution. (2014). [Respiratory equipment — Compressed "
    "gases for breathing apparatus (BS EN 12021:2014)]"
    "(https://knowledge.bsigroup.com/products/respiratory-equipment-compressed-gases-for-breathing-apparatus-2). Medical-air quality "
    "framework where medical air is supplied.",
    "Department of Health, Estates and Facilities Division. (2006). [Medical Gas "
    "Pipeline Systems (HTM 02-01)]"
    "(https://www.england.nhs.uk/wp-content/uploads/2021/05/HTM_02-01_Part_A.pdf). Piped-system inspection/test/maintenance framework, "
    "not a UK certificate mandate.",
    "International Organization for Standardization. (2018-2019). [Pressure "
    "regulators for use with medical gases]"
    "(https://www.iso.org/standard/67190.html) (ISO 10524-1:2018, ISO 10524-2:2018, "
    "ISO 10524-3:2019). Regulator frameworks.",
    "National Fire Protection Association. Medical Gas and Vacuum Systems "
    "Installation Handbook. Framework reference; author not independently "
    "verifiable, cited to the publisher only.",
    "Chrisman, M. (ASHE Management Monograph). [Medical Gas Cylinder and Bulk "
    "Tank Storage](https://ashe.org/tankstorage?page=45), summarizing NFPA 99/101 "
    "cylinder-storage requirements, not a NABH cubic-metre mandate.",
    "Sarangi, S., Babbar, S., & Taneja, D. (2018). [Safety of the medical gas "
    "pipeline system](https://doi.org/10.4103/joacp.JOACP_274_16). Journal of Anaesthesiology Clinical Pharmacology, 34(1), "
    "99-102.",
]

SOP = SOPSpec(
    sop_no="SOP-FMS.4",
    title="Medical Gases, Vacuum and Compressed Air",
    standard_code_range="FMS.4.a-d",
    what_is_this_for=(
        "This SOP tells engineering, theatre, ICU and quality staff, in one place, "
        "how this hospital procures, stores, handles, distributes, uses and "
        "replenishes medical gases; how it keeps alternate sources ready and "
        "actually tested; and -- where a piped system exists -- how that pipeline "
        "is inspected, tested and maintained. If you change a cylinder, open a "
        "plant room, or check gas identity at a workstation, this SOP is for you."
    ),
    worked_example=(
        "A theatre nurse is about to open a new oxygen cylinder at 2am. This SOP "
        "is what tells her to check the cylinder identity and connector before "
        "fitting it, who else must be present for that check, and which record "
        "to log it in -- not to assume the label on the rack is correct."
    ),
    why_nabh_asks=(
        "NABH requires written guidance for the whole gas lifecycle (Commitment, "
        "asterisked), safe handling/storage/distribution/use (Core), tested "
        "alternate sources (Core), and -- where a piped system exists -- an "
        "implemented operational, inspection, testing and maintenance plan "
        "(Commitment, asterisked)."
    ),
    purpose=(
        "To define how «Hospital Name» procures, handles, stores, distributes, "
        "uses and replenishes the medical gases it actually uses; keeps alternate "
        "sources ready and functioning-tested; and -- where a piped medical-gas "
        "pipeline system (MGPS) exists -- operates, inspects, tests and maintains "
        "it."
    ),
    scope=(
        "Applies to every medical gas, vacuum and compressed-air system "
        "{{HOSPITAL_NAME}} actually uses, per the AAC.1 service directory. A gas "
        "this hospital does not use is a recorded absence, not a gap. This SOP "
        "does not cover electrical backup of the plant (FMS.1.e), a gas leak "
        "treated as a declared emergency (FMS.5), or biomedical-waste cylinder "
        "disposal (HIC.3) -- those remain their own documents."
    ),
    responsibilities=[
        ("Head of the Institution",
         "Is accountable that medical gases, vacuum and compressed air are "
         "managed as this SOP requires."),
        ("Named Engineering/Gas-Plant Lead",
         "Holds the written guidance, store checks, backup tests and piped-"
         "system file (or recorded absence)."),
        ("Clinical Users",
         "Check gas identity at the point of use and never force a mismatched "
         "connector."),
        ("Quality/Accreditation Coordinator",
         "Audits a sample of the records this SOP produces, at «Hospital to "
         "define» frequency."),
        ("All Staff",
         "Treat mixed full/empty cylinders, an untested reserve, a forced "
         "connector, or an unlabelled piped terminal, as defects to report."),
    ],
    blocks=[
        ProcedureBlock(
            heading="4.1 Written guidance: procurement, handling, storage, distribution, usage and replenishment (FMS.4.a, Commitment, ASTERISKED)",
            why_it_matters=(
                "A hospital can use oxygen correctly at the theatre table and "
                "still store it against a heater, or buy it correctly and never "
                "replenish the reserve -- this is the chapter's first documented-"
                "evidence anchor because the guidance has to cover the whole "
                "lifecycle, not just the act an assessor happens to ask about."
            ),
            steps=[
                "1. Written guidance governs the implementation of procurement, "
                "handling, storage, distribution, usage and replenishment of "
                "medical gases -- all six acts, not a supplier brochure or a "
                "pocket guide offered as the hospital SOP.",
                "2. «Hospital to define which gases this hospital actually uses» "
                "(oxygen as a minimum if any medical gas is used; nitrous oxide, "
                "medical air, carbon dioxide, vacuum, compressed air only if in "
                "AAC.1), who may procure from which licensed source, how a "
                "delivery is accepted (identity, pressure, pin-index or DISS, "
                "expiry/batch as the supplier provides), and how storage, "
                "distribution, use and replenishment are each governed.",
                "3. A gas the AAC.1 directory does not use is a recorded absence, "
                "not a gap to be explained away. Guidance that covers cylinders in "
                "stores but is silent on who changes a cylinder at 2am does not "
                "satisfy this step.",
                "4. FMS.3's equipment PPM is not this step's gas procurement -- "
                "the two remain separate documents even where the same lead holds "
                "both.",
            ],
            technical_sources=[
                "British Compressed Gases Association. [Medical Gases guidance notes]"
                "(https://bcga.co.uk/pubcat/guidance-notes/).",
                "Chrisman, M. (ASHE Management Monograph). [Medical Gas Cylinder and "
                "Bulk Tank Storage](https://ashe.org/tankstorage?page=45), "
                "summarizing NFPA 99/101 requirements.",
            ],
        ),
        ProcedureBlock(
            heading="4.2 Safe handling, storage, distribution and use (FMS.4.b, Core)",
            why_it_matters=(
                "A \"full\" rack that actually contains empties, or a theatre "
                "opening a new cylinder with no second person checking gas "
                "identity, is this step failing in exactly the moment it matters "
                "most -- at the point of use, not in the store."
            ),
            steps=[
                "1. Medical gases are handled, stored, distributed and used in a "
                "safe manner: full and empty cylinders are segregated; cylinders "
                "are chained or nested, upright, away from oil, grease, heaters "
                "and electrical panels; pin-index/DISS/NIST connections are never "
                "forced; regulators match the ISO 10524 framework.",
                "2. Oxygen-enriched areas are not where a sparking tool is used; "
                "portable cylinders in transit are capped and not rolled on their "
                "side down a stair.",
                "3. «Hospital to define how staff handle, store, distribute and "
                "use medical gases, including full/empty segregation and identity "
                "check at use» -- the check that the gas at the workstation is "
                "the gas intended.",
                "4. The local fire authority's conditions on the occupancy (per "
                "FMS.1/FMS.5) may add store-room conditions; this step still owns "
                "how a porter moves a cylinder. PESO/Gas Cylinder Rules, where "
                "applicable, live on ROM.2.c and are not restated here as a NABH "
                "protocol.",
            ],
        ),
        ProcedureBlock(
            heading="4.3 Alternate sources and tests at a predefined frequency (FMS.4.c, Core)",
            why_it_matters=(
                "A reserve bank that has never been opened on test, or a "
                "changeover that is manual at 3am with no one trained, is not a "
                "backup -- it is a single point of failure that looks like a "
                "backup on paper."
            ),
            steps=[
                "1. Alternate sources for medical gases, vacuum and compressed "
                "air are provided for failure, and their functioning is tested at "
                "a predefined frequency. Alternate oxygen is the reserve that "
                "supplies points of use when the primary manifold bank, primary "
                "cylinders, or primary concentrator fails: a second manifold "
                "bank, a reserve cylinder set sized for the duration this "
                "hospital has defined, or a documented diversion.",
                "2. Alternate vacuum is a portable suction on every critical "
                "point of use if the piped vacuum fails, or a second pump. "
                "Alternate compressed air/medical air is the reserve this "
                "hospital has defined, or a recorded absence if that gas is not "
                "used.",
                "3. The test is a functioning test: gas actually flows from the "
                "alternate source to a defined point of use, vacuum actually "
                "aspirates, alarms actually annunciate. A paper changeover "
                "checklist with no flow is not a test.",
                "4. «Hospital to define which alternate source exists for each "
                "gas/vacuum/air this hospital uses, the functioning-test method, "
                "and the predefined frequency». FMS.1.e remains electrical backup "
                "of the plant; this step is the gas path.",
            ],
            technical_sources=[
                "Department of Health, Estates and Facilities Division. (2006). "
                "[Medical Gas Pipeline Systems (HTM 02-01)](https://www.england.nhs.uk/wp-content/uploads/2021/05/HTM_02-01_Part_A.pdf).",
                "Sarangi, S., Babbar, S., & Taneja, D. (2018). [Safety of the "
                "medical gas pipeline system](https://doi.org/10.4103/joacp.JOACP_274_16). Journal of Anaesthesiology Clinical "
                "Pharmacology, 34(1), 99-102.",
            ],
        ),
        ProcedureBlock(
            heading="4.4 Operational, inspection, testing and maintenance plan for piped installation (FMS.4.d, Commitment, ASTERISKED)",
            why_it_matters=(
                "This is the chapter's second documented-evidence anchor -- but "
                "only where a piped medical-gas pipeline system (MGPS) actually "
                "exists. A commissioning certificate from the year the pipe was "
                "laid is not an implemented plan, and a pipeline SOP invented for "
                "a hospital with no piped system is worse than a recorded "
                "absence."
            ),
            steps=[
                "1. There is an operational, inspection, testing and maintenance "
                "plan for piped medical gas, compressed air and vacuum "
                "installation. If this hospital has no piped MGPS, this OE is a "
                "recorded absence against AAC.1, signed by the named lead -- not "
                "a pipeline SOP written for the sake of assessment.",
                "2. If a piped system exists, the operational plan (who may "
                "isolate a zone, who may open a plant room), the inspection plan "
                "(plant, alarms, terminal units, labelling), the testing plan "
                "(pressure, identity after work, alarm function), and the "
                "maintenance plan (filters, dryers, pumps, manifolds) are "
                "«Hospital to define».",
                "3. Work on a live oxygen pipe is a planned isolation with "
                "clinical notice -- not an ad hoc repair during a live case.",
                "4. A terminal unit that delivers the wrong gas after a repair is "
                "a failure of this OE and a FMS.5 emergency if patients are on "
                "the line.",
            ],
            technical_sources=[
                "Department of Health, Estates and Facilities Division. (2006). "
                "[Medical Gas Pipeline Systems (HTM 02-01)](https://www.england.nhs.uk/wp-content/uploads/2021/05/HTM_02-01_Part_A.pdf).",
                "British Standards Institution. (2014). [Respiratory equipment — "
                "Compressed gases for breathing apparatus (BS EN 12021:2014)](https://knowledge.bsigroup.com/products/respiratory-equipment-compressed-gases-for-breathing-apparatus-2).",
                "International Organization for Standardization. (2018). [Pressure "
                "regulators for use with medical gases (ISO 10524-2:2018)](https://www.iso.org/standard/67190.html).",
                "National Fire Protection Association. Medical Gas and Vacuum Systems "
                "Installation Handbook.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the FMS.4 Records folder).",
    related_documents=[
        "Policy — Medical Gases, Vacuum and Compressed Air (FMS.4)",
        "Hospital's Service Directory (AAC.1)",
        "Hospital's Alternate Electricity/Water Backup SOP (FMS.1.e)",
        "Hospital's Fire and Non-Fire Emergencies SOP (FMS.5)",
        "Hospital's Applicable-Legislation Register (ROM.2.c)",
    ],
    verified_sources=FMS4_REFS,
    review_text=(
        "This policy is reviewed at «Hospital to define the review interval for "
        "this policy», and sooner when a wrong-gas or empty-reserve event "
        "occurred, or when FMS.1, FMS.2, FMS.3, FMS.5 or AAC.1 that this document "
        "hands work to are revised."
    ),
)


RECORDS = [
    RecordSpec(
        oe_code="FMS.4.a",
        oe_requirement="Written guidance governs the implementation of procurement, handling, storage, distribution, usage and replenishment of medical gases.",
        record_title="FMS.4 Record 1 — Medical-gas written-guidance implementation log",
        what_is_this=(
            "A log showing the written gas guidance was actually followed for a "
            "procurement, a store check, a distribution and a replenishment -- not "
            "just that the guidance document exists. The chapter's first "
            "asterisked, documented-evidence record."
        ),
        real_example=(
            "An oxygen cylinder delivery is accepted: the identity, pressure and "
            "batch are checked against the guidance before the delivery is signed "
            "for and moved to store."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- a Commitment requirement where the "
            "organisation must show the written guidance was implemented across "
            "all six acts (procurement, handling, storage, distribution, usage, "
            "replenishment), not filed and ignored."
        ),
        how_to_fill=[
            ("Date", "Date of the procurement/store/distribution/replenishment act."),
            ("Gas", "Which gas this hospital uses (oxygen, nitrous oxide, medical air, etc.)."),
            ("Act Covered", "Procurement / handling / storage / distribution / usage / replenishment."),
            ("Guidance Followed? (Y/N)", "Whether the written guidance was followed for this act."),
            ("Checks Performed", "Identity, pressure, pin-index/DISS, expiry/batch as applicable."),
            ("Confirmed By", "Named engineering/gas-plant lead."),
        ],
        verified_sources=[
            "British Compressed Gases Association. [Medical Gases guidance notes](https://bcga.co.uk/pubcat/guidance-notes/).",
        ],
        column_headers=["Date", "Gas", "Act Covered", "Guidance Followed? (Y/N)",
                         "Checks Performed", "Confirmed By"],
        worked_example_row=["04/02/2026", "Oxygen", "Procurement (delivery acceptance)",
                             "Y", "Identity, pressure, batch checked against supplier note",
                             "Engineering Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.4.b",
        oe_requirement="Medical gases are handled, stored, distributed and used in a safe manner.",
        record_title="FMS.4 Record 2 — Gas store and identity-check record",
        what_is_this=(
            "A record of store checks (full/empty segregation, chaining, "
            "distance from heat/oil) and identity checks at the point of use -- "
            "the two moments where a mix-up actually causes harm."
        ),
        real_example=(
            "A weekly store check finds one 'full' cylinder was actually empty "
            "and mis-racked; it is corrected and logged the same day."
        ),
        why_nabh_asks=(
            "NABH requires safe handling, storage, distribution and use of "
            "medical gases -- a Core requirement checked against the store and "
            "the point of use, not just a written rule."
        ),
        how_to_fill=[
            ("Date of Check", "Date the store or point-of-use check was performed."),
            ("Location", "Gas store, theatre, ICU point of use, etc."),
            ("Full/Empty Segregated? (Y/N)", "Whether full and empty cylinders are correctly segregated."),
            ("Identity Check at Use Performed? (Y/N)", "Whether gas identity was checked before use, where applicable."),
            ("Defect Found", "Any mix-up, forced connector, or storage violation found."),
            ("Confirmed By", "Named engineering lead or clinical user."),
        ],
        verified_sources=[
            "Chrisman, M. (ASHE Management Monograph). [Medical Gas Cylinder and "
            "Bulk Tank Storage](https://ashe.org/tankstorage?page=45), "
            "summarizing NFPA 99/101 requirements.",
        ],
        column_headers=["Date of Check", "Location", "Full/Empty Segregated? (Y/N)",
                         "Identity Check at Use Performed? (Y/N)", "Defect Found", "Confirmed By"],
        worked_example_row=["11/02/2026", "Central gas store", "N (one full cylinder mis-racked as empty)",
                             "N/A", "Mis-racked cylinder corrected same day", "Engineering Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.4.c",
        oe_requirement="Alternate sources for medical gases, vacuum and compressed air are provided for, in case of failure, and their functioning is tested at a predefined frequency.",
        record_title="FMS.4 Record 3 — Alternate gas and vacuum source functioning-test record",
        what_is_this=(
            "A record of functioning tests -- gas actually flowing, vacuum "
            "actually aspirating, alarms actually annunciating -- for every "
            "alternate source this hospital uses, not a paper changeover "
            "checklist."
        ),
        real_example=(
            "The reserve oxygen manifold bank is tested by switching over and "
            "confirming flow at a theatre outlet; the test is logged with the "
            "result, not just that the switch was turned."
        ),
        why_nabh_asks=(
            "NABH requires alternate gas/vacuum/compressed-air sources to be "
            "tested at a predefined frequency -- a Core requirement that a "
            "functioning test, not a paper checklist, must satisfy."
        ),
        how_to_fill=[
            ("Date of Test", "Date the functioning test was run."),
            ("Source Tested", "Reserve manifold bank / portable suction / reserve compressed-air source."),
            ("Point of Use Tested", "Where flow/aspiration/alarm was confirmed."),
            ("Result (Pass/Fail)", "Whether the alternate source actually functioned as required."),
            ("Fault/Observation", "Any fault found, e.g. delayed changeover, alarm failure."),
            ("Confirmed By", "Named engineering lead present at the test."),
        ],
        verified_sources=[
            "Department of Health, Estates and Facilities Division. (2006). "
            "[Medical Gas Pipeline Systems (HTM 02-01)](https://www.england.nhs.uk/wp-content/uploads/2021/05/HTM_02-01_Part_A.pdf).",
        ],
        column_headers=["Date of Test", "Source Tested", "Point of Use Tested",
                         "Result (Pass/Fail)", "Fault/Observation", "Confirmed By"],
        worked_example_row=["20/02/2026", "Reserve oxygen manifold bank", "Theatre 1 outlet",
                             "Pass", "None", "Engineering Lead «Name»"],
    ),
    RecordSpec(
        oe_code="FMS.4.d",
        oe_requirement="There is an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation.",
        record_title="FMS.4 Record 4 — Piped MGPS operational, inspection, testing and maintenance file (or recorded absence)",
        what_is_this=(
            "Where a piped medical-gas pipeline system (MGPS) exists, the file "
            "showing it was actually inspected, tested and maintained -- not just "
            "commissioned once. Where no piped system exists, a signed recorded "
            "absence against AAC.1. The chapter's second asterisked, documented-"
            "evidence record."
        ),
        real_example=(
            "This hospital has a piped oxygen and vacuum system: the quarterly "
            "inspection confirms plant, alarms and terminal-unit labelling are "
            "all correct, and the entry is logged with the inspector's name."
        ),
        why_nabh_asks=(
            "NABH asterisks this OE -- a Commitment requirement where the "
            "organisation must show an implemented plan if a piped system "
            "exists, or a genuine recorded absence if it does not -- never an "
            "invented pipeline SOP for a hospital with no pipeline."
        ),
        how_to_fill=[
            ("Date", "Date of inspection/test/maintenance, or date of the recorded-absence sign-off."),
            ("Piped MGPS Present? (Y/N)", "Whether this hospital has a piped system at all."),
            ("Activity", "Inspection / testing (pressure, identity, alarm) / maintenance (filters, dryers, pumps), or N/A if no MGPS."),
            ("Area/Plant Covered", "Plant room, terminal units, specific zone."),
            ("Result", "Pass/fail or finding; isolation-with-clinical-notice recorded if work was done on a live line."),
            ("Confirmed By", "Named engineering lead (signs the recorded absence if no MGPS)."),
        ],
        verified_sources=[
            "Department of Health, Estates and Facilities Division. (2006). "
            "[Medical Gas Pipeline Systems (HTM 02-01)](https://www.england.nhs.uk/wp-content/uploads/2021/05/HTM_02-01_Part_A.pdf).",
            "International Organization for Standardization. (2018). [Pressure "
            "regulators for use with medical gases (ISO 10524-2:2018)](https://www.iso.org/standard/67190.html).",
        ],
        column_headers=["Date", "Piped MGPS Present? (Y/N)", "Activity", "Area/Plant Covered",
                         "Result", "Confirmed By"],
        worked_example_row=["01/03/2026", "Y", "Quarterly inspection", "Plant room, all terminal units",
                             "Pass — plant, alarms, labelling all correct", "Engineering Lead «Name»"],
    ),
]


def main() -> None:
    sop_path = OUT_ROOT / "SOP_FMS.4.a_to_d_medical_gases_vacuum_compressed_air.docx"
    build_sop(SOP, sop_path)
    print(f"built {sop_path}")

    manifest_entries = [{
        "file": sop_path.name,
        "document_type": "sop",
        "standard_code": "FMS.4",
        "title": "Medical Gases, Vacuum and Compressed Air",
    }]

    for idx, rec in enumerate(RECORDS, start=1):
        fname = f"FMS.4_Record_{idx:02d}_{rec.record_title.split('—')[-1].strip().lower().replace(' ', '_').replace(',', '').replace('/', '-')[:60]}.docx"
        rec_path = OUT_ROOT / "Records" / fname
        build_record(rec, rec_path)
        print(f"built {rec_path}")
        manifest_entries.append({
            "file": f"Records/{fname}",
            "document_type": "record",
            "standard_code": "FMS.4",
            "record_index": idx,
            "title": rec.record_title.split("—")[-1].strip(),
        })

    import json
    manifest_path = OUT_ROOT / "manifest.json"
    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing = [e for e in existing if e["standard_code"] != "FMS.4"]
    else:
        existing = []
    existing.extend(manifest_entries)
    manifest_path.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"updated {manifest_path} ({len(manifest_entries)} FMS.4 entries)")


if __name__ == "__main__":
    main()
