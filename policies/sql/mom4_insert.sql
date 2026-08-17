-- MOM.4 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 3, printed page 78
-- (PDF page index 84). Header (book's grammar): "Medications orders are written
-- in a uniform manner." Levels: a Commitment, b Commitment, c Commitment,
-- d Commitment.
-- ONE OE CARRIES THE ASTERISK -- MOM.4.a.
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
  'MOM.4',
  'MOM',
  array['MOM.4.a', 'MOM.4.b', 'MOM.4.c', 'MOM.4.d'],
  $q$Uniform Medication Orders$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} writes medication orders in a uniform manner: only authorised personnel write them; they are written in a uniform location in the medical record that also carries the patient's name and unique identification number; they are legible, dated, timed and signed; and they contain the name of the medicine, the route of administration, the strength to be administered, and the frequency or time of administration.

The chapter intent is that the organisation has a safe and organised medication process, and that prescription is governed by written guidance. An order that anyone can write, that lives in a different place in each file, that cannot be read, or that does not name the drug, the route, the strength and the time, is not that process. This document is the written-order artefact of that process.

This document is not the rational-prescribing policy and it is not the verbal-order policy. Those are owned by the safe-and-rational-prescribing policy of {{HOSPITAL_NAME}} (MOM.3). A verbal order, once it is written, becomes a MOM.4 order and is then governed here.$q$,
  $q$This policy applies to every location in which a medication order is written at {{HOSPITAL_NAME}}: in-patient wards, the emergency area, day-care, out-patient consulting rooms, the operation theatre and recovery, intensive or high-dependency areas where they exist, and any other clinical location in which a medicine is ordered in the medical record. It binds every person who writes a medication order, every person who transcribes a verbal order into writing, and the staff who refuse to act on an order that is not written by an authorised person, is not in the uniform location, is not legible, dated, timed and signed, or does not contain the required content.

It covers: that only authorised personnel write medication orders; that those orders are written in a uniform location in the medical records, which also reflects the patient's name and unique identification number; that orders are legible, dated, timed and signed; and that orders contain the name of the medicine, the route of administration, the strength to be administered, and the frequency or time of administration.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Generation of the unique identification number at registration is governed by the registration, admission and transfer policy of {{HOSPITAL_NAME}} (AAC.2). This policy requires that the uniform order location also reflects the patient's name and that unique identification number. It does not generate the number.
- The medical record itself — its structure, retention, and who may make an entry as a record-keeping act — is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the location of the medication order within that record, the legibility, dating, timing and signing of the order, and the content the order must carry. IMS does not decide whether an order is a valid medication order; this document does not write the hospital's whole record policy.
- Rational prescribing, the minimum requirements of a prescription as a prescribing standard, drug-allergy ascertainment before prescribing, and the verbal-order process are governed by the safe-and-rational-prescribing policy of {{HOSPITAL_NAME}} (MOM.3, sibling, drafted in this same chapter pass). This document owns the written order artefact. A verbal order is written under MOM.3's verbal-order process; once it exists as writing, it is a MOM.4 order and must meet this document's authorisation, location, legibility and content rules. MOM.3 does not write the uniform-location or authorised-writer rules; this document does not rewrite rational-prescribing method.
- Who is registered to practise as a medical practitioner is governed by the National Medical Commission Act, 2019 and State Medical Council registration, verified under the human resource policies of {{HOSPITAL_NAME}} (HRM, not yet drafted). Who is registered to practise as a nurse is governed by the Indian Nursing Council Act, 1947 and State Nursing Council registration, likewise verified under HRM. This policy owns that only the people the hospital has authorised to write medication orders actually write them. HRM verifies the credential; this document uses that verification and refuses an order written by a person who is not on the authorised list.
- Dispensing, including that an incomplete order is not dispensed, is governed by the safe-dispensing policy of {{HOSPITAL_NAME}} (MOM.5). Administration, including that an incomplete order is not administered, is governed by the safe-administration policy of {{HOSPITAL_NAME}} (MOM.6). This document owns the written artefact those later steps read.
- Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents — who may prescribe them, how they are stored, and how they are accounted — are governed by the high-risk-classes policy of {{HOSPITAL_NAME}} (MOM.8). An order for such an agent is still a MOM.4 order for authorisation, location, legibility and content. This document does not write the narcotic register and does not name the Narcotic Drugs and Psychotropic Substances Act as this document's statute.
- The two identifiers used at the point of care are governed by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1). Name and unique identification number on the order location are identity on the artefact; they are not a substitute for the administration-time identity check under MOM.6.c.$q$,
  $q${{HOSPITAL_NAME}} requires that only authorised personnel write medication orders. An order written by a person who is not authorised is not an order of this hospital and is not acted on.

