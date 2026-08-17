-- AAC.7 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 1, printed pages 53-54
-- (PDF page index 59-60). Levels: a Commitment, b Commitment, c Core, d Commitment.
-- ZERO OEs CARRY THE ASTERISK. Whole standard is Tier 2. TIER1_OES = [].
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
  'AAC.7',
  'AAC',
  array['AAC.7.a', 'AAC.7.b', 'AAC.7.c', 'AAC.7.d'],
  $q$Continuity of Care, Handover and Internal Transfer$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} keeps patient care continuous and multidisciplinary: a named qualified individual responsible for the patient at every phase of care; sharing of information about care and response to treatment among medical, nursing and other care-providers, including referrals to other departments; standardised handover at every staffing shift, between shifts and during transfers between units; and safe transfer of a patient from one unit of this hospital to another.

A patient who changes shift, unit or clinician without a named person, without the information the next team needs, or without a safe move between units, is a patient whose care has stopped being continuous. This document is the process that prevents that.$q$,
  $q$This policy applies to every location in which a patient of {{HOSPITAL_NAME}} is under care and from which that patient may move to another location inside this hospital: the emergency area, every in-patient ward, day-care, the operation theatre and recovery, intensive or high-dependency areas where they exist, and any diagnostic or procedural area that receives a patient from a unit. It binds the individual identified as responsible for the patient's care, the medical, nursing and other care-providers who share information and make internal referrals, the staff who give and receive handover, and the staff who accompany an internal transfer.

It covers identification of the responsible individual at every phase; sharing of information among providers, including referral to another department of this hospital; standardised hand-over communication during each staffing shift, between shifts and during transfers between units or departments; and safe transfer of a patient from one unit of {{HOSPITAL_NAME}} to another.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Transfer-in from another organisation, transfer-out to another organisation, and referral of a patient this hospital cannot accept, are governed by the registration, admission and transfer policy of {{HOSPITAL_NAME}} (AAC.2.f). This policy owns unit-to-unit movement inside this hospital (AAC.7.d). The two are not the same act. AAC.2 does not perform internal transfer; this document does not perform between-organisation transfer.
- Suitably qualified personnel standing behind a defined healthcare service — the roster and resourcing of a specialty — are governed by the definition-and-display policy of {{HOSPITAL_NAME}} (AAC.1.b). This policy owns the per-patient named individual identified as responsible for this patient's care at this phase. A service having qualified staff is not the same as a named person being responsible for this patient now.
- The transmission-based precaution category, when one is in force, must appear in the nursing handover under the infection-control policies of {{HOSPITAL_NAME}} (HIC.2). This policy owns the handover method. HIC.2 owns the infection-control content that must appear in it. Personal protective equipment, isolation rooms and the precaution assignment register are not restated here.
- The medical record itself — its contents, retention and confidentiality — is governed by the information-management policies of {{HOSPITAL_NAME}}. This policy owns what is communicated at handover, at referral between departments, and at internal transfer; it does not define the record.
- Initial assessment and the care plan are governed by the assessment policy of {{HOSPITAL_NAME}}. Discharge from the organisation is governed by the discharge policy of {{HOSPITAL_NAME}}.$q$,
  $q${{HOSPITAL_NAME}} identifies a qualified individual as responsible for the patient's care during every phase of that care. A phase without a named person is a break in continuity.

{{HOSPITAL_NAME}} shares information about the patient's care and response to treatment among medical, nursing and other care-providers, including when the patient is referred to another department of this hospital.

{{HOSPITAL_NAME}} implements standardised hand-over communication during each staffing shift, between shifts, and during transfers between units or departments. The method is structured and written; it is not left to memory or to an unstructured conversation.

{{HOSPITAL_NAME}} transfers a patient from one unit of this hospital to another only when the receiving unit has accepted the patient, handover has been given, a checklist is complete, a named person accompanies the patient, and monitoring required en route is performed.

