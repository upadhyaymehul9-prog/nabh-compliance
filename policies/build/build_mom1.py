# -*- coding: utf-8 -*-
"""Builds the MOM.1 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): MOM.1.b, MOM.1.c, MOM.1.d
  Tier 2 (lighter pass):   MOM.1.a, MOM.1.e, MOM.1.f

THREE of six OEs are asterisked. The draft builds deep blocks for b, c and d.
a, e and f are lean. MOM.1.e is a pointer only to MOM.9.

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 3 Management of Medication, standard MOM.1 and OEs
MOM.1.a-f, read from the official standards PDF (downloaded 2026-08-17 from the
NABH website's Explore NABH Standards page), printed page 76, PDF page index 82.

Asterisks verified 2026-08-17: scripts/asterisk_extract.py re-run against that
download (self-validation passed, 408 OEs, 132 asterisks, output matched the
committed scripts/shco_oe_asterisks.json on all 408 entries) and the MOM.1 page
read directly. MOM.1.b, MOM.1.c and MOM.1.d carry the asterisk; MOM.1.a, MOM.1.e
and MOM.1.f are unasterisked.
"""
from policy_build_common import emit_and_verify, make_disclaimer

STANDARD_CODE = "MOM.1"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.1.a", "MOM.1.b", "MOM.1.c", "MOM.1.d", "MOM.1.e", "MOM.1.f",
]
TIER1_OES = ["MOM.1.b", "MOM.1.c", "MOM.1.d"]

POLICY_TITLE = "Pharmacy Services and the Multidisciplinary Medication Committee"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} runs pharmacy services and the management of medication under a multidisciplinary committee: a formulary that matches the patients this hospital actually treats and the healthcare services it has defined; written guidance that the committee uses to implement pharmacy services and medication usage; a procedure for acquiring formulary medicines and medicines not listed in the formulary; a procedure to obtain a medicine when the pharmacy is closed; a pointer that implantable prosthesis and medical devices are used under the implant policy; and clinician use of the current formulary.

The chapter intent is a safe and organised medication process. Availability, storage, prescription, dispensing and administration are governed by written guidance. This document is the first of that process: the committee, the formulary, acquisition, and after-hours obtainment. It is not the storage policy, the prescription policy, the dispensing policy or the administration policy.

Medications, in the chapter's language, also include blood and blood components, implants and medical devices. Blood and blood components are not managed here as ward-stock medicines; the clinical transfusion method is the transfusion policy of {{HOSPITAL_NAME}}. Implantable prosthesis and medical devices are not rewritten here; MOM.1.e points to the implant policy. Pharmacy oversight of floor-stock medicines remains this committee's work."""

SCOPE = """This policy applies to the pharmacy of {{HOSPITAL_NAME}}, every location in which medicines are stocked outside the pharmacy, the multidisciplinary committee that guides pharmacy services and medication usage, the staff who acquire medicines, the staff who obtain a medicine when the pharmacy is closed, and the clinicians who prescribe from the formulary. It binds employed personnel and any contracted pharmacy arrangement that operates under this hospital's unique identification number.

