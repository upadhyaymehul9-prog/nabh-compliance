-- PSQ.2 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 6 PSQ, printed pages 102-103.
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
  'PSQ.2',
  'PSQ',
  array['PSQ.2.a', 'PSQ.2.b', 'PSQ.2.c', 'PSQ.2.d', 'PSQ.2.e'],
  $q$Key Indicators for Continual Improvement$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} identifies and monitors key indicators to oversee clinical structures, processes and outcomes; infection-control activities; managerial structures, processes and outcomes; and patient-safety activities; and how the quality team regularly verifies that data and analyses it to identify opportunities for improvement.

The chapter intent is that the organisation collects data on structures, processes and outcomes, especially in high-risk situations, then collates, analyses and uses it for further improvements. A dashboard copied from Annexure 1 that nobody verifies, or infection rates redefined beside HIC.5, is not that intent.

This document is hospital-wide indicator identification, monitoring, verification and analysis. It is not HAI surveillance method, unit QA, or the safety/QI programmes that use the findings.$q$,
  $q$This policy applies to the quality team and to every area that supplies indicator data at {{HOSPITAL_NAME}}.

It covers: clinical structure/process/outcome indicators; infection-control activity indicators; managerial structure/process/outcome indicators; patient-safety activity indicators; and regular verification and analysis by the quality team.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The patient-safety and QI programmes that use these indicators are PSQ.1. This document owns the indicators. PSQ.1 owns the programmes.
- Clinical audit parameters are PSQ.3.b. An audit parameter is not by itself a key indicator under this document, though data may overlap.
- HAI surveillance method (definitions, device-days, rates) is HIC.5. Hand-hygiene and bundle process measures are HIC.2/HIC.4. PSQ.2.b oversees infection-control activities as quality indicators. It may use HIC.5/HIC.4 figures as inputs. It does not invent a second case-definition book. Historical HIC.1/HIC.3 text that assigned surveillance method to "CQI" is a 2nd Edition name; do not revive it here.
- Falls, pressure ulcers and similar clinical risk programmes are COP.12. Patient-safety indicators here (PSQ.2.d) may include those rates; COP.12 still owns identification and management at the bedside.
- Medication-error incidence as a clinical/safety indicator may use MOM.7 capture. MOM.7 still captures the event.
- Transfusion-reaction figures, if used, come from COP.5; this document does not own the transfusion process.
- Waiting-time and discharge-time indicators, if used, do not rewrite AAC.2 registration or AAC.8 discharge method.
- Annexure 1 of the same 3rd Edition book lists Key Performance Indicators. It is a framework for what NABH publishes as KPIs. This hospital identifies its own key indicators; the annexure is not pasted as a mandated set, and unused services (for example ICU SMR where there is no ICU) are recorded absences against AAC.1.
- ROM/FMS managerial indicators (budget, occupancy, equipment downtime) remain those chapters when drafted; this document oversees managerial indicators as quality tools, not the finance ledger.
- This chapter is PSQ, not CQI.$q$,
  $q${{HOSPITAL_NAME}} identifies and monitors key indicators for clinical structures, processes and outcomes; infection-control activities; managerial structures, processes and outcomes; and patient-safety activities.

{{HOSPITAL_NAME}} requires the quality team to verify that data regularly and to analyse it to identify opportunities for improvement.

