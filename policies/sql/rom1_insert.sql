-- ROM.1 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 7 ROM, printed page 110
-- (PDF page index 116). THREE OEs CARRY THE ASTERISK -- ROM.1.a, b, e.
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
  'ROM.1',
  'ROM',
  array['ROM.1.a', 'ROM.1.b', 'ROM.1.c', 'ROM.1.d', 'ROM.1.e'],
  $q$Identification of Those Responsible for Governance$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} identifies those responsible for governance and documents their roles and responsibilities; how those persons lay down the organisation's vision, mission and values and make them public; how they monitor and measure performance against the stated mission; how they appoint the senior leaders; and how they support the ethical management framework of the organisation.

The chapter intent is that the management of the healthcare organisation is aware of and manages the key components of governance, that those responsible for governance are identified and their roles defined, and that governance is professional and ethical. A membership list that does not say what the board does, or a vision statement that lives only in a quality file, is not that intent.

The chapter note states that "Responsible for Governance" refers to the governing entity of the healthcare organisation and can exist in many configurations — for example the owner(s), the board of directors, or in the case of public hospitals the respective Ministry (Health/Railways/Labour). This document does not pick one configuration as a NABH mandate.

This document is the identification of governance and the acts those persons perform under ROM.1. It is not day-to-day leadership (ROM.2), not approval of plans and budget (ROM.3.a), and not management's risk-management duty (ROM.4).$q$,
  $q$This policy applies to those responsible for governance at {{HOSPITAL_NAME}} and to the people who record, publish and support the acts this document requires.

It covers: identification of the governing entity and documented roles; vision, mission and values laid down and made public; monitoring and measuring performance against the stated mission; appointment of senior leaders; and support for the ethical management framework.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The person heading the organisation day-to-day is ROM.2 (sibling). Governance appoints senior leaders here (ROM.1.d). ROM.2 owns that the head has administrative qualifications and experience, complies with applicable legislations, and has performance reviewed. Do not use one file for both.
- Approval of strategic and operational plans and the annual budget is ROM.3.a (sibling). Governance identified here is who approves there.
- Measurable service standards are ROM.3.d (sibling). Performance against the mission here is not those service standards counted twice.
- Staff rights and responsibilities are ROM.3.e (sibling). The ethical management framework here is governance support for ethics, not the staff-rights document.
- Management support for the patient-safety and QI programmes is PSQ.4 (drafted UNAPPROVED on sibling branch cursor/draft-psq1-psq5-unapproved-9324). PSQ.4 owns culture of safety, leader awareness of that programme, earmarked funds, and workforce feedback. This document owns governance identity and ethics support. Do not duplicate PSQ.4 here.
- The patient-safety and QI programmes themselves are PSQ.1 (sibling branch). Committees that run those programmes are not this governing entity unless this hospital has recorded that they are the same body — they usually are not.
- Patient and family rights are PRE.1/PRE.2 (sibling branch cursor/draft-pre1-pre6-unapproved-9324). This ethical framework is organisational ethics, not the patient-rights list.
- Informed consent method is PRE.3. Clinical ethics at the bedside is not this governance OE.
- HRM (not yet drafted) owns the employment file, job descriptions as HR documents, and credentialing. Appointment of senior leaders here is the governance act of appointing. HRM files the appointment.
- FMS (not yet drafted) owns the facility. Governance does not become the fire officer.
- G20/OECD Principles of Corporate Governance (chapter reference 21) and Arnwine on board roles (chapter reference 2) are frameworks for what a governing entity can do. They are not pasted as this hospital's board charter, and they do not make every SHCO a company.
- Companies Act, 2013, the Societies Registration Act, 1860, a state public-trusts Act, or a ministry order apply only if this hospital's legal form actually engages them. They are not numbered ROM chapter references and are not in paragraph 2 of the disclaimer. Legal form is stated at step 1.
- MSME registration, if any, is not this standard.$q$,
  $q${{HOSPITAL_NAME}} identifies those responsible for governance and documents their roles and responsibilities.

