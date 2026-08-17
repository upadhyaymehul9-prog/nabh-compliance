-- COP.3 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 2, printed pages 62-63
-- (PDF page index 68-69). Levels: a Commitment, b Commitment, c Commitment, d Commitment.
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
  'COP.3',
  'COP',
  array['COP.3.a', 'COP.3.b', 'COP.3.c', 'COP.3.d'],
  $q$Cardio-Pulmonary Resuscitation$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} provides cardio-pulmonary resuscitation uniformly: services available to patients at all times; assigned roles complied with during an event and the events recorded; equipment and medications for resuscitation available in the areas where they are needed; and a multidisciplinary committee that analyses every resuscitation and takes corrective and preventive action.

A crash that is answered by whoever is nearest, with a trolley that is incomplete, and with no record that can be reviewed, is not a resuscitation service. This document is the process that prevents that.$q$,
  $q$This policy applies to every location in {{HOSPITAL_NAME}} in which a patient may require cardio-pulmonary resuscitation: the emergency area, every in-patient ward, day-care, the operation theatre and recovery, intensive or high-dependency areas where they exist, diagnostic and procedural areas, and any other clinical location the hospital names. It binds the staff who respond, the staff who record the event, the staff who check and restore the kit, and the multidisciplinary committee that reviews every resuscitation.

It covers availability of resuscitation services at all times; assigned roles and the record of events during cardio-pulmonary resuscitation; equipment and medications for use during resuscitation in various areas; and post-event analysis of all resuscitations with corrective and preventive measures.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Recognition of deterioration and the early-warning escalation that hands a crashing patient to this protocol are governed by the assessment policy of {{HOSPITAL_NAME}} (AAC.3.e). This policy owns the resuscitation once it is started. AAC.3 does not write the cardio-pulmonary resuscitation method.
- Life-stabilising treatment of an emergency patient in the emergency area, ambulance operation, triage and the emergency-area operational rules are governed by the emergency-care policy of {{HOSPITAL_NAME}} (COP.2). When that care is cardio-pulmonary resuscitation, this protocol is the method used. COP.2 does not write a second resuscitation algorithm.
- Generation of the unique identification number is governed by the registration, admission and transfer policy of {{HOSPITAL_NAME}} (AAC.2). A resuscitation record carries that number; this policy does not issue it.
- Reprocessing of reusable resuscitation equipment — resuscitation bags, laryngoscope blades and handles where they are reusable, and related airway devices — is governed by the sterilisation and disinfection policy of {{HOSPITAL_NAME}} (HIC.6). This policy owns that a ready kit is available in the named areas. HIC.6 owns how a used item is reprocessed before it returns to the kit. This document does not restate high-level disinfection, sterilisation or device classification.
- Hand hygiene, personal protective equipment and standard precautions during a resuscitation are governed by the infection-control policies of {{HOSPITAL_NAME}} (HIC.2). They are followed; they are not rewritten here.
- Medication storage, look-alike / sound-alike controls and the medication process are governed by the medication policies of {{HOSPITAL_NAME}} (MOM, not yet drafted). This policy owns that resuscitation medications are present in the kit; it does not write the hospital-wide medication process.
- The medical record itself is governed by the information-management policies of {{HOSPITAL_NAME}}. This policy owns the resuscitation-event record that is written into it.$q$,
  $q${{HOSPITAL_NAME}} makes resuscitation services available to patients at all times. A service that exists only during ordinary hours is not this service.

{{HOSPITAL_NAME}} assigns roles for cardio-pulmonary resuscitation, requires that those roles are complied with during an event, and records the events.

{{HOSPITAL_NAME}} keeps the equipment and medications for cardio-pulmonary resuscitation available in the various areas it has named.

{{HOSPITAL_NAME}} has a multidisciplinary committee analyse every cardio-pulmonary resuscitation, and takes corrective and preventive measures based on that analysis.

