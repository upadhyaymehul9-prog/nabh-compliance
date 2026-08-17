# -*- coding: utf-8 -*-
"""Builds the MOM.2 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): MOM.2.c, MOM.2.e
  Tier 2 (lighter pass):   MOM.2.a, MOM.2.b, MOM.2.d, MOM.2.f

TWO of six OEs are asterisked. The draft builds deep blocks for c and e.
a, b, d and f are lean.

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 3 Management of Medication, standard MOM.2 and OEs
MOM.2.a-f, read from the official standards PDF (downloaded 2026-08-17 from the
NABH website's Explore NABH Standards page), printed pages 76-77, PDF page
index 82-83.

Asterisks verified 2026-08-17: scripts/asterisk_extract.py re-run against that
download (self-validation passed, 408 OEs, 132 asterisks, output matched the
committed scripts/shco_oe_asterisks.json on all 408 entries) and the MOM.2 pages
read directly. MOM.2.c and MOM.2.e carry the asterisk; MOM.2.a, MOM.2.b, MOM.2.d
and MOM.2.f are unasterisked.
"""
from policy_build_common import emit_and_verify, make_disclaimer

STANDARD_CODE = "MOM.2"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.2.a", "MOM.2.b", "MOM.2.c", "MOM.2.d", "MOM.2.e", "MOM.2.f",
]
TIER1_OES = ["MOM.2.c", "MOM.2.e"]

POLICY_TITLE = "Storage and Availability of Medications"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} stores medications so that they are available where they are required: a clean, safe and secure environment that incorporates the manufacturer's recommendations; inventory control throughout the organisation; a defined list of high-risk medications including look-alike/sound-alike items and a mechanism for storing them; high-risk medications stored where they are clinically necessary; a defined emergency-medication list stored uniformly; and emergency medications available at all times and replenished promptly when used.

The chapter intent is a safe and organised medication process. Availability and safe storage are governed by written guidance. The pharmacy has oversight of medications stocked out of the pharmacy. Emergency medications are standardised throughout the organisation, readily available, and replenished promptly. This document is that storage and availability process. It is not the formulary-and-committee policy, and it is not the prescription policy.

Blood and blood components are not stored here as ward-stock medicines; the clinical transfusion method, including storage pending transfusion, is the transfusion policy of {{HOSPITAL_NAME}}. Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are stored under the controlled-agents policy, not under this cupboard. Implantable prosthesis and medical devices are not this stock."""

SCOPE = """This policy applies to every location at {{HOSPITAL_NAME}} in which a medicine is stored: the pharmacy, every ward cupboard and trolley, the emergency area, the operation theatre and recovery, intensive or high-dependency areas where they exist, day-care, the ambulance insofar as emergency medicines are carried, and any other clinical location that holds stock. It binds the pharmacy, the staff who check and replenish, and the multidisciplinary medication committee insofar as it oversees floor stock.

