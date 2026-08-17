# -*- coding: utf-8 -*-
"""Builds the MOM.9 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): MOM.9.a only
  Tier 2 (lighter pass):   MOM.9.b, MOM.9.c

ONE of three OEs is asterisked. The draft builds a deep block for a.
b and c are lean.

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 3 Management of Medication, standard MOM.9 and OEs
MOM.9.a-c, read from the official standards PDF (downloaded 2026-08-17 from the
NABH website's Explore NABH Standards page), printed page 81, PDF page index 87.
Chapter summary on printed page 75 (PDF page index 81) carries the same standard
text with a period; the OE page header has no period.

Asterisks verified 2026-08-17: scripts/asterisk_extract.py re-run against that
download (self-validation passed, 408 OEs, 132 asterisks, output matched the
committed scripts/shco_oe_asterisks.json on all 408 entries) and the MOM.9 page
read directly. MOM.9.a carries the asterisk; MOM.9.b and MOM.9.c are
unasterisked.

MOM.1.e is the chapter-level pointer ("Implantable prosthesis and medical
devices are used in accordance with laid down criteria"). This document is the
owning criteria. MOM.1 does not rewrite them.
"""
from policy_build_common import emit_and_verify, make_disclaimer

STANDARD_CODE = "MOM.9"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.9.a", "MOM.9.b", "MOM.9.c",
]
TIER1_OES = ["MOM.9.a"]

POLICY_TITLE = "Implantable Prosthesis and Medical Devices"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} uses implantable prostheses and medical devices in accordance with laid-down criteria: written guidance that addresses procurement and usage of the implants this hospital actually uses; counselling of the patient and family for usage and precautions; and recording of batch and serial number in the patient's medical records, the master logbook and the discharge summary.

The chapter intent includes implants and medical devices among medications, and requires that they are used in accordance with laid-down criteria. An implant chosen because the visiting surgeon brought it, a patient who discovers the precautions after discharge, or a discharge summary that names the procedure and not the implant's numbers, is not those criteria. This document is the process that makes the criteria operational.

MOM.1.e of this chapter points at the same subject. This document is the owning criteria. The multidisciplinary-committee policy of {{HOSPITAL_NAME}} does not rewrite them."""

SCOPE = """This policy applies to every location at {{HOSPITAL_NAME}} in which an implantable prosthesis or an implantable medical device is procured, stored pending use, counselled for, implanted, or recorded: the operation theatre and procedure rooms, the wards that receive the patient afterwards, the stores or pharmacy function that receives the device, and the records function that holds the master logbook and produces the discharge summary. It binds the clinicians who select and implant, the staff who procure and hold stock, the person who counsels the patient and family, and whoever writes batch and serial number into the three places this standard names.

It covers: written guidance addressing procurement and usage of implantable prostheses; counselling of the patient and family for usage of the implantable prosthesis and medical devices, including precautions if any; and recording of the batch and the serial number in the patient's medical records, the master logbook and the discharge summary.