{{HOSPITAL_NAME}} treats an unidentified responsible person, an undocumented handover, or an unaccompanied internal move as a defect, not as a shortcut taken under pressure.$q$,
  array[
    $s$1. Named responsible individual at every phase

During all phases of care, a qualified individual is identified as responsible for the patient's care. Qualification means registration with the professional council that governs the role: the National Medical Commission Act, 2019 and State Medical Council registration for doctors; the Indian Nursing Council Act, 1947 and State Nursing Council registration for nurses; and the corresponding councils for the other professions {{HOSPITAL_NAME}} employs. Human-resource procedures verify that registration; this step uses it.

The name and role of the responsible individual are recorded in the case record at each phase — at least: emergency care, admission to an in-patient or day-care area, any intra-operative or procedural phase, each in-patient unit, and until discharge or until another named individual takes over. When responsibility changes, the outgoing individual names the incoming individual and the change is recorded. A patient is not left without a named responsible individual because a shift ended or a unit changed.

How the responsible individual is identified at each phase — board, record field, handover sheet, or other method — is [Hospital to define — how the responsible individual is identified at each phase].

This is the per-patient named individual. It is not the AAC.1.b requirement that a defined service be backed by suitably qualified personnel.$s$,
    $s$2. Sharing information among providers, including internal referral

Information about the patient's care and response to treatment is shared among medical, nursing and other care-providers, including referrals to other departments of {{HOSPITAL_NAME}}.

When a referral to another department is made, the referring clinician records the reason, the information sent, and the receiving department's response. The information shared includes at least the current or working diagnosis, significant findings, treatment already given and the response to it, and pending investigations.

How that information is shared — written referral, electronic order, joint round, or other method — and how an internal referral is recorded are [Hospital to define — how clinical information is shared among providers and how an internal referral is recorded].

The medical record that holds this information is governed by the information-management policies of {{HOSPITAL_NAME}}. This step owns that the information is communicated, not the design of the record.$s$,
    $s$3. Standardised handover at shift, between shifts, and between units

{{HOSPITAL_NAME}} implements standardised hand-over communication during each staffing shift, between shifts, and during transfers between units or departments.

The structured method used at every such handover is [Hospital to define — the structured handover method used at every shift and at every unit-to-unit transfer]. This policy requires a structured method. It does not mandate a named proprietary or published tool. A method in common use, including SBAR, is permitted if {{HOSPITAL_NAME}} chooses it; it is not the only acceptable method, and it is not required.

The principle is that of the World Health Organization Patient Safety Solutions, Communication During Patient Hand-Overs (2007), cited in the chapter's own References list (items 1 and 6): information needed to continue care must travel with the patient and must be communicated in a standardised way.

Handover is recorded. The receiving staff confirm they have received it. Handover between units is performed before or at the moment of the internal transfer at step 4, using the same structured method.

The transmission-based precaution category, when one is in force, appears in the nursing handover because HIC.2 requires that content. This step owns the method into which that content is placed. Personal protective equipment, isolation practice and the precaution assignment register remain in HIC.2 and are not restated here.$s$,
    $s$4. Safe internal transfer

Patient transfer within the organisation is done safely. This step is unit-to-unit movement inside {{HOSPITAL_NAME}} — emergency to ward, ward to intensive or high-dependency area, ward to operation theatre, theatre to recovery, recovery to ward, ward to a diagnostic or procedural area and back, and any other internal move. It is not AAC.2.f. AAC.2 owns transfer-in from another organisation, transfer-out to another organisation, and referral of a patient this hospital cannot accept. This step owns the move from one unit of this hospital to another.

Before the patient leaves the sending unit:

- the receiving unit has accepted the patient and has a bed or space ready;
- the named responsible individual at the sending unit and at the receiving unit are identified under step 1;
- handover has been given under step 3;
- an internal-transfer checklist is completed — [Hospital to define — the internal-transfer checklist], covering at least identity, current condition, ongoing treatment, monitoring required en route, equipment that travels with the patient, and infection-control status as already recorded under HIC.2;
- who accompanies the patient is named — [Hospital to define — who accompanies an internal transfer, by patient condition];
- monitoring required en route is stated and performed.

The transfer is recorded: time of leaving, time of arrival, who accompanied, and condition on arrival. A patient is not sent to find the receiving unit, and is not moved through public areas without the accompaniment and monitoring this step requires.$s$,
    $s$5. Records, review and the order of operations

Every named responsible individual, every shared-information or internal-referral entry, every handover, and every internal transfer is recorded against the unique identification number issued at registration and is retrievable. The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}}.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for continuity, handover and internal-transfer records] for a named responsible individual at each phase, for internal referrals that show what was shared, for handover that used the structured method, and for internal transfers that show checklist, accompaniment, monitoring en route, and times.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a handover or internal-transfer incident exposes a gap, or when the registration-and-transfer, infection-control or information-management policies that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} identifying a responsible individual at every phase of care, for a working standardised handover, and for internal transfer that is performed as a clinical act rather than as a porterage.

The clinicians identified as responsible for a patient at step 1 remain responsible until another named individual has taken over, including during an internal transfer until the receiving individual has accepted the patient.

Nursing staff give and receive handover under the structured method at step 3, record it, and do not complete a shift or a unit-to-unit move without it.

The staff who accompany an internal transfer complete the checklist, perform the monitoring required en route, and hand the patient to the named receiving individual.

Medical, nursing and other care-providers share information and record internal referrals under step 2.

The quality or accreditation coordinator audits the records at step 5 and reports findings to the head of the institution.