{{HOSPITAL_NAME}} requires those persons to lay down the organisation's vision, mission and values and to make them public.

{{HOSPITAL_NAME}} requires those persons to monitor and measure the performance of the organisation against the stated mission.

{{HOSPITAL_NAME}} requires those persons to appoint the senior leaders in the organisation.

{{HOSPITAL_NAME}} requires those persons to support the ethical management framework of the organisation.

{{HOSPITAL_NAME}} does not treat an unnamed owner, a vision poster with no governing body behind it, or a copied Companies Act board charter in a hospital that is not a company, as this standard.$q$,
  array[
    $s$1. Those responsible for governance identified; roles and responsibilities defined and documented

Those responsible for governance are identified, and their roles and responsibilities are defined and documented. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask who governs this hospital and what those persons are documented as doing. The answer must be a named governing entity this hospital actually has, not a generic "board" copied from a company hospital into a trust, or a ministry organogram that does not apply.

The reason this is the safety step is that without a named governing entity, later OEs (vision, appointment, ethics, budget at ROM.3.a, risk at ROM.4) have no actor. The common error is a letterhead that names trustees who never meet, or a quality committee counted as governance because it is the only committee that minutes exist for.

Who is responsible for governance, how that entity is constituted from this hospital's legal form, and the written roles and responsibilities, are [Hospital to define — those responsible for governance (the governing entity) and their documented roles and responsibilities]. The chapter note allows owner(s), a board of directors, or a ministry for a public hospital. This hospital states which configuration it is. G20/OECD Principles of Corporate Governance (chapter reference 21) and Arnwine (chapter reference 2) are frameworks, not a mandated board charter and not a reason to import the Companies Act, 2013. A public hospital does not invent a companies-Act board. A society or trust uses its constitutive instrument, not a pasted company memorandum.$s$,
    $s$2. Vision, mission and values laid down and made public

Those responsible for governance lay down the organisation's vision, mission and values and make them public. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask who wrote them and where a patient or a member of staff can read them. The answer must be a set laid down by the governing entity identified at step 1 and actually displayed or otherwise made public, not a consultant's brochure the board never adopted.

The reason this is written separately from step 1 is that identifying governors is not the same act as stating what the organisation is for. The common error is a mission statement in the quality manual that the governing entity never approved, or a public poster that differs from the approved text.

The written vision, mission and values, how the governing entity laid them down, and how they are made public, are [Hospital to define — the vision, mission and values laid down by those responsible for governance, and how they are made public]. Rego et al. (chapter reference 37) and Determining Your Core Values, Mission, and Vision (chapter reference 16) are frameworks, not pasted statements. Making them public is not PRE.1 rights display and is not PRE.5 tariff display.$s$,
    $s$3. Performance monitored and measured against the stated mission

Those responsible for governance monitor and measure the performance of the organisation against the stated mission.

How that monitoring is done, at what interval, which measures are used, and how it is recorded, are [Hospital to define — how those responsible for governance monitor and measure performance against the stated mission]. This is performance against the mission at step 2. It is not ROM.3.d service standards, not PSQ.2 key indicators, and not ROM.2.d review of the leader, though those may supply data.$s$,
    $s$4. Senior leaders appointed by those responsible for governance

Those responsible for governance appoint the senior leaders in the organisation.

Which posts count as senior leaders, who appoints, and how the appointment is recorded, are [Hospital to define — which posts are senior leaders and how those responsible for governance appoint them]. Appointment is the governance act. HRM (when drafted) owns the employment file. ROM.2 owns that the person heading the organisation has the administrative qualifications and experience the standard requires. This step does not write those qualifications.$s$,
    $s$5. Governance support for the ethical management framework

Those responsible for governance support the ethical management framework of the organisation. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask what the ethical framework is and what the governing entity did to support it. The answer must be a framework this hospital uses and evidence of governance support (adoption, resource, review), not a downloaded code of ethics the board never saw.

The reason this is the ethics step is that the chapter intent requires governance that is professional and ethical. Support is an act of the governing entity: it adopts or endorses the framework, it does not leave ethics only with a quality officer. The common error is to paste the NMC code, or the Mental Healthcare Act, 2017, as if either were this organisational framework. Clinical consent remains PRE.3. Patient rights remain PRE.1/PRE.2. Professional conduct of an RMP remains that professional's regulator. This OE is governance support for the organisation's ethical management framework.

What the ethical management framework is, how those responsible for governance support it, and how that support is recorded, are [Hospital to define — the ethical management framework and how those responsible for governance support it]. Chatterjee and Srinivasan on ethical issues in the Indian health-care sector (chapter reference 9), Biller-Andorno (chapter reference 6) and Bruning (chapter reference 8) are frameworks, not pasted codes. This document does not print MHCA 2017, CPA 2019 or CEA 2010 as this framework.$s$,
    $s$6. Records, review and the order of operations

The identification of the governing entity, the documented roles, the vision/mission/values and the record that they were made public, performance-against-mission records, senior-leader appointment records, and the ethical framework with evidence of governance support, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for governance-identification records] for: a named governing entity that matches this hospital's legal form rather than a copied company board; roles that say what those persons do; vision/mission/values laid down by that entity and actually made public; performance review against the mission that is not only PSQ.2 or ROM.3.d counted twice; appointments that are governance acts; ethics support that is not only a PRE rights poster; and no Companies Act or Societies Registration Act offered as this 3rd Edition OE.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when the governing entity changed, or when ROM.2–4, PSQ.4 or PRE.1 that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} having an identified governing entity under this document, and operates day-to-day under ROM.2.

