-- COP.4 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 2, printed page 63
-- (PDF page index 69). Levels: a Core, b Commitment, c Commitment, d Excellence.
-- TWO OEs CARRY THE ASTERISK -- COP.4.a (Core) and COP.4.d (Excellence).
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
  'COP.4',
  'COP',
  array['COP.4.a', 'COP.4.b', 'COP.4.c', 'COP.4.d'],
  $q$Nursing Care$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} provides nursing care in consonance with clinical protocols: nursing care aligned and integrated with overall patient care and documented in the patient record; assignment of patient care according to current good clinical and nursing practice; nurses provided with the equipment that care requires; and nursing clinical practice guidelines that reflect current standards of practice and are actually used.

Nursing that is done and not written, assigned by habit rather than by the patient's need, or guided by a medical protocol that never tells a nurse what to observe, is not the care this standard asks for. This document is the process that makes nursing visible in the record, assigned, equipped and guided.$q$,
  $q$This policy applies to every setting in which a nurse of {{HOSPITAL_NAME}} provides care: the out-patient department, day-care, every in-patient ward, the emergency area, the operation theatre and recovery, intensive or high-dependency areas where they exist, labour and procedure rooms, and any other clinical location in which nursing care is given. It binds the nurses who provide and document care, the nurses in charge who assign care, the nursing administration that holds the nursing clinical practice guidelines, and the clinicians whose overall plan the nursing care is aligned with.

It covers: nursing care aligned and integrated with overall patient care and documented in the patient record; assignment of patient care as per current good clinical and nursing practice guidelines; appropriate and adequate equipment for safe and efficient nursing services; and development and implementation of nursing clinical practice guidelines reflecting current standards of practice.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Standardised handover method, including shift-to-shift and unit-to-unit handover, is governed by the continuity-of-care policy of {{HOSPITAL_NAME}} (AAC.7). This policy owns the nursing content of the patient record — what was observed, what was done, and how that care aligned with the overall plan. AAC.7 owns the method by which that information is handed over. The two are not the same act. This document does not write a handover tool.
- The medical record itself — its structure, retention, numbering and confidentiality — is governed by the information-management policies of {{HOSPITAL_NAME}} (IMS, not yet drafted). This policy owns the nursing entries written into that record. It does not design the form.
- The documented care plan produced by the initial assessment is governed by the assessment policy of {{HOSPITAL_NAME}} (AAC.3). This policy requires that nursing care is aligned with that overall plan and that the alignment is visible in the nursing entries. It does not rewrite the care-plan method.
- Hospital-wide evidence-based clinical protocols for a given condition are governed by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1.c and COP.1.d). This policy's nursing clinical practice guidelines (COP.4.d) are nursing standards of practice. They are not a second set of medical protocols, and COP.1 does not write them.
- Hand hygiene, personal protective equipment, transmission-based precautions, injection safety and linen handling as infection-control methods are governed by the infection-control policies of {{HOSPITAL_NAME}} (HIC.2). Nurses follow those methods in the course of nursing care. This document points at HIC.2; it does not restate five moments, PPE donning, isolation categories or the injection-safety rules.
- Reprocessing of reusable nursing equipment is governed by the sterilisation and disinfection policy of {{HOSPITAL_NAME}} (HIC.6). This policy owns that nurses have the equipment they need, ready for use.
- Verification of nursing qualifications, Indian Nursing Council / State Nursing Council registration and credentials is governed by the human resource policies of {{HOSPITAL_NAME}} (HRM, not yet drafted). This policy uses that verification when assigning care; it does not restate the credentialing method.
- Planned maintenance of equipment may be performed under the facility-management policies of {{HOSPITAL_NAME}} (FMS, not yet drafted). This policy owns that the equipment nurses need is present and usable at the point of care.$q$,
  $q${{HOSPITAL_NAME}} aligns and integrates nursing care with overall patient care, and documents that nursing care in the patient record. Care that was given and not written is not available to the next nurse, the treating clinician, or the record.