All staff are expected to report a patient who had no named responsible individual, a handover that was unstructured, or an internal move that was improvised rather than performed under this policy.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.7.
- National Medical Commission Act, 2019 and State Medical Council registration; Indian Nursing Council Act, 1947 and State Nursing Council registration; and the corresponding councils for the other professions {{HOSPITAL_NAME}} employs — who may be identified as the qualified individual responsible for a patient's care.
- Clinical Establishments (Registration and Regulation) Act, 2010 and the rules under it, where adopted by the State — the duty to maintain records of patients; or the corresponding State clinical establishments or nursing home registration law where the 2010 Act is not in force.
- World Health Organization, Patient Safety Solutions, Communication During Patient Hand-Overs (2007) — cited in the chapter's own References list (items 1 and 6); the principle that information needed to continue care travels with the patient and is communicated in a standardised way. The structured method itself is chosen under step 3.
- Internal documents of {{HOSPITAL_NAME}}: the method for identifying the responsible individual; the internal-referral method; the structured handover method; the internal-transfer checklist; the registration, admission and transfer policy; the infection-control policies; the assessment policy; the discharge policy; and the information-management policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every in-patient ward; the emergency area; day-care; the operation theatre and recovery; nursing administration; every head of department; and whoever arranges internal transfer.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The structured handover method and the internal-transfer checklist — the working documents this policy requires — are held at every unit that sends or receives a patient.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO and OE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

SBAR — Situation, Background, Assessment, Recommendation (a structured handover method in common use; permitted if chosen at step 3, not mandated)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the professional registration statutes that govern who may be identified as responsible for a patient's care — the National Medical Commission Act, 2019 and State Medical Council registration, the Indian Nursing Council Act, 1947 and State Nursing Council registration, and the corresponding councils for the other professions {{HOSPITAL_NAME}} employs — and the Clinical Establishments (Registration and Regulation) Act, 2010 and the rules under it, where adopted by the State, or the corresponding State law. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "AAC.7.a", "requirement": "During all phases of care, a qualified individual is identified as responsible for the patient's care", "steps": "Steps 1, 5", "evidence": "The written method for identifying the responsible individual at each phase; sample case records showing the name and role recorded at emergency, admission, each in-patient unit and at any change of responsibility; records showing the incoming individual was named before the outgoing individual stood down; the audit sample at step 5 covering a named responsible individual at each phase", "responsible": "The named clinician remains responsible until another named individual has taken over; human-resource procedures verify professional registration; quality or accreditation coordinator audits"}, {"oe_code": "AAC.7.b", "requirement": "Information about the patient's care and response to treatment is shared among medical, nursing and other care-providers, including referrals to other departments", "steps": "Steps 2, 5", "evidence": "The written method for sharing clinical information and recording an internal referral; sample internal referrals showing reason, information sent (working diagnosis, findings, treatment and response, pending investigations) and receiving-department response; the audit sample at step 5 of internal referrals that show what was shared", "responsible": "Medical, nursing and other care-providers share information and record internal referrals; information-management policies own the record that holds it; quality or accreditation coordinator audits"}, {"oe_code": "AAC.7.c", "requirement": "Standardised hand-over communication is implemented during each staffing shift, between shifts and during transfers between units or departments", "steps": "Steps 3, 4, 5", "evidence": "The written structured handover method used at every shift and at every unit-to-unit transfer, naming the method chosen and not treating any one published tool as mandatory; sample handover records with receiving-staff confirmation, spanning shift handover and unit-to-unit handover; records showing the HIC.2 precaution category appears in the nursing handover when one is in force, without this document restating PPE or isolation; the audit sample at step 5 of handover that used the structured method", "responsible": "Nursing staff give and receive handover; sending and receiving units complete unit-to-unit handover before internal transfer; HIC.2 owns infection-control content of the handover; quality or accreditation coordinator audits"}, {"oe_code": "AAC.7.d", "requirement": "Patient transfer within the organisation is done safely", "steps": "Steps 4, 5", "evidence": "The written internal-transfer checklist and the written rule on who accompanies, by patient condition; sample internal-transfer records showing receiving-unit acceptance, named responsible individuals, handover, completed checklist, accompaniment, monitoring en route, time of leaving, time of arrival and condition on arrival; records distinguishable from AAC.2 between-organisation transfer; the audit sample at step 5 of internal transfers", "responsible": "Sending and receiving clinicians remain responsible until the receiving individual has accepted the patient; accompanying staff complete the checklist and monitor en route; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. AAC.7 standard text and all four OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 1 Access, Assessment and Continuity of Care, printed pages 53-54 (PDF page index 59-60). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: AAC.7.a Commitment, AAC.7.b Commitment, AAC.7.c Core, AAC.7.d Commitment.
   ZERO OEs CARRY THE ASTERISK. AAC.7.a, AAC.7.b, AAC.7.c and AAC.7.d are all unasterisked. Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the AAC.7 pages read directly from the extracted page text, and the committed asterisk file's agreement with live shco_full_oes as of 2026-08-13. AAC.7 was not among the 14 mismatches of the 2026-08-10 audit.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. If a standard carries no asterisked OE at all, the whole standard is Tier 2. AAC.7 carries no asterisked OE. TIER1_OES = []. Every OE is Tier 2: procedure steps state the requirement and the method without extended rationale paragraphs. AAC.7.c is Core (assessed at every visit) but not asterisked; Core is not a substitute for the asterisk when allocating depth. Reviewer to note the shallower treatment of the whole standard is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. T2 quick check (2026-08-17), not a deep cross-reference audit. AAC.2.f vs AAC.7.d: between-organisation transfer-in/out and referral are AAC.2; unit-to-unit movement inside this hospital is AAC.7.d. Stated in Scope of this document and in AAC.2's Scope. Flagged here so the division is not lost if one is approved without the other.
