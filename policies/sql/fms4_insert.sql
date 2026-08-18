-- FMS.4 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 8 FMS, printed pages 117-118
-- (PDF page indices 123-124). TWO OEs CARRY THE ASTERISK -- FMS.4.a, d.
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
  'FMS.4',
  'FMS',
  array['FMS.4.a', 'FMS.4.b', 'FMS.4.c', 'FMS.4.d'],
  $q$Medical Gases, Vacuum and Compressed Air$q$,
  $q$This document sets out the programme of {{HOSPITAL_NAME}} for medical gases, vacuum and compressed air: the written guidance that governs procurement, handling, storage, distribution, usage and replenishment of medical gases; safe handling, storage, distribution and use; alternate sources for medical gases, vacuum and compressed air in case of failure and tests of those sources at a predefined frequency; and the operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation where a piped system exists.

The chapter intent includes safe medical gases and vacuum systems. A cylinder store with full and empty mixed, an oxygen manifold whose reserve was never opened on test, or a copied HTM 02-01 manual for a hospital that only uses portable cylinders, is not that intent.

This document is the gas, vacuum and compressed-air programme. It is not FMS.1 electrical backup (though MGPS plant may be an essential circuit there). It is not FMS.3 equipment PPM of a flowmeter inventoried as a device. It is not FMS.5 fire plan, though a gas leak is a non-fire emergency FMS.5 must name. It is not HIC.3 BMW. It is not the billing ledger.$q$,
  $q$This policy applies to medical gases, medical vacuum and medical compressed air used at {{HOSPITAL_NAME}}, whether supplied from portable cylinders, a manifold, or a piped medical gas pipeline system (MGPS), and to the people who procure, handle, store, distribute, use, replenish, test backups and maintain those systems.

It covers: written guidance for procurement, handling, storage, distribution, usage and replenishment of medical gases; safe handling, storage, distribution and use; alternate sources for gases, vacuum and compressed air and tests at a predefined frequency; and operational, inspection, testing and maintenance of piped installation where one exists.

If this hospital has no piped MGPS, FMS.4.d is a recorded absence against AAC.1, not a copied pipeline SOP. Cylinder and manifold duties (a, b, and c insofar as cylinder reserve is the alternate source) still apply if gases are used. If a gas, vacuum or compressed air is not in the AAC.1 directory (for example piped vacuum in a hospital that uses portable suction only), that is a recorded absence, not a copied ICU MGPS SOP.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- AAC.1 unused services: unused piped vacuum or unused MGPS is a recorded absence. HANDOFF ACCEPTED.
- FMS.1.e essential-circuit electricity may include MGPS plant, manifold alarms and vacuum pumps. Plant power is FMS.1; the gas programme is here.
- FMS.2.d monthly rounds may find a leaking cylinder or a blocked manifold room; the finding is closed here. FMS.2.g hazardous materials are building chemicals; cylinders as medical gas are this document. FMS.2.f condemns a surplus regulator through the unused-material route after this inventory releases it.
- FMS.3 may inventory flowmeters, regulators and suction units as devices (PPM/calibration). ISO 10524-1/2/3 (chapter references 14-16) are the regulator frameworks this programme uses; FMS.3 still holds the device file if this hospital lists the regulator as equipment.
- FMS.5 owns fire and non-fire emergency plans. A medical-gas leak, manifold-room fire, or oxygen-enriched fire is a named non-fire or fire emergency there; this document owns prevention, detection at the plant, isolation and backup supply. HANDOFF ACCEPTED from AAC.6 lab fire pointing at FMS.5 — lab fire is FMS.5; oxygen handling is here.
- COP anaesthesia / critical care (COP.10 / COP.5 as drafted) own clinical use of gases at the workstation. This document owns that the gas that arrives is the gas that was intended, at a pressure the workstation can use.
- MOM does not own medical oxygen as a drug in this chapter split; procurement of medical gases is this written guidance. A cylinder that is also a store item still follows this handling SOP.
- ROM.2.c applicable-legislation register is where PESO, Gas Cylinder Rules or the Explosives Act appear if they apply to this occupancy. They are not numbered FMS chapter references and are not in this document's paragraph 2.
- ROM.4.d/e own outsourced filling or pipeline-maintenance agreements with service parameters. The technical tests remain this document.
- HIC.3 BMW: an empty cylinder is not a yellow bag. Do not put BMW in this programme.
- PRE.5 billing is not a gas tariff. HANDOFF ACCEPTED.
- UK DH HTM Medical Gas Pipeline Systems (chapter reference 6), NFPA medical gas / cylinder storage (chapter references 12 and 17), BCGA (2), BS EN 12021 (3), BOC handling (23) and Sarangi et al. (19) are frameworks, not pasted protocols and not a mandate to hold a UK HTM certificate.$q$,
  $q${{HOSPITAL_NAME}} uses written guidance that governs procurement, handling, storage, distribution, usage and replenishment of medical gases.