If {{HOSPITAL_NAME}} does not implant prostheses or implantable medical devices, this document is adapted to record that absence against the service directory and is not used to invent an implant programme.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The written definition of healthcare services is governed by the definition-and-display policy of {{HOSPITAL_NAME}} (AAC.1). Implant types offered must match that directory. This document aligns procurement and usage to the types the directory names; it does not rewrite the directory. A type the directory does not define is not implanted here.
- The discharge process, and the clinical content list of the discharge summary (reasons for admission, findings, diagnosis, condition at discharge, investigations, procedures, medication and other treatment, follow-up advice), are governed by the discharge policy of {{HOSPITAL_NAME}} (AAC.8). AAC.8 owns that a summary is given and that clinical content. MOM.9.c owns that batch AND serial number ALSO appear in the medical record, the master logbook, AND the discharge summary. AAC.8 Scope hands that number-traceability to this document. This document mirrors that split: it does not write the discharge process and does not rewrite AAC.8's clinical content list.
- Clinical procedures and operations, including the act of implanting during a procedure, the surgical-safety checklist, site-marking and the operation note, are governed by the procedures-and-operation-theatre policy of {{HOSPITAL_NAME}} (COP.11). COP.11 requires implants to be confirmed at the pause and identified in the operation note. This document owns procurement criteria, counselling for usage and precautions, and traceability of batch and serial number in the three places named. Implanting is the surgical act; this document is the criteria and the numbers.
- Sterilisation and the check before use of reusable instruments, and the processing record for an implant load, are governed by the sterilisation-and-disinfection policy of {{HOSPITAL_NAME}} (HIC.6, approved). This document does not write the sterilisation cycle. Traceability of the device's batch and serial number after implantation is here.
- The method of informed consent generally, including surgical consent, is governed by the patient-rights policies of {{HOSPITAL_NAME}} (PRE, not yet drafted). MOM.9.b is counselling for usage of the implantable prosthesis and medical devices, including precautions if any. That counselling is not the same act as surgical consent. PRE does not write the implant-precaution counselling. This document does not write the surgical consent form.
- MOM.1.e of the multidisciplinary-committee policy of {{HOSPITAL_NAME}} (MOM.1, sibling) states that implantable prosthesis and medical devices are used in accordance with laid-down criteria. Those criteria are this document. MOM.1 does not rewrite them.
- Ordinary medication procurement and formulary are governed by the other medication policies of {{HOSPITAL_NAME}} (MOM.1 formulary and acquisition, siblings). An implant is a regulated medical device, not a ward-stock tablet. This document owns implant procurement criteria.
- The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the implant batch and serial content written into that record, the master logbook and the discharge summary.
- Generation of the unique identification number is governed by the registration and admission policy of {{HOSPITAL_NAME}} (AAC.2). This policy requires that number on the implant record; it does not issue the number."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} uses implantable prostheses and medical devices in accordance with written criteria that address procurement and usage of the types it actually uses. A type that is not a defined service is not implanted. {{HOSPITAL_NAME}} is not a manufacturer of those devices.

{{HOSPITAL_NAME}} counsels the patient and family for usage of the implantable prosthesis and medical devices, including precautions if any. That counselling is in addition to surgical consent, not a substitute for it and not the same act.

{{HOSPITAL_NAME}} records the batch and the serial number of the implantable prosthesis and medical devices in the patient's medical records, the master logbook and the discharge summary. A number in only one of those three places is incomplete.

{{HOSPITAL_NAME}} procures implantable devices from a source licensed under the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940. This hospital does not become a manufacturer by implanting."""

PROCEDURE_STEPS = [
"""1. Written guidance addresses procurement and usage of implantable prostheses

Written guidance at {{HOSPITAL_NAME}} addresses procurement and usage of implantable prostheses. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask what criteria govern an implant that enters a patient, and the answer must be written guidance this hospital uses, not a supplier brochure and not a visiting surgeon's usual brand.

The reason the guidance has to be written, and has to cover both procurement and usage, is that an implant fails at either end. Procurement without criteria is a device that arrived because it was offered, not because this hospital chose it against a licensed source, a type this hospital actually implants, and a match to the service directory. Usage without criteria is a device implanted because it was in the cupboard, without the counselling and the numbers the later steps require. The common error is a file titled "implant policy" that lists orthopaedic catalogue codes this hospital has never used, or that copies a manufacturer's technique guide as if it were the hospital's criteria. That file is not laid-down criteria. Another common error is treating MOM.1.e's one-line pointer as if the committee policy had already written the criteria. MOM.1.e points here. This step is the criteria.

The types of implantable prosthesis and implantable medical device this hospital uses, aligned with the service directory of {{HOSPITAL_NAME}}, or the recorded absence if this hospital does not implant, are [Hospital to define — the types of implantable prosthesis and medical device this hospital uses, aligned with the service directory, or the recorded absence if none are used]. A type the directory does not define is not procured and not implanted. If none are used, the rest of this step is the recorded absence; it is not a theatre implant SOP invented for assessment.

Where types are used, the written guidance addresses procurement and usage. Procurement is from a source licensed to manufacture, import or distribute that device under the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940. Implants are regulated devices. This hospital does not become a manufacturer by putting a licensed device into a patient, and it does not procure from an unlicensed source. How this hospital procures (who selects the licensed source, who receives the device, how stock is held pending use, how a loaner or consignment set is accepted), and how usage is authorised against the types in the directory, are [Hospital to define — how implantable prostheses and medical devices are procured from a licensed source and how usage is authorised against the types in the service directory]. This document does not print a brand list as a NABH mandate and does not print implant sizes or techniques. Those clinical choices remain the operating surgeon's, inside the types this hospital has written.

The surgical act of implanting remains the procedures-and-operation-theatre policy of {{HOSPITAL_NAME}}. Sterility of reusable instruments remains the sterilisation policy. This step owns the criteria under which a device is allowed to enter that theatre.