It covers: storage in a clean, safe and secure environment incorporating the manufacturer's recommendations; sound inventory control throughout the organisation; a defined list and mechanism for storage of high-risk medications including look-alike/sound-alike medications; storage of high-risk medications in areas where it is clinically necessary; a defined emergency-medication list stored uniformly; and emergency medications available all the time and replenished promptly when used.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The formulary, the multidisciplinary committee, acquisition, and obtainment when the pharmacy is closed are governed by the pharmacy-committee policy of {{HOSPITAL_NAME}} (MOM.1). This document stores what that process has acquired. It does not rewrite the formulary.
- Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents — secure storage, cupboard, register and destruction — are governed by MOM.8 (not yet drafted). This document's Scope hands that storage to MOM.8. The Narcotic Drugs and Psychotropic Substances Act, 1985 is not inherited here as a wholesale storage statute. An NDPS item is not stored under this policy's ordinary cupboard even if it is also high-risk or an emergency medicine; MOM.8 owns that cupboard. Chemo and radioactive preparation and storage likewise wait for MOM.8.
- Implantable prosthesis and medical devices are governed by MOM.9 (not yet drafted).
- Transfusion of blood and blood components is governed by the transfusion policy of {{HOSPITAL_NAME}} (COP.5). Units are not ward-stock medicines under this process. COP.5 owns storage pending transfusion. This document does not restate hanging a unit.
- Cardio-pulmonary resuscitation kits in named areas are governed by the resuscitation policy of {{HOSPITAL_NAME}} (COP.3). COP.3 owns that a resuscitation kit is present in the areas the hospital has named, and that used items are restored to ready. This document owns the hospital-wide emergency-medication list, uniform storage of those medicines, availability at all times, and replenishment when used. COP.3 does not print this list. This document does not print a kit inventory as a mandated crash-cart contents list. Split: COP.3 = kit presence for CPR; MOM.2 = emergency-medicine list, uniform storage, always available, replenish.
- Emergency-area operation, ambulance equipment and the emergency medicines carried on the ambulance as part of ambulance fitness are governed by the emergency-care policy of {{HOSPITAL_NAME}} (COP.2). COP.2 owns that the ambulance is stocked with the emergency medications this hospital has listed. This document owns that list and the uniform storage and replenishment of those medicines wherever they are held, including the emergency area. Neither prints a mandated kit list.
- Procedural sedation and anaesthesia are governed by COP.9 and COP.10. Those policies own the clinical act. This document stores the medicines those acts use, except that any narcotic or psychotropic among them is stored under MOM.8. This document does not write sedation or anaesthetic method.
- Two identifiers at the point of care are governed by COP.1. The unique identification number is generated under AAC.2. Applied, not rewritten.
- The service directory is governed by AAC.1. Emergency medicines and high-risk stock must match defined services.
- Safe injection is governed by HIC.2. Pharmaceutical waste, including expired stock, enters HIC.3. This document requires that expired stock is not left as if it were available; it does not restate colour categories and does not name the Bio-Medical Waste Management Rules in the statutory paragraph of the disclaimer.
- Device-associated care bundles are governed by HIC.4. They are not this storage process.
- Counselling about medicines is governed by PRE (not yet drafted). The medical record itself is governed by IMS (not yet drafted)."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} stores medications in a clean, safe and secure environment, incorporating the manufacturer's recommendations. A cupboard that is unlocked because it is inconvenient, or a refrigerator used for food and medicines together, is not that environment.

{{HOSPITAL_NAME}} applies sound inventory control to medications throughout the organisation, including stock held outside the pharmacy.

{{HOSPITAL_NAME}} defines a list of high-risk medications, including look-alike/sound-alike medications, and a mechanism for storing them. The list is this hospital's. A printed international list left unadapted is not that list.

{{HOSPITAL_NAME}} stores high-risk medications in the areas where they are clinically necessary, and not as a default in every cupboard.

{{HOSPITAL_NAME}} defines a list of emergency medications and stores that list uniformly wherever those medicines are held.

{{HOSPITAL_NAME}} keeps emergency medications available all the time and replenishes them promptly when used. A drawer that was emptied at the last crash and not refilled is not availability."""

PROCEDURE_STEPS = [
"""1. Clean, safe and secure storage incorporating the manufacturer's recommendations

Medications are stored in a clean, safe and secure environment, incorporating the manufacturer's recommendation(s).

The locations in which medications are stored, and the method that keeps those locations clean, safe and secure, are [Hospital to define — the locations in which medications are stored, and the method that keeps those locations clean, safe and secure]. Secure means access is limited to named staff; it is not an unlocked trolley in a corridor. Clean means the storage is not a food refrigerator, a dirty utility, or a shelf with spills left on it. Manufacturer's recommendations means the conditions on the product (light, temperature band, or other stated condition) are followed as written on that product. This document does not state a temperature in degrees, a humidity figure, or a cold-chain hour. Those values, where the hospital must set a local operating figure, are [Hospital to define — any local operating figures for storage conditions, taken from the manufacturer's recommendation for the products stocked, not invented here as NABH mandates].

The Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules govern storage of medicines insofar as they set conditions and schedules. This step follows those conditions. It does not reprint the schedules. It does not name the Narcotic Drugs and Psychotropic Substances Act; NDPS, chemo and radioactive storage are MOM.8.

Expired or unusable stock is removed from the location that looks like available stock and enters the pharmaceutical-waste stream under HIC.3. This step does not restate colour categories.

