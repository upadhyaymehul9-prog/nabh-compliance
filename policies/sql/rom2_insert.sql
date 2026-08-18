-- ROM.2 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 7 ROM, printed page 110
-- (PDF page index 116). NO OE CARRIES THE ASTERISK. Whole standard is Tier 2.
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
  'ROM.2',
  'ROM',
  array['ROM.2.a', 'ROM.2.b', 'ROM.2.c', 'ROM.2.d'],
  $q$The Organisation's Leader$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} is headed by a leader responsible for operating the organisation on a day-to-day basis: that this person has requisite and appropriate administrative qualifications; that this person has requisite and appropriate administrative experience; that this leader is responsible for and complies with laid-down and applicable legislations, regulations and notifications; and that the performance of the organisation's leader is reviewed for effectiveness.

The chapter intent is that responsibilities of the leaders at all levels are defined and that management executes its responsibility for compliance with all applicable regulations. A name on the letterhead without qualifications, or a copied central-Act list that does not match this hospital's legal form and services, is not that intent.

This document is the day-to-day head. It is not the identification of those responsible for governance (ROM.1), not approval of the annual budget (ROM.3.a), and not management's organisation-wide risk duty (ROM.4).$q$,
  $q$This policy applies to the person heading {{HOSPITAL_NAME}} and to those who appoint and review that person.

It covers: administrative qualifications of the head; administrative experience of the head; the leader's responsibility for and compliance with applicable legislations, regulations and notifications; and review of that leader's performance for effectiveness.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Those responsible for governance, and their appointment of senior leaders, are ROM.1 (sibling). ROM.1.d is the governance act of appointing. This document owns that the person heading the organisation has the qualifications and experience, complies with applicable law, and is reviewed. Do not use one file for both.
- ROM.3 owns professional functioning (plans, budget, committees, service standards, staff rights). The head operates those systems day-to-day; this document does not rewrite them.
- ROM.4 owns management's risk, reporting-of-failures and outsourcing duties. The head executes; this document does not rewrite those systems.
- PSQ.4 (sibling branch cursor/draft-psq1-psq5-unapproved-9324) owns that leaders at all levels are aware of the patient-safety and QI programme. This document owns the person heading the organisation. Awareness of PSQ.1 is not this qualification OE.
- HRM (not yet drafted) owns the employment file, credentialing of clinical staff, and job descriptions as HR documents. Qualifications and experience here are the administrative requirements of the head. HRM files them.
- AAC.1 owns defined services. The applicable-legislation register at step 3 must match services this hospital actually runs. It does not rewrite the directory.
- PRE.3 (sibling branch) owns consent method. NMC professional duties of an RMP are not this administrative-head OE unless the same person is both, in which case both records exist.
- Clay-Williams et al. on medical leadership (chapter reference 11) and Daly et al. (chapter reference 14) are frameworks. They are not a mandate that the head must be a doctor, or must not be a doctor.
- India Code (chapter reference 23) is the lookup for central and state Acts. It is not itself a statute dumped into paragraph 2. The applicable list is stated at step 3 from this hospital's legal form and services. Companies Act, 2013, Societies Registration Act, 1860, CEA 2010, CPA 2019, MHCA 2017 and MSME registration are not a checklist.$q$,
  $q${{HOSPITAL_NAME}} is headed by a leader who is responsible for operating the organisation on a day-to-day basis.

{{HOSPITAL_NAME}} requires that person to have requisite and appropriate administrative qualifications.

{{HOSPITAL_NAME}} requires that person to have requisite and appropriate administrative experience.

{{HOSPITAL_NAME}} requires that leader to be responsible for and to comply with laid-down and applicable legislations, regulations and notifications.

{{HOSPITAL_NAME}} reviews the performance of the organisation's leader for effectiveness.