It covers: development, update and implementation of a list of medications appropriate to the patients and to the scope of clinical services; implementation of pharmacy services and medication usage following written guidance through a multidisciplinary committee; the procedure for acquiring formulary medications and medications not listed in the formulary; the procedure to obtain medication when the pharmacy is closed; a pointer that implantable prosthesis and medical devices are used in accordance with laid-down criteria under the implant policy; and clinician adherence to the current formulary.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The written definition of healthcare services is governed by the definition-and-display policy of {{HOSPITAL_NAME}} (AAC.1). The formulary must match those defined services. This document does not rewrite the service directory. A specialty the directory does not name does not acquire a matching formulary as if the service existed.
- Generation of the unique identification number is governed by the registration, admission and transfer policy of {{HOSPITAL_NAME}} (AAC.2). Acquisition records, after-hours issue records and committee minutes that concern a named patient carry that number; this policy does not issue it.
- Two identifiers at the point of care are governed by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1). This policy does not invent a third identification system.
- Transfusion of blood and blood components is governed by the transfusion policy of {{HOSPITAL_NAME}} (COP.5). The chapter intent includes blood among medications. COP.5 owns hanging a unit, bedside identity, consent, emergency availability of a unit, and the reaction pathway. This document does not restate that method. Blood and blood components are not managed as ward-stock medicines under this process. Pharmacy oversight here is of floor-stock medicines, not of a donated unit.
- Device-associated care bundles are governed by the device-bundle policy of {{HOSPITAL_NAME}} (HIC.4). They are not this medication process.
- Safe injection practice is governed by the infection-prevention-and-control-practices policy of {{HOSPITAL_NAME}} (HIC.2). This document does not rewrite injection technique.
- Pharmaceutical waste, including expired and discarded medicines, enters the hospital-wide biomedical-waste programme governed by the support-services infection-control policy of {{HOSPITAL_NAME}} (HIC.3). This policy requires that expired or unusable stock is not left in a cupboard as if it were available; it does not restate colour categories, storage times or common-treatment-facility handover, and it does not name the Bio-Medical Waste Management Rules in the statutory paragraph of the disclaimer.
- Storage of medicines, including high-risk and look-alike/sound-alike controls, inventory, and the emergency-medication list, is governed by the storage-and-availability policy of {{HOSPITAL_NAME}} (MOM.2, sibling, drafted in this pass). This document owns the committee and the formulary that feed that storage; it does not write cupboard method.
- Safe and rational prescription is governed by the prescription policy of {{HOSPITAL_NAME}} (MOM.3, sibling, drafted in this pass). This document owns that clinicians use the current formulary; it does not write how a prescription is decided or written.
- Uniform order writing in the record is governed by MOM.4 (not yet drafted).
- Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents — their secure storage, use, prescription by appropriate caregivers, preparation and record — are governed by MOM.8 (not yet drafted). This document does not inherit the Narcotic Drugs and Psychotropic Substances Act, 1985 as a wholesale storage statute. NDPS cupboard, register and destruction wait for MOM.8.
- Implantable prosthesis and medical devices are governed by MOM.9 (not yet drafted). MOM.1.e is a pointer only. This document does not rewrite procurement criteria, counselling, or batch-and-serial recording.
- Counselling and education of the patient about medicines are governed by the patient-rights policies of {{HOSPITAL_NAME}} (PRE, not yet drafted).
- The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the formulary, committee, acquisition and after-hours content written into working records."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} maintains a list of medications appropriate to the patients it treats and to the healthcare services it has defined. The list is developed, updated and implemented. A copied formulary that does not match this hospital's services is not that list.

{{HOSPITAL_NAME}} implements pharmacy services and medication usage following written guidance, through a multidisciplinary committee.

{{HOSPITAL_NAME}} acquires formulary medications, and medications not listed in the formulary, against a written procedure. A non-formulary medicine is not obtained by informal purchase because a clinician asked once.

{{HOSPITAL_NAME}} has a written procedure to obtain medication when the pharmacy is closed. After-hours obtainment is a recorded act, not an unlocked cupboard.

{{HOSPITAL_NAME}} uses implantable prosthesis and medical devices under the implant policy. This document does not rewrite that policy.

{{HOSPITAL_NAME}} requires clinicians to adhere to the current formulary. A personal preference that bypasses the list without the non-formulary procedure is a defect."""

PROCEDURE_STEPS = [
"""1. Formulary list developed, updated and implemented

{{HOSPITAL_NAME}} develops, updates and implements a list of medications appropriate for its patients and as per the scope of its clinical services. The current list, how it is developed and updated, and where it is held, are [Hospital to define — the current formulary list, how it is developed and updated, and where it is held].

Appropriate means the list matches the service directory maintained under the definition-and-display policy of {{HOSPITAL_NAME}}. A hospital that does not define oncology as a service does not carry an oncology-only list as if it did. A hospital that defines emergency services includes the emergency medicines that service requires. The National List of Essential Medicines (chapter reference 21) and the WHO Model Lists of Essential Medicines (chapter reference 19) may inform the hospital's list; they are not pasted as the formulary.

The list in force is the current version. A superseded list left at a nursing station is not the formulary. Implementation means the list is the list used to acquire, stock and prescribe, not a file in the quality office.

This step does not write storage, prescription method, or after-hours obtainment; those are later steps and sibling policies.""",

"""2. Pharmacy services and medication usage through a multidisciplinary committee

Pharmacy services and medication usage at {{HOSPITAL_NAME}} are implemented following written guidance through a multidisciplinary committee. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask who guides the pharmacy and what written method that group uses. The answer must be a committee that meets and a guidance document the pharmacy and the wards actually follow, not a terms-of-reference file that has never produced a minute.

The reason a committee is the safety step is that medication use fails in the gap between a pharmacist's list and a clinician's habit. A formulary that only pharmacy owns is ignored on the ward. A formulary that only a medical superintendent owns is not stocked. Written guidance that a mixed group has adopted is how acquisition, after-hours obtainment, floor-stock oversight and formulary change become one process. The common error is a "pharmacy committee" that is the pharmacist plus whoever was free, meeting when an inspection is due, with guidance copied from another hospital's formulary. That is a meeting, not implementation following written guidance.