Pharmacy oversight of floor-stock, as the pharmacy-committee policy requires, includes that these locations are known to the pharmacy.""",

"""2. Inventory control throughout the organisation

Sound inventory control practices guide storage of the medications throughout the organisation.

The inventory-control method used in the pharmacy and in every location that holds stock outside the pharmacy is [Hospital to define — the inventory-control method used in the pharmacy and in every out-of-pharmacy stock location]. Throughout means ward cupboards, trolleys, the emergency area, theatre and the ambulance are in the same method, not only the pharmacy bin card. The method records what is held, that it is within expiry, and that near-expiry is handled so that an expired strip is not the one that is given. This document does not mandate a named inventory system, a number of days of stock, or a near-expiry window in days.

Acquisition remains the pharmacy-committee policy. This step stores and accounts for what was acquired. After-hours obtainment under that policy is deducted here when the pharmacy reopens.""",

"""3. High-risk medications including look-alike/sound-alike — list and storage mechanism

{{HOSPITAL_NAME}} defines a list of high-risk medications, including look-alike/sound-alike medications, and a mechanism for storing them. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask which medicines this hospital treats as high-risk and how they are stored so that the wrong one is not picked. The answer must be this hospital's list and this hospital's storage mechanism, in use on the ward, not a printout of an international table in a quality file.

The reason a local list and a storage mechanism are the safety step is that high-risk harm is a picking error and a look-alike error, not a theory. Concentrated electrolytes stored next to ordinary saline, two bottles whose names differ by a letter standing together on a shelf, a look-alike pair that is obvious to the pharmacist and invisible to the night nurse, are how a listed risk becomes a given dose. The failure without this step is "we know which ones are dangerous" with no list and no physical separation. The common error is to pin up the Institute for Safe Medication Practices high-alert list or the confused-drug-names list and to leave storage unchanged. Those lists (chapter references 3, 4, 7, 12 and 14, and the Malaysian LASA guide at chapter reference 5) are frameworks this hospital may use. They are not mandated as this hospital's list. Tall Man lettering is a method the hospital may adopt; it is not required by name.