{{HOSPITAL_NAME}} handles, stores, distributes and uses medical gases in a safe manner.

{{HOSPITAL_NAME}} provides alternate sources for medical gases, vacuum and compressed air in case of failure, and tests their functioning at a predefined frequency.

{{HOSPITAL_NAME}} maintains an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation where a piped system exists.

{{HOSPITAL_NAME}} does not treat a copied HTM manual for a cylinder-only hospital, mixed full and empty cylinders, or an untested manifold reserve, as that duty.$q$,
  array[
    $s$1. Written guidance: procurement, handling, storage, distribution, usage and replenishment

Written guidance governs the implementation of procurement, handling, storage, distribution, usage and replenishment of medical gases. This step is the documented-evidence anchor of a Commitment requirement the standard asterisks. An assessor will ask for the guidance and then to see a procurement, a store, a distribution and a replenishment that followed it. The answer must be implemented written guidance covering all six acts, not a supplier brochure, not a BOC pocket guide offered as the hospital SOP, and not FMS.3 device PPM offered as gas procurement.

The reason the book lists six acts is that a hospital can buy oxygen correctly and still store it against a heater, or use it correctly at the theatre table and never replenish the reserve. BCGA (chapter reference 2), BOC Handle medical gases safely (chapter reference 23) and NFPA Medical Gas Cylinder Storage (chapter reference 17) are handling/storage frameworks. ISO 10524-1/2/3 (chapter references 14-16) are regulator frameworks. They are not pasted as this hospital's guidance. The common error is guidance that covers cylinders in stores and is silent on who changes a cylinder at 02:00, or that names medical air and vacuum in the title for a hospital that has neither.

Which gases this hospital actually uses (oxygen as a minimum if any medical gas is used; nitrous oxide, medical air, carbon dioxide, vacuum, compressed air only if in AAC.1), who may procure from which licensed source, how a delivery is accepted (identity, pressure, pin-index or DISS, expiry/batch as the supplier provides), how storage, distribution, use and replenishment are each governed, are [Hospital to define — written guidance governing procurement, handling, storage, distribution, usage and replenishment of the medical gases this hospital actually uses]. A gas the directory does not use is a recorded absence.$s$,
    $s$2. Safe handling, storage, distribution and use

Medical gases are handled, stored, distributed and used in a safe manner.

This is Core and unasterisked; it is still a technical process. Full and empty are segregated; cylinders are chained or nested, upright, away from oil, grease, heaters and electrical panels; pin-index / DISS / NIST connections are not forced; regulators match ISO 10524 as the framework; oxygen-enriched areas are not the place a sparking tool is used; portable cylinders in transit are capped and not rolled on their side down a stair. NFPA cylinder storage (chapter reference 17) and BOC (chapter reference 23) inform those rules; they are not a NABH cubic-metre threshold for every SHCO. The local fire authority's conditions on the occupancy (NBC 2016 as applied — FMS.5 / FMS.1) may add store-room conditions; this step still owns how a porter moves a cylinder.

The failure mode is a "full" rack that contains empties, a cylinder used as a doorstop, a grease-on-oxygen regulator, or a theatre that opens a new cylinder without a second person to check the gas identity. How staff handle, store, distribute and use, including the check that the gas at the workstation is the gas intended, are [Hospital to define — safe handling, storage, distribution and use of medical gases, including full/empty segregation and identity check at use]. PESO / Gas Cylinder Rules, if they apply, live on ROM.2.c; they are not restated as a NABH protocol here.$s$,
    $s$3. Alternate sources and tests at a predefined frequency

Alternate sources for medical gases, vacuum and compressed air are provided for, in case of failure and their functioning is tested at a predefined frequency.

This is Core and unasterisked; it is still a technical process. Alternate oxygen is the reserve that will supply the points of use when the primary manifold bank, primary cylinders at the bedside, or primary concentrator fails: a second manifold bank, a reserve cylinder set sized for the duration this hospital has defined, or a documented diversion. Alternate vacuum is a portable suction on every critical point of use if the piped vacuum fails, or a second pump. Alternate compressed air / medical air is the reserve this hospital has defined, or a recorded absence if that gas is not used. HTM Medical Gas Pipeline Systems (chapter reference 6) and Sarangi et al. (chapter reference 19) are pipeline-safety frameworks for changeover and alarm; they are not a mandate to install a piped system.

The failure mode is a reserve bank that has never been opened on test, a changeover that is manual at 03:00 with no one trained, or a "portable suction available" that is in a locked CSSD. The test is a functioning test: gas actually flows from the alternate source to a defined point of use, vacuum actually aspirates, alarms actually annunciate. A paper changeover checklist with no flow is not a test.

Which alternate source exists for each gas/vacuum/air this hospital uses, the functioning-test method, and the predefined frequency, are [Hospital to define — alternate sources for medical gases, vacuum and compressed air, the functioning test, and the predefined frequency]. FMS.1.e remains electrical backup of the plant; this step is the gas path.$s$,
    $s$4. Operational, inspection, testing and maintenance plan for piped installation

There is an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation. This step is the documented-evidence anchor of a Commitment requirement the standard asterisks. An assessor will ask to walk the plant room and then to see the last inspection, the last pressure/alarm test and the last maintenance. The answer must be a plan that was operated, not a commissioning certificate from the year the pipe was laid, not HTM 02-01 copied in full, and not FMS.3 PPM of a suction bottle offered as MGPS maintenance.

If this hospital has no piped MGPS, this OE is a recorded absence against AAC.1, signed by the named lead, not a pipeline SOP invented for assessment. If a piped system exists, HTM Medical Gas Pipeline Systems (chapter reference 6) is the inspection/test/maintenance framework (identity, pressure, alarm, isolation, anti-confusion, oil-free air as BS EN 12021 chapter reference 3 where medical air is piped). ISO 10524-2 (chapter reference 15) is the line-regulator framework. NFPA Medical Gas and Vacuum Systems Handbook (chapter reference 12) is a further framework. None of these is a UK or US certificate mandate for an Indian SHCO.

The operational plan (who may isolate a zone, who may open a plant room), the inspection plan (plant, alarms, terminal units, labelling), the testing plan (pressure, identity after work, alarm function), the maintenance plan (filters, dryers, pumps, manifolds), and the rule that work on a live oxygen pipe is a planned isolation with clinical notice, are [Hospital to define — the operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation, or the recorded absence if no piped system exists]. A terminal unit that delivers the wrong gas after a repair is a failure of this OE and a FMS.5 emergency if patients are on the line.$s$,
    $s$5. Records, review and the order of operations

The written gas guidance covering the six acts, safe-handling records (store checks, identity checks), alternate-source functioning-test records at the predefined frequency, and — where a piped system exists — the MGPS operational/inspection/testing/maintenance file, or the recorded absence of a piped system, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for medical-gas records] for: guidance that covers procurement through replenishment of gases actually used; full/empty segregation rather than mixed racks; functioning backup tests rather than a paper changeover; piped-system maintenance that is not a commissioning certificate, or a signed recorded absence if no MGPS; FMS.1.e plant electricity left there; FMS.5 leak-as-emergency left there; AAC.1 unused gases recorded as absences; PESO not invented in paragraph 2; and HIC.3 BMW not used as cylinder disposal.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a wrong-gas or empty-reserve event occurred, or when FMS.1, FMS.2, FMS.3, FMS.5 or AAC.1 that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable that medical gases, vacuum and compressed air are managed as this document requires.