{{HOSPITAL_NAME}} adopts an American Heart Association cardio-pulmonary resuscitation framework as the clinical framework it uses. The edition and the algorithm in force are this hospital's choice. This document does not print a numbered algorithm and does not state joule doses or drug doses.$q$,
  array[
    $s$1. Resuscitation services available at all times

Resuscitation services are available to patients at all times. All times means every hour of every day the hospital has a patient, including nights, weekends and holidays.

Who responds, how they are summoned, and the arrangement when the ordinary team is already occupied, are [Hospital to define — who responds to a resuscitation, how they are summoned, and the arrangement when the ordinary team is already occupied]. Professional registration of the responders is verified under the human resource policies of {{HOSPITAL_NAME}}; this step uses that verification.

The assessment policy of {{HOSPITAL_NAME}} (AAC.3.e) owns recognising deterioration and starting the call. This step owns that, once the call is made, a resuscitation service exists to receive it. Life-stabilising treatment in the emergency area uses this service; the emergency-care policy (COP.2) does not write a second method.$s$,
    $s$2. Assigned roles during resuscitation and the record of events

During cardio-pulmonary resuscitation, assigned roles and responsibilities are complied with, and the events during cardio-pulmonary resuscitation are recorded.

The assigned roles, and who takes each role at an event, are [Hospital to define — the assigned resuscitation roles and how they are allocated at an event]. This policy requires assigned roles that are complied with. It does not mandate a named proprietary role-set. A role-set in common use in an American Heart Association team is permitted if {{HOSPITAL_NAME}} chooses it; it is not the only acceptable set, and it is not required.

Events are recorded against the unique identification number: at least the date and time the event was recognised, the time the team was summoned, the time the team arrived, the roles filled, the interventions performed, the medications given, and the outcome. The record form, and where it is filed, are [Hospital to define — the resuscitation-event record and where it is filed]. Doses, energy levels and the algorithm in force are those of the American Heart Association edition adopted at step 3 — recorded as given, not printed here as mandates.

A resuscitation without a record is an event this hospital cannot review at step 4.$s$,
    $s$3. Equipment and medications in various areas

The equipment and medications for use during cardio-pulmonary resuscitation are available in various areas of the organisation.

The areas in which a resuscitation kit is held, the contents of the kit, and how completeness is checked, are [Hospital to define — the areas that hold a resuscitation kit, the contents of the kit, and how completeness is checked]. This document does not print a kit list as a mandated inventory and does not state joule doses or drug doses.

After an event, used reusable items — resuscitation bags, laryngoscope blades and related airway devices — are sent for reprocessing under the sterilisation and disinfection policy of {{HOSPITAL_NAME}} (HIC.6). This step owns that the kit is then restored to ready. HIC.6 owns the reprocessing method. A used item is not put back on the trolley as if it were ready.

The framework this hospital adopts for resuscitation practice is an American Heart Association framework; the edition and the algorithm in force are [Hospital to define — the American Heart Association edition and the resuscitation algorithm in force]. The algorithm is not printed in this policy.$s$,
    $s$4. Multidisciplinary post-event analysis and corrective action

A multidisciplinary committee does a post-event analysis of all cardio-pulmonary resuscitations, and corrective and preventive measures are taken based on this.

All means every event in which cardio-pulmonary resuscitation was started, including events that did not restore circulation. An event that is not reviewed is an event this hospital has decided not to learn from.

The committee's composition, the interval at which it meets, and where its minutes and actions are held, are [Hospital to define — the resuscitation-review committee composition, meeting interval, and where minutes and actions are held]. Analysis uses the event record at step 2 and the kit-check record at step 3. Corrective and preventive actions are assigned, dated and closed. An action that is recorded and not done is not an action.$s$,
    $s$5. Records, review and the order of operations

Every resuscitation call, every event record, every kit check, every restoration of a kit after use, and every committee analysis with its actions is recorded against the unique identification number where a patient is involved, and is retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for resuscitation records] for a service that can be shown to exist outside ordinary hours, for event records that name roles and the interventions performed, for kit checks in the named areas, for used items sent to reprocessing rather than returned to the trolley, and for every event having a committee analysis with actions.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a failed call, an incomplete kit or an unreviewed event exposes a gap, or when the assessment, emergency-care, sterilisation or infection-control policies that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} having a resuscitation service at all times, for kits that are actually present in the named areas, and for every event being analysed.

The named responders at step 1 attend when summoned, fill the assigned roles at step 2, and complete the event record.

Nursing and clinical staff in each named area check the kit at step 3, send used reusable items for reprocessing under HIC.6, and restore the kit to ready.

The multidisciplinary committee at step 4 analyses every event and assigns corrective and preventive actions. The person assigned an action closes it.

The quality or accreditation coordinator audits the records at step 5 and reports findings to the head of the institution.