The high-risk list, including look-alike/sound-alike pairs, is [Hospital to define — this hospital's list of high-risk medications, including look-alike/sound-alike pairs]. The list matches the formulary and the services defined under AAC.1. A pair this hospital does not stock is not on the list as decoration. A concentrated electrolyte this hospital does stock is on the list if the hospital's method treats it as high-risk. The multidisciplinary medication committee under the pharmacy-committee policy keeps this list current when the formulary changes.

The mechanism for storing those medications is [Hospital to define — the mechanism for storing high-risk medications including look-alike/sound-alike medications]. Mechanism means a physical and procedural method: how they are separated, how they are labelled in the location, who may access them, and how a pick is checked. This document does not mandate a colour, a shelf height, or a named labelling convention. It requires that the mechanism exists and is the same idea in every location that holds the item, so that a nurse moving from ward to theatre does not meet a different habit.

NDPS, chemo and radioactive agents that are also high-risk are stored under MOM.8, not under this mechanism's ordinary cupboard. This list may name them as high-risk; the cupboard is still MOM.8. Sedative and anaesthetic medicines that are not NDPS are stored under this mechanism where they are high-risk; the clinical act remains COP.9 or COP.10.

The list and the storage mechanism are held at [Hospital to define — where the high-risk and look-alike/sound-alike list and the storage mechanism are held], including in every location that stocks an item on the list. A list that lives only in the pharmacy is not a mechanism the ward can use.""",

"""4. High-risk medications stored where clinically necessary

High-risk medications are stored in areas of the organisation where it is clinically necessary.

The areas in which each high-risk item is stored, and the clinical reason it is stored there, are [Hospital to define — the areas in which each high-risk item is stored, and the clinical reason it is stored there]. Clinically necessary means the item is needed for the work of that area, not that every cupboard copies the pharmacy. Concentrated items that are not needed on a general ward are not stored there by default. An area that needs the item for the service it provides stores it under the mechanism at step 3.

This step does not extend NDPS storage into a ward cupboard; MOM.8 still owns that cupboard even where clinical necessity exists.""",

"""5. Emergency-medication list defined and stored uniformly

The list of emergency medications is defined and is stored uniformly. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask what this hospital treats as an emergency medicine and whether the drawer in the emergency area, the ward, and theatre hold the same things in the same way. The answer must be one list and one arrangement, not a different crash habit in each room.

The reason a defined list stored uniformly is the safety step is that emergency medicines fail at the moment of use, when the person opening the drawer is not the person who stocked it. A lidocaine that is on the left in theatre and on the right on the ward, an item present in the emergency area and missing on the medical ward, a trolley whose contents depend on which nurse last tidied it, are how "we have emergency medicines" becomes a search during a crash. The chapter intent stresses that emergency medications are standardised throughout the organisation. The common error is to treat the resuscitation policy's kit as this list — a crash-cart contents page copied from a training course, different in each area, never reconciled with pharmacy. COP.3 owns that a resuscitation kit exists in named areas. This step owns the medicines on the emergency list, the uniform way they are stored, and, with step 6, that they are always there and refilled. This document does not print a kit list. COP.3 does not print this list.

The emergency-medication list is [Hospital to define — this hospital's emergency-medication list]. The list matches the services defined under AAC.1 and the emergency work this hospital actually holds out. It is not a generic tertiary-hospital cart. Items that are also NDPS remain in the MOM.8 cupboard even if they appear on this list; this list does not create a second narcotic drawer. Items used in sedation or anaesthesia that are on this list are stored here as emergency stock; the clinical act remains COP.9 or COP.10.

Uniform storage means [Hospital to define — how emergency medications are stored uniformly wherever they are held: the arrangement, the locations, and how a location is kept to the same arrangement]. Uniform means a person who can find an item in one named location can find the same item in the same relative place in every other named location that holds the list. It does not mean every cupboard in the building holds emergency medicines — locations are named. It does mean that those named locations do not each invent an arrangement. The ambulance, where COP.2 requires emergency medicines, uses this list and this arrangement insofar as the ambulance carries those medicines.

The list and the uniform-storage method are held at [Hospital to define — where the emergency-medication list and the uniform-storage method are held], including in every named location. The multidisciplinary medication committee reviews the list when services change.""",

"""6. Emergency medications available all the time and replenished promptly

Emergency medications are available all the time and are replenished promptly when used.

All the time means every hour the hospital has a patient, including nights, weekends and holidays. A list that is complete at the morning check and empty after an evening event, with no refill until the next working day, is not availability.

How completeness is checked, and how used items are replenished, are [Hospital to define — how completeness of emergency medications is checked, and how used items are replenished]. Promptly is this hospital's definition of the refill, not a number of minutes stated here as a mandate. After a resuscitation, COP.3 restores the kit to ready, including sending reusable equipment for reprocessing. This step replenishes the medicines. The two acts are coordinated; neither is a substitute for the other. A used ampoule is not left as a gap because "the trolley was checked last week".

Expired emergency stock is removed and replaced before it is the only stock. Pharmaceutical waste of the removed item follows HIC.3.""",

"""7. Records, review and the order of operations

Every storage-location list, inventory record, high-risk list, look-alike/sound-alike pair, emergency-medication list, completeness check and replenishment is recorded and is retrievable. Patient-specific replenishment after use carries the unique identification number where a patient event caused the use.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for medication-storage, high-risk and emergency-medication records] for: storage locations that are clean, safe, secure and aligned to the manufacturer's recommendation rather than a food refrigerator; inventory that includes out-of-pharmacy stock; a high-risk and look-alike/sound-alike list that is this hospital's and a storage mechanism in use, not only a pinned international table; high-risk items stored where clinically necessary rather than in every cupboard; an emergency-medication list stored uniformly in named locations; and emergency medicines present and replenished rather than left empty after use. NDPS items found in an ordinary cupboard are a defect of the MOM.8 boundary.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a look-alike pick, an empty emergency drawer, a high-risk item stored where it was not needed, or a revision of the pharmacy-committee, resuscitation, emergency-care, transfusion or controlled-agents policies that this document hands work to, exposes a gap.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} storing medicines in a clean, safe and secure way, for a high-risk list that is actually used, and for emergency medicines that are present when they are needed.