{{HOSPITAL_NAME}} assigns patient care as per current good clinical and nursing practice guidelines. Assignment is a clinical act, not a convenience roster.

{{HOSPITAL_NAME}} provides nurses with appropriate and adequate equipment for safe and efficient nursing services.

{{HOSPITAL_NAME}} develops and implements nursing clinical practice guidelines that reflect current standards of practice. A guideline that exists as a file and is not used is not implemented.$q$,
  array[
    $s$1. Nursing care aligned, integrated and documented in the patient record

Nursing care is aligned and integrated with overall patient care, and is documented in the patient record. This step is the documented-evidence anchor of a requirement the standard places at Core and asterisks: an assessor will ask to see, in the record, that what the nurse did belongs to the same plan as what the clinician ordered, and that it was written at the time, not reconstructed later.

Aligned and integrated means the nursing observations, the nursing actions and the nursing evaluation sit against the current overall care plan — the plan the assessment policy of {{HOSPITAL_NAME}} (AAC.3) produces — and against the condition-specific clinical protocol the uniform-care policy (COP.1) has adopted for that patient, where one exists. A nursing note that could belong to any patient, or that records tasks without relating them to the plan, is not alignment. A nurse who follows a personal routine that contradicts the plan is not integrated care.

The reason this step exists as a written requirement, rather than as "nurses always document," is that the record is the only place the next shift, the treating clinician, and a later reviewer can see what was actually done. Verbal nursing care dies at the end of the shift. A Kardex, a whiteboard or a messaging-app update that is not the patient record is not the record. When the nursing entry is missing, the overall plan has a hole in it: the clinician cannot see the response to treatment, the next nurse cannot see what was already tried, and the hospital cannot show that nursing care was part of the same care. That is why documentation in the patient record is the safety step, and why the standard asterisks it.

The common error is a complete medical note and a thin, delayed or copied nursing entry — or an entry that lists tasks (medications given, vitals taken) without connecting them to the plan (why those observations matter for this patient today). The control is a nursing entry, against the unique identification number, made in the patient record, that states the observations, the care given, the response, and the link to the current plan. Copy-forward of yesterday's note as if it were today's assessment is forbidden.

What the nursing entry contains, the form or fields used, and the expected timing of the entry relative to the care, are [Hospital to define — the nursing-entry content, the form or fields used, and the expected timing of the entry]. The information-management policies of {{HOSPITAL_NAME}} own the structure of the record. This step owns the nursing content that is written into it.

Handover of that content from one nurse to the next, and from one unit to another, uses the structured method owned by the continuity-of-care policy of {{HOSPITAL_NAME}} (AAC.7). This step does not write that method. A completed handover is not a substitute for the nursing entry in the record: handover communicates; the record retains. Making one is not making the other.

Hand hygiene, personal protective equipment and transmission-based precautions applied while giving the care remain the infection-control policies of {{HOSPITAL_NAME}} (HIC.2). The nursing entry records that care was given; it does not restate the five moments or the PPE sequence.

The unique identification number on every nursing entry is the number issued at registration (AAC.2.b). This step does not generate it.$s$,
    $s$2. Assignment of patient care

Assignment of patient care is done as per current good clinical / nursing practice guidelines.

Who assigns nursing care, for which period, and on what basis, are [Hospital to define — who assigns nursing care, for which period, and on what basis]. The basis is current good practice, not a permanent named-nurse-to-bed list that ignores acuity, skill or the patient's current plan. An acuity-based method is permitted if {{HOSPITAL_NAME}} chooses it; it is not required, and this document does not import a staffing ratio.

Assignment uses the professional registration already verified under the human resource policies of {{HOSPITAL_NAME}}. A nurse is not assigned care this hospital has not verified they are registered to give.

The assignment is recorded. A patient without a named assigned nurse for the current period is a break in nursing care.$s$,
    $s$3. Equipment for safe and efficient nursing

Nurses are provided with appropriate and adequate equipment for providing safe and efficient nursing services.

The nursing equipment that must be present, by area, and how absence or failure is reported, are [Hospital to define — the nursing equipment that must be present by area, and how absence or failure is reported]. Adequacy is judged against the care this hospital's nurses actually give in that area, not against a generic catalogue.

Reusable items are reprocessed between patients under the sterilisation and disinfection policy of {{HOSPITAL_NAME}} (HIC.6). This step owns that a ready item is available to the nurse. Planned maintenance may be performed under the facility-management policies; this step owns that an item that is missing, failed or still dirty is not counted as available.

This document does not state a required number of devices per bed.$s$,
    $s$4. Nursing clinical practice guidelines

The organisation develops and implements nursing clinical practice guidelines reflecting current standards of practice. This step is the documented-evidence anchor of a requirement the standard places at Excellence and asterisks. An assessor will ask which nursing guidelines are in use and how a nurse actually applies them, not whether a medical protocol exists.

A nursing clinical practice guideline tells a nurse how to nurse: what to observe, what to do, what to record, and when to escalate, for the nursing problems this hospital's patients present. It is not a reprint of the hospital-wide medical protocol owned by the uniform-care policy of {{HOSPITAL_NAME}} (COP.1.c). That protocol guides the clinical condition. This guideline guides the nursing work around it. Adopting only the medical protocol and calling it a nursing guideline is the common error this step exists to stop: the nurse is then left with a diagnosis pathway and no nursing standard, and assignment at step 2 has nothing current to assign against.

The reason the guideline must be implemented, not merely developed, is the same reason a protocol folder is not uniform care. A nursing guideline that sits in nursing administration and is unknown on the ward is a document, not a practice. Implementation means the current version is held where the care is given, staff who assign and give care can name it, and the nursing entry at step 1 can be read against it. A withdrawn guideline is removed from the points of use.

Current standards of practice means the guideline is dated, cites the nursing or clinical source it drew on, and is reviewed. Sources this hospital may use include Indian Nursing Council standards of nursing practice and other recognised nursing guidance. Chapter references 5, 6, 37 and 63 of this chapter discuss nurse staffing and engagement; they inform that assignment and practice are related. They are not imported as required staffing numbers. This document does not state a nurse-to-patient ratio.

The nursing clinical practice guidelines in current use, the nursing problems or processes they cover, and where they are held, are [Hospital to define — the nursing clinical practice guidelines in current use, the nursing problems or processes they cover, and where they are held]. How staff are shown the current version, and the review interval for each guideline, are [Hospital to define — how staff are shown the current nursing clinical practice guidelines, and the review interval for each guideline].

A new or revised guideline is issued to every setting in which that nursing care is given, and the previous version is withdrawn on the same date — the same control the uniform-care policy uses for medical protocols, applied here to nursing guidelines.$s$,
    $s$5. Records, review and the order of operations

Every nursing entry, every assignment, every equipment-absence report, and every nursing clinical practice guideline in force is recorded against the unique identification number where a patient is involved, and is retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for nursing-care records] for: nursing entries in the patient record that connect observations and actions to the current overall plan rather than a copied task list; assignment records that name the nurse for the period; equipment-absence reports that were acted on; and nursing clinical practice guidelines that are the version in use in the settings that give that care, distinct from the medical protocols of COP.1.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a missing nursing entry, an unassigned patient, a missing piece of equipment or an unused guideline exposes a gap, or when the continuity-of-care, assessment, uniform-care, infection-control or information-management policies that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} documenting nursing care in the patient record, for assignment that follows current good practice, for equipment that is actually present, and for nursing clinical practice guidelines that are used.