{{HOSPITAL_NAME}} writes medication orders in a uniform location in the medical record. That location also reflects the patient's name and unique identification number.

{{HOSPITAL_NAME}} requires that medication orders are legible, dated, timed and signed. An order that cannot be read, that has no date, that has no time, or that is unsigned, is not acted on until it is clarified and completed.

{{HOSPITAL_NAME}} requires that a medication order contains the name of the medicine, the route of administration, the strength to be administered, and the frequency or time of administration. An order that lacks any of those elements is incomplete and is not dispensed or administered.

{{HOSPITAL_NAME}} treats a verbal order, once written, as a medication order under this document.$q$,
  array[
    $s$1. Only authorised personnel write medication orders

{{HOSPITAL_NAME}} ensures that only authorised personnel write medication orders. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask who may write an order on yesterday's charts, not whether a list of designations exists in a file. The answer must be that the person whose name is on the order was authorised to write it, and that an unauthorised name is refused.

The reason this is the safety step is that a medication order is both a clinical instruction and, for Schedule H and Schedule H1 medicines, a legal document under the Drugs and Cosmetics Act, 1940 and the rules under it. An unauthorised writer produces an artefact that looks like an order and is treated as one by a busy ward, a pharmacy, or a covering nurse, but is not a prescription this hospital can stand behind and is not a practising act the National Medical Commission Act, 2019 (or, where a nurse writes, the Indian Nursing Council Act, 1947) recognises. The common error is the workaround that follows a busy round: a student, an intern whose authorisation has not been defined, a ward clerk, or a nurse who is not on the hospital's writer list, writing in the consultant's name; a stamp in place of a signature; a telephone message written by whoever answered the phone. That workaround is how a person who may not practise here writes an order that is then dispensed and given. It is forbidden here.

Who may write a medication order at {{HOSPITAL_NAME}} is [Hospital to define — who may write medication orders, by role, and whether a registered nurse may write]. The statutory gate for a medical practitioner is current registration under the National Medical Commission Act, 2019 and the State Medical Council. The statutory gate for a nurse, if this hospital's written rule permits a registered nurse to write an order, is current registration under the Indian Nursing Council Act, 1947 and the State Nursing Council, and a scope of writing that the hospital has named. Registration is not, by itself, authorisation to write every class of order in every location. Human-resource procedures verify registration; this step uses that verification and adds the hospital's further gate: the person is on the authorised-writers list for the setting and the class of order. A person whose registration has lapsed, who is not on that list, or who is writing outside the named scope, does not write.

The authorised-writers list, including the settings and any class-of-order limits, is held at [Hospital to define — where the authorised-writers list is held, and who keeps it current]. The named keeper uses the human-resource verification; this document does not restate the credentialing file. Visiting and honorary practitioners write only if they are on that list.

A verbal order is taken under the verbal-order process of the safe-and-rational-prescribing policy of {{HOSPITAL_NAME}} (MOM.3). The person who writes that verbal order into the record must be a person authorised under this step. Once written, the order is a MOM.4 order: it sits in the uniform location, it is dated, timed and signed (or signed as a read-back transcription pending the prescriber's countersignature under MOM.3), and it carries the content at step 4. MOM.3 owns that verbal orders are used safely; this step owns that the writing is done by an authorised person. Stretching MOM.3 to let an unauthorised person "just write it down" is the failure this paragraph exists to stop.

This step does not authorise a pharmacist to write a treatment order unless the hospital's written rule and the pharmacist's professional registration both allow a defined class of writing. Dispensing remains under the safe-dispensing policy. This step does not write the narcotic, chemotherapy or radioactive prescribing rules; those remain under the high-risk-classes policy of {{HOSPITAL_NAME}}. An order for such an agent is still written only by a person authorised here and, where MOM.8 requires a further appropriate caregiver, by a person who meets that further rule as well.

An order found to have been written by a person who was not authorised is not acted on. It is returned for a valid order, and the event is treated as a defect, not as a paperwork inconvenience.$s$,
    $s$2. Uniform location, with the patient's name and unique identification number

Medication orders are written in a uniform location in the medical records, which also reflects the patient's name and unique identification number.

The uniform location, for in-patient, out-patient, emergency and any other record this hospital uses, is [Hospital to define — the uniform location in the medical record where medication orders are written, for in-patient, out-patient and emergency records]. Orders written only in a progress note, on a loose slip, on a glove, or in a private diary are not in the uniform location and are not acted on until they are entered there.

The unique identification number is generated at registration under the registration, admission and transfer policy of {{HOSPITAL_NAME}}. This step requires that number, and the patient's name, on the order location. It does not issue the number. An unidentified emergency patient is identified under that registration mechanism; orders are then written on a location that carries the name and number as soon as they exist.

The medical record itself remains under the information-management policies. This step owns only that the medication order has one home in that record, and that the home identifies the patient.$s$,
    $s$3. Orders are legible, dated, timed and signed

Medication orders are legible, dated, timed and signed.

An order that cannot be read by the person who must dispense or administer it is not legible. An order with a date but no time, a time but no date, or a name-stamp without a signature, is incomplete. How an incomplete, illegible or unsigned order is clarified before it is acted on is [Hospital to define — how an incomplete, illegible or unsigned order is clarified before it is acted on]. The order is not guessed.

The National Coordinating Council for Medication Error Reporting and Prevention recommendations on accuracy of prescription and medication-order writing (chapter references 25 and 26) are a recognised framework this hospital may use when it writes the clarification method and any local list of error-prone abbreviations. This document does not import that Council's abbreviation table, leading-zero rule, or metric-system table as a NABH mandate. It requires that the order can be read, and that it carries a date, a time and a signature.

Countersignature of a transcribed verbal order follows the verbal-order process of the safe-and-rational-prescribing policy; the written line still has a time, a date and the writer's identification under this step.$s$,
    $s$4. Required content of a medication order

Medication orders contain the name of the medicine, the route of administration, the strength to be administered, and the frequency or time of administration. An order that lacks any of those four elements is incomplete. It is not dispensed and it is not administered until it is completed.

The safe-and-rational-prescribing policy of {{HOSPITAL_NAME}} owns the minimum requirements of a prescription as a prescribing standard. This step owns that the written order artefact in the uniform location actually carries these four elements. The two are consistent; they are not the same act.

A change of dose, route or frequency is a new order under this step: dated, timed, signed, in the uniform location, written by an authorised person. A cancelled order is marked so that it cannot be read as current.$s$,
    $s$5. Records, review and the order of operations

Every medication order is recorded in the uniform location against the unique identification number: the authorised writer, the date and time, the signature, and the name, route, strength and frequency or time of the medicine.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for medication-order records] for: orders written only by a person on the authorised-writers list; orders only in the uniform location, with name and unique identification number present; orders that are legible, dated, timed and signed; and orders that contain the four required content elements rather than a guessed completion.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when an unauthorised writer, an order found outside the uniform location, an illegible order that was acted on, or a missing content element that reached the patient exposes a gap, or when the prescribing, dispensing, administration, human-resource or information-management policies that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} accepting medication orders only from authorised personnel, only in the uniform location, and only when they are legible, dated, timed, signed and complete.