Those responsible for governance, as identified at step 1, own the acts at steps 1-5.

HRM (when drafted) files appointments. PSQ.4 remains management support for the patient-safety and QI programmes. PRE remains patient rights and consent.

The quality or accreditation coordinator audits the records at step 6 and reports findings to the head of the institution and to those responsible for governance.

All staff are expected to treat an unnamed governing entity, a mission statement the board never adopted, and a pasted Companies Act charter that does not match this hospital's legal form, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 7 ROM, standard ROM.1.
- G20/OECD Principles of Corporate Governance (2015). OECD — chapter reference 21; framework for a governing entity, not a mandate that this hospital is a company.
- Arnwine, D. L. (2002). Effective Governance: The Roles and Responsibilities of Board Members. Baylor University Medical Center Proceedings, 15(1), 19-22 — chapter reference 2; framework.
- Rego, A., Araújo, B., & Serrão, D. (2015). The mission, vision and values in hospital management. Journal of Hospital Administration, 5(1) — chapter reference 37; framework.
- Determining Your Core Values, Mission, and Vision. (2015). Complete Guide to Practice Management — chapter reference 16; framework.
- Chatterjee, C., & Srinivasan, V. (2013). Ethical issues in health care sector in India. IIMB Management Review, 25(1), 5 — chapter reference 9; framework for the ethical management framework, not a pasted code.
- Biller-Andorno, N. (2004). Ethics, EBM, and hospital management. Journal of Medical Ethics, 30(2), 136-140 — chapter reference 6; framework.
- Bruning, P. (2013). Improving Ethical Decision Making in Health Care Leadership. Business and Economics Journal, 04(02) — chapter reference 8; framework.
- Internal documents of {{HOSPITAL_NAME}}: the constitutive instrument; the documented roles of those responsible for governance; vision, mission and values; the ethical management framework; ROM.2–4; PSQ.4; PRE.1–3.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with those responsible for governance and the quality or accreditation coordinator.