Nursing administration authors and keeps current the nursing clinical practice guidelines at step 4, holds the assignment method at step 2, and reports equipment shortfalls at step 3.

The nurse in charge of each area assigns care for the period, keeps the current nursing guidelines in that area, and does not count missing or un-reprocessed equipment as available.

Nurses provide care aligned with the overall plan, write the nursing entry in the patient record at step 1, follow HIC.2 while giving care, and apply the current nursing guideline. They do not treat handover as a substitute for the entry.

Treating clinicians keep the overall care plan current so that nursing alignment at step 1 has a plan to align with.

The quality or accreditation coordinator audits the records at step 5 and reports findings to the head of the institution.

All staff are expected to treat a patient whose nursing care was not written, a period with no named assigned nurse, and a guideline that is not the version in use, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.4.
- Indian Nursing Council Act, 1947 and State Nursing Council registration — who may be assigned as a nurse and the professional-practice context of nursing clinical practice guidelines. No section number. This document does not convert the Act into a named staffing ratio or a mandated course list.
- Barton, N. (2013), Acuity-Based Staffing — chapter reference 5; Brooks Carthon et al. (2019) on nurse engagement and staffing — chapter reference 6; Nguyen (2015) and Whitehead and Myers (2016) — chapter references 37 and 63. Cited only as informing that assignment may take account of acuity and skill. No ratio is mandated.
- Internal documents of {{HOSPITAL_NAME}}: the nursing-entry content and form; the assignment method; the nursing-equipment list by area; the nursing clinical practice guidelines; the continuity-of-care policy; the assessment policy; the uniform-care policy; the infection-control policies; the sterilisation and disinfection policy; the human resource policies; the facility-management policies; and the information-management policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: nursing administration; every in-patient ward; the emergency area; day-care; the operation theatre and recovery; intensive or high-dependency areas where they exist; the out-patient department; and every head of department whose staff work with nursing care.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The nursing-entry guidance, the assignment method and the nursing clinical practice guidelines — the working documents this policy requires — are held in every area that provides nursing care.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, PPE, WHO and SOP.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