The multidisciplinary committee that guides pharmacy services and medication usage — composition, chair, meeting interval, and where minutes are held — is [Hospital to define — the multidisciplinary committee that guides pharmacy services and medication usage: composition, chair, meeting interval, and where minutes are held]. Multidisciplinary means more than one profession. A committee of doctors that never includes the person who runs the pharmacy, or a committee of the pharmacy that never includes a prescribing clinician and nursing, is not this committee. This document does not mandate a proprietary name (Drug and Therapeutics Committee or other). It requires a named mixed group that does this work.

The written guidance for pharmacy services and medication usage, and where it is held, are [Hospital to define — the written guidance for pharmacy services and medication usage, and where it is held]. That guidance is the method the committee uses. It covers at least: how the formulary at step 1 is kept current; how floor-stock outside the pharmacy is overseen; how acquisition at step 3 is done; how after-hours obtainment at step 4 is done; and how a change to any of those is approved. Storage method remains the storage policy; prescription method remains the prescription policy; this guidance names those boundaries rather than rewriting them.

Pharmacy oversight of medications stocked out of the pharmacy is this committee's work under that guidance. Oversight means the pharmacy knows what is on the ward, that it is the current formulary item, and that expired or unusable stock is removed. It does not mean the pharmacist hangs a transfusion; blood and blood components remain under the transfusion policy. It does not mean this committee writes the NDPS cupboard; narcotic, psychotropic, chemotherapeutic and radioactive agents remain under MOM.8.

Who is in charge of the pharmacy, and the registered-pharmacist arrangement, are [Hospital to define — who is in charge of the pharmacy, and the registered-pharmacist arrangement]. The Pharmacy Act, 1948 governs pharmacy services insofar as a pharmacy is conducted here. A person who is not a registered pharmacist does not become one by sitting on this committee. Human-resource procedures verify registration; this step uses that verification. This document does not invent a staffing number or a mandated round-the-clock pharmacist.

The committee records decisions against a dated minute: formulary additions and deletions, non-formulary approvals as a class of process (individual patient approvals sit in the acquisition record at step 3), after-hours incidents that expose a gap, and changes to the written guidance. A decision that is remembered and not minuted is not a committee decision.

Medicines used for procedural sedation and for anaesthesia are selected as a clinical act under those clinical policies. This committee still owns that those medicines, if stocked, appear on the formulary or are acquired under step 3. Storage of any controlled drug among them is MOM.8, not this minute.""",

"""3. Acquisition of formulary medications and of medications not listed in the formulary

{{HOSPITAL_NAME}} adheres to a written procedure for the acquisition of formulary medications and of medications not listed in the formulary. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask how a listed medicine is bought and how an unlisted medicine is obtained for a named patient. The answer must be two written routes, not a single purchase order that does not distinguish them.

The reason the two routes exist is that a formulary that can be bypassed without a procedure is not a formulary. The failure without this step is the clinician who sends an attendant to a neighbourhood shop, or the store that orders whatever was written because "the doctor wants it", until the list on the wall and the stock on the shelf are different lists. The common error is a non-formulary stamp that is never refused, so that every request becomes non-formulary and the formulary dies by exception.

The procedure for acquiring formulary medications is [Hospital to define — the procedure for acquiring formulary medications]. Formulary acquisition is from a licensed source. The Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules govern the acquisition and sale of medicines. This hospital does not acquire from an unlicensed seller because the price was lower. Schedule H and Schedule H1 conditions of sale are observed; this step does not reprint those schedules. No quantity, lead-time in days, or temperature is stated here as a mandate.

The procedure for acquiring a medication not listed in the formulary, including who may request and who may approve, is [Hospital to define — the procedure for acquiring a medication not listed in the formulary, including who may request and who may approve]. Non-formulary acquisition is an exception with a recorded reason, a named patient or a named defined indication, an approval, and a licensed source. A standing informal list of "we always keep this even though it is not on the formulary" is formulary by the back door and is forbidden; either the item is added to the formulary under step 1 or each obtainment uses this procedure. Approval is not the same person as the requester by default; the hospital's written procedure names the approver.

The licensed sources from which medications are acquired are [Hospital to define — the licensed sources from which medications are acquired]. Licence evidence is held with the pharmacy or stores. A source that cannot show a current licence is not used.