The named keeper of the authorised-writers list at step 1 keeps that list current against human-resource verification of registration.

Every person who writes a medication order writes only if authorised, writes in the uniform location, dates, times and signs, and includes the name of the medicine, the route, the strength and the frequency or time.

Pharmacy staff and the persons who administer medicines refuse an order that is not written by an authorised person, is not in the uniform location, is not legible, dated, timed and signed, or lacks required content, and obtain a valid order.

The quality or accreditation coordinator audits the records at step 5 and reports findings to the head of the institution.

All staff are expected to treat an unauthorised writer, an order outside the uniform location, an illegible or unsigned order that was acted on, and a missing content element, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 3 Management of Medication, standard MOM.4.
- National Medical Commission Act, 2019 and State Medical Council registration — insofar as they govern who may write a medication order as a medical practitioner.
- Indian Nursing Council Act, 1947 and State Nursing Council registration — insofar as hospital rules permit a registered nurse to write a medication order within that professional scope.
- Drugs and Cosmetics Act, 1940 and the rules under it — insofar as a prescription or medication order is a legal document for the sale or supply of Schedule H and Schedule H1 medicines. No section number is imported as a mandate.
- National Coordinating Council for Medication Error Reporting and Prevention, Recommendations to Enhance Accuracy of Prescription/Medication Order Writing (chapter references 25 and 26) — a recognised framework the hospital may use; this document does not import that Council's abbreviation table or numeric writing rules as a NABH mandate.
- Internal documents of {{HOSPITAL_NAME}}: the authorised-writers list; the uniform order location in each record type; the clarification method for incomplete or illegible orders; the safe-and-rational-prescribing policy; the safe-dispensing policy; the safe-administration policy; the high-risk-classes medication policy; the registration, admission and transfer policy; the uniform-care policy; the human resource policies; and the information-management policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every in-patient ward; the emergency area; day-care; out-patient consulting rooms; the operation theatre and recovery; intensive or high-dependency areas where they exist; pharmacy; nursing administration; and every head of department whose staff write medication orders.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The authorised-writers list and the statement of the uniform order location — the working documents this policy requires — are held in every location that writes orders.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