All staff are expected to start the call when resuscitation is required, and to report a call that was not answered, a kit that was incomplete, or an event that was not recorded.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.3.
- National Medical Commission Act, 2019 and State Medical Council registration; Indian Nursing Council Act, 1947 and State Nursing Council registration — professional-practice obligations of registered practitioners to maintain resuscitation competence. No section number. This document does not convert those Acts into a named course requirement.
- American Heart Association, 2015 Guidelines Update for CPR and ECC, and the 2017 Focused Update on Adult Basic Life Support and Cardiopulmonary Resuscitation Quality (chapter references 1, 14, 26, 27, 28) — the framework {{HOSPITAL_NAME}} may adopt. The edition and algorithm in force are chosen at step 3. This document does not import a numbered algorithm, joule table or drug-dose table.
- Internal documents of {{HOSPITAL_NAME}}: the resuscitation call and response arrangement; the assigned-role set; the event-record form; the kit-location and completeness-check method; the resuscitation-review committee terms; the assessment policy; the emergency-care policy; the sterilisation and disinfection policy; the infection-control policies; the medication policies; and the information-management policies.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every in-patient ward; the emergency area; day-care; the operation theatre and recovery; intensive or high-dependency areas where they exist; nursing administration; every head of department; and the members of the resuscitation-review committee.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The call method, the role set, the event-record form and the kit-check list — the working documents this policy requires — are held in every area that holds a kit.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, PPE, WHO and SOP.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

