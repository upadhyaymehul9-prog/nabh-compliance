-- FMS.1 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 8 FMS, printed page 116
-- (PDF page index 122). Chapter 8 printed pages 115-120. ONE OE CARRIES THE ASTERISK -- FMS.1.f.
-- UNAPPROVED DRAFT. Do not run this insert until the owner confirms the write.


insert into public.shco_policy_masters (
  standard_code,
  chapter,
  oe_codes,
  policy_title,
  purpose,
  scope,
  policy_statement,
  procedure_steps,
  responsibility,
  references_text,
  distribution,
  abbreviations,
  disclaimer,
  oe_mapping,
  universal_facts_checklist,
  version,
  revision_history,
  status
) values (
  'FMS.1',
  'FMS',
  array['FMS.1.a', 'FMS.1.b', 'FMS.1.c', 'FMS.1.d', 'FMS.1.e', 'FMS.1.f'],
  $q$Planned Facilities, Utilities and Environment-Friendly Measures$q$,
  $q$This document sets out how the environment and facilities of {{HOSPITAL_NAME}} operate in a planned manner and how the organisation promotes environment-friendly measures: how facilities and space provisions match the scope of services; how as-built and updated drawings are maintained as statutory and occupancy documents require; how internal and external sign postings are understood by patients, families and the community; how potable water and electricity are available round the clock; how alternate sources for electricity and water are provided as backup for failure or shortage and how their functioning is tested; and how the organisation takes initiatives toward an energy-efficient and environment-friendly hospital.

The chapter intent is a safe and secure environment for patients, families, staff and visitors, including safe water and electricity, and work toward energy efficiency. A floor plan that does not match the services actually offered, a DG set that is cranked weekly but never takes the essential-circuit load, or a green-hospital poster with no measured initiative, is not that intent.

This document is planned operation of the facility and its utilities, and the energy/environment initiatives. It is not FMS.2 safety devices, monthly rounds, electrical audits, unused-material disposal or hazardous materials. It is not FMS.3 medical-equipment PPM. It is not FMS.4 medical gases. It is not FMS.5 fire and non-fire emergency plans. It is not the billing ledger.$q$,
  $q$This policy applies to the physical facilities of {{HOSPITAL_NAME}}, to the people who plan space, hold drawings, post wayfinding, operate potable-water and electrical systems and their backups, and to those who run energy-efficiency and environment-friendly initiatives.

It covers: appropriateness of facilities and space to the defined scope of services; as-built and updated drawings; internal and external sign postings; round-the-clock potable water and electricity; alternate electricity and water sources and the tests that prove they work; and energy-efficient / environment-friendly initiatives.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- AAC.1 owns the defined scope of services. THIS document's FMS.1.a owns that the built space and facilities are appropriate to that scope. A service the directory does not provide is a recorded absence, not a copied ICU floor plate. AAC.1.b resourcing of defined services is not this space check counted twice.
- AAC.6.e owns radiation, restricted-area, pregnancy-caution and PC-PNDT safety signage. THIS document's FMS.1.c owns hospital-wide internal and external wayfinding in a language patients, families and the community understand. Radiation/PC-PNDT signs are not the wayfinding system, and wayfinding is not those statutory notices counted twice. HANDOFF ACCEPTED from the AAC.6 FMS.1.c flag.
- FMS.2 owns patient-safety devices and infrastructure, facilities for the differently-abled, extra-security/access planning, monthly facility inspection rounds, electrical safety audits, unused-material identification and disposal, and hazardous-materials identification and safe use. Those methods are not this document.
- FMS.3 owns the medical and support-service equipment programme (inventory, PPM, calibration, recalls, downtime). A generator, pump or UPS that is plant is this document's utility; a ventilator or steriliser is FMS.3 equipment. HIC.6 owns steriliser validation as a reprocessing act; it does not become this utility programme.
- FMS.4 owns medical gases, vacuum and compressed air. Piped MGPS plant electricity/water needs may be essential circuits here; the gas programme is FMS.4.
- FMS.5 owns fire and non-fire emergency plans, exit plans, drills, fire-equipment maintenance and service continuity. A power or water failure that becomes an emergency is handed to FMS.5; routine backup testing is this document.
- ROM.3.a owns approval of the strategic plan and budget. Capital for space, plant and energy work may be approved there; the facility method is here. ROM.3 facility KPIs, if used, are inputs; this document does not write the hospital-wide service-standard set.
- ROM.4.a is management's duty that proactive risk exists across the organisation. Facility inspection rounds and the fire plan are FMS.2.d and FMS.5. This document's utilities and drawings may feed that risk system; it does not write it. HANDOFF ACCEPTED: ROM.4 flagged FMS facility method; FMS.2/FMS.5 write rounds and fire; this writes planned utilities.
- PRE.5 owns patient-facing expected cost. This document does not own billing, GST, payer contracts or a facility tariff file. PRE.6 complaint redressal may include a facilities complaint; the complaint route stays PRE.6. HANDOFF ACCEPTED: PRE.5's "ROM/FMS billing" is not absorbed here.
- HIC.2 historically tagged potable-water testing to an Entry-Level "FMS 3 a" checklist row. Under the 3rd Edition, round-the-clock availability of potable water is FMS.1.d; quality testing uses WHO Guidelines for Drinking-water Quality, 4th edition (chapter reference 20) as the framework, not a NABH interval. HIC.3 owns biomedical waste colour, transport and SPCB — not this document. BMW Rules are not restated here.
- HIC.3 kitchen/FSSAI is food, not this potable-water system.
- Coulliette and Arduino (chapter reference 5) is the dialysis-water quality framework. If this hospital does not provide dialysis, that is a recorded absence against AAC.1, not a copied haemodialysis water SOP.
- Indian Public Health Standards 2022 (chapter reference 18) and NBC 2016 (chapter reference 4) are space and building-code frameworks. They are not a NABH bed-count, occupancy-subdivision or sprinkler mandate for every SHCO. NBC 2016 applies insofar as the local building and fire authority has applied it to this facility.
- PSQ.2 owns managerial indicators as quality tools. A utility-failure rate may be supplied from these records; PSQ.2 owns the indicator set.$q$,
  $q${{HOSPITAL_NAME}} requires that facilities and space provisions are appropriate to the scope of services.

{{HOSPITAL_NAME}} maintains as-built and updated drawings as statutory requirements and the occupancy of this building require.

{{HOSPITAL_NAME}} provides internal and external sign postings in a manner understood by patients, families and the community.

{{HOSPITAL_NAME}} requires that potable water and electricity are available round the clock.

{{HOSPITAL_NAME}} provides alternate sources for electricity and water as backup for failure or shortage, and tests their functioning at a predefined frequency.

{{HOSPITAL_NAME}} takes initiatives toward an energy-efficient and environment-friendly hospital.

{{HOSPITAL_NAME}} does not treat a DG set that is cranked but never takes essential-circuit load, a drawing that does not match the built floor, or a green-hospital poster with no measured initiative, as that duty.$q$,
  array[
    $s$1. Facilities and space appropriate to the scope of services

Facilities and space provisions are appropriate to the scope of services.

The defined scope is AAC.1. This step is the built match: waiting, clinical, diagnostic, utility, storage and staff spaces this hospital actually runs can physically hold those services without using a corridor as a ward, a sluice as sterile store, or an undefined specialty's floor plate copied from another hospital.

How appropriateness is judged (against AAC.1 and, as a framework, IPHS 2022 chapter reference 18 and NBC 2016 occupancy as the local authority applied it), who records a mismatch, and what happens when a service is added or withdrawn, are [Hospital to define — how facilities and space are shown to be appropriate to the defined scope of services]. A service the directory does not provide is a recorded absence.$s$,
    $s$2. As-built and updated drawings

As-built and updated drawings are maintained as per statutory requirements.

NBC 2016 (chapter reference 4) is the Indian building-code framework the local building and fire authority typically uses for occupancy, means of egress and services drawings. This step is that this hospital holds the as-built set that occupancy and that authority actually required, and that the set is updated when the building or a major service run changes. A brochure floor plan, or a consultant drawing that was never marked as-built, is not this OE.

Which drawings are held (architectural, structural, electrical single-line, plumbing/water, fire/detection as FMS.5 will use them, medical-gas as FMS.4 will use them if piped), where the controlled set lives, who updates it after a change, and which statutory or occupancy condition requires which sheet, are [Hospital to define — the as-built and updated drawings maintained as statutory and occupancy requirements require]. FMS.5 uses fire drawings; this step holds the controlled set. FMS.4 uses MGPS drawings if a piped system exists.$s$,
    $s$3. Internal and external sign postings

There are internal and external sign postings in the organisation in a manner understood by the patient, families and community.

Wayfinding is this OE: how a first-time family finds the entrance, registration, toilets, emergency, lifts, wards and exit, in language they actually read. AAC.6.e radiation/PC-PNDT/pregnancy signs are safety notices, not this wayfinding system. FMS.5.b exit plans for fire and non-fire emergencies are the emergency exit display; they must be consistent with these signs but are not this OE counted twice.

Languages, scripts, and how a visitor who cannot read the local majority language is still directed, plus who inspects faded or contradictory signs, are [Hospital to define — internal and external sign postings in a manner understood by patients, families and the community].$s$,
    $s$4. Round-the-clock potable water and electricity

Potable water and electricity are available round the clock. This is a Core requirement. Availability is the OE: a tap that should serve patients and a circuit that should serve care are live at 03:00, not only at the morning check.

Potable water. Round-the-clock availability means the points of use this hospital has defined for drinking, clinical wash, kitchen (as HIC.3 uses water, not as this document rewriting HIC.3), CSSD if present, and dialysis if present, actually deliver water when needed. A roof tank that is full on paper while the OT scrub is dry because a valve is shut is a failure of this OE. Quality testing is not a second NABH interval invented here: WHO Guidelines for Drinking-water Quality, 4th edition (chapter reference 20) is the framework for which parameters are tested, at which points, and how often. Those local values are [Hospital to define — potable-water quality-testing parameters, sample points and interval using WHO GDWQ 4th edition as framework, not as a pasted protocol]. Dialysis water, if dialysis is in the AAC.1 directory, uses Coulliette and Arduino (chapter reference 5) as the haemodialysis-water framework; if dialysis is not provided, that is a recorded absence, not a copied RO-plant SOP. Legionella control for aerosolising systems this hospital actually runs (cooling towers, decorative fountains, unused dead-legs) is [Hospital to define — Legionella and stagnant-water control for systems this hospital actually runs], or a recorded absence if none of those systems exist.

Electricity. Round-the-clock availability means essential clinical and life-safety circuits — at minimum the areas this hospital actually runs that cannot wait for restoration: emergency, OT if present, labour, ICU/HDU if present, nursery if present, blood bank if present, ventilators and their compressors, emergency lighting, fire detection (FMS.5), and medical-gas plant or manifold alarms (FMS.4) — remain energised. A live incoming meter with a dark theatre because a changeover never closed is a failure of this OE.

Who watches availability (including night and holiday), how an interruption is recorded, and the restoration target this hospital sets, are [Hospital to define — how round-the-clock potable water and electricity availability is watched, recorded and restored]. This step does not invent a NABH minutes-to-restore clock.$s$,
    $s$5. Alternate electricity and water, and testing that they actually work

Alternate sources for electricity and water are provided as a backup for any failure or shortage, and their functioning is tested at a predefined frequency.

Alternate electricity. The backup is the source that will carry the essential circuits named at step 4 when the incoming supply fails or is shed: diesel generator, UPS/inverter for the circuits that cannot tolerate a start delay (ventilators, monitors, lights over an open table), and any automatic mains-failure changeover this hospital has installed. The failure mode this OE exists to catch is a weekly no-load crank that proves the starter motor, not that the set will take theatre, ICU and emergency lighting together, or a UPS whose batteries have not been discharge-tested. A start-only test is not a functioning test.

How the loaded test is done (essential-circuit load, not the workshop socket), who is present so a changeover failure is seen before a night outage, how fuel, coolant and battery condition are recorded, and the predefined frequency, are [Hospital to define — alternate-electricity source, essential-circuit list, loaded-test method and predefined test frequency]. NBC 2016 (chapter reference 4) and the electrical practice it points at (IS 732 wiring practice and IS 3043 earthing as NBC-pointed frameworks, not as extra paragraph-2 statutes) inform how the installation should behave; they are not a pasted Central Electricity Authority regulation in this document's Disclaimer. Central Electricity Authority electrical-supply regulations are not a numbered FMS chapter reference.

Alternate water. The backup is the source that actually moves water to the points of use at step 4 when the municipal or borewell supply fails or is short: reserve tanks with working float valves, a second borewell if this hospital has one, a tanker contract that can deliver at night, and pumps that auto-start. A sealed tanker MoU with no night number, or a tank whose outlet valve has seized, is not backup.

How the alternate water source is proved (tank-to-tap movement, pump auto-start, tanker mobilisation drill), and the predefined frequency, are [Hospital to define — alternate-water source, the test that proves water actually moves, and the predefined test frequency].

A utility failure that becomes a declared emergency is handed to FMS.5; this step is the test before that night.$s$,
    $s$6. Energy-efficient and environment-friendly initiatives

The organisation takes initiatives towards an energy-efficient and environment friendly hospital. This step is the documented-evidence anchor of an Excellence requirement the standard asterisks. An assessor will ask what was actually done, what it measured, and what changed. The answer must be initiatives with a record, not a green-hospital poster, not a single LED retrofit offered as the whole OE, and not Dhillon (chapter reference 7) copied as if this hospital had implemented a named green-hospital certification.

The reason this is a distinct OE, and not a sentence under utilities, is that FMS.1.d and FMS.1.e are that water and electricity exist and that backup works. This OE is that the organisation takes initiatives toward using less energy and harming the environment less, while still meeting those availability duties. The common error is to file an electricity bill, or a tree-planting photograph, and call that the programme; or to shut HVAC in clinical areas in the name of efficiency so that FMS.1.d availability and HIC environmental conditions fail.

Dhillon, V. S. (2015), Green Hospital and Climate Change (chapter reference 7), is the chapter's green-hospital framework. It is not a mandate to hold a named green-building rating, not a pasted energy-audit form, and not authority to reduce clinical ventilation below what this hospital's services require. Initiatives this hospital actually runs — measured electricity or fuel use, lighting or HVAC set-back in non-clinical hours, solar if installed, rainwater or condensate reuse if installed, segregation of municipal waste from the HIC.3 biomedical stream (this document does not rewrite HIC.3 colours), reduction of single-use non-clinical materials — are recorded with a baseline and a result. HIC.3 remains the BMW colour, transport and SPCB method; environment-friendly hospital here is not a second BMW SOP.

Which initiatives are in force this year, the named owner, the baseline and the review of result, and what is out of scope as HIC.3 BMW or as a certification this hospital does not hold, are [Hospital to define — the energy-efficient and environment-friendly initiatives, with baseline and result, and the named owner]. An unused rooftop solar array, or an energy audit that produced no action, is not this OE.$s$,
    $s$7. Records, review and the order of operations

The space-to-scope record, the controlled as-built drawing set and update log, the wayfinding inspection, potable-water and electricity availability and quality-test records, loaded backup-test records for electricity and water, and the energy/environment initiative file with baseline and result, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for planned-facility and utility records] for: space that matches AAC.1 rather than a copied floor plate; drawings that match the built hospital and the occupancy the authority actually required; wayfinding that is not AAC.6.e radiation signs counted twice; potable water and electricity that were available at night, not only at the morning check; backup tests that took essential-circuit load and that actually moved water, not a no-load crank; energy initiatives with a measured result rather than a poster; dialysis-water method only if dialysis is in AAC.1; and BMW colours left with HIC.3.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a backup test failed under load, or when AAC.1, AAC.6, FMS.2, FMS.4, FMS.5 or HIC.3 that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable that facilities operate as this document requires.

A named facilities or engineering lead holds drawings, utility records, backup tests and the energy-initiative file as this hospital has defined those roles.

Clinical heads confirm that space still matches the AAC.1 services they actually run.

AAC.6.e, FMS.2, FMS.3, FMS.4, FMS.5, HIC.3, ROM.3, ROM.4, PRE.5 and PRE.6 remain the owning methods named in Scope.

The quality or accreditation coordinator audits the records at step 7.

All staff are expected to treat a dark essential circuit, a dry clinical tap, a drawing that does not match the floor, and a green poster with no initiative, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.1.
- National Building Code of India, 2016. Bureau of Indian Standards — chapter reference 4; occupancy, services and as-built drawing framework as the local building and fire authority has applied it to this facility; not a universal sprinkler or bed-count mandate.
- Guidelines for Drinking-water Quality (4th Edition). World Health Organization (2011) — chapter reference 20; potable-water quality-testing framework, not a pasted protocol or a NABH interval.
- Coulliette, A. D., & Arduino, M. J. (2015). Hemodialysis and Water Quality. Semin Dial, 26(4), 427-438 — chapter reference 5; dialysis-water framework only if dialysis is in the AAC.1 directory.
- Dhillon, V. S. (2015). Green Hospital and Climate Change: Their Interrelationship and the Way Forward. JOURNAL OF CLINICAL AND DIAGNOSTIC RESEARCH — chapter reference 7; energy-efficiency framework, not a named rating mandate.
- Indian Public Health Standards. (2022). National Health Mission — chapter reference 18; space-planning framework, not a NABH bed-count mandate.
- Internal documents of {{HOSPITAL_NAME}}: AAC.1 service directory; as-built drawing set; wayfinding; potable-water and electrical records; backup-test records; energy-initiative file; FMS.2, FMS.3, FMS.4, FMS.5; HIC.3; AAC.6.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the named facilities or engineering lead and the quality or accreditation coordinator.

Copies issued to: engineering/facilities staff who operate utilities and backups; department heads whose space must match AAC.1.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder].

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