3. AAC.1.b vs AAC.7.a: AAC.1.b is suitably qualified personnel for a defined service (roster/resourcing). AAC.7.a is the per-patient named responsible individual at each phase. Stated in Scope. Not the same requirement.
4. HIC.2 vs AAC.7.c: HIC.2 requires the precaution category in the nursing handover. AAC.7 owns the handover METHOD; HIC.2 owns the infection-control CONTENT that must appear in it. One-line T2 flag only. PPE, isolation and the precaution assignment register are not restated. Nothing added to the reconciliation list against the approved HIC set beyond this flag.
5. IMS owns the medical record; this document owns what is communicated at handover, internal referral and internal transfer. Forward reference; IMS not yet drafted.
6. FORWARD REFERENCES: assessment and care plan -- AAC.3; discharge -- AAC.8; between-organisation transfer -- AAC.2 (drafted). Each is a deliberate boundary.

STATUTORY AND EXTERNAL FACTS
7. National Medical Commission Act, 2019 / State Medical Council, Indian Nursing Council Act, 1947 / State Nursing Council, and corresponding councils -- cited only as the professional registration statutes that govern who may be identified as responsible for a patient's care. No section number. No assertion which professionals {{HOSPITAL_NAME}} employs.
8. Clinical Establishments Act, 2010 -- cited only as applying where the State has adopted it, with the State-law alternative, at the level of the Act's general scheme on patient records. No section number.
9. WHO Patient Safety Solutions, Communication During Patient Hand-Overs (2007) -- cited in the chapter's own References list (items 1 and 6) and used here as the principle that information travels with the patient in a standardised way. The structured method is [Hospital to define]. SBAR is named only as a common example that is permitted, not mandated.
10. NO NUMBERS ARE STATED as requirements -- no handover duration, no accompaniment grade-by-acuity table, no transfer-time ceilings. Every such value is [Hospital to define]. Consistent with the no-numbers default.
11. EXTERNAL CLINICAL/TECHNICAL FACT-CHECKING: skipped under the standing rule except where something looked wrong on its face. Nothing did. The draft does not prescribe a named handover tool.

EDITORIAL POSITIONS TAKEN
12. Step 4's refusal to send a patient to find the receiving unit, and the requirement that accompaniment and monitoring match the patient's condition, are editorial positions; the standard requires that internal transfer is done safely, not these specifics.
13. Step 3's refusal to mandate SBAR is an editorial position taken so that the hospital's chosen structured method is the requirement, not a branded tool the standard does not name.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
14. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the professional registration statutes (NMC Act 2019, INC Act 1947, corresponding councils) and the Clinical Establishments Act 2010 (or corresponding State law) -- the statutes this document's References actually cite. It does NOT name the Bio-Medical Waste Management Rules, 2016 or the Food Safety and Standards Act, 2006. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Between-organisation transfer-in, transfer-out and referral -- AAC.2.f.
- Suitably qualified personnel for a defined service -- AAC.1.b.
- Precaution category, PPE and isolation -- HIC.2 (content only; method of handover is here).
- The medical record as a document -- IMS.
- Initial assessment and care plan -- AAC.3.
- Discharge summary -- AAC.8.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 10 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 8 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 10; a search for "Hospital to define" without brackets finds all 10, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: how the responsible individual is identified at each phase; how clinical information is shared among providers and how an internal referral is recorded; the structured handover method used at every shift and at every unit-to-unit transfer; the internal-transfer checklist; who accompanies an internal transfer, by patient condition; the audit interval for these records; the review interval for this policy; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
