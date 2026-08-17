-- PSQ.4 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 6 PSQ, printed pages 103-104.
-- NO OE CARRIES THE ASTERISK. Whole standard is Tier 2. NOT 2nd Edition CQI.
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
  'PSQ.4',
  'PSQ',
  array['PSQ.4.a', 'PSQ.4.b', 'PSQ.4.c', 'PSQ.4.d'],
  $q$Management Support for Patient Safety and Quality$q$,
  $q$This document sets out how management at {{HOSPITAL_NAME}} creates a culture of safety; how leaders at all levels are aware of the intent of the patient-safety quality-improvement programme and the approach to its implementation; how management makes available adequate resources and earmarks adequate funds from the annual budget; and how management uses workforce feedback to improve the programme.

The chapter intent is that department leaders play an active role and that management supports the patient-safety and quality programme. A poster about safety culture, or a budget line that is never spent, is not that intent.$q$,
  $q$This policy applies to those who manage {{HOSPITAL_NAME}} and to leaders at all levels who must know the intent and approach of the programme.

It covers: creating a culture of safety; leader awareness of intent and implementation approach; resources and earmarked funds from the annual budget; and use of workforce feedback to improve the programme.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The patient-safety and QI programmes themselves are PSQ.1. This document owns management support for them.
- Incident reporting by staff is PSQ.5. A culture of safety includes that reporting is possible; the incident system is PSQ.5.
- PRE.6 (drafted UNAPPROVED on a sibling branch) owns patient/family feedback and complaints. This OE (PSQ.4.d) is feedback obtained from the workforce.
- ROM (not yet drafted) owns governance, the annual budget as a governance act (ROM.3.a), and management ensuring proactive risk management (ROM.4). This document owns that funds are earmarked for this programme and that management creates a safety culture as a PSQ requirement. ROM.3.a approves the budget; this step earmarks a portion for patient safety and QI. ROM.4.b (integration of QI, risk and strategy) is not this culture OE.
- HRM (not yet drafted) owns staff rights and the training file. Leader awareness here is of this programme's intent and approach, not the HRM induction curriculum as a whole.
- AHRQ Culture of Safety (chapter reference 3), Weaver et al. (chapter reference 47) and Wagner et al. (chapter reference 45) are frameworks for culture; they are not a mandated survey instrument.
- This chapter is PSQ, not CQI.$q$,
  $q${{HOSPITAL_NAME}} requires management to create a culture of safety.

{{HOSPITAL_NAME}} requires leaders at all levels to be aware of the intent of the patient-safety quality-improvement programme and the approach to its implementation.

{{HOSPITAL_NAME}} makes available adequate resources for that programme and earmarks adequate funds from its annual budget in this regard.

{{HOSPITAL_NAME}} uses feedback obtained from the workforce to improve the programme.

{{HOSPITAL_NAME}} does not treat a safety-culture poster, or an unspent budget line, as that support.$q$,
  array[
    $s$1. Culture of safety

The management creates a culture of safety.

How management creates and shows that culture — what leaders do, how staff can speak up, how that is recorded — is [Hospital to define — how management creates a culture of safety and how that is evidenced]. AHRQ Culture of Safety (chapter reference 3), Frankel and Leonard (chapter reference 10) and Weaver et al. (chapter reference 47) are frameworks. This document does not print a named culture survey as a NABH mandate. Creating a culture is not the same act as implementing the incident system (PSQ.5) or supporting the ethical framework (ROM.1.e when drafted).$s$,
    $s$2. Leaders aware of intent and approach

The leaders at all levels in the organisation are aware of the intent of the patient safety quality improvement program and the approach to its implementation.

How that awareness is produced and checked for leaders at all levels this hospital actually has, is [Hospital to define — how leaders at all levels are made aware of the intent of the patient-safety quality-improvement programme and the approach to its implementation]. Intent is the chapter intent and PSQ.1 programmes. Approach is how this hospital implements them. A single seminar for consultants is not 'all levels'.$s$,
    $s$3. Resources and earmarked funds

The management makes available adequate resources required for patient safety and quality improvement programme, earmarks adequate funds from its annual budget in this regard.

What resources are made available, and how funds are earmarked in the annual budget, are [Hospital to define — the resources made available for the patient-safety and QI programme, and how adequate funds are earmarked in the annual budget]. ROM.3.a (when drafted) owns governance approval of the annual budget. This step owns the earmark for this programme. This document does not print a rupee figure as a NABH mandate. Swensen et al. on the business case for QI (chapter reference 39) is a framework, not a costing table.$s$,
    $s$4. Workforce feedback used to improve the programme

The management uses the feedback obtained from the workforce to improve patient safety and quality improvement programme.

How workforce feedback is obtained, how management uses it, and how a resulting change to the programme is recorded, are [Hospital to define — how workforce feedback is obtained and how management uses it to improve the patient-safety and QI programme]. Patient/family feedback remains PRE.6. A suggestion box that is never opened is not this OE.$s$,
    $s$5. Records, review and the order of operations

Culture-of-safety method, leader-awareness records, resource and budget-earmark records, and workforce-feedback use, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for management-support records] for: culture evidenced as more than a poster; leaders at more than one level aware; resources and an earmark in the annual budget; workforce feedback used; and no patient-complaint file counted as workforce feedback.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when an earmark was absent from the budget, or only one level of leader could explain the programme, or when PSQ.1 or ROM that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for management support of the patient-safety and QI programme at {{HOSPITAL_NAME}}.