{{HOSPITAL_NAME}} does not treat an unverified copy of Annexure 1, or a second HAI case-definition book, as that monitoring.$q$,
  array[
    $s$1. Clinical structure, process and outcome indicators

The organisation identifies and monitors key indicators to oversee the clinical structures, processes and outcomes.

Which clinical indicators this hospital monitors, how they are collected, and the monitoring interval, are [Hospital to define — the key clinical structure, process and outcome indicators, how they are collected, and the monitoring interval]. Donabedian (chapter reference 6) is the book's own structure-process-outcome frame; it is not a mandated indicator list. Annexure 1 of this edition is a framework. A service not provided is a recorded absence, not a copied ICU mortality ratio.$s$,
    $s$2. Infection-control activity indicators

The organisation identifies and monitors the key indicators to oversee infection control activities.

Which infection-control indicators are monitored, and how they use (not replace) HIC.5 surveillance and HIC.4 bundle-compliance figures, are [Hospital to define — the key indicators used to oversee infection-control activities, and how they take HIC.5/HIC.4 figures as inputs rather than redefining case definitions]. This step does not write NHSN definitions.$s$,
    $s$3. Managerial structure, process and outcome indicators

The organisation identifies and monitors the key indicators to oversee the managerial structures, processes and outcomes.

Which managerial indicators are monitored is [Hospital to define — the key managerial structure, process and outcome indicators, how they are collected, and the monitoring interval]. The finance ledger and facility registers remain ROM/FMS when drafted.$s$,
    $s$4. Patient-safety activity indicators

The organisation identifies and monitors the key indicators to oversee patient safety activities.

Which patient-safety indicators are monitored is [Hospital to define — the key indicators used to oversee patient-safety activities, how they are collected, and the monitoring interval]. Falls and pressure-ulcer rates, if used, still leave identification and management with COP.12. Medication-error rates, if used, still leave capture with MOM.7. Needlestick figures, if used, still leave occupational method with HIC.4.$s$,
    $s$5. Verification and analysis by the quality team

Data is regularly verified by the quality team and is analysed to identify the opportunities for improvement.

How the quality team verifies (completeness, definitions used, sample checks) and analyses, the regular interval, and how opportunities are handed to PSQ.1 reviews, are [Hospital to define — how the quality team regularly verifies indicator data, how it is analysed, and how opportunities for improvement are recorded]. Unverified dashboard numbers are not this OE. Dimick (chapter reference 5) and Jones et al. (chapter reference 18) are frameworks for what makes a good indicator, not pasted selection tools.$s$,
    $s$6. Records, review and the order of operations

The indicator lists, collection methods, verification records and analysis that produced opportunities, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for key-indicator records] for: clinical, IC, managerial and patient-safety indicators actually monitored; unused-service absences recorded; HIC.5 not rewritten; data verified and analysed; and no Annexure 1 paste offered as the hospital's identified set.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when an unverified dashboard was used for a decision, or HAI definitions were rewritten here, or when PSQ.1, HIC.5, COP.12 or MOM.7 that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable for {{HOSPITAL_NAME}} identifying and monitoring these key indicators and for the quality team verifying and analysing the data.

The quality team verifies and analyses at step 5. Area leads supply source data. HIC.5 still owns surveillance method. COP.12 and MOM.7 still own their clinical capture.

The named lead for key indicators is [Hospital to define — the named lead for key indicators].

The quality or accreditation coordinator audits the records at step 6 and reports findings to the head of the institution.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 6 PSQ, standard PSQ.2, and Annexure 1 Key Performance Indicators as a framework, not a mandated paste.
- Donabedian, A. (1983). Quality Assessment and Monitoring — chapter reference 6; structure-process-outcome frame.
- Dimick, J. B. (2010). What Makes a "Good" Quality Indicator? — chapter reference 5; framework.
- Jones, P., et al. (2014). What makes a good healthcare quality indicator? — chapter reference 18; framework.
- Internal documents of {{HOSPITAL_NAME}}: the four indicator lists and collection methods; verification and analysis records; the patient-safety and QI programmes; HIC.5 surveillance; COP.12; MOM.7.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: the quality team; HIC; nursing administration; and area leads who supply data.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder].

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP, PPE and HAI.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

PSQ — Patient Safety and Quality Improvement (SHCO 3rd Edition Chapter 6; not CQI)
KPI — key performance indicator

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