Copies issued to: the governing entity; the head of the institution; and senior leaders appointed under step 4.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The vision, mission and values — the public documents this policy requires — are held where they are made public.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

ROM — Responsibilities of Management (SHCO 3rd Edition Chapter 7)
OECD — Organisation for Economic Co-operation and Development

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

The requirements in this document are accreditation requirements of the NABH SHCO 3rd Edition rather than duties under a named Act of Parliament. In particular those arising under no named Act of Parliament; the duties in this document are accreditation requirements of the NABH SHCO 3rd Edition are written here as accreditation method, not as a copied statute. This policy does not import the Consumer Protection Act, 2019, the Clinical Establishments Act, 2010, or the Mental Healthcare Act, 2017 as a checklist. Statutory duties that arise under other documents of {{HOSPITAL_NAME}} remain those documents. {{HOSPITAL_NAME}} is responsible for verifying any statutory duty that applies to it; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "ROM.1.a", "requirement": "Those responsible for governance are identified, and their roles and responsibilities are defined and documented.", "steps": "Steps 1, 6", "evidence": "The named governing entity matching this hospital's legal form (owner(s), board, ministry, or other configuration this hospital actually has) rather than a copied company board or a quality committee counted as governance; the constitutive instrument or equivalent that identifies that entity; the written roles and responsibilities showing what those persons do, not only who they are; the recorded refusal to print the Companies Act, 2013 or the Societies Registration Act, 1860 as a NABH mandate; the recorded use of G20/OECD Principles and Arnwine (chapter references 21 and 2) as frameworks not a pasted charter; induction or briefing of members of the governing entity; the location of the roles document; the audit sample at step 6 of a living governing entity rather than a letterhead list of absentees", "responsible": "Those responsible for governance are identified at step 1; head of the institution is accountable that the identification exists; quality or accreditation coordinator audits"}, {"oe_code": "ROM.1.b", "requirement": "Those responsible for governance lay down the organisation's vision, mission and values and make them public.", "steps": "Steps 2, 1, 6", "evidence": "The written vision, mission and values showing they were laid down by the governing entity identified at step 1 rather than a consultant brochure never adopted; the record of how they are made public (where a patient, family member or staff member can actually read them) rather than a quality-office file; the recorded split that PRE.1 rights display and PRE.5 tariff display are not this making-public; the recorded use of Rego et al. and the core-values chapter reference (37 and 16) as frameworks not pasted statements; the location of the public text; the audit sample at step 6 of public text that matches the approved set", "responsible": "Those responsible for governance lay down and make public; head of the institution implements display; PRE.1/PRE.5 remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "ROM.1.c", "requirement": "Those responsible for governance monitor and measure the performance of the organisation against the stated mission.", "steps": "Steps 3, 2, 6", "evidence": "The written method and sample records of governance monitoring against the stated mission; the recorded split that ROM.3.d, PSQ.2 and ROM.2.d may supply data and do not replace this OE; the audit sample at step 6", "responsible": "Those responsible for governance monitor; ROM.3/PSQ.2/ROM.2 remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "ROM.1.d", "requirement": "Those responsible for governance appoint the senior leaders in the organisation.", "steps": "Steps 4, 6", "evidence": "The written list of senior-leader posts and sample appointment records as a governance act; the recorded split that HRM files the appointment and ROM.2 owns qualifications of the head; the audit sample at step 6", "responsible": "Those responsible for governance appoint; HRM files; ROM.2 owns the head's qualifications; quality or accreditation coordinator audits"}, {"oe_code": "ROM.1.e", "requirement": "Those responsible for governance support the ethical management framework of the organisation.", "steps": "Steps 5, 6", "evidence": "The written ethical management framework showing what it covers as organisational ethics rather than a pasted NMC code, MHCA 2017, CPA 2019 or CEA 2010; evidence of governance support (adoption, endorsement, resource or review by the entity at step 1) rather than a quality officer's private file; the recorded splits that PRE.1/PRE.2 own patient rights, PRE.3 owns consent method, and PSQ.4 owns culture of safety as a patient-safety programme requirement; the recorded use of Chatterjee and Srinivasan, Biller-Andorno and Bruning (chapter references 9, 6 and 8) as frameworks not pasted codes; induction or briefing of the governing entity on the framework; the location of the framework; the audit sample at step 6 of support that is an act of governance", "responsible": "Those responsible for governance support the framework; PRE and PSQ.4 remain those documents; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. ROM.1 standard text and all five OEs were read from the official SHCO 3rd Edition PDF, Chapter 7, printed page 110 (PDF page index 116). Header: "The organisation identifies those responsible for governance and their roles are defined." Intent printed page 109 (PDF page index 115), including the note on configurations of the governing entity. PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Core, b Commitment, c Achievement, d Commitment, e Core.
   THREE OEs CARRY THE ASTERISK -- ROM.1.a, b, e. c and d are unasterisked (Tier 2).
   Asterisks verified 2026-08-17 against the page and scripts/shco_oe_asterisks.json (owner-cleared ROM/FMS/HRM/IMS audit; no re-audit of the 123 OEs in this session).

TIERING UNDER THE STANDING RULE
1. THREE OF FIVE OEs ARE TIER 1. Tier 1: a, b, e -- steps 1, 2, 5 carry the reasoning. Tier 2: c, d. Shallower treatment of c-d is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of ROM.1.a/b/e against HIC/AAC/COP/MOM masters and PRE/PSQ drafts on sibling branches. Search terms: governance, board, vision, mission, ethics, committee.
   ROM.2 / ROM.3 / ROM.4 -- siblings. Stated in Scope.
   PSQ.4 -- management support for patient safety and QI. Not duplicated. Stated in Scope and step 5.
   PRE.1/PRE.2/PRE.3 -- patient rights and consent. Not this ethical framework. Stated in Scope and step 5.
   HRM -- employment file. Flagged; not yet drafted.
3. FORWARD REFERENCES: HRM appointment file; FMS not this document.
4. T2 QUICK CHECK: ROM.1.c vs ROM.3.d / PSQ.2 / ROM.2.d -- flagged. ROM.1.d vs ROM.2 qualifications -- flagged.

STATUTORY AND EXTERNAL FACTS
5. No named Act of Parliament is a numbered ROM chapter reference. Chapter reference 23 (India Code) is a repository, used by ROM.2.c, not a statute dumped here. P2 is accreditation-only. Companies Act 2013, Societies Registration Act 1860, state public-trusts Acts, CEA 2010, CPA 2019, MHCA 2017 and MSME registration are not a checklist. Legal form is [Hospital to define].
6. OECD corporate-governance principles, Arnwine, Rego, Chatterjee and Srinivasan -- frameworks, not pasted.
7. NO NUMBERS ARE STATED as requirements. No mandated board size or meeting frequency.

EDITORIAL POSITIONS TAKEN
8. Refusal to import Companies Act / Societies Registration Act as a NABH mandate is required by the multi-tenant template and by the chapter note that governance can be owners, a board, or a ministry.
9. Distinguishing this ethical framework from PRE rights/consent and from PSQ.4 culture of safety is an editorial position required by three different OEs.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
10. P1/P3/P4 shared. P2 uses make_disclaimer_accreditation_only(). AAC.1 defaulted-statute bug refused.

DELIBERATELY NOT INCLUDED
- Day-to-day leadership -- ROM.2. Plans and budget -- ROM.3.a. Risk management -- ROM.4. Patient-safety programme support -- PSQ.4.
- A named Companies Act board. A pasted NMC or MHCA ethics code.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 10 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 8 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 10; a search for "Hospital to define" without brackets finds all 10, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: governing entity and roles; vision/mission/values and how made public; performance-against-mission method; senior-leader posts and appointment method; ethical framework and how governance supports it; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