A non-formulary medicine still enters pharmaceutical-waste handling under HIC.3 if it expires unused; this step does not write colour-coded waste. A non-formulary narcotic, psychotropic, chemotherapeutic or radioactive agent, if ever required, is still acquired only under this procedure and is then stored and used under MOM.8; this step does not open an NDPS cupboard.

Blood and blood components are not acquired as formulary or non-formulary ward stock under this step. Units are issued under the transfusion policy from a licensed blood bank or blood centre.

Each acquisition that concerns a named patient is recorded against the unique identification number. Stock acquisition of formulary items is recorded in the pharmacy or stores record the hospital uses. The record shows which route was used.""",

"""4. Obtaining medication when the pharmacy is closed

There is a procedure to obtain medication when the pharmacy is closed. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask what happens at night, on a holiday, or whenever the pharmacy shutter is down and a patient needs a medicine that is not already on the ward. The answer must be a written method staff have used, not a claim that someone has a key.

The reason a written after-hours method is the safety step is that the closed pharmacy is when informal practice replaces the formulary. A ward that "just keeps extras" because after-hours obtainment is humiliating, an unlocked door because the night supervisor is tired of calling, or a neighbourhood shop receipt with no record in the hospital, are the same failure: a medicine entered the patient without the process that exists in daylight. The common error is an after-hours SOP that describes a pharmacist on call in a hospital that has no such person, or a key in a drawer that everyone uses and nobody records. That SOP is fiction. This step requires the method this hospital can actually run.

When the pharmacy is treated as closed, and the procedure to obtain medication during that period, are [Hospital to define — when the pharmacy is treated as closed, and the procedure to obtain medication during that period]. Closed is this hospital's definition: the hours and conditions when the ordinary dispensing window is not operating. This document does not state opening hours. It requires that the definition exists and that the obtainment method matches it. If the hospital runs a round-the-clock pharmacy, it still writes what "closed" would mean (unplanned closure, pharmacist absence) and how a medicine is then obtained; silence is not a procedure.

Who may access medications when the pharmacy is closed, and how that access is recorded, are [Hospital to define — who may access medications when the pharmacy is closed, and how that access is recorded]. Access is named and limited. A person who may not dispense in daylight does not acquire an implied right to dispense at night except as the written procedure states. The Pharmacy Act, 1948 is not suspended because the shutter is down. The record states the medicine, the quantity, the patient (unique identification number), the person who obtained, the time, and the reason the pharmacy was closed. A key-issue register that does not name the patient is incomplete for a patient-specific obtainment.

After-hours obtainment is from hospital stock under this procedure, or by a written alternative the hospital has defined (on-call pharmacist, a named licensed source that will supply out of hours). Sending an attendant to an unnamed shop is not the procedure. What is taken is deducted from stock and is reconciled when the pharmacy reopens. A missing strip that is noticed days later is a defect of this step, not of inventory alone.

Narcotic and psychotropic after-hours access, if it occurs, is still MOM.8's cupboard and register, used through this hospital's after-hours rule; this step does not create a second NDPS key. Emergency medicines that must be present on the ward at all times are stored under the storage policy; this step is for a medicine that is not already in that location when the pharmacy is closed.

The after-hours procedure is held with the written guidance at step 2 and is known to the night and holiday staff who would use it. A procedure that lives only in the quality office is not a procedure to obtain medication when the pharmacy is closed.""",

"""5. Implantable prosthesis and medical devices — pointer to the implant policy

Implantable prosthesis and medical devices are used in accordance with laid-down criteria. Those criteria, procurement, counselling, and recording of batch and serial numbers, are governed by the implant policy of {{HOSPITAL_NAME}} (MOM.9, not yet drafted). This step is a pointer only. It does not rewrite MOM.9.

Whether implantable prosthesis and medical devices are used at this hospital is a service-directory decision under AAC.1. If they are not a defined service, this step records that fact and still does not invent implant criteria. If they are, MOM.9 is the method.

This committee does not approve an implant as if it were a non-formulary tablet. An implant is not added to the medicine formulary as a substitute for MOM.9.""",

"""6. Clinician adherence to the current formulary

Clinicians adhere to the current formulary. Adherence means prescribing from the list in force at step 1, or using the non-formulary procedure at step 3 when a listed medicine will not do. A personal substitute that is not on the list and was not approved is not adherence.

How clinician adherence to the current formulary is monitored is [Hospital to define — how clinician adherence to the current formulary is monitored]. Monitoring may use the prescription-audit process owned by the prescription policy; this step owns that formulary adherence is one of the things looked at. The current list is the list clinicians can actually see — at the place they prescribe, not only in the pharmacy.