CPR — Cardio-Pulmonary Resuscitation
AHA — American Heart Association
CAPA — Corrective and Preventive Action

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the professional-practice obligations under the National Medical Commission Act, 2019 and the Indian Nursing Council Act, 1947 insofar as registered practitioners must maintain resuscitation competence. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "COP.3.a", "requirement": "Resuscitation services are available to patients at all times", "steps": "Steps 1, 5", "evidence": "The written response arrangement naming who responds, how they are summoned, and the arrangement when the ordinary team is already occupied, including nights, weekends and holidays; roster or equivalent showing a service outside ordinary hours; the audit sample at step 5 of a service that can be shown to exist outside ordinary hours", "responsible": "Named responders attend when summoned; head of the institution is accountable that the service exists at all times; quality or accreditation coordinator audits"}, {"oe_code": "COP.3.b", "requirement": "During cardiopulmonary resuscitation, assigned roles and responsibilities are complied with, and the events during cardiopulmonary resuscitation are recorded", "steps": "Steps 2, 5", "evidence": "The written assigned-role set and how roles are allocated at an event; sample event records showing date and time of recognition, summoning and arrival, roles filled, interventions, medications and outcome, against the unique identification number; the location of the record; the audit sample at step 5 of event records that name roles and interventions", "responsible": "Responders fill assigned roles and complete the event record; quality or accreditation coordinator audits"}, {"oe_code": "COP.3.c", "requirement": "The equipment and medications for use during cardiopulmonary resuscitation are available in various areas of the organization", "steps": "Steps 3, 5", "evidence": "The written list of areas that hold a kit, the contents, and the completeness-check method; kit-check records for those areas; records of used reusable items sent for reprocessing under HIC.6 and the kit restored to ready rather than a used item returned to the trolley; the American Heart Association edition and algorithm in force, not printed as a numbered protocol in this policy; the audit sample at step 5 of kit checks and restoration after use", "responsible": "Staff in each named area check and restore the kit; HIC.6 owns reprocessing of reusable items; quality or accreditation coordinator audits"}, {"oe_code": "COP.3.d", "requirement": "A multidisciplinary committee does a post-event analysis of all cardiopulmonary resuscitations, and corrective and preventive measures are taken based on this", "steps": "Steps 4, 5", "evidence": "The written committee composition, meeting interval and location of minutes; sample analyses covering events that restored circulation and events that did not; assigned corrective and preventive actions with dates and closure; the audit sample at step 5 of every event having a committee analysis with actions", "responsible": "The multidisciplinary committee analyses every event and assigns actions; the person assigned an action closes it; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. COP.3 standard text and all four OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 2 Care of Patients, printed pages 62-63 (PDF page index 68-69). The PDF was downloaded on 2026-08-17 from the NABH website's Explore NABH Standards page. Levels: COP.3.a Commitment, COP.3.b Commitment, COP.3.c Commitment, COP.3.d Commitment.
   ZERO OEs CARRY THE ASTERISK. COP.3.a, COP.3.b, COP.3.c and COP.3.d are all unasterisked. Verified three ways on 2026-08-17: scripts/asterisk_extract.py re-run against the freshly downloaded PDF (self-validation passed; output matched committed scripts/shco_oe_asterisks.json on all 408 entries), the COP.3 pages read directly from the extracted page text, and the committed asterisk file. COP.3 was not among the 14 mismatches of the 2026-08-10 audit.
   SECOND LOOK 2026-08-17 (glyph-level, printed p.62-63 / PDF index 68-69): every ASTERISK character on those two pages was mapped to its line. Printed p.62 has two asterisks — COP.2.f (ED quality-assurance programme) and COP.2.k (disaster/epidemic plan), both before the COP.3 header. Printed p.63 has four asterisks — COP.4.a, COP.4.d, COP.5.b, COP.5.c — after COP.3.d. COP.3.a-d lines contain no asterisk glyph. Zero is correct; the whole standard is Tier 2 under the standing rule, not an extraction miss.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. If a standard carries no asterisked OE at all, the whole standard is Tier 2. COP.3 carries no asterisked OE. TIER1_OES = []. Every OE is Tier 2: procedure steps state the requirement and the method without extended rationale paragraphs. Reviewer to note the shallower treatment of the WHOLE STANDARD is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. T2 quick check (2026-08-17), not a deep cross-reference audit. AAC.3.e vs COP.3: AAC.3 owns recognising deterioration and handing the crashing patient to this protocol; COP.3 owns the resuscitation. Stated in Scope of this document and in AAC.3's Scope. Flag for master-policy-todos.md so the division is not lost if one is approved without the other.
3. AAC.2 / COP.2 vs COP.3: life-stabilising treatment in the emergency area uses this protocol; COP.2 (not yet drafted) owns the emergency area and must not write a second resuscitation algorithm. Flag for COP.2 drafting.
4. HIC.6 vs COP.3.c: HIC.6 owns reprocessing of resuscitation bags, laryngoscope blades and related airway devices. COP.3 owns having a ready kit in named areas and restoring it after use. Stated in Scope. Do not rewrite HLD, sterilisation or Spaulding classification. Flag for master-policy-todos.md.
5. HIC.2 vs COP.3: PPE and hand hygiene during resuscitation remain HIC.2. One-line T2 flag only.
6. FORWARD REFERENCES: emergency-area operational rules -- COP.2 (drafted this pass, UNAPPROVED; this document does not rewrite triage or ambulance); medication process -- MOM, not yet drafted; medical-record structure -- IMS, not yet drafted; human-resource credentialing of responders -- HRM, not yet drafted.

STATUTORY AND EXTERNAL FACTS
7. National Medical Commission Act, 2019 and Indian Nursing Council Act, 1947 -- cited only as professional-practice obligations of registered practitioners to maintain resuscitation competence. No section number. No named course (BLS/ACLS) is mandated.
8. Clinical Establishments Act, 2010 -- NOT cited.
9. Bio-Medical Waste Management Rules, 2016 and Food Safety and Standards Act, 2006 -- NOT named.
10. American Heart Association 2015 Guidelines / 2017 Focused Update (chapter references 1, 14, 26, 27, 28) -- named as the framework the hospital adopts. Edition and algorithm are [Hospital to define]. NO numbered ACLS algorithm, NO joule doses, NO drug doses are stated as requirements.
11. NO NUMBERS ARE STATED as requirements -- no response-time minutes, no cart-check frequencies, no staffing ratios, no energy or dose tables. Every such value is [Hospital to define]. Consistent with the no-numbers default.
12. EXTERNAL CLINICAL/TECHNICAL FACT-CHECKING: skipped under the standing rule except where something looked wrong on its face. Nothing did. The draft deliberately refuses to invent an algorithm.

EDITORIAL POSITIONS TAKEN
13. Step 3's rule that a used reusable item is not returned to the trolley as if ready is an editorial position required to keep the HIC.6 division operational; the standard requires availability of equipment, not this restoration sequence.
14. Step 4's rule that "all" includes events that did not restore circulation is an editorial position; the standard says all cardiopulmonary resuscitations.
15. Refusal to mandate a named AHA role-set or a named BLS/ACLS course is an editorial position so that the hospital's assigned roles and competence method are the requirement.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
16. Paragraphs 1, 3 and 4 are the shared HIC.3-6 block, hash-checked at build time. Paragraph 2 names the National Medical Commission Act, 2019 and the Indian Nursing Council Act, 1947 insofar as registered practitioners must maintain resuscitation competence -- the statutes this document's References actually cite. It does NOT name the Bio-Medical Waste Management Rules, 2016, the Food Safety and Standards Act, 2006, or the Clinical Establishments Act 2010. The HIC wholesale inherit is refused by the build.

DELIBERATELY NOT INCLUDED
- Early-warning recognition and escalation -- AAC.3.e.
- Emergency-area, triage, ambulance -- COP.2.
- Reprocessing method for bags and blades -- HIC.6.
- A numbered ACLS/BLS algorithm, joule table or drug-dose table.
- A mandated named course.
- The five optional sections are left unset, matching HIC.1-6 and AAC.1.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 11 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 9 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 2 of 11; a search for "Hospital to define" without brackets finds all 11, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: who responds, how they are summoned, and the arrangement when the ordinary team is already occupied; the assigned resuscitation roles and how they are allocated; the resuscitation-event record and where it is filed; the areas that hold a kit, the contents, and how completeness is checked; the American Heart Association edition and algorithm in force; the resuscitation-review committee composition, meeting interval, and where minutes and actions are held; the audit interval for these records; the review interval for this policy; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