The person in charge of the pharmacy holds the high-risk list and the emergency-medication list, oversees floor-stock storage, and replenishes after use. The named pharmacy lead is [Hospital to define — the named person in charge of pharmacy storage].

Nursing and clinical staff in each named location keep that location to the uniform emergency arrangement, apply the high-risk storage mechanism, check completeness, and report a gap rather than working around it.

The multidisciplinary medication committee under the pharmacy-committee policy keeps the high-risk and emergency lists current when the formulary or the service directory changes.

Staff who run a resuscitation restore the kit under COP.3; this hospital's pharmacy replenishes the medicines under this document.

The quality or accreditation coordinator audits the records at step 7 and reports findings to the head of the institution.

All staff are expected to treat an unlocked medicine store, a look-alike pair stored as if they were ordinary neighbours, and an emergency drawer left empty after use, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.2.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules — insofar as they govern storage of medicines (conditions and schedules). This document does not cite the Narcotic Drugs and Psychotropic Substances Act, 1985; that storage is MOM.8.
- High-Alert Medications in Acute Care Settings, Institute for Safe Medication Practices (2018) — chapter reference 7; a recognised framework the hospital may use when writing its high-risk list; not mandated as the list.
- List of Confused Drug Names, Institute for Safe Medication Practices (2019) — chapter reference 12; a recognised look-alike/sound-alike framework; not mandated as the hospital's pairs.
- FDA and ISMP Lists of Look-Alike Drug Names with Recommended Tall Man Letters (2016) — chapter reference 4; Tall Man lettering is a method the hospital may adopt; not required by name.
- Bryan R, Aronson JK, Williams A, Jordan S. The problem of look-alike, sound-alike name errors: Drivers and solutions. Br J Clin Pharmacol. 2021;87:386–394 — chapter reference 3; informs why a storage mechanism is needed; not imported as a protocol.
- Look-Alike, Sound-Alike Medication Names, World Health Organization (2017) — chapter reference 14; a recognised patient-safety solution; not a mandated pair list.
- Guide on handling look alike, sound alike medications, Ministry of Health, Malaysia (2012) — chapter reference 5; a recognised guide the hospital may draw on; not pasted.
- High-Risk Medicines, Clinical Excellence Commission — chapter reference 8; a recognised framework; not mandated.
- Internal documents of {{HOSPITAL_NAME}}: the storage-location method; the inventory-control method; the high-risk and look-alike/sound-alike list and storage mechanism; the emergency-medication list and uniform-storage method; the completeness-check and replenishment method; the formulary and pharmacy-committee policy; the resuscitation policy; the emergency-care policy; the transfusion policy; the sedation and anaesthesia policies; the controlled-agents policy; and the infection-control policies."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: the pharmacy; every in-patient ward; the emergency area; the operation theatre and recovery; intensive or high-dependency areas where they exist; day-care; the ambulance arrangement; nursing administration; and the members of the multidisciplinary medication committee.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The high-risk list, the look-alike/sound-alike pairs, the storage mechanism, the emergency-medication list and the uniform-storage arrangement — the working documents this policy requires — are held in every location that stocks those medicines.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

ISMP — Institute for Safe Medication Practices
LASA — Look-Alike Sound-Alike
NDPS — Narcotic Drugs and Psychotropic Substances (Act, 1985), named only as the statute MOM.8 will own; not inherited here

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