A named engineering or gas-plant lead holds the written guidance, store, backup tests and piped-system file (or recorded absence) as this hospital has defined those roles.

Clinical users check gas identity at the point of use and do not force a mismatched connector.

FMS.1, FMS.2, FMS.3, FMS.5, AAC.1, ROM.2.c, ROM.4 and COP anaesthesia/critical-care documents remain the owning methods named in Scope.

The quality or accreditation coordinator audits the records at step 5.

All staff are expected to treat mixed full and empty cylinders, an untested reserve, a forced connector, and a piped terminal that is unlabelled, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.4.
- Medical Gases. British Compressed Gases Association — chapter reference 2; handling framework.
- Respiratory equipment. Compressed gases for breathing apparatus. BS EN 12021:2014 — chapter reference 3; medical-air quality framework where medical air is supplied.
- Medical Gas Pipeline Systems. (2006). Department of Health: Estates and Facilities Division (HTM) — chapter reference 6; piped-system inspection/test/maintenance framework, not a UK certificate mandate.
- Pressure regulators for use with medical gases — ISO 10524-1:2018, ISO 10524-2:2018, ISO 10524-3:2019 — chapter references 14-16; regulator frameworks.
- Hart, J. R. (2018). Medical Gas and Vacuum Systems Handbook. National Fire Protection Association — chapter reference 12; framework.
- Medical Gas Cylinder Storage. (2018). National Fire Protection Association — chapter reference 17; cylinder-storage framework, not a NABH cubic-metre mandate.
- Sarangi, S., Babbar, S., & Taneja, D. Safety of the medical gas pipeline system. J Anaesthesiol Clin Pharmacol, 34(1), 99-102 — chapter reference 19; framework.
- Handle medical gases safely. BOC. (2017) — chapter reference 23; handling framework, not this hospital's SOP.
- Internal documents of {{HOSPITAL_NAME}}: medical-gas written guidance; cylinder-store checks; backup-test records; MGPS file or recorded absence; FMS.1, FMS.2, FMS.3, FMS.5; AAC.1; ROM.2.c.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the named gas-plant or engineering lead and the quality or accreditation coordinator.