FMS — Facility Management and Safety (SHCO 3rd Edition Chapter 8)
NBC — National Building Code of India, 2016
DG — diesel generator
UPS — uninterruptible power supply
IPHS — Indian Public Health Standards
GDWQ — WHO Guidelines for Drinking-water Quality
MGPS — medical gas pipeline system
RO — reverse osmosis

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the National Building Code of India, 2016, insofar as the local building and fire authority has applied it to this facility through occupancy, building permission and as-built drawing requirements. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "FMS.1.a", "requirement": "Facilities and space provisions are appropriate to the scope of services.", "steps": "Steps 1, 7", "evidence": "The recorded match of built space to the AAC.1 directory rather than a copied floor plate; recorded absences for unused services; IPHS 2022 and NBC 2016 used as frameworks not bed-count mandates; the audit sample at step 7", "responsible": "Named facilities lead holds the space record; AAC.1 remains the directory; quality or accreditation coordinator audits"}, {"oe_code": "FMS.1.b", "requirement": "As-built and updated drawings are maintained as per statutory requirements.", "steps": "Steps 2, 7", "evidence": "The controlled as-built set the occupancy actually required, with an update log after a building or major-service change, rather than a brochure plan; NBC 2016 as the local-authority framework; FMS.4/FMS.5 use of those sheets recorded as users not second masters; the audit sample at step 7", "responsible": "Named facilities lead holds the controlled set; quality or accreditation coordinator audits"}, {"oe_code": "FMS.1.c", "requirement": "There are internal and external sign postings in the organisation in a manner understood by the patient, families and community.", "steps": "Steps 3, 7", "evidence": "Wayfinding in the languages this hospital has defined, inspected for faded or contradictory signs; the recorded split that AAC.6.e owns radiation/PC-PNDT signs and FMS.5.b owns emergency exit display; the audit sample at step 7", "responsible": "Named facilities lead holds wayfinding; AAC.6.e and FMS.5.b remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "FMS.1.d", "requirement": "Potable water and electricity are available round the clock.", "steps": "Steps 4, 7", "evidence": "Availability records covering night and holiday, not only a morning check; essential-circuit list actually energised; WHO GDWQ 4th edition quality-testing record as framework not a NABH interval; dialysis-water method or recorded absence vs AAC.1; the audit sample at step 7 of a tap and a circuit that worked after hours", "responsible": "Named engineering lead watches availability; HIC.3 kitchen water use remains HIC.3; quality or accreditation coordinator audits"}, {"oe_code": "FMS.1.e", "requirement": "Alternate sources for electricity and water are provided as a backup for any failure/shortage and their functioning is tested at a predefined frequency.", "steps": "Steps 5, 4, 7", "evidence": "Named alternate electricity and water sources; loaded essential-circuit test records at the predefined frequency rather than a no-load crank; tank-to-tap or pump auto-start records rather than a sealed tanker MoU; IS 732/IS 3043 named as NBC-pointed frameworks not extra P2 statutes; the audit sample at step 7", "responsible": "Named engineering lead runs the tests; FMS.5 receives a declared emergency; quality or accreditation coordinator audits"}, {"oe_code": "FMS.1.f", "requirement": "The organisation takes initiatives towards an energy-efficient and environment friendly hospital.", "steps": "Steps 6, 7", "evidence": "The written energy-efficient and environment-friendly initiative file showing named owner, baseline and result for initiatives this hospital actually runs this year rather than a green-hospital poster, a single LED retrofit offered as the whole OE, an unused rooftop array, or an energy audit that produced no action; the recorded use of Dhillon 2015 (chapter reference 7) as a green-hospital framework not a named rating mandate and not authority to cut clinical ventilation below what the services require; the recorded split that FMS.1.d/e remain availability and backup testing and that this OE is measured initiative, and that HIC.3 remains BMW colour, transport and SPCB so environment-friendly hospital is not a second biomedical-waste SOP; induction or briefing of the named owner; the location of the file; the audit sample at step 7 of a baseline that changed a result rather than a photograph", "responsible": "Head of the institution is accountable that initiatives exist; named owner holds the file with baseline and result; HIC.3 remains BMW; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. FMS.1 standard text and all six OEs were read from the official SHCO 3rd Edition PDF, Chapter 8, printed page 116 (PDF page index 122). Header: "The organisation's environment and facilities operate in a planned manner and promotes environment-friendly measures." PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Chapter 8 printed pages 115-120 (PDF indices 121-126). Levels: a Commitment, b Commitment, c Core, d Core, e Commitment, f Excellence.
   ONE OE CARRIES THE ASTERISK -- FMS.1.f. a-e are unasterisked (Tier 2). FMS.1.c and FMS.1.d are Core and still Tier 2 because they are unasterisked; d and e are drafted at technical T2 density under the FMS chapter calibration.
   Asterisks verified 2026-08-18 against the page and scripts/shco_oe_asterisks.json.

TIERING UNDER THE STANDING RULE
1. ONE OF SIX OEs IS TIER 1. Tier 1: f -- step 6 carries the reasoning. Tier 2: a-e, with d/e given named test methods, failure modes and WHO GDWQ / NBC-pointed IS frameworks rather than one-line placeholders. Shallower T1-style reasoning on a-e is a DECISION UNDER THE STANDING RULE; technical substance on d/e is the FMS calibration, not a silent promotion to Tier 1.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-18) of FMS.1.f against HIC.3 BMW and FMS.1.d/e utilities.
   Environment-friendly initiatives vs HIC.3 BMW colours -- HANDOFF ACCEPTED. Stated in Scope and step 6.
   Energy initiative vs cutting clinical power/water -- stated in step 6 so FMS.1.d/e do not fail.