The written procurement-and-usage guidance is held at [Hospital to define — where the written guidance on procurement and usage of implantable prostheses is held].""",

"""2. Patient and family are counselled for usage and precautions

The patient and his or her family are counselled for the usage of the implantable prosthesis and medical devices, including precautions if any. The official OE text spells "devises"; this hospital counsels for devices.

Counselling covers what the implant is for, how the patient should use or live with it, and any precautions (movement limits, when to seek help, identification cards or alert jewellery if this hospital issues them, follow-up). How that counselling is recorded, and who performs it, are [Hospital to define — who counsels the patient and family for usage of the implantable prosthesis and medical devices including precautions, and how the counselling is recorded].

This counselling is not surgical consent. Surgical consent, including consent for the procedure that will implant the device, is obtained under the patient-rights policies of {{HOSPITAL_NAME}} by the doctor who will operate, before the procedure. A signed consent that is silent on how to live with the implant, or a counselling note that is treated as consent for incision, is the wrong document for the wrong OE. If this hospital does not implant, this step is the recorded absence at step 1.""",

"""3. Batch and serial number in the medical records, the master logbook and the discharge summary

The batch and the serial number of the implantable prosthesis and medical devices are recorded in the patient's medical records, the master logbook and the discharge summary. All three. Batch AND serial number. A sticker in the operation note and nowhere else is incomplete. A logbook without the discharge summary is incomplete. A discharge summary that names the procedure and not the numbers is incomplete.

The discharge policy of {{HOSPITAL_NAME}} owns that a discharge summary is given and owns its clinical content list. This step owns that the batch and serial number also appear there, and in the medical record, and in the master logbook. AAC.8 Scope hands that number-traceability to this document; this step is the landing.

Where the master logbook is held, and who writes the batch and serial number into the medical record, the master logbook and the discharge summary, are [Hospital to define — where the implant master logbook is held, and who writes batch and serial number into the medical records, the master logbook and the discharge summary]. If this hospital does not implant, this step is the recorded absence at step 1; it is not an empty logbook kept for display.

A device without a serial number as issued is recorded with the identifiers it carries (batch and whatever unique identifier the licensed device supplies). This document does not invent a serial number the manufacturer did not give. It requires that whatever batch and serial (or equivalent unique device identifier) the device carries is written in all three places.""",

"""4. Records, review and the order of operations

The written procurement-and-usage guidance, the licensed-source evidence, the counselling record, the medical-record entry, the master logbook entry and the discharge-summary entry of batch and serial number are retrievable against the unique identification number.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for implantable-prosthesis records] for: types implanted matching the service directory, or a recorded absence if none are used; procurement from a licensed source; counselling for usage and precautions recorded in addition to surgical consent; batch and serial number present in the medical record AND the master logbook AND the discharge summary; and no manufacturer's technique guide offered as this hospital's criteria.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when an implant type not in the directory was used, a discharge summary omitted the numbers, a device arrived from an unlicensed source, or counselling was treated as surgical consent, or when the discharge, surgical, sterilisation or multidisciplinary-committee policies that this document hands work to are revised.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} implanting only the types it has defined, procuring them from a licensed source, counselling for usage and precautions, and writing batch and serial number in all three places.

The named lead for implantable prostheses and medical devices authors and keeps current the written procurement-and-usage guidance at step 1, holds the master logbook method at step 3, and sees that counselling at step 2 is recorded. The named lead is [Hospital to define — the named lead for implantable prostheses and medical devices].

Operating surgeons implant only types in the directory, against the criteria, and do not treat a visiting brand as a substitute for those criteria. The person who counsels records the counselling. The person assigned at step 3 writes the numbers into the medical record, the master logbook and the discharge summary.

The quality or accreditation coordinator audits the records at step 4 and reports findings to the head of the institution.

All staff are expected to treat an undefined implant type, a missing serial in the discharge summary, and counselling used as surgical consent, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.9.
- Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940 — insofar as implantable prostheses and medical devices are regulated devices. This hospital procures from a licensed source and does not become a manufacturer by implanting.
- Internal documents of {{HOSPITAL_NAME}}: the written procurement-and-usage guidance; the licensed-source evidence; the counselling record; the implant master logbook; the service directory; the discharge policy; the procedures-and-operation-theatre policy; the sterilisation policy; the multidisciplinary-committee policy (MOM.1.e pointer); and the patient-rights policies."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: the operation theatre; stores or pharmacy insofar as they receive implantable devices; the wards that receive implant patients; the records function that holds the master logbook and produces discharge summaries; nursing administration; and the named lead.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The procurement-and-usage guidance and the master logbook — the working documents this policy requires — are held where implants are used.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

