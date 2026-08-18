-- ROM.3 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 7 ROM, printed page 111
-- (PDF page index 117). ONE OE CARRIES THE ASTERISK -- ROM.3.d.
-- Official ROM.3.e uses "organization".
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
  'ROM.3',
  'ROM',
  array['ROM.3.a', 'ROM.3.b', 'ROM.3.c', 'ROM.3.d', 'ROM.3.e'],
  $q$Professional Functioning$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} displays professionalism in its functioning: how those responsible for governance approve the strategic and operational plans and the organisation's annual budget; how the organisation coordinates functioning with departments and external agencies and monitors progress toward defined goals and objectives; how the functioning of committees is reviewed for effectiveness; how the organisation documents measurable service standards and monitors them; and how it documents staff rights and responsibilities.

The chapter intent is professional and ethical governance and defined management responsibilities. A budget the board never saw, or service standards that are slogans without a measure, is not that professionalism.

This document is professional functioning. It is not identification of the governing entity (ROM.1), not the day-to-day head (ROM.2), and not organisation-wide risk management (ROM.4).$q$,
  $q$This policy applies to those responsible for governance, the person heading {{HOSPITAL_NAME}}, the people who coordinate departments and external agencies, the committees whose functioning is reviewed, and the people who set and monitor service standards and who hold the staff-rights document.

It covers: governance approval of strategic and operational plans and the annual budget; coordination with departments and external agencies and monitoring of goals; review of committee functioning; documented measurable service standards and their monitoring; and documented staff rights and responsibilities.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Those responsible for governance are identified in ROM.1 (sibling). This document owns what they approve here (plans and budget). ROM.1.c monitors performance against the mission; this document's ROM.3.d monitors measurable service standards. They may share data; they are not the same OE.
- The person heading the organisation is ROM.2 (sibling). That person operates these systems day-to-day. This document owns the systems.
- PSQ.4.c (sibling branch cursor/draft-psq1-psq5-unapproved-9324) owns that management earmarks adequate funds from the annual budget for the patient-safety and QI programme. THIS document's ROM.3.a owns governance approval of the annual budget. The earmark sits inside a budget this OE approved. Do not rewrite PSQ.4.c here, and do not treat an earmark as budget approval.
- PSQ.1 owns the patient-safety and QI programmes and their committees. PSQ.3 owns clinical audit. This document's ROM.3.c owns that committee functioning is reviewed for effectiveness — including those committees and any other committee this hospital actually runs. It does not rewrite PSQ.1 or PSQ.3 method.
- PSQ.2 owns key indicators as tools for continual improvement. ROM.3.d owns documented measurable service standards and monitoring them. An indicator may measure a service standard; the service-standard document is this OE.
- AAC.1 owns the written definition of healthcare services. Service standards here measure how those defined services are delivered. Unused services are a recorded absence, not a copied ICU standard.
- PRE.1/PRE.2 (sibling branch) own patient and family rights. ROM.3.e is staff rights and responsibilities. Do not use one poster for both.
- HRM (not yet drafted) owns the employment file, job descriptions, grievance as an HR process, and training. This document owns that staff rights and responsibilities are documented as a governance/management act. HRM may hold the working copy.
- FMS (not yet drafted) may own facility service levels. A facility KPI is not this hospital-wide service-standard set counted twice.
- Choudhuri on strategic planning (chapter reference 10) and Strategic Planning: Why It Makes a Difference (chapter reference 41) are frameworks, not pasted plans. No rupee figure is a NABH mandate.$q$,
  $q${{HOSPITAL_NAME}} requires those responsible for governance to approve the strategic and operational plans and the organisation's annual budget.

{{HOSPITAL_NAME}} coordinates functioning with departments and external agencies and monitors progress in achieving defined goals and objectives.

{{HOSPITAL_NAME}} reviews the functioning of committees for their effectiveness.

{{HOSPITAL_NAME}} documents service standards that are measurable and monitors them.

{{HOSPITAL_NAME}} documents staff rights and responsibilities.