Copies issued to: staff who change cylinders; OT/ICU/emergency leads who use piped or cylinder gas; contracted pipeline maintainer if outsourced.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder].

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

FMS — Facility Management and Safety (SHCO 3rd Edition Chapter 8)
MGPS — medical gas pipeline system
HTM — Health Technical Memorandum (UK DH medical-gas pipeline guidance; framework only)
DISS — Diameter Index Safety System
NIST — Non-Interchangeable Screw Thread
PESO — Petroleum and Explosives Safety Organisation (ROM.2.c register if applicable; not a paragraph-2 statute of this document)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

The requirements in this document are accreditation requirements of the NABH SHCO 3rd Edition rather than duties under a named Act of Parliament. In particular those arising under no named Act of Parliament; the duties in this document are accreditation requirements of the NABH SHCO 3rd Edition are written here as accreditation method, not as a copied statute. This policy does not import the Consumer Protection Act, 2019, the Clinical Establishments Act, 2010, or the Mental Healthcare Act, 2017 as a checklist. Statutory duties that arise under other documents of {{HOSPITAL_NAME}} remain those documents. {{HOSPITAL_NAME}} is responsible for verifying any statutory duty that applies to it; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "FMS.4.a", "requirement": "Written guidance governs the implementation of procurement, handling, storage, distribution, usage and replenishment of medical gases.", "steps": "Steps 1, 5", "evidence": "The written guidance covering procurement, handling, storage, distribution, usage and replenishment of the gases this hospital actually uses, with sample records of a delivery accepted, a store, a distribution and a replenishment that followed it, rather than a supplier brochure or a BOC pocket guide offered as the hospital SOP; recorded absences for gases not in AAC.1; the recorded use of BCGA, BOC, NFPA cylinder storage and ISO 10524 as frameworks not pasted protocols; induction of staff who procure or change cylinders; the location of the guidance; the audit sample at step 5 of all six acts present rather than store-only guidance", "responsible": "Named gas-plant lead holds the written guidance; AAC.1 remains the directory; quality or accreditation coordinator audits"}, {"oe_code": "FMS.4.b", "requirement": "Medical gases are handled, stored, distributed and used in a safe manner", "steps": "Steps 2, 5", "evidence": "Store checks showing full/empty segregation, chained upright cylinders, matched regulators (ISO 10524 framework) and identity check at use rather than a cylinder used as a doorstop; PESO flagged to ROM.2.c not P2; the audit sample at step 5", "responsible": "Named gas-plant lead with clinical users at the point of use; quality or accreditation coordinator audits"}, {"oe_code": "FMS.4.c", "requirement": "Alternate sources for medical gases, vacuum and compressed air are provided for, in case of failure and their functioning is tested at a predefined frequency", "steps": "Steps 3, 5", "evidence": "Named alternate sources for each gas/vacuum/air actually used; functioning-test records (flow from the reserve, vacuum that aspirates, alarms that annunciate) at the predefined frequency rather than a paper changeover; recorded absences where a gas is not used; split from FMS.1.e plant electricity; the audit sample at step 5", "responsible": "Named gas-plant lead runs functioning tests; FMS.1.e remains electrical backup; quality or accreditation coordinator audits"}, {"oe_code": "FMS.4.d", "requirement": "There is an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation.", "steps": "Steps 4, 5", "evidence": "The piped-system operational, inspection, testing and maintenance file showing last inspection, pressure/alarm test and maintenance rather than a commissioning certificate from the year the pipe was laid, or the signed recorded absence against AAC.1 if this hospital has no piped MGPS rather than a copied pipeline SOP; the recorded use of HTM medical-gas pipeline (chapter reference 6), ISO 10524-2, NFPA handbook and BS EN 12021 as frameworks not UK/US certificate mandates; the recorded split that FMS.3 may still hold a regulator device file and FMS.5 owns a wrong-gas or leak emergency; induction of staff who may isolate a zone; the location of the MGPS file or absence record; the audit sample at step 5 of a terminal unit identity/pressure check or of the signed absence", "responsible": "Named gas-plant lead holds the MGPS plan or the recorded absence; AAC.1 remains unused-service rules; FMS.5 remains emergency plans; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. FMS.4 standard text and OEs a-b were read from the official SHCO 3rd Edition PDF, Chapter 8, printed page 117 (PDF page index 123); OEs c-d from printed page 118 (PDF page index 124). OE-page header has no period after "compressed air". FMS.4.b and FMS.4.c have no terminal period in the book — preserved in mapping requirement fields. PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Commitment, b Core, c Core, d Commitment.
   TWO OEs CARRY THE ASTERISK -- FMS.4.a and FMS.4.d. b and c are Core and still Tier 2 because they are unasterisked; they are drafted at technical T2 density.
   Asterisks verified 2026-08-18 against the pages and scripts/shco_oe_asterisks.json.

TIERING UNDER THE STANDING RULE
1. TWO OF FOUR OEs ARE TIER 1. Tier 1: a, d -- steps 1 and 4 carry the reasoning. Tier 2: b, c, with named failure modes and HTM/ISO/NFPA/BCGA frameworks. Shallower T1-style reasoning on b/c is a DECISION UNDER THE STANDING RULE.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-18) of FMS.4.a/d against AAC.1, FMS.1.e, FMS.3, FMS.5.
   Unused MGPS vs AAC.1 recorded absence -- HANDOFF ACCEPTED.
   Plant electricity vs gas path -- FMS.1.e vs this document.
   Regulator as device (FMS.3) vs gas programme -- both named.
   Leak/wrong-gas as emergency -- FMS.5.