Those responsible for governance (ROM.1, when drafted) set the conditions; this document still requires the earmark and the culture as PSQ duties.

Leaders at all levels must be able to state the intent and the approach.

The named lead who prepares the earmark and the workforce-feedback summary is [Hospital to define — the named lead for management support of the patient-safety and QI programme].

The quality or accreditation coordinator audits the records at step 5 and reports findings to the head of the institution.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 6 PSQ, standard PSQ.4.
- Culture of Safety. AHRQ Patient Safety Network (2019) — chapter reference 3; framework, not a mandated survey.
- Frankel, A., & Leonard, M. (2013). Update on Safety Culture. AHRQ — chapter reference 10; framework.
- Weaver, S. J., et al. (2013). Promoting a Culture of Safety as a Patient Safety Strategy — chapter reference 47; framework.
- Swensen, S. J., et al. (2013). The business case for health-care quality improvement — chapter reference 39; framework, not a costing table.
- Internal documents of {{HOSPITAL_NAME}}: the culture-of-safety method; leader-awareness method; budget earmark; workforce-feedback method; the PSQ.1 programmes; ROM policies when drafted.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: those responsible for governance; heads of department; nursing administration; and the named lead.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder].

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

PSQ — Patient Safety and Quality Improvement (SHCO 3rd Edition Chapter 6; not CQI)
QI — quality improvement
ROM — Responsibilities of Management (NABH chapter; not yet drafted)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

The requirements in this document are accreditation requirements of the NABH SHCO 3rd Edition rather than duties under a named Act of Parliament. In particular those arising under no named Act of Parliament; the duties in this document are accreditation requirements of the NABH SHCO 3rd Edition are written here as accreditation method, not as a copied statute. This policy does not import the Consumer Protection Act, 2019, the Clinical Establishments Act, 2010, or the Mental Healthcare Act, 2017 as a checklist. Statutory duties that arise under other documents of {{HOSPITAL_NAME}} remain those documents. {{HOSPITAL_NAME}} is responsible for verifying any statutory duty that applies to it; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "PSQ.4.a", "requirement": "The management creates a culture of safety.", "steps": "Steps 1, 5", "evidence": "The written method for creating a culture of safety and sample evidence that is more than a poster; the recorded splits that PSQ.5 owns the incident system and ROM.1.e will own ethical framework; AHRQ/Weaver used as frameworks not a mandated survey; the audit sample at step 5", "responsible": "Head of the institution and management create the culture; quality or accreditation coordinator audits"}, {"oe_code": "PSQ.4.b", "requirement": "The leaders at all levels in the organisation are aware of the intent of the patient safety quality improvement program and the approach to its implementation.", "steps": "Steps 2, 5", "evidence": "The written awareness method covering leaders at all levels this hospital has; sample records showing more than one level can state intent and approach; the audit sample at step 5", "responsible": "Leaders at all levels must be aware; named lead produces awareness; quality or accreditation coordinator audits"}, {"oe_code": "PSQ.4.c", "requirement": "The management makes available adequate resources required for patient safety and quality improvement programme, earmarks adequate funds from its annual budget in this regard.", "steps": "Steps 3, 5", "evidence": "The written resources and the budget earmark for this programme; the recorded split that ROM.3.a will own governance approval of the annual budget; no rupee figure as a NABH mandate; the audit sample at step 5", "responsible": "Management earmarks and provides resources; ROM.3 will own budget approval; quality or accreditation coordinator audits"}, {"oe_code": "PSQ.4.d", "requirement": "The management uses the feedback obtained from the workforce to improve patient safety and quality improvement programme.", "steps": "Steps 4, 5", "evidence": "The written workforce-feedback method and sample uses that changed the programme; the recorded split that PRE.6 owns patient/family feedback; the audit sample at step 5", "responsible": "Management uses workforce feedback; PRE.6 remains patient complaints; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. PSQ.4 standard text and OEs a-b printed page 103 (index 109), c-d printed page 104 (index 110), official SHCO 3rd Edition PDF Chapter 6. Header: "The patient safety and quality improvement programme are supported by the management." Official PSQ.4.b uses "program" (American spelling) in the OE. PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Achievement, b Commitment, c Commitment, d Excellence.
   NO OE CARRIES THE ASTERISK. Whole standard is Tier 2. This is PSQ, not CQI.

TIERING UNDER THE STANDING RULE
1. Whole standard is Tier 2. Shallower treatment of the WHOLE STANDARD is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. T2 quick check (2026-08-17). PSQ.1 programmes vs this support -- flagged. PSQ.5 incident system vs culture -- flagged. PRE.6 patient feedback vs PSQ.4.d workforce feedback -- flagged. ROM.3.a budget approval vs this earmark -- flagged. ROM.4.b integration vs this culture -- flagged.

STATUTORY AND EXTERNAL FACTS
3. No named Act. P2 accreditation-only. AHRQ culture refs 3, 10, 47 -- frameworks, not mandated surveys. No rupee figure as a NABH mandate.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
4. make_disclaimer_accreditation_only().

DELIBERATELY NOT INCLUDED
- Programme method -- PSQ.1. Incident system -- PSQ.5. Governance budget approval -- ROM.3.a.
- A mandated safety-culture survey. A rupee earmark as a NABH number.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 10 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 8 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 10; a search for "Hospital to define" without brackets finds all 10, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: culture-of-safety method; leader-awareness method; resources and budget earmark; workforce-feedback method; named lead; audit interval; review interval; intranet location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