{{HOSPITAL_NAME}} does not treat an unapproved budget, a dormant committee list, or a slogan without a measure, as professional functioning.$q$,
  array[
    $s$1. Governance approval of strategic and operational plans and the annual budget

Those responsible for governance approve the strategic and operational plans and the organisation's annual budget.

What the strategic plan, operational plan and annual budget are, who presents them, and how approval is recorded, are [Hospital to define — how those responsible for governance approve the strategic and operational plans and the annual budget]. PSQ.4.c earmarks funds for the patient-safety and QI programme from that budget; it does not approve the budget. This document does not print a rupee figure or a mandated financial year-end as a NABH mandate. Choudhuri (chapter reference 10) is a framework, not a pasted plan.$s$,
    $s$2. Coordination with departments and external agencies; monitoring of goals

The organisation coordinates the functioning with departments and external agencies and monitors the progress in achieving the defined goals and objectives.

Which departments, which external agencies, which goals and objectives, how coordination is done, and how progress is monitored, are [Hospital to define — how functioning is coordinated with departments and external agencies and how progress toward defined goals and objectives is monitored]. External agencies are those this hospital actually deals with (for example a referred hospital, a diagnostic partner, a municipal authority). AAC.1 unused services do not invent an agency.$s$,
    $s$3. Review of committee functioning for effectiveness

The functioning of committees is reviewed for their effectiveness.

Which committees this hospital actually runs, who reviews them, at what interval, and how effectiveness is recorded, are [Hospital to define — how the functioning of committees is reviewed for effectiveness]. PSQ.1 committees, the infection-control committee (HIC.1), the medication committee (MOM.1) and any other named committee remain those documents for what they do. This step owns that their functioning is reviewed for effectiveness. A membership list of absentees is not a review.$s$,
    $s$4. Documented measurable service standards, monitored

The organisation documents the service standards that are measurable and monitors them. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask which service standards exist, whether they can be measured, and whether they were monitored. The answer must be a documented set this hospital uses against the services it actually runs, not a slogan ("we provide quality care") and not PSQ.2's indicator file counted twice.

The reason this is the professionalism step is that a hospital that cannot say what good looks like, in a form that can be counted, cannot show it improved. The common error is to paste Annexure 1 KPIs, or AAC.1's service directory, and call that service standards. AAC.1 names what is offered. PSQ.2 names indicators used as tools for continual improvement. This OE names service standards that are measurable and the monitoring of those standards. An indicator may be how a standard is monitored; the standard itself is written here.

Which service standards, how each is measurable, how they are monitored, and how that is recorded, are [Hospital to define — the documented measurable service standards and how they are monitored]. A service the directory does not provide is a recorded absence, not a copied ICU waiting-time standard. This document does not print a mandated turnaround-time figure as a NABH number.$s$,
    $s$5. Staff rights and responsibilities documented

The organization documents staff rights and responsibilities.

What those rights and responsibilities are, where they are documented, and how staff are made aware of them, are [Hospital to define — how staff rights and responsibilities are documented and made known]. Official spelling in the OE is "organization". Patient rights remain PRE.1/PRE.2. HRM (when drafted) may hold the working copy and the grievance file. This step owns that the document exists as a management act.$s$,
    $s$6. Records, review and the order of operations

The approved plans and budget, coordination and goal-monitoring records, committee-effectiveness reviews, the measurable service-standard set and monitoring records, and the staff-rights document, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for professional-functioning records] for: plans and budget actually approved by the governing entity; PSQ.4.c earmark sitting inside that budget rather than replacing approval; committee reviews that are not only membership lists; service standards that are measurable and monitored rather than slogans or a second PSQ.2 file; staff rights distinct from PRE patient rights; and no rupee figure offered as a NABH mandate.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when the governing entity or the service directory changed, or when ROM.1, ROM.2, ROM.4, PSQ.2, PSQ.4 or AAC.1 that this document hands work to are revised.$s$
  ],
  $q$Those responsible for governance approve plans and the annual budget at step 1 and receive committee-effectiveness and service-standard monitoring.

The person heading the organisation coordinates departments and external agencies at step 2 and operates these systems day-to-day.

Committee chairs remain responsible for their own committees' work under the owning documents (PSQ.1, HIC.1, MOM.1 and others). This document reviews functioning.

HRM (when drafted) may hold the staff-rights working copy.

The quality or accreditation coordinator audits the records at step 6.

All staff are expected to treat an unapproved budget, a dormant committee, and a slogan offered as a service standard, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 7 ROM, standard ROM.3. Official ROM.3.e uses "organization".
- Choudhuri, D. (2015). Strategic Planning: A Comprehensive Approach — chapter reference 10; framework, not a pasted plan.
- Strategic Planning: Why It Makes a Difference, and How to Do It. (2009). Journal of Oncology Practice, 5(3), 139-143 — chapter reference 41; framework.
- Internal documents of {{HOSPITAL_NAME}}: strategic and operational plans; annual budget; committee list and effectiveness reviews; measurable service standards; staff rights and responsibilities; ROM.1, ROM.2, ROM.4; PSQ.2, PSQ.4; AAC.1; PRE.1.$q$,
  $q$Controlled master copy: office of those responsible for governance, {{HOSPITAL_NAME}}, with the head of the institution and the quality or accreditation coordinator.

Copies issued to: committee chairs; department heads who operate service standards.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The staff-rights document is held where staff can actually read it.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

ROM — Responsibilities of Management (SHCO 3rd Edition Chapter 7)
QI — quality improvement

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