{{HOSPITAL_NAME}} does not treat a letterhead name, or a copied Act list that does not match this hospital, as that leadership.$q$,
  array[
    $s$1. Administrative qualifications of the head

The person heading the organisation has requisite and appropriate administrative qualifications.

Which qualifications are requisite and appropriate for this hospital, and how they are recorded, are [Hospital to define — the requisite and appropriate administrative qualifications of the person heading the organisation, and how they are evidenced]. Clay-Williams et al. (chapter reference 11) is a framework, not a mandate that the head is (or is not) a doctor. HRM files the certificates when drafted.$s$,
    $s$2. Administrative experience of the head

The person heading the organisation has requisite and appropriate administrative experience.

What experience is requisite and appropriate, and how it is recorded, are [Hospital to define — the requisite and appropriate administrative experience of the person heading the organisation, and how it is evidenced]. Experience is not the same act as the qualifications at step 1.$s$,
    $s$3. Compliance with applicable legislations, regulations and notifications

The leader is responsible for and complies with the laid-down and applicable legislations, regulations and notifications.

Which legislations, regulations and notifications apply to this hospital's legal form and to the services it actually runs, who maintains that register, and how the leader's compliance is evidenced, are [Hospital to define — the register of laid-down and applicable legislations, regulations and notifications, and how the leader's compliance is evidenced]. India Code (chapter reference 23) is the lookup, not a paste of every central Act. A hospital that is not a company does not invent Companies Act compliance as a NABH mandate. A State that has not adopted CEA does not invent a CEA board. Statutory duties that already live in other documents of {{HOSPITAL_NAME}} (for example BMW under HIC.3, NDPS under MOM.8, PC-PNDT under AAC.5) remain those documents; this step owns that the leader is responsible for the applicable set as a whole. This document does not print a rupee penalty or a named inspectorate as a NABH mandate.$s$,
    $s$4. Review of the leader's performance for effectiveness

The performance of the organisation's leader is reviewed for effectiveness.

Who reviews, against what, at what interval, and how it is recorded, are [Hospital to define — how the performance of the organisation's leader is reviewed for effectiveness]. Those responsible for governance (ROM.1) are the natural reviewers; this hospital says so. This review is not ROM.1.c performance of the organisation against the mission, though data may overlap.$s$,
    $s$5. Records, review and the order of operations

The head's qualification and experience records, the applicable-legislation register and compliance evidence, and the leader-performance review records, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for leader records] for: qualifications and experience actually held rather than a letterhead name; a legislation register that matches this hospital's legal form and defined services rather than a copied central-Act dump; performance review of the leader that is not only ROM.1.c counted twice; and no Companies Act, Societies Registration Act, CEA, CPA or MHCA offered as a blanket checklist.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when the head changes, or when ROM.1, ROM.3, ROM.4 or AAC.1 that this document hands work to are revised.$s$
  ],
  $q$Those responsible for governance (ROM.1) appoint the head and review that person's performance.

The person heading the organisation is responsible for day-to-day operation and for compliance with the applicable set at step 3.

HRM (when drafted) files qualifications and experience.

The quality or accreditation coordinator audits the records at step 5 and reports findings to those responsible for governance.

All staff are expected to treat a letterhead head with no recorded qualifications, and a copied Act list that does not apply here, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 7 ROM, standard ROM.2.
- India Code: Home. Digital repository of all central and state acts. Government of India — chapter reference 23; lookup for the hospital's applicable-legislation register, not a pasted statute list.
- Clay-Williams, R., et al. (2017). Medical leadership, a systematic narrative review. BMJ Open, 7(9), e014474 — chapter reference 11; framework, not a mandate that the head is a doctor.
- Daly, J., et al. (2014). The importance of clinical leadership in the hospital setting. Journal of Healthcare Leadership, 75 — chapter reference 14; framework.
- Internal documents of {{HOSPITAL_NAME}}: the head's appointment; qualification and experience records; the applicable-legislation register; ROM.1, ROM.3, ROM.4; AAC.1.$q$,
  $q$Controlled master copy: office of those responsible for governance, {{HOSPITAL_NAME}}, with the head of the institution and the quality or accreditation coordinator.

Copies issued to: the person heading the organisation.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder].

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

ROM — Responsibilities of Management (SHCO 3rd Edition Chapter 7)
CEA — Clinical Establishments Act, 2010 (named only to refuse it as a blanket checklist)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

The requirements in this document are accreditation requirements of the NABH SHCO 3rd Edition rather than duties under a named Act of Parliament. In particular those arising under no named Act of Parliament; the duties in this document are accreditation requirements of the NABH SHCO 3rd Edition are written here as accreditation method, not as a copied statute. This policy does not import the Consumer Protection Act, 2019, the Clinical Establishments Act, 2010, or the Mental Healthcare Act, 2017 as a checklist. Statutory duties that arise under other documents of {{HOSPITAL_NAME}} remain those documents. {{HOSPITAL_NAME}} is responsible for verifying any statutory duty that applies to it; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "ROM.2.a", "requirement": "The person heading the organisation has requisite and appropriate administrative qualifications.", "steps": "Steps 1, 5", "evidence": "The written statement of requisite administrative qualifications and the current head's evidence; the recorded split that HRM files certificates; the audit sample at step 5", "responsible": "Those responsible for governance appoint a qualified head; HRM files; quality or accreditation coordinator audits"}, {"oe_code": "ROM.2.b", "requirement": "The person heading the organisation has requisite and appropriate administrative experience.", "steps": "Steps 2, 5", "evidence": "The written statement of requisite administrative experience and the current head's evidence; the recorded split that this is not step 1 counted twice; the audit sample at step 5", "responsible": "Those responsible for governance appoint an experienced head; quality or accreditation coordinator audits"}, {"oe_code": "ROM.2.c", "requirement": "The leader is responsible for and complies with the laid-down and applicable legislations, regulations and notifications.", "steps": "Steps 3, 5", "evidence": "The current applicable-legislation register matching this hospital's legal form and AAC.1 services, using India Code (chapter reference 23) as lookup rather than a pasted central-Act dump; sample compliance evidence; the recorded refusal to dump Companies Act, Societies Registration Act, CEA, CPA or MHCA as a checklist; the recorded split that HIC.3/MOM.8/AAC.5 (and other owning documents) keep their own statutes; the audit sample at step 5", "responsible": "The head is responsible for the applicable set; owning clinical/IPC/medication documents keep their statutes; quality or accreditation coordinator audits"}, {"oe_code": "ROM.2.d", "requirement": "The performance of the organisation's leader is reviewed for effectiveness.", "steps": "Steps 4, 5", "evidence": "The written review method and sample reviews; the recorded split that ROM.1.c is organisation-against-mission, not this review of the leader; the audit sample at step 5", "responsible": "Those responsible for governance review the head; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. ROM.2 standard text and all four OEs were read from the official SHCO 3rd Edition PDF, Chapter 7, printed page 110 (PDF page index 116). Header: "The organisation is headed by a leader who shall be responsible for operating the organisation on a day-to-day basis." PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Commitment, b Commitment, c Core, d Achievement.
   NO OE CARRIES THE ASTERISK. Whole standard is Tier 2, including Core ROM.2.c. Asterisks verified 2026-08-17 against the page and scripts/shco_oe_asterisks.json.

TIERING UNDER THE STANDING RULE
1. Whole standard is Tier 2. Shallower treatment of the WHOLE STANDARD is a DECISION UNDER THE STANDING RULE, not an omission. ROM.2.c is Core and still Tier 2 because it is unasterisked.

CROSS-REFERENCE AND OVERLAP CHECK
2. T2 quick check (2026-08-17). ROM.1.d appointment vs this qualifications/experience -- flagged. ROM.1.c organisation-against-mission vs ROM.2.d leader review -- flagged. PSQ.4 leader awareness of the safety programme -- flagged. HRM employment file -- flagged. AAC.1 services vs the legislation register -- flagged. Owning documents keep their own statutes (HIC.3, MOM.8, AAC.5) -- stated.

STATUTORY AND EXTERNAL FACTS
3. No named Act is a numbered ROM chapter reference. India Code (ch 23) is a lookup. P2 is accreditation-only. Companies Act / Societies / CEA / CPA / MHCA / MSME are not a checklist. Applicable list is hospital-defined from legal form and defined services.
4. Clay-Williams / Daly -- frameworks, not a doctor-as-head mandate.
5. NO NUMBERS ARE STATED as requirements. No mandated years of experience.

EDITORIAL POSITIONS TAKEN
6. Keeping P2 accreditation-only despite ROM.2.c being about legislation is required by the statute-matching rule: the bibliography names a repository, not an Act. Dumping Companies Act onto a trust hospital would be the AAC.1 defaulted-statute bug.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
7. P1/P3/P4 shared. P2 uses make_disclaimer_accreditation_only().

DELIBERATELY NOT INCLUDED
- Governance identity -- ROM.1. Plans/budget -- ROM.3. Risk -- ROM.4.
- A pasted central-Act encyclopaedia. A mandate that the head is a doctor.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 9 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 7 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 9; a search for "Hospital to define" without brackets finds all 9, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: qualifications; experience; the applicable-legislation register and compliance evidence; leader-performance review method; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