NMC — National Medical Commission
INC — Indian Nursing Council
NCCMERP — National Coordinating Council for Medication Error Reporting and Prevention
UID — Unique Identification Number
IMS — Information Management System (the information-management chapter of these standards)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the National Medical Commission Act, 2019, insofar as it governs who may write a medication order as a medical practitioner, the Indian Nursing Council Act, 1947 insofar as hospital rules permit a registered nurse to write a medication order within that professional scope, and the Drugs and Cosmetics Act, 1940 and the rules under it insofar as a prescription or medication order is a legal document for the sale or supply of Schedule H and Schedule H1 medicines. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "MOM.4.a", "requirement": "The organisation ensures that only authorised personnel write orders.", "steps": "Steps 1, 5", "evidence": "The written authorised-writers list, by role, setting and any class-of-order limits, stating the statutory gate of current National Medical Commission Act, 2019 and State Medical Council registration for a medical practitioner and, if this hospital permits a registered nurse to write, the statutory gate of current Indian Nursing Council Act, 1947 and State Nursing Council registration together with the named scope of writing, and showing that registration is used from human-resource verification rather than restated as a credentialing method; the named keeper of that list and where the list is held, with visiting and honorary practitioners included only if they are on the list; sample medication orders against the unique identification number showing the writer was on the list for that setting and class, rather than a student, an undefined intern, a ward clerk, or a nurse who is not on the list writing in a consultant's name, and rather than a stamp in place of a signature; the recorded rule that a verbal order taken under the safe-and-rational-prescribing policy is written into the record only by a person authorised under this step and then becomes a MOM.4 order; the recorded statement that a pharmacist does not write a treatment order unless the hospital's written rule and professional registration both allow a defined class of writing, and that narcotic, chemotherapy and radioactive prescribing rules remain under the high-risk-classes policy while the order artefact remains a MOM.4 order; records of an order found to have been written by a person who was not authorised being refused and treated as a defect rather than dispensed or administered; induction or briefing records showing staff who write, dispense or administer have been shown the authorised-writers list; the audit sample at step 5 of orders written only by a person on that list", "responsible": "Named keeper holds the authorised-writers list against human-resource verification; persons who write orders write only if on that list; pharmacy and administering staff refuse an unauthorised order; head of the institution is accountable that unauthorised persons do not write; quality or accreditation coordinator audits"}, {"oe_code": "MOM.4.b", "requirement": "Medication orders are written in a uniform location in the medical records, which also reflects the patient's name and unique identification number.", "steps": "Steps 2, 5", "evidence": "The written uniform location for in-patient, out-patient and emergency records; sample orders in that location showing the patient's name and unique identification number, which is generated under the registration policy and not issued here; records showing an order written only in a progress note or on a loose slip was not acted on until entered in the uniform location; the recorded division that information-management policies own the record and this policy owns the order's home in it", "responsible": "Persons who write orders write in the uniform location; information-management policies own the record; registration policy owns generation of the unique identification number; quality or accreditation coordinator audits"}, {"oe_code": "MOM.4.c", "requirement": "Medication orders are legible, dated, timed and signed.", "steps": "Steps 3, 5", "evidence": "The written clarification method for an incomplete, illegible or unsigned order; sample orders showing a date, a time and a signature rather than a stamp alone; records showing an illegible order was clarified rather than guessed; the recorded statement that NCCMERP order-writing recommendations are a framework and not a mandated abbreviation table", "responsible": "Persons who write orders date, time and sign a legible order; pharmacy and administering staff refuse an order that cannot be read; quality or accreditation coordinator audits"}, {"oe_code": "MOM.4.d", "requirement": "Medication orders contain the name of the medicine, route of administration, strength to be administered and frequency/time of administration.", "steps": "Steps 4, 5", "evidence": "Sample orders in the uniform location showing name of medicine, route, strength and frequency or time of administration; records of an incomplete order not dispensed and not administered until completed; records of a change of dose, route or frequency entered as a new dated, timed and signed order; the recorded division that the prescribing policy owns prescription minimums as a prescribing standard and this step owns the written artefact", "responsible": "Persons who write orders include the four content elements; pharmacy and administering staff refuse an incomplete order; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. MOM.4 standard text and all four OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 3 Management of Medication, printed page 78 (PDF page index 84). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page and opened for this draft (md5 39e3bc86d73d651b9cfef283bbf018a9). OE-page header quote: "Medications orders are written in a uniform manner." (the book's grammar). Chapter-summary line on printed page 75 (PDF page index 81) uses "Medication orders are written in a uniform manner." This draft quotes the OE-page header. Levels: MOM.4.a Commitment, MOM.4.b Commitment, MOM.4.c Commitment, MOM.4.d Commitment.
   ONE OE CARRIES THE ASTERISK -- MOM.4.a. The draft builds one deep block (step 1 for a). MOM.4.b, MOM.4.c and MOM.4.d are unasterisked and are correspondingly Tier 2.
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; 408 OEs, 132 asterisks; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the MOM.4 page read directly from the extracted page text, and the committed asterisk file. MOM.4 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. ONE OF FOUR OEs IS TIER 1. Tier 1: MOM.4.a only -- procedure step 1 carries the reasoning (why an unauthorised writer is a legal and clinical failure, why a stamp or a student writing in a consultant's name is the common error, why a verbal order once written is still a MOM.4 authorisation problem). Tier 2: MOM.4.b (step 2), MOM.4.c (step 3), MOM.4.d (step 4) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b-d is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of MOM.4.a against the approved HIC.1-HIC.6 masters and the AAC.1-AAC.8 and COP.1-COP.13 drafts. Search terms: medication order, prescription, authorised, authorized, write orders, NMC, nursing council.
   AAC.2 -- generates the unique identification number. MOM.4.b requires name and that number on the order location; it does not generate the number. Stated in Scope and step 2.
   IMS -- owns the medical record. MOM.4 owns order location, legibility and content. Stated in Scope.
   MOM.3 -- owns rational prescribing and verbal orders. MOM.4 owns the written order artefact. A verbal order once written becomes a MOM.4 order. Stated in Scope and step 1. Flagged for the MOM.3 drafter to mirror.
   HRM / NMC credentialing -- verifies who may practise. MOM.4.a owns that only those authorised people write orders. Stated in Scope and step 1.
   MOM.8 -- high-risk classes (NDPS, chemo, radioactive). An order for those agents is still a MOM.4 order; this document does not write the narcotic register and does not name NDPS in P2.
   MOM.5 / MOM.6 -- refuse incomplete or unauthorised orders at dispense and at administer. Stated in Scope.
3. FORWARD REFERENCES: MOM.3 verbal orders and rational prescribing; MOM.5 dispensing; MOM.6 administration; MOM.8 high-risk classes; HRM credentialing; IMS record; AAC.2 UID generation; COP.1 two identifiers at the point of care. Each is a deliberate boundary.
4. T2 QUICK CHECK: MOM.4.b vs AAC.2 UID and IMS record -- flagged in Scope. MOM.4.c vs IMS record-keeping -- flagged. MOM.4.d vs MOM.3.b minimum requirements of a prescription -- flagged: MOM.3 owns the prescribing standard, MOM.4 owns the written artefact. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. National Medical Commission Act, 2019 -- cited insofar as it governs who may write a medication order as a medical practitioner. No section number. Hospital-defined authorisation is additional, not a substitute for registration.
6. Indian Nursing Council Act, 1947 -- cited in References and in P2 because this document permits the hospital to authorise a registered nurse to write, if hospital rules and professional scope allow. If the hospital's filled-in list does not include nurses as writers, the insofar-as clause does not attach a writing duty the hospital has not created.
7. Drugs and Cosmetics Act, 1940 and the rules under it -- cited insofar as a prescription or medication order is a legal document for Schedule H and Schedule H1 medicines. No section number. No wholesale drug-storage method.
8. NDPS Act 1985 is NOT named in P2 and is not written as a register or destruction method. Forward-ref MOM.8.
9. NCCMERP Recommendations to Enhance Accuracy of Prescription/Medication Order Writing (chapter refs 25 and 26) -- used as a recognised framework. NOT used as a mandated abbreviation ban-list, leading-zero rule, or metric table.
10. NO NUMBERS ARE STATED as requirements -- no abbreviation counts, no countersignature-hour windows, no signature-format millimetres. Every such value is [Hospital to define]. Consistent with the no-numbers default.
11. Bio-Medical Waste Management Rules, 2016, Food Safety and Standards Act, 2006, and Clinical Establishments Act, 2010 are NOT named in P2. CEA is not defaulted from AAC.

EDITORIAL POSITIONS TAKEN
12. Step 1's rule that a stamp is not a signature, that a student or undefined intern writing in a consultant's name is not an authorised order, and that a verbal order may not be written down by an unauthorised person, are editorial positions.
13. Step 1's refusal to let a pharmacist write a treatment order unless hospital rule and registration both allow a defined class, and the refusal to cite NDPS as this document's statute, are editorial positions required by the owner's instruction.
14. Step 2's rule that a progress-note-only or loose-slip order is not in the uniform location is an editorial position; the standard requires a uniform location, not this exclusion list.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
15. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the National Medical Commission Act, 2019, the Indian Nursing Council Act, 1947, and the Drugs and Cosmetics Act, 1940 -- the statutes this document's References actually rely on. It does NOT name NDPS, BMW Rules 2016, FSS Act 2006, or CEA 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Rational prescribing method, allergy ascertainment, verbal-order process -- MOM.3.
- Dispensing, recalls, near-expiry handling at the hatch, dispensed-pack labelling -- MOM.5.
- Administration checks, tubing misconnections, self-administration -- MOM.6.
- Narcotic register, storage and destruction -- MOM.8.
- Generation of the unique identification number -- AAC.2.
- The medical record policy -- IMS.
- Credentialing method -- HRM.
- A mandated error-prone-abbreviation table or leading-zero rule as NABH.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 9 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 7 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 9; a search for "Hospital to define" without brackets finds all 9, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: who may write medication orders, by role, and whether a registered nurse may write; where the authorised-writers list is held and who keeps it current; the uniform order location for in-patient, out-patient and emergency records; how an incomplete, illegible or unsigned order is clarified; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