The requirements in this document are accreditation requirements of the NABH SHCO 3rd Edition rather than duties under a named Act of Parliament. In particular those arising under no named Act of Parliament; the duties in this document are accreditation requirements of the NABH SHCO 3rd Edition are written here as accreditation method, not as a copied statute. This policy does not import the Consumer Protection Act, 2019, the Clinical Establishments Act, 2010, or the Mental Healthcare Act, 2017 as a checklist. Statutory duties that arise under other documents of {{HOSPITAL_NAME}} remain those documents. {{HOSPITAL_NAME}} is responsible for verifying any statutory duty that applies to it; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "ROM.3.a", "requirement": "Those responsible for governance approve the strategic and operational plans and the organisation's annual budget.", "steps": "Steps 1, 6", "evidence": "Sample approved strategic plan, operational plan and annual budget showing governance approval; the recorded split that PSQ.4.c earmarks programme funds from this budget and does not approve it; the audit sample at step 6", "responsible": "Those responsible for governance approve; PSQ.4.c remains the earmark; quality or accreditation coordinator audits"}, {"oe_code": "ROM.3.b", "requirement": "The organisation coordinates the functioning with departments and external agencies and monitors the progress in achieving the defined goals and objectives.", "steps": "Steps 2, 6", "evidence": "The written coordination method and sample progress-monitoring records; the recorded split that unused AAC.1 services do not invent an agency; the audit sample at step 6", "responsible": "Head of the institution coordinates; department heads and named external-agency leads participate; quality or accreditation coordinator audits"}, {"oe_code": "ROM.3.c", "requirement": "The functioning of committees is reviewed for their effectiveness.", "steps": "Steps 3, 6", "evidence": "The committee list this hospital actually runs and sample effectiveness reviews; the recorded split that PSQ.1/HIC.1/MOM.1 own what those committees do; the audit sample at step 6 of a review that is not a membership list of absentees", "responsible": "Named reviewer (governance or head); committee chairs remain owning-document leads; quality or accreditation coordinator audits"}, {"oe_code": "ROM.3.d", "requirement": "The organisation documents the service standards that are measurable and monitors them.", "steps": "Steps 4, 6", "evidence": "The written measurable service-standard set aligned to AAC.1 defined services rather than slogans or a copied ICU list for a service not offered; sample monitoring records showing the standards were actually measured; the recorded split that AAC.1 names what is offered, PSQ.2 owns key indicators as QI tools, and this OE owns the service standards themselves; the recorded refusal to paste Annexure 1 or a mandated turnaround-time figure as a NABH number; induction or briefing of department heads who operate the standards; the location of the set; the audit sample at step 6 of monitoring that used the documented measures", "responsible": "Head of the institution keeps the set current; department heads monitor in their areas; AAC.1/PSQ.2 remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "ROM.3.e", "requirement": "The organization documents staff rights and responsibilities.", "steps": "Steps 5, 6", "evidence": "The documented staff rights and responsibilities (official spelling organization); the recorded split that PRE.1/PRE.2 own patient rights and HRM holds the employment/grievance file when drafted; the audit sample at step 6", "responsible": "Head of the institution ensures the document exists; HRM may hold the working copy; PRE remains patient rights; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. ROM.3 standard text and all five OEs were read from the official SHCO 3rd Edition PDF, Chapter 7, printed page 111 (PDF page index 117). Header: "The organisation displays professionalism in its functioning." Official ROM.3.e uses "organization". PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Commitment, b Achievement, c Commitment, d Achievement, e Commitment.
   ONE OE CARRIES THE ASTERISK -- ROM.3.d. a, b, c, e are unasterisked (Tier 2).
   Asterisks verified 2026-08-17 against the page and scripts/shco_oe_asterisks.json.

TIERING UNDER THE STANDING RULE
1. ONE OF FIVE OEs IS TIER 1. Tier 1: d -- step 4 carries the reasoning. Tier 2: a, b, c, e. Shallower treatment of a-c and e is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of ROM.3.d against AAC.1 and PSQ.2 (sibling branch). Service directory vs service standards vs key indicators -- stated in Scope and step 4.
   PSQ.4.c budget earmark vs ROM.3.a budget approval -- HANDOFF ACCEPTED. Stated in Scope and step 1.
   ROM.3.c vs PSQ.1/HIC.1/MOM.1 committees -- flagged.
   ROM.3.e vs PRE.1/PRE.2 patient rights vs HRM -- flagged.
3. FORWARD REFERENCES: HRM staff-rights working copy; FMS facility KPIs.
4. T2 QUICK CHECK: ROM.1.c mission performance vs ROM.3.d service standards -- flagged. ROM.3.b external agencies vs AAC.1 unused services -- flagged.

STATUTORY AND EXTERNAL FACTS
5. No named Act is a numbered ROM chapter reference. P2 is accreditation-only. No rupee figure as a NABH mandate.
6. Choudhuri / JOP strategic-planning papers -- frameworks, not pasted plans.
7. NO NUMBERS ARE STATED as requirements. No mandated TAT.

EDITORIAL POSITIONS TAKEN
8. Accepting PSQ.4.c's forward-ref: this OE approves the budget; PSQ.4.c earmarks from it.
9. Distinguishing ROM.3.d from AAC.1 and PSQ.2 is required by three different OEs.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
10. P1/P3/P4 shared. P2 uses make_disclaimer_accreditation_only().

DELIBERATELY NOT INCLUDED
- Governance identity -- ROM.1. Day-to-day head -- ROM.2. Risk -- ROM.4. PSQ.4 culture/earmark method.
- A pasted Annexure 1 as mandated service standards.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 10 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 8 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 10; a search for "Hospital to define" without brackets finds all 10, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: how plans and budget are approved; coordination and goal-monitoring method; committee-effectiveness review; the measurable service-standard set and monitoring; staff rights and responsibilities document; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