MDR — Medical Devices Rules, 2017

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

STATUTE_CLAUSE = (
    "the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, "
    "insofar as they govern implantable prostheses and medical devices as regulated devices"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.9.a",
        "requirement": "Written guidance address procurement and usage of implantable prostheses",
        "steps": "Steps 1, 4",
        "evidence": "The written guidance addressing procurement and usage of implantable prostheses this hospital actually uses, covering licensed source under the Medical Devices Rules, 2017 read with the Drugs and Cosmetics Act, 1940, who selects that source, who receives the device, how stock or a loaner or consignment set is accepted, and how usage is authorised against the types in the service directory, showing criteria this hospital uses rather than a supplier brochure, a visiting surgeon's usual brand, a manufacturer's technique guide offered as hospital criteria, or a catalogue of types this hospital has never implanted; the types of implantable prosthesis and implantable medical device in use, aligned with the service directory, or the recorded absence if this hospital does not implant, showing that absence is a record and not a theatre implant SOP invented for assessment, and showing that a type the directory does not define is not procured and not implanted; the recorded position that this hospital does not become a manufacturer by implanting a licensed device, and that MOM.1.e of the multidisciplinary-committee policy is a pointer to these criteria rather than a second set of criteria; the recorded division that the surgical act of implanting remains the procedures-and-operation-theatre policy and that sterilisation of reusable instruments remains the sterilisation policy; the location where the written guidance is held; induction or briefing records showing theatre and stores staff have been shown that an undefined type is not implanted; the audit sample at step 4 of types implanted matching the service directory, or a recorded absence if none are used, and of procurement from a licensed source",
        "responsible": "Named lead holds the written procurement-and-usage guidance and the type list or recorded absence; head of the institution is accountable that undefined types are not implanted and that this hospital does not hold itself out as a manufacturer; operating surgeons implant only against those criteria; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.9.b",
        "requirement": "Patient and his/her family are counselled for the usage of the implantable prosthesis and medical devises including precautions if any",
        "steps": "Steps 2, 1, 4",
        "evidence": "The written method of who counsels and how counselling for usage and precautions is recorded; sample records showing counselling covering usage and precautions in addition to surgical consent; records showing a signed surgical consent silent on living with the implant was not treated as this counselling, and a counselling note was not treated as consent for incision; the recorded absence if this hospital does not implant; the audit sample at step 4 of counselling recorded in addition to surgical consent",
        "responsible": "Person who counsels records it; named lead holds the method; patient-rights policies own surgical consent; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "MOM.9.c",
        "requirement": "The batch and the serial number of the implantable prosthesis and medical devises are recorded in the patients' medical records, the master logbook and the discharge summary",
        "steps": "Steps 3, 1, 4",
        "evidence": "The named master logbook and the named persons who write batch and serial number into the medical records, the master logbook AND the discharge summary; sample implant episodes showing batch and serial (or the unique identifier the licensed device carries) present in all three places, not only a sticker in the operation note; the recorded split that the discharge policy owns that a summary is given and its clinical content list, and that this step owns that the numbers also appear there; the recorded absence if this hospital does not implant; the audit sample at step 4 of batch and serial number in all three places",
        "responsible": "Person assigned at step 3 writes the numbers in all three places; named lead holds the logbook method; AAC.8 owns the discharge summary as a document; quality or accreditation coordinator audits",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. MOM.9 standard text and all three OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 3 Management of Medication, printed page 81 (PDF page index 87). Page header on the OE page quoted from the book: "Implantable prosthesis and medical devices are used in accordance with laid down criteria" (no period). Chapter summary on printed page 75 (PDF page index 81) carries the same text with a period. The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: MOM.9.a Commitment, MOM.9.b Commitment, MOM.9.c Commitment.
   ONE OE CARRIES THE ASTERISK -- MOM.9.a. The draft builds one deep block (step 1 for a). MOM.9.b and MOM.9.c are unasterisked and are correspondingly Tier 2.
   Official OE MOM.9.b and MOM.9.c spell "devises"; mapping requirements quote that official spelling; procedure prose uses "devices".
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the MOM.9 page read directly from the extracted page text, and the committed asterisk file. MOM.9 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. ONE OF THREE OEs IS TIER 1. Tier 1: MOM.9.a only -- procedure step 1 carries the reasoning (why a manufacturer's technique guide is not hospital criteria, why MOM.1.e is a pointer not a second policy, why unused implant services are a recorded absence). Tier 2: MOM.9.b (step 2), MOM.9.c (step 3) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b and c is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of MOM.9.a against the approved HIC masters and the AAC/COP drafts. Search terms: implant, prosthesis, batch, serial, discharge summary, Medical Devices Rules.
   AAC.1 -- implant types offered must match the service directory. Stated in Scope and step 1.
   AAC.8.c/d -- AAC.8 owns that a summary is given and its clinical content list; MOM.9.c owns that batch AND serial ALSO appear in the medical record, master logbook AND discharge summary. AAC.8 Scope hands this to MOM; this draft mirrors that split in Scope and step 3. Flagged for the AAC.8 drafter to keep the handoff.
   COP.11 -- implanting during a procedure is the surgical act (pause confirmation, operation-note identification); MOM.9 owns procurement criteria, counselling, traceability numbers. Stated in Scope and step 1. Flagged so COP.11's implant-record mention is not read as owning MOM.9.c.
   MOM.1.e -- chapter-level pointer; this document is the owning criteria. Stated in Purpose, Scope and step 1. Flagged for the MOM.1 drafter to point here and not rewrite.
   HIC.6 -- sterilisation and implant-load processing records remain HIC.6; post-implantation batch/serial traceability is here. Stated in Scope.
   PRE (undrafted) -- surgical consent method vs MOM.9.b counselling for usage/precautions. Stated in Scope and step 2.
3. FORWARD REFERENCES: AAC.8 discharge; PRE consent; MOM.1.e pointer; IMS record. Each is a deliberate boundary.
4. T2 QUICK CHECK: MOM.9.b vs PRE consent -- flagged. MOM.9.c vs AAC.8 discharge summary -- flagged and mirrored. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940 -- named in P2 and References insofar as implants are regulated devices. Hospital procures from a licensed source and does not become a manufacturer. No section number. No UDI numeric scheme printed as a mandate.
6. NDPS Act 1985 is NOT named in this document or in P2.
7. NO NUMBERS ARE STATED as requirements -- no implant sizes, no retention-year counts, no brand lists as NABH mandates. Every such value is [Hospital to define].
8. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act, 2010 are NOT named in P2.

EDITORIAL POSITIONS TAKEN
9. Step 1's rule that MOM.1.e is a pointer and that a manufacturer's technique guide is not hospital criteria are editorial positions required by the owner's instruction.
10. Step 1's rule that a hospital that does not implant records absence rather than inventing a programme is an editorial position.
11. Step 2's split between counselling and surgical consent is an editorial position required by the overlap brief; the standard requires counselling, not this distinction of documents.
12. Step 3's reading that a device without a manufacturer serial is recorded with the identifiers it carries, without inventing a serial, is an editorial position.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
13. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Medical Devices Rules, 2017, read with the Drugs and Cosmetics Act, 1940, insofar as they govern implantable prostheses and medical devices as regulated devices -- the statute this document's References actually rely on. It does NOT name NDPS, BMW Rules 2016, FSS Act 2006, or CEA 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Service directory method -- AAC.1.
- Discharge process and clinical content list of the summary -- AAC.8.
- Surgical act of implanting, checklist, operation note -- COP.11.
- Sterilisation cycle and implant-load biological monitoring -- HIC.6.
- Surgical consent method -- PRE.
- MOM.1 committee process; MOM.1.e is a pointer only.
- NDPS.
- Brand lists, sizes, techniques as NABH mandates.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 11 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 9 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 11; a search for "Hospital to define" without brackets finds all 11, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: types of implantable prosthesis and medical device used, aligned with the service directory, or recorded absence; how they are procured from a licensed source and how usage is authorised; where the written guidance is held; who counsels for usage and precautions and how that is recorded; where the master logbook is held and who writes batch and serial into the medical record, logbook and discharge summary; the named lead; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 3, printed page 81
-- (PDF page index 87). Levels: a Commitment, b Commitment, c Commitment.
-- ONE OE CARRIES THE ASTERISK -- MOM.9.a.
-- MOM.1.e is the chapter-level pointer; this document owns the criteria.
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
        json_name="mom9_draft.json",
        sql_name="mom9_insert.sql",
    )