INC — Indian Nursing Council
CPG — Clinical Practice Guideline
UID — Unique Identification Number

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Indian Nursing Council Act, 1947 and State Nursing Council registration, insofar as who may be assigned as a nurse and as the professional-practice context of nursing clinical practice guidelines. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "COP.4.a", "requirement": "Nursing care is aligned and integrated with overall patient care, and is documented in the patient record", "steps": "Steps 1, 5", "evidence": "The written nursing-entry content, the form or fields used, and the expected timing of the entry relative to the care; sample patient records showing nursing observations, actions and evaluation written in the patient record against the unique identification number, connected to the current overall care plan produced under AAC.3 and to the condition-specific protocol under COP.1 where one exists, rather than a task list that could belong to any patient or a copy-forward of yesterday's note; records showing a Kardex, whiteboard or messaging-app update was not treated as the patient record; records distinguishable from AAC.7 handover (handover present as the method of communication, nursing entry present as the retained record, neither treated as a substitute for the other); the stated division that IMS owns record structure and this policy owns nursing content; briefing or induction records showing nurses have been shown the entry standard; the audit sample at step 5 of nursing entries that connect observations and actions to the current overall plan rather than a copied task list, including entries from more than one setting", "responsible": "Nurses write the aligned entry in the patient record; treating clinicians keep the overall plan current; AAC.7 owns handover method; information-management policies own record structure; quality or accreditation coordinator audits"}, {"oe_code": "COP.4.b", "requirement": "Assignment of patient care is done as per current good clinical / nursing practice guidelines", "steps": "Steps 2, 5", "evidence": "The written assignment method naming who assigns, for which period, and on what basis, without a mandated staffing ratio; sample assignment records naming the nurse for the period; records showing assignment used verified professional registration; the audit sample at step 5 of assignment records that name the nurse for the period", "responsible": "Nurse in charge assigns care; human resource policies verify registration; quality or accreditation coordinator audits"}, {"oe_code": "COP.4.c", "requirement": "Nurses are provided with appropriate and adequate equipment for providing safe and efficient nursing services", "steps": "Steps 3, 5", "evidence": "The written nursing-equipment list by area and the method for reporting absence or failure; sample reports of missing or failed equipment and the action taken; records showing reusable items counted as available only after reprocessing under HIC.6; the audit sample at step 5 of equipment-absence reports that were acted on", "responsible": "Nursing administration and the nurse in charge keep equipment present; HIC.6 owns reprocessing; facility-management policies may perform planned maintenance; quality or accreditation coordinator audits"}, {"oe_code": "COP.4.d", "requirement": "The organization develops and implements nursing clinical practice guidelines reflecting current standards of practice", "steps": "Steps 4, 1, 5", "evidence": "The written set of nursing clinical practice guidelines in current use, naming the nursing problems or processes each covers, dated, citing the nursing or clinical source drawn on, and held where the care is given rather than only in nursing administration; records showing each guideline is distinct from the hospital-wide medical protocols owned by COP.1.c, not a reprint of those protocols labelled as nursing; records of issue to every setting in which that nursing care is given and withdrawal of the previous version on the same date; the written method by which staff who assign and give care are shown the current version, and the review interval for each guideline; sample nursing entries at step 1 that can be read against the current guideline for that nursing problem; briefing or induction records of nurses in the settings that use each guideline; records of a withdrawn guideline removed from points of use; the audit sample at step 5 of nursing clinical practice guidelines that are the version in use in the settings that give that care, distinct from the medical protocols of COP.1, and of no undated or personal nursing routine found substituting for the current guideline", "responsible": "Nursing administration authors, issues and withdraws the guidelines; nurses in charge keep the current version in their area; nurses apply the current guideline; quality or accreditation coordinator audits implementation rather than filing"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. COP.4 standard text and all four OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 2 Care of Patients, printed page 63 (PDF page index 69). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: COP.4.a Core, COP.4.b Commitment, COP.4.c Commitment, COP.4.d Excellence.
   TWO OEs CARRY THE ASTERISK -- COP.4.a and COP.4.d. The draft builds two separate deep blocks (step 1 for a; step 4 for d). COP.4.b (assignment) and COP.4.c (equipment) are unasterisked and are correspondingly Tier 2.
   COP.4.a is Core AND asterisked, so it is Tier 1. Core is not what allocates depth; the asterisk is. Contrast COP.1.a (Core, unasterisked, Tier 2).
   Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the COP.4 page read directly from the extracted page text, and the committed asterisk file. COP.4 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. Tier 1: COP.4.a, COP.4.d -- procedure steps 1 and 4 carry the reasoning (why the nursing entry in the patient record is the safety step; why a medical protocol is not a nursing guideline). Tier 2: COP.4.b (step 2) and COP.4.c (step 3) -- requirement and method without extended rationale. Reviewer to note the shallower treatment of b and c is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of COP.4.a/d against the approved HIC masters and the AAC drafts. Files: /tmp/aac_drafts/hic1 through hic6 and aac1 through aac8. Search terms: nursing, handover, patient record, assignment, clinical practice guideline, equipment.
   AAC.7 owns handover METHOD (structured communication at shift and at internal transfer). This draft owns nursing CONTENT of the patient record. Stated in Scope and step 1: handover communicates; the record retains; neither substitutes. Flag for master-policy-todos.md so the division is not lost if one is approved without the other.
   AAC.3 owns the care plan. This draft requires nursing care to align with that plan and to make the alignment visible in the nursing entry. Not a rewrite of AAC.3. Stated in Scope.
   COP.1.c/d own hospital-wide medical protocols and uniform application across settings. COP.4.d owns nursing CPGs. Intra-COP division stated in both Scopes (COP.1 already drafted in this pass). Flag so COP.1 and COP.4 are not approved as if they were the same protocol set.
   HIC.2 owns HH, PPE, TBP, injection safety. This draft points and does not restate. Nothing added to the reconciliation list against the approved HIC set.
   HIC.6 owns reprocessing of reusable nursing equipment. COP.4.c owns availability at the point of care. T2 flag; stated in Scope.
3. FORWARD REFERENCES: medical-record structure -- IMS, not yet drafted; nurse credentialing method -- HRM, not yet drafted; planned maintenance method -- FMS, not yet drafted. Each is a deliberate boundary.
4. T2 QUICK CHECK: COP.4.b assignment vs HRM credentialing -- this uses verification, does not restate it. COP.4.b vs AAC.1.b suitably qualified personnel for a defined service -- AAC.1.b is roster/resourcing of a specialty; this is per-period assignment of a nurse to a patient. Not the same. COP.4.c vs FMS equipment programme -- availability at the point of care is here; the maintenance method is theirs.

STATUTORY AND EXTERNAL FACTS
5. Indian Nursing Council Act, 1947 -- cited insofar as who may be assigned as a nurse and as the professional-practice context of nursing CPGs. No section number. No staffing ratio.
6. Clinical Establishments Act, 2010 -- NOT cited.
7. Bio-Medical Waste Management Rules, 2016 and Food Safety and Standards Act, 2006 -- NOT named.
8. Barton 2013, Brooks Carthon 2019, Nguyen 2015, Whitehead and Myers 2016 (chapter references 5, 6, 37, 63) -- USED only to inform that assignment may take account of acuity and skill. NOT USED as required ratios. NO nurse-to-patient number appears anywhere in this draft.
9. NO NUMBERS ARE STATED as requirements -- no staffing ratios, no entry-within-N-minutes rule as a mandate (timing is [Hospital to define]), no devices-per-bed. Consistent with the no-numbers default.
10. EXTERNAL CLINICAL/TECHNICAL FACT-CHECKING (Tier 1): no clinical numeric claim is stated. The division between medical protocols and nursing CPGs is an organisational fact, not a cited international numeric standard. INC standards of nursing practice are named as an acceptable source, not imported as a protocol.

EDITORIAL POSITIONS TAKEN
11. Step 1's rule that a Kardex, whiteboard or messaging-app update is not the patient record, and that copy-forward of yesterday's note is forbidden, are editorial positions; the standard requires documentation in the patient record, not these exclusions.
12. Step 1's rule that handover is not a substitute for the nursing entry is an editorial position required to keep the AAC.7 division operational.
13. Step 4's rule that a medical protocol labelled as a nursing guideline does not satisfy COP.4.d, and that issue and withdrawal must reach every setting on the same date, are editorial positions; the standard requires nursing CPGs reflecting current standards, not these specifics.
14. Step 2's refusal to mandate acuity-based staffing or a ratio is an editorial position required by the no-numbers default and by the chapter references being about association, not a SHCO mandate.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
15. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the Indian Nursing Council Act, 1947 and State Nursing Council registration -- the statute this document's References actually cite. It does NOT name the Bio-Medical Waste Management Rules, 2016, the Food Safety and Standards Act, 2006, or the Clinical Establishments Act 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Handover method -- AAC.7.
- Care-plan method -- AAC.3.
- Hospital-wide medical protocols -- COP.1.c/d.
- HH, PPE, TBP, injection safety -- HIC.2.
- Reprocessing method -- HIC.6.
- Record structure -- IMS.
- A nurse-to-patient ratio or acuity tool as a mandate.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 10 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 8 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 10; a search for "Hospital to define" without brackets finds all 10, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: the nursing-entry content, form or fields, and expected timing; who assigns nursing care, for which period, and on what basis; the nursing equipment that must be present by area and how absence or failure is reported; the nursing clinical practice guidelines in current use, the problems they cover, and where they are held; how staff are shown the current nursing CPGs and the review interval for each; the audit interval for these records; the review interval for this policy; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