3. FORWARD REFERENCES LANDED: AAC.6 lab fire vs this oxygen handling vs FMS.5 fire plan. PRE.5 billing -- not absorbed. ROM.4 outsourcing of filling/pipeline -- service parameters there, tests here.
4. T2 QUICK CHECK: FMS.4.b vs FMS.2.g hazardous materials -- flagged (cylinders here). FMS.4.c vs FMS.1.e -- flagged.

STATUTORY AND EXTERNAL FACTS
5. No named Act is a numbered FMS gas reference. P2 is accreditation-only. PESO / Gas Cylinder Rules / Explosives Act are flagged to ROM.2.c, not forced into P2. NBC 2016 may condition the store via occupancy; fire plan remains FMS.5.
6. HTM / ISO 10524 / NFPA / BCGA / BS EN 12021 / BOC / Sarangi -- frameworks, not pasted protocols, not foreign certificates.
7. No invented NABH cylinder-store cubic-metre or test-interval mandate. Functioning-test frequency is hospital-defined.

EDITORIAL POSITIONS TAKEN
8. Cylinder-only hospitals still owe a, b, and c; d is a recorded absence if no piped system.
9. MOM does not absorb medical-oxygen procurement in this split.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
10. P1/P3/P4 shared. P2 uses make_disclaimer_accreditation_only(). BMW/FSS/CPA/CEA 2010/MHCA/PESO are not imported.

DELIBERATELY NOT INCLUDED
- Fire-plan method (FMS.5). Electrical backup method (FMS.1.e). Device PPM (FMS.3) except regulator-as-device split.
- BMW. Billing. A pasted HTM 02-01.
- PESO in P2.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 9 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 7 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 9; a search for "Hospital to define" without brackets finds all 9, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: written guidance covering the six acts for gases actually used; safe-handling method; alternate sources, functioning test and frequency; MGPS OITM plan or recorded absence; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "18-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