3. FORWARD REFERENCES LANDED: AAC.6.e wayfinding vs radiation signs -- accepted in Scope/step 3. ROM.4 facility method -- utilities here; rounds FMS.2; fire FMS.5. PRE.5 billing -- not absorbed. HIC.2 Entry-Level "FMS 3 a" potable water -- 3rd Edition availability is FMS.1.d.
4. T2 QUICK CHECK: FMS.1.a vs AAC.1 scope -- flagged. FMS.1.b drawings vs FMS.4/FMS.5 users -- flagged. FMS.1.c vs FMS.5.b exit display -- flagged. ROM.3 budget vs this method -- flagged. PSQ.2 indicators -- flagged. Dialysis water vs AAC.1 unused service -- flagged.

STATUTORY AND EXTERNAL FACTS
5. NBC 2016 is chapter reference 4 and is named in P2 insofar as the local building/fire authority applied it (occupancy, permission, as-built drawings). WHO GDWQ is a framework, not a statute. BMW Rules / FSS Act are not in P2. CEA electrical-supply regulations are not a numbered FMS chapter reference and are not in P2; IS 732 and IS 3043 are named as NBC-pointed frameworks only.
6. Coulliette & Arduino -- dialysis water only if dialysis exists. Dhillon -- green-hospital framework, not a rating mandate. IPHS 2022 -- space framework, not a bed-count mandate.
7. NO invented NABH intervals. Quality-test and backup-test frequencies are hospital-defined. No sprinkler, occupancy-subdivision or minutes-to-restore clock as a SHCO-wide NABH mandate.

EDITORIAL POSITIONS TAKEN
8. Availability (1.d) is distinct from backup testing (1.e) and from energy initiatives (1.f).
9. PRE.5 billing is not a facilities tariff. FMS does not own GST/ledger/payer.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
10. P1/P3/P4 shared. P2 names NBC 2016 as applied by the local authority. BMW/FSS/CPA/CEA 2010/MHCA are not imported.

DELIBERATELY NOT INCLUDED
- FMS.2 safety devices, rounds, electrical audits, unused materials, hazardous materials.
- FMS.3 equipment PPM. FMS.4 gases. FMS.5 fire plan.
- BMW colour code (HIC.3). Kitchen FSSAI (HIC.3). Billing (PRE.5 / accounts).
- PESO / Gas Cylinder Rules (not this standard; flagged under FMS.4).
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 14 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 12 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 14; a search for "Hospital to define" without brackets finds all 14, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: space-to-scope method; drawing set and update owner; wayfinding languages and inspection; potable-water quality parameters/points/interval; Legionella/stagnant-water control or absence; availability watch and restoration; alternate electricity loaded-test method and frequency; alternate water test and frequency; energy initiatives with baseline and result; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "18-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