The requirements in this document are accreditation requirements of the NABH SHCO 3rd Edition rather than duties under a named Act of Parliament. In particular those arising under no named Act of Parliament; the duties in this document are accreditation requirements of the NABH SHCO 3rd Edition are written here as accreditation method, not as a copied statute. This policy does not import the Consumer Protection Act, 2019, the Clinical Establishments Act, 2010, or the Mental Healthcare Act, 2017 as a checklist. Statutory duties that arise under other documents of {{HOSPITAL_NAME}} remain those documents. {{HOSPITAL_NAME}} is responsible for verifying any statutory duty that applies to it; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "PSQ.2.a", "requirement": "The organisation identifies and monitors key indicators to oversee the clinical structures, processes and outcomes.", "steps": "Steps 1, 5, 6", "evidence": "The written clinical indicator list and collection method, with recorded absences for services not provided; sample monitoring records; Donabedian used as a frame not a paste; the audit sample at step 6", "responsible": "Named lead holds the clinical list; area leads supply data; quality team verifies; quality or accreditation coordinator audits"}, {"oe_code": "PSQ.2.b", "requirement": "The organisation identifies and monitors the key indicators to oversee infection control activities.", "steps": "Steps 2, 5, 6", "evidence": "The written IC-indicator list showing HIC.5/HIC.4 figures used as inputs rather than a second case-definition book; sample monitoring; the recorded refusal to revive a 'CQI owns surveillance' assignment; the audit sample at step 6", "responsible": "HIC.5 owns surveillance method; this document oversees IC indicators; quality or accreditation coordinator audits"}, {"oe_code": "PSQ.2.c", "requirement": "The organisation identifies and monitors the key indicators to oversee the managerial structures, processes and outcomes.", "steps": "Steps 3, 5, 6", "evidence": "The written managerial indicator list; the recorded split that ROM/FMS own the ledger and facility registers when drafted; sample monitoring; the audit sample at step 6", "responsible": "Named lead holds the managerial list; ROM/FMS remain those chapters; quality or accreditation coordinator audits"}, {"oe_code": "PSQ.2.d", "requirement": "The organisation identifies and monitors the key indicators to oversee patient safety activities.", "steps": "Steps 4, 5, 6", "evidence": "The written patient-safety indicator list; the recorded splits that COP.12, MOM.7 and HIC.4 still own bedside/capture/occupational method; sample monitoring; the audit sample at step 6", "responsible": "Named lead holds the patient-safety list; owning clinical documents remain; quality or accreditation coordinator audits"}, {"oe_code": "PSQ.2.e", "requirement": "Data is regularly verified by the quality team and is analysed to identify the opportunities for improvement.", "steps": "Steps 5, 1, 6", "evidence": "The written verification and analysis method and regular interval; sample verified datasets and analyses that produced opportunities handed to PSQ.1; the audit sample at step 6 of verified rather than dashboard-only data", "responsible": "Quality team verifies and analyses; PSQ.1 receives opportunities; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. PSQ.2 standard text and OEs a (printed p.102 / index 108) and b-e (printed p.103 / index 109) were read from the official SHCO 3rd Edition PDF, Chapter 6. Header: "The organisation identifies key indicators to monitor the structures, processes and outcomes which are used as tools for continual improvement." PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Commitment, b Core, c Commitment, d Core, e Commitment.
   NO OE CARRIES THE ASTERISK. Whole standard is Tier 2. TIER1_OES = [].
   This is PSQ, not 2nd Edition CQI.

TIERING UNDER THE STANDING RULE
1. Whole standard is Tier 2. Shallower treatment of the WHOLE STANDARD is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. T2 quick check (2026-08-17). PSQ.1 programmes vs these indicators -- flagged. HIC.5 surveillance method vs PSQ.2.b IC indicators -- flagged. Historical HIC.1/HIC.3 "belongs to CQI" -- flagged, not patched. COP.12 / MOM.7 / COP.5 as source rates -- flagged. Annexure 1 as framework not mandate -- stated. ROM/FMS managerial ledger -- flagged.

STATUTORY AND EXTERNAL FACTS
3. No named Act. P2 accreditation-only. Donabedian ch 6, Dimick ch 5, Jones ch 18 -- frameworks.
4. NO NUMBERS ARE STATED as NABH-mandated indicator values.

EDITORIAL POSITIONS TAKEN
5. Annexure 1 is a framework, not a mandated paste. Unused ICU SMR is a recorded absence.
6. PSQ.2.b uses HIC.5 figures; it does not take surveillance method from HIC.5.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
7. make_disclaimer_accreditation_only(). AAC.1 defaulted-statute bug refused.

DELIBERATELY NOT INCLUDED
- Safety/QI programme method -- PSQ.1. Clinical audit -- PSQ.3. HAI case definitions -- HIC.5.
- A mandated paste of Annexure 1. A 2nd Edition CQI indicator file.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 11 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 9 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 11; a search for "Hospital to define" without brackets finds all 11, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: clinical indicators; IC indicators; managerial indicators; patient-safety indicators; verification/analysis method; named lead; audit interval; review interval; intranet location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