A clinician who repeatedly bypasses the list is a committee matter at step 2, not only a personal preference.""",

"""7. Records, review and the order of operations

Every formulary version, committee minute, formulary and non-formulary acquisition, after-hours obtainment, and adherence review is recorded and is retrievable. Patient-specific records carry the unique identification number.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for pharmacy-committee, formulary, acquisition and after-hours records] for: a formulary that matches the current service directory; committee minutes that show the written guidance in use; formulary acquisition from a licensed source; non-formulary obtainment that used the exception procedure rather than an informal shop purchase; after-hours obtainment that was recorded and reconciled; and implant questions handed to MOM.9 rather than absorbed here.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when an unlicensed acquisition, an after-hours obtainment that was not recorded, a formulary that does not match the directory, or a revision of the storage, prescription, transfusion, implant or infection-control policies that this document hands work to, exposes a gap.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} having a formulary that matches defined services, a multidisciplinary committee that actually guides pharmacy services, licensed acquisition, and a usable after-hours obtainment method.

The named chair of the multidisciplinary medication committee is [Hospital to define — the named chair of the multidisciplinary medication committee]. The chair holds the written guidance, the formulary version, and the minutes.

The person in charge of the pharmacy keeps the formulary in use, acquires against step 3, oversees floor-stock as the guidance requires, and reconciles after-hours obtainment when the pharmacy reopens. Registration as a pharmacist is verified under the human resource policies.

Clinicians prescribe from the current formulary or use the non-formulary procedure. They do not send attendants to unnamed shops.

Staff named in the after-hours procedure obtain medication only as that procedure states and complete the record.

The quality or accreditation coordinator audits the records at step 7 and reports findings to the head of the institution.

All staff are expected to treat an unlicensed acquisition, an unrecorded after-hours taking, and a personal non-formulary habit, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.1.
- Pharmacy Act, 1948 — insofar as it governs pharmacy services and the registered pharmacist.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules — insofar as they govern the acquisition and sale of medicines, including Schedule H and Schedule H1 conditions of sale.
- National List of Essential Medicines, Department of Pharmaceuticals, Ministry of Chemicals and Fertilizers (2018) — chapter reference 21; may inform the hospital formulary; not pasted as the list.
- Model Lists of Essential Medicines, World Health Organization — chapter reference 19; a recognised framework the hospital may use; not mandated as the formulary.
- Promoting rational use of medicines: core components, World Health Organization (2012) — chapter reference 23; informs that a committee and a formulary are known methods; not imported as a protocol.
- Internal documents of {{HOSPITAL_NAME}}: the formulary list; the multidisciplinary-committee terms, minutes and written pharmacy-services guidance; the formulary and non-formulary acquisition procedures; the after-hours obtainment procedure; the service directory; the storage-and-availability policy; the prescription policy; the transfusion policy; the implant policy; the infection-prevention and support-services infection-control policies; and the human resource policies."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: the pharmacy; stores; every in-patient ward; the emergency area; the operation theatre and recovery; intensive or high-dependency areas where they exist; day-care; nursing administration; every head of department whose staff prescribe; and the members of the multidisciplinary medication committee.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The current formulary, the written pharmacy-services guidance, the acquisition procedures and the after-hours obtainment procedure — the working documents this policy requires — are held in the pharmacy and in every area that stocks medicines outside the pharmacy.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

NLEM — National List of Essential Medicines
NMC — National Medical Commission
NDPS — Narcotic Drugs and Psychotropic Substances (Act, 1985), named only as the statute MOM.8 will own; not inherited here

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