STATUTE_CLAUSE = (
    "the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, insofar as they "
    "govern storage of medicines (conditions and schedules)"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.2.a",
        "requirement": "Medications are stored in a clean, safe and secure environment, incorporating the manufacturer's recommendations.",
        "steps": "Steps 1, 7",
        "evidence": "The named storage locations and the method that keeps them clean, safe and secure; any local operating figures taken from the manufacturer's recommendation rather than invented as mandates; records of expired stock removed into the HIC.3 stream; the recorded division that NDPS/chemo/radioactive storage is MOM.8; the audit sample at step 7 of locations that are not a food refrigerator or an unlocked corridor trolley",
        "responsible": "Person in charge of the pharmacy oversees locations; nursing staff in each location keep them clean, safe and secure; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.2.b",
        "requirement": "Sound inventory control practices guide storage of medications throughout the organisation.",
        "steps": "Steps 2, 7",
        "evidence": "The written inventory-control method covering pharmacy and every out-of-pharmacy stock location; sample records of what is held, expiry and near-expiry handling; records of after-hours obtainment deducted when the pharmacy reopened; the audit sample at step 7 of inventory that includes ward and emergency-area stock, not only the pharmacy",
        "responsible": "Person in charge of the pharmacy runs inventory; location staff count and report; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.2.c",
        "requirement": "The organisation defines a list of high-risk medications, including look-alike/sound-alike medications, and a mechanism for storing them.",
        "steps": "Steps 3, 4, 7",
        "evidence": "This hospital's dated high-risk list including look-alike/sound-alike pairs, matching the current formulary and the service directory rather than an unadapted ISMP high-alert or confused-names printout left as decoration, and showing that a pair this hospital does not stock is not on the list and that a concentrated electrolyte this hospital does stock is on the list if the hospital's method treats it as high-risk; the written storage mechanism stating how those items are separated, how they are labelled in the location, who may access them, and how a pick is checked, without a mandated colour, shelf height or named labelling convention, and showing the same idea in every location that holds the item rather than a theatre habit and a ward habit; the recorded statement that ISMP lists, WHO LASA patient-safety solution, Tall Man lettering and the Malaysian LASA guide (chapter references 3, 4, 5, 7, 12, 14) are frameworks the hospital may use and are not this hospital's mandated list or mandated lettering; the recorded division that NDPS, chemo and radioactive agents named as high-risk are still stored under MOM.8, and that non-NDPS sedative or anaesthetic high-risk items are stored here while COP.9 and COP.10 own the clinical act; the location of the list and mechanism in the pharmacy and in every location that stocks an item on the list, rather than a pharmacy-only file; committee records showing the list updated when the formulary changed; induction or briefing records of staff who pick from those locations; the audit sample at step 7 of a local list and a mechanism in use rather than a pinned international table with unchanged shelves",
        "responsible": "Person in charge of the pharmacy holds the list and the mechanism; multidisciplinary medication committee keeps the list current; location staff apply the mechanism; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.2.d",
        "requirement": "High-risk medications are stored in areas where it is clinically necessary.",
        "steps": "Steps 4, 3, 7",
        "evidence": "The written map of which high-risk item is stored in which area and why; records showing a concentrated item not needed on a general ward was not stored there by default; the recorded MOM.8 boundary for NDPS even where clinical necessity exists; the audit sample at step 7",
        "responsible": "Person in charge of the pharmacy and the committee decide locations; location staff do not add high-risk stock by habit; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.2.e",
        "requirement": "The list of emergency medications is defined and is stored uniformly.",
        "steps": "Steps 5, 6, 7",
        "evidence": "This hospital's dated emergency-medication list, matching the services defined under AAC.1 and the emergency work this hospital actually holds out rather than a generic tertiary-hospital cart, and showing that NDPS items on the list remain in the MOM.8 cupboard rather than creating a second narcotic drawer, and that sedative or anaesthetic items on the list are stored here as stock while COP.9 and COP.10 own the clinical act; the written uniform-storage method naming the locations that hold the list and the arrangement used in each, so that a person who can find an item in one named location can find the same item in the same relative place in the others, without printing a crash-cart contents list as a NABH mandate; the recorded split that COP.3 owns kit presence for cardio-pulmonary resuscitation in named areas and restoration of reusable equipment, COP.2 owns that the ambulance is stocked with this hospital's emergency medicines, and this document owns the list, the uniform storage, availability and replenishment; records of the ambulance using this list insofar as it carries those medicines; the location of the list and the arrangement in every named location rather than only in the quality office; committee records showing the list reviewed when services changed; induction or briefing records of staff who open those drawers; the audit sample at step 7 of the same list stored in the same arrangement in named locations rather than a different crash habit in each room",
        "responsible": "Person in charge of the pharmacy holds the list and the uniform arrangement; location staff keep each named location to that arrangement; COP.3 owns kit presence; COP.2 owns ambulance stocking against this list; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.2.f",
        "requirement": "Emergency medications are available all the time and are replenished promptly when used.",
        "steps": "Steps 6, 5, 7",
        "evidence": "The written completeness-check and replenishment method, including this hospital's definition of prompt refill without a mandated number of minutes; sample checks covering nights, weekends and holidays; records of replenishment after use coordinated with COP.3 kit restoration; records of expired emergency stock replaced before it was the only stock; the audit sample at step 7 of drawers that were not left empty after use",
        "responsible": "Location staff check and report gaps; pharmacy replenishes medicines; COP.3 restores the kit; quality or accreditation coordinator audits",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. MOM.2 standard text and all six OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 3 Management of Medication, printed pages 76-77 (PDF page index 82-83). Header quoted from those pages: "Medications are stored appropriately and are available where required." The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page (https://nabh-portal-live.s3.ap-south-1.amazonaws.com/wp-content/uploads/2025/07/13110738/SHCO-Standards-3rd-Edition.pdf, md5 39e3bc86d73d651b9cfef283bbf018a9, 188 pages). Levels: MOM.2.a Core, MOM.2.b Commitment, MOM.2.c Core, MOM.2.d Achievement, MOM.2.e Commitment, MOM.2.f Core.
   TWO OEs CARRY THE ASTERISK -- MOM.2.c and MOM.2.e. The draft builds two separate deep blocks (step 3 for c; step 5 for e). MOM.2.a, MOM.2.b, MOM.2.d and MOM.2.f are unasterisked and are correspondingly Tier 2.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed, 408 OEs, 132 asterisks; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the MOM.2 pages read directly from the extracted page text, and the committed asterisk file.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. TWO OF SIX OEs ARE TIER 1. Tier 1: MOM.2.c, MOM.2.e -- procedure steps 3 and 5 carry the reasoning (why a pinned ISMP table with unchanged shelves is not a storage mechanism, why a different crash habit in each room is not uniform storage, why COP.3's kit is not this list). Tier 2: MOM.2.a (step 1), MOM.2.b (step 2), MOM.2.d (step 4), MOM.2.f (step 6) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of a, b, d and f is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of MOM.2.c/e against the approved HIC.1-HIC.6 masters, the AAC.1-AAC.8 drafts and the COP.1-COP.13 drafts. Search terms: storage, high-risk, look-alike, LASA, emergency medication, crash, cart, trolley, NDPS, sedation, anaesthesia, transfusion.
   COP.3 -- CRITICAL SPLIT, stated in Scope and step 5. COP.3 owns kit presence for CPR in named areas. MOM.2.e/f own the emergency-medication list, uniform storage, availability and replenishment. Do not print a kit list. Flagged for parent log.
   COP.2 -- ambulance and emergency area stock against this hospital's emergency-medication list. COP.2 owns ambulance fitness; this owns the list and uniform storage. Flagged for parent log.
   COP.9 / COP.10 -- this stores (non-NDPS) sedative and anaesthetic medicines; those policies own the clinical act. NDPS cupboard is MOM.8. Stated in Scope and steps 3 and 5.
   MOM.8 -- NDPS/chemo/radioactive storage handed off in Scope. Not inherited as a wholesale statute.
   COP.5 -- blood not ward-stock; storage pending transfusion is COP.5.
   MOM.1 -- formulary and committee feed this storage; not rewritten.
   HIC.2 / HIC.3 / HIC.4 -- injection, pharmaceutical waste, device bundles. Pointed, not restated.
   AAC.1 -- lists must match defined services.
   COP.1 / AAC.2 -- identifiers and UID. Applied.
   PRE / IMS -- undrafted forward references.
3. FORWARD REFERENCES: MOM.8 NDPS cupboard; MOM.9 implants; PRE; IMS. Each is a deliberate boundary.
4. T2 QUICK CHECK: MOM.2.a vs D&C storage conditions -- statute cited, no temperature invented. MOM.2.b vs MOM.1 after-hours deduction -- flagged in step 2. MOM.2.d vs MOM.8 even where clinically necessary -- flagged in step 4. MOM.2.f vs COP.3 kit restoration -- medicines vs reusable equipment; flagged in step 6. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. Drugs and Cosmetics Act, 1940 and Rules -- cited insofar as they govern storage of medicines (conditions, schedules). No schedule reprinted. No temperature in degrees as a mandate.
6. NDPS Act 1985 is NOT named in P2. Scope hands NDPS/chemo/radioactive storage to MOM.8.
7. ISMP high-alert (ch ref 7), confused names (12), Tall Man (4), Bryan et al. LASA (3), WHO LASA solution (14), Malaysian LASA guide (5), CEC high-risk (8) -- frameworks, not mandated lists or lettering.
8. NO NUMBERS ARE STATED as requirements -- no temperatures, no stock-day figures, no refill minutes, no near-expiry days. Every such value is [Hospital to define].
9. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act, 2010 are NOT named in P2.

EDITORIAL POSITIONS TAKEN
10. Step 3's refusal to treat an unadapted ISMP printout as this hospital's list, and the refusal to mandate Tall Man lettering by name, are editorial positions required by the owner's instruction that those lists are frameworks.
11. Step 5's split with COP.3 (kit presence vs emergency-medicine list) and the refusal to print a kit list are editorial positions required by the owner's instruction.
12. Step 1's reading that a food refrigerator is not a medication store is an editorial position consistent with "clean, safe and secure" and manufacturer's recommendations.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
13. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Drugs and Cosmetics Act, 1940 and Rules insofar as they govern storage of medicines -- the statute this document's References actually rely on. It does NOT name NDPS, BMW Rules 2016, FSS Act 2006, or CEA 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Formulary, committee, acquisition, after-hours obtainment -- MOM.1.
- Prescription, verbal orders, reconciliation -- MOM.3.
- NDPS / chemo / radioactive cupboard -- MOM.8.
- Implant storage as devices -- MOM.9.
- Transfusion storage pending hanging -- COP.5.
- CPR kit presence and algorithm -- COP.3.
- Ambulance operational rules -- COP.2.
- Sedation and anaesthetic method -- COP.9 / COP.10.
- Injection technique -- HIC.2.
- BMW colours -- HIC.3.
- A mandated ISMP list, Tall Man convention, or crash-cart contents page.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 17 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 15 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 17; a search for "Hospital to define" without brackets finds all 17, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: storage locations and the method that keeps them clean, safe and secure; any local operating figures for storage conditions; the inventory-control method; the high-risk list including LASA pairs; the high-risk storage mechanism; where that list and mechanism are held; the areas in which each high-risk item is stored and why; the emergency-medication list; how emergency medications are stored uniformly; where that list and method are held; how completeness is checked and how used items are replenished; the named person in charge of pharmacy storage; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 3, printed pages 76-77
-- (PDF page index 82-83). Levels: a Core, b Commitment, c Core, d Achievement,
-- e Commitment, f Core.
-- TWO OEs CARRY THE ASTERISK -- MOM.2.c, MOM.2.e.
-- UNAPPROVED DRAFT. Do not run this insert until the owner confirms the write.
"""

if __name__ == "__main__":
    emit_and_verify(
        standard_code=STANDARD_CODE,
        chapter=CHAPTER,
        oe_codes=OE_CODES,
        policy_title=POLICY_TITLE,
        purpose=PURPOSE,
        scope=SCOPE,
        policy_statement=POLICY_STATEMENT,
        procedure_steps=PROCEDURE_STEPS,
        responsibility=RESPONSIBILITY,
        references_text=REFERENCES,
        distribution=DISTRIBUTION,
        abbreviations=ABBREVIATIONS,
        disclaimer=DISCLAIMER,
        oe_mapping=OE_MAPPING,
        universal_facts_checklist=UNIVERSAL_FACTS_CHECKLIST,
        version=VERSION,
        revision_history=REVISION_HISTORY,
        tier1_oes=TIER1_OES,
        statute_clause=STATUTE_CLAUSE,
        sql_header=SQL_HEADER,
        json_name="mom2_draft.json",
        sql_name="mom2_insert.sql",
    )