STATUTE_CLAUSE = (
    "the Pharmacy Act, 1948, insofar as it governs pharmacy services and the registered "
    "pharmacist, and the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, "
    "insofar as they govern the acquisition and sale of medicines"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.1.a",
        "requirement": "A list of medications appropriate to the patients and to the scope of clinical services is developed, updated and implemented.",
        "steps": "Steps 1, 2, 7",
        "evidence": "The current formulary list, dated and version-controlled; the written method for developing and updating it; alignment of that list with the current service directory; the location where the list is held; records showing superseded lists withdrawn from nursing stations; the audit sample at step 7 of a formulary that matches defined services",
        "responsible": "Multidisciplinary committee keeps the list current; person in charge of the pharmacy implements it in acquisition and stock; head of the institution is accountable that the list matches defined services; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.1.b",
        "requirement": "Pharmacy services and medication usage are implemented following written guidance through a multidisciplinary committee.",
        "steps": "Steps 2, 1, 7",
        "evidence": "The named multidisciplinary committee, its composition showing more than one profession including the person who runs the pharmacy, a prescribing clinician and nursing rather than a single-profession meeting or a pharmacist-only group, the chair, the meeting interval and the location of minutes, showing a group that meets and decides rather than a terms-of-reference file opened for inspection; the written guidance for pharmacy services and medication usage covering how the formulary is kept current, how floor-stock outside the pharmacy is overseen, how formulary and non-formulary acquisition is done, how after-hours obtainment is done, and how a change to any of those is approved, held where the pharmacy and the wards that stock medicines can use it rather than only in the quality office, and naming the storage policy and the prescription policy as boundaries instead of rewriting cupboard or prescription method; sample minutes showing formulary additions and deletions, process decisions on non-formulary and after-hours gaps, and changes to the written guidance, dated and attributable, rather than an undated discussion; the named person in charge of the pharmacy and the registered-pharmacist arrangement, with current registration under the Pharmacy Act, 1948 used from human-resource verification, and with no invented staffing number or mandated round-the-clock pharmacist presented as a NABH requirement; records of pharmacy oversight of floor-stock medicines (what is on the ward, that it is the current formulary item, that expired or unusable stock was removed) distinguished from hanging a blood component (COP.5) and from the NDPS cupboard (MOM.8); records showing medicines used for sedation or anaesthesia, if stocked, appearing on the formulary or acquired under step 3 while storage of any controlled drug among them remains MOM.8; induction or briefing records of committee members and of staff who run the pharmacy and floor-stock; the location of the written guidance; the audit sample at step 7 of committee minutes that show the written guidance in use rather than a dormant committee",
        "responsible": "Named chair holds the guidance, formulary version and minutes; person in charge of the pharmacy implements the guidance; committee members attend and decide; head of the institution is accountable that pharmacy services are guided by that committee; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.1.c",
        "requirement": "The organisation follows a written procedure for acquiring formulary medications and medications not listed in the formulary.",
        "steps": "Steps 3, 2, 7",
        "evidence": "The written formulary-acquisition procedure, showing purchase from a licensed source under the Drugs and Cosmetics Act, 1940 and Rules including Schedule H and Schedule H1 conditions of sale without reprinting those schedules or stating a mandated lead-time, quantity or temperature; the written non-formulary procedure naming who may request, who may approve (not the requester by default unless the hospital's procedure records a defined exception), the recorded reason, the named patient or named defined indication, and the licensed source, and showing that a standing informal list of unlisted items kept as if they were formulary is forbidden; licence evidence for the named sources, held with pharmacy or stores, and records of a source that could not show a current licence not being used; sample formulary acquisition records in the pharmacy or stores record; sample non-formulary records against the unique identification number showing the exception route used rather than an attendant sent to an unnamed neighbourhood shop or a store order that did not distinguish the two routes; records of non-formulary narcotic, psychotropic, chemotherapeutic or radioactive agents, if ever required, still acquired under this procedure and then stored under MOM.8 rather than opening an NDPS cupboard here; records showing blood and blood components not acquired as ward-stock under this step; records of unused expired non-formulary stock entering the HIC.3 waste stream without this document restating colour categories; the location of the two procedures; briefing records of stores and pharmacy staff; the audit sample at step 7 of licensed formulary acquisition and of non-formulary obtainment that used the exception procedure",
        "responsible": "Person in charge of the pharmacy acquires against the two routes; named approver decides non-formulary requests; clinicians request rather than purchase informally; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.1.d",
        "requirement": "There is a written procedure to obtain medication when the pharmacy is closed.",
        "steps": "Steps 4, 2, 7",
        "evidence": "The written definition of when the pharmacy is treated as closed (hours and conditions when the ordinary dispensing window is not operating, including unplanned closure) and the procedure to obtain medication during that period, showing a method this hospital can actually run rather than an on-call pharmacist who does not exist or a key in a drawer that everyone uses and nobody records, and containing no mandated opening-hours figure presented as a NABH requirement; the named persons who may access medications when the pharmacy is closed, and the record of that access stating the medicine, the quantity, the patient unique identification number, the person who obtained, the time, and the reason the pharmacy was closed, rather than a key-issue register that does not name the patient; sample after-hours records showing obtainment from hospital stock or from the hospital's written alternative (on-call pharmacist or named licensed out-of-hours source) and not from an unnamed shop; records of deduction from stock and reconciliation when the pharmacy reopened, including a missing quantity treated as a defect; the recorded statement that the Pharmacy Act, 1948 is not suspended because the shutter is down; the recorded division that narcotic and psychotropic after-hours access remains MOM.8's cupboard used through this after-hours rule, and that emergency medicines that must already be on the ward are MOM.2 storage rather than this obtainment; the location of the after-hours procedure with the written guidance at step 2, and briefing records of night and holiday staff who would use it rather than a procedure that lives only in the quality office; the audit sample at step 7 of after-hours obtainment that was recorded and reconciled",
        "responsible": "Named after-hours staff obtain only as the procedure states and complete the record; person in charge of the pharmacy reconciles when the pharmacy reopens; committee reviews after-hours incidents that expose a gap; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.1.e",
        "requirement": "Implantable prosthesis and medical devices are used in accordance with laid-down criteria.",
        "steps": "Steps 5, 7",
        "evidence": "The recorded pointer that criteria, procurement, counselling and batch-and-serial recording are owned by the implant policy (MOM.9); the service-directory statement of whether implants are a defined service; records showing an implant was not added to the medicine formulary as a substitute for MOM.9; the audit sample at step 7 of implant questions handed to MOM.9",
        "responsible": "MOM.9 owns the method when drafted; this committee does not absorb implant criteria; quality or accreditation coordinator audits the pointer",
    },
    {
        "oe_code": "MOM.1.f",
        "requirement": "Clinicians adhere to the current formulary.",
        "steps": "Steps 6, 3, 7",
        "evidence": "The written method for monitoring clinician adherence; the current formulary available at the place of prescribing; sample records of non-formulary use that went through step 3; records of repeated bypass treated as a committee matter; the audit sample at step 7",
        "responsible": "Clinicians prescribe from the current list or use the non-formulary procedure; committee addresses repeated bypass; quality or accreditation coordinator audits",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. MOM.1 standard text and all six OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 3 Management of Medication, printed page 76 (PDF page index 82). Header quoted from that page: "Multidisciplinary committee guides pharmacy services and management of medication." The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page (https://nabh-portal-live.s3.ap-south-1.amazonaws.com/wp-content/uploads/2025/07/13110738/SHCO-Standards-3rd-Edition.pdf, md5 39e3bc86d73d651b9cfef283bbf018a9, 188 pages). Levels: MOM.1.a Commitment, MOM.1.b Core, MOM.1.c Commitment, MOM.1.d Commitment, MOM.1.e Commitment, MOM.1.f Excellence.
   THREE OEs CARRY THE ASTERISK -- MOM.1.b, MOM.1.c and MOM.1.d. The draft builds three separate deep blocks (step 2 for b; step 3 for c; step 4 for d). MOM.1.a, MOM.1.e and MOM.1.f are unasterisked and are correspondingly Tier 2. MOM.1.e is a pointer only to MOM.9.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed, 408 OEs, 132 asterisks; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the MOM.1 page read directly from the extracted page text, and the committed asterisk file.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. THREE OF SIX OEs ARE TIER 1. Tier 1: MOM.1.b, MOM.1.c, MOM.1.d -- procedure steps 2, 3 and 4 carry the reasoning (why a dormant committee is not written guidance, why a formulary that can be bypassed without a procedure is not a formulary, why an unlocked after-hours key is not a procedure to obtain medication). Tier 2: MOM.1.a (step 1), MOM.1.e (step 5), MOM.1.f (step 6) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of a, e and f is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of MOM.1.b/c/d against the approved HIC.1-HIC.6 masters, the AAC.1-AAC.8 drafts and the COP.1-COP.13 drafts. Search terms: pharmacy, formulary, medication, after-hours, acquisition, blood, implant, NDPS, injection, waste.
   COP.5 -- CRITICAL DIVISION, stated in Purpose, Scope and steps 2-3. Chapter intent includes blood among medications. COP.5 owns hanging a unit. This document does not restate transfusion method. Blood and blood components are not ward-stock medicines here. Pharmacy oversight is of floor-stock medicines. Flagged for parent log.
   AAC.1 -- formulary must match defined services. Stated in Scope and step 1.
   COP.1 / AAC.2 -- two identifiers and UID generation. Applied, not rewritten.
   HIC.2 -- injection safety. Pointed; not restated.
   HIC.3 -- pharmaceutical waste. Pointed; colours not restated; BMW Rules not in P2.
   HIC.4 -- device bundles are not this medication process. Stated in Scope.
   PRE (undrafted) -- counselling/education. Forward reference.
   IMS (undrafted) -- the record itself. Forward reference.
   MOM.8 -- NDPS/chemo/radioactive. Not inherited as a wholesale statute. Stated in Scope and steps 2-4.
   MOM.9 -- implants. MOM.1.e is a pointer only. Stated in step 5.
   MOM.2 / MOM.3 -- siblings drafted in this pass; storage and prescription not rewritten here.
3. FORWARD REFERENCES: MOM.4 order writing; MOM.8 NDPS cupboard; MOM.9 implants; PRE education; IMS record; HRM pharmacist registration. Each is a deliberate boundary.
4. T2 QUICK CHECK: MOM.1.a vs AAC.1 service directory -- flagged in Scope. MOM.1.e vs MOM.9 -- pointer only; flagged for parent log as the owning standard. MOM.1.f vs MOM.3 prescription audit -- monitoring may use that audit; this owns formulary adherence as a look-for. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. Pharmacy Act, 1948 -- cited insofar as it governs pharmacy services and the registered pharmacist. No section number. Registration is not suspended when the pharmacy is closed. No mandated staffing number.
6. Drugs and Cosmetics Act, 1940 and Rules -- cited insofar as they govern acquisition and sale of medicines, including Schedule H / H1 conditions of sale. No reprint of schedules. No quantity, lead-time or temperature as a mandate.
7. NLEM 2018 (chapter ref 21) and WHO EML (chapter ref 19) -- frameworks that may inform the formulary; not pasted as the list.
8. WHO promoting rational use (chapter ref 23) -- informs that a committee and a formulary are known methods; not imported as a protocol.
9. NDPS Act 1985 is NOT named in P2 and is not written as storage method. Forward-ref MOM.8.
10. NO NUMBERS ARE STATED as requirements -- no pharmacy hours, no stock-day figures, no temperatures, no doses. Every such value is [Hospital to define]. Consistent with the no-numbers default.
11. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act, 2010 are NOT named in P2.

EDITORIAL POSITIONS TAKEN
12. Step 2's refusal to mandate the name "Drug and Therapeutics Committee", while requiring a mixed-profession group, is an editorial position.
13. Step 3's rule that a standing informal unlisted stock is formulary by the back door, and that the approver is not the requester by default, are editorial positions; the standard requires a procedure, not this separation.
14. Step 4's rule that the Pharmacy Act is not suspended because the shutter is down, and that a key-issue register without the patient is incomplete for patient-specific obtainment, are editorial positions.
15. Step 5's refusal to rewrite MOM.9, and the refusal to add an implant to the medicine formulary as a substitute, are editorial positions required by the owner's instruction.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
16. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Pharmacy Act, 1948 insofar as it governs pharmacy services and the registered pharmacist, and the Drugs and Cosmetics Act, 1940 and Rules insofar as they govern the acquisition and sale of medicines -- the statutes this document's References actually rely on. It does NOT name NDPS, BMW Rules 2016, FSS Act 2006, or CEA 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Storage, LASA, emergency-medication list -- MOM.2.
- Rational prescription, allergies, verbal orders, reconciliation -- MOM.3.
- Uniform order writing -- MOM.4.
- Dispensing, recall, labelling -- MOM.5.
- Administration -- MOM.6.
- Post-administration monitoring, ADR reporting -- MOM.7.
- NDPS / chemo / radioactive storage and use -- MOM.8.
- Implant criteria, counselling, batch/serial -- MOM.9 (pointer only at MOM.1.e).
- Transfusion method -- COP.5.
- Injection technique -- HIC.2.
- BMW colour categories -- HIC.3.
- Device bundles -- HIC.4.
- Patient counselling -- PRE.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 16 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 14 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 16; a search for "Hospital to define" without brackets finds all 16, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: the current formulary list, how it is developed and updated, and where it is held; the multidisciplinary committee composition, chair, meeting interval and where minutes are held; the written pharmacy-services guidance and where it is held; who is in charge of the pharmacy and the registered-pharmacist arrangement; the formulary-acquisition procedure; the non-formulary acquisition procedure including who may request and who may approve; the licensed sources; when the pharmacy is treated as closed and the after-hours obtainment procedure; who may access medications when the pharmacy is closed and how that access is recorded; how clinician adherence is monitored; the named chair; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 3, printed page 76
-- (PDF page index 82). Levels: a Commitment, b Core, c Commitment, d Commitment,
-- e Commitment, f Excellence.
-- THREE OEs CARRY THE ASTERISK -- MOM.1.b, MOM.1.c, MOM.1.d.
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
        json_name="mom1_draft.json",
        sql_name="mom1_insert.sql",
    )
