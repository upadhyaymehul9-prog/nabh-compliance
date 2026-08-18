-- ROM.4 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 7 ROM, printed page 111
-- (PDF page index 117). TWO OEs CARRY THE ASTERISK -- ROM.4.a, c.
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
  'ROM.4',
  'ROM',
  array['ROM.4.a', 'ROM.4.b', 'ROM.4.c', 'ROM.4.d', 'ROM.4.e'],
  $q$Patient Safety and Risk Management as Integral to Care and Hospital Management$q$,
  $q$This document sets out how management at {{HOSPITAL_NAME}} ensures that patient-safety aspects and risk-management issues are an integral part of patient care and hospital management: how management ensures proactive risk management across the organisation; how it ensures integration between quality improvement, risk management and strategic planning; how it ensures implementation of systems for internal and external reporting of system and process failures; how it ensures documented agreements for all outsourced services that include service parameters; and how it monitors the quality of outsourced services and makes improvements as required.

The chapter intent is that leaders ensure patient-safety and risk-management issues are integral to care and to hospital management. A risk register that lives only in the quality office, or an outsourcing handshake with no service parameters, is not that intent.

This document is management's duty that those systems exist and are integral. It is not the patient-safety programme (PSQ.1), not the incident system (PSQ.5), not bedside vulnerable-patient programmes (COP.12), and not FMS facility-risk rounds.$q$,
  $q$This policy applies to management at {{HOSPITAL_NAME}}, to the people who operate organisation-wide risk management, to those who report system and process failures internally and externally, and to those who contract and monitor outsourced services.

It covers: proactive risk management across the organisation; integration of QI, risk management and strategic planning; systems for internal and external reporting of system and process failures; documented outsourcing agreements that include service parameters; and monitoring of outsourced quality with improvement.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- PSQ.1.c (sibling branch cursor/draft-psq1-psq5-unapproved-9324) is quality-system proactive analysis of patient-safety risks. THIS document's ROM.4.a is management ensuring proactive risk management across the organisation (care and hospital management, not only the quality file). PSQ.1.c does not become this duty, and this duty does not rewrite PSQ.1.c method. HANDOFF ACCEPTED.
- COP.12 owns bedside identification of the vulnerable patient, falls, pressure ulcers, thrombosis and restraint. Those programmes remain COP.12. Organisation-wide management risk here may use their rates as inputs. It does not rewrite the bedside tools. HANDOFF ACCEPTED from the COP.12/PSQ.1.c/ROM.4 split already logged.
- FMS (not yet drafted) owns facility inspection rounds, fire and non-fire emergencies, hazardous materials and medical-equipment risk as facility work. This document owns that management ensures proactive risk management including those domains as a management duty. It does not write the fire plan.
- PSQ.5 owns the incident management system (capture, sentinel identification, analysis, CAPA, informing stakeholders). THIS document's ROM.4.c is management ensuring systems for internal and external reporting of system and process failures — the governance duty that those systems are implemented. PSQ.5 is the incident SOP those reports use. ROM.4.c must not silently become that SOP. HANDOFF ACCEPTED.
- PRE.6 (sibling branch) owns patient/family complaint redressal. A complaint may describe a process failure; redressal remains PRE.6; this OE is reporting of system and process failures as a management system.
- MOM.7 owns medication-event capture. Dual entry with PSQ.5 when the event is also an incident. This document does not capture the medication event.
- PSQ.1 owns the QI programme. ROM.3.a owns approval of strategic plans. THIS document's ROM.4.b owns that management ensures integration between QI, risk management and strategic planning. It does not rewrite PSQ.1 or ROM.3.a.
- PSQ.4 owns culture of safety and earmarked funds. Culture is not this risk register. Funds for risk work may be earmarked there; the risk duty is here.
- AAC.1 unused services: an unused outsourced ICU is a recorded absence, not a copied SLA.
- ISO 31000:2018 (chapter reference 38), Alam (chapter reference 1) and Kaya et al. (chapter reference 26) are frameworks for risk management. They are not a mandate to be ISO-certified or to paste a named FMEA form.
- Indian Contract Act, 1872 is not a numbered ROM chapter reference and is not in paragraph 2. Outsourcing agreements are accreditation method with service parameters; the hospital's own counsel owns contract law.$q$,
  $q${{HOSPITAL_NAME}} requires management to ensure proactive risk management across the organisation.

{{HOSPITAL_NAME}} requires management to ensure integration between quality improvement, risk management and strategic planning within the organisation.

{{HOSPITAL_NAME}} requires management to ensure implementation of systems for internal and external reporting of system and process failures.

{{HOSPITAL_NAME}} requires management to ensure documented agreements for all outsourced services that include service parameters.

{{HOSPITAL_NAME}} monitors the quality of outsourced services and makes improvements as required.

{{HOSPITAL_NAME}} does not treat a quality-office risk register unused on the wards, or a handshake with no service parameters, as that duty.$q$,
  array[
    $s$1. Proactive risk management across the organisation

Management ensures proactive risk management across the organisation. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask what risks management looks at before harm, across the organisation, and what changed. The answer must be a management-owned system that covers patient care and hospital management, not PSQ.1.c's quality-system analysis counted twice, and not COP.12's bedside falls tool counted as organisation-wide risk.

The reason this is the management step is that the chapter intent makes patient-safety and risk-management issues integral to care and to hospital management. PSQ.1.c analyses patient-safety risks as a quality-system act. COP.12 identifies a vulnerable patient at the bedside. FMS (when drafted) inspects the facility. This OE is that management ensures a proactive risk system that takes those inputs — and other domains this hospital actually runs — and acts before harm. The common error is one FMEA workshop in the quality office, or a copied ISO 31000 manual with no named owner.

How management ensures proactive risk management across the organisation (scope across care and hospital management, who owns it, how often, how an improvement is recorded), is [Hospital to define — how management ensures proactive risk management across the organisation]. ISO 31000:2018 (chapter reference 38), Alam (chapter reference 1) and Kaya et al. (chapter reference 26) are frameworks, not a certified-system mandate and not a pasted FMEA form. A service the directory does not provide is a recorded absence.$s$,
    $s$2. Integration of quality improvement, risk management and strategic planning

Management ensures integration between quality improvement, risk management and strategic planning within the organisation.

How that integration is shown — that a strategic plan (ROM.3.a), a QI programme (PSQ.1) and this risk system talk to each other rather than three unrelated files — is [Hospital to define — how management ensures integration between quality improvement, risk management and strategic planning]. This step does not rewrite PSQ.1 or ROM.3.a.$s$,
    $s$3. Systems for internal and external reporting of system and process failures

Management ensures implementation of systems for internal and external reporting of system and process failures. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask what is reported internally, what is reported externally, and that management ensured those systems exist. The answer must be implemented systems, not a sentence in this policy, and not PSQ.5's incident SOP offered as the whole of this OE.

The reason this is distinct from PSQ.5 is that the book splits them. PSQ.5 is the incident management system: what counts as an incident, sentinel identification, analysis, CAPA, informing stakeholders of a near miss, adverse event or sentinel event. This OE is management ensuring systems for reporting system and process failures internally and externally — a governance duty that reporting happens, including failures that may not be coded as a clinical incident. The common error is to file only sentinel events with NABH's assessment team and call that the system, or to leave external reporting only with whichever specialty document already names a regulator.

What counts as a system or process failure for this OE, the internal reporting route, the external reporting route (which bodies this hospital has defined, including any statutory report that already lives in an owning document), and how management ensures those systems are implemented, are [Hospital to define — the systems for internal and external reporting of system and process failures, and how management ensures they are implemented]. PSQ.5 remains the incident SOP. PRE.6 remains complaint redressal. MOM.7 remains medication-event capture. HIC.4 needlestick and HIC.5 HAI case-finding remain those documents. Dual entry when the same event meets more than one definition. This document does not print a mandatory 24-hour NABH clock or a named regulator as a universal mandate.$s$,
    $s$4. Documented agreements for outsourced services, including service parameters

Management ensures that it has a documented agreement for all outsourced services that include service parameters.

Which services are outsourced, the documented agreement for each, and which service parameters it contains, are [Hospital to define — the documented agreements for outsourced services, including service parameters]. A service this hospital does not outsource is a recorded absence. A handshake, or a rate card with no service parameters, is not this OE. Indian Contract Act 1872 is not imported as a NABH mandate.$s$,
    $s$5. Monitoring quality of outsourced services and improvement

Management monitors the quality of the outsourced services and improvements are made as required.

How quality is monitored, how often, and how an improvement is recorded, are [Hospital to define — how the quality of outsourced services is monitored and how improvements are made]. Monitoring uses the service parameters at step 4. HIC.6/AAC.4/AAC.5 remain the owning method where the outsourced work is CSSD, laboratory or imaging.$s$,
    $s$6. Records, review and the order of operations

The organisation-wide risk system and its actions, the record of QI–risk–strategy integration, internal and external failure-reporting systems and sample reports, outsourcing agreements with service parameters, and outsourced-quality monitoring with improvements, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for management risk and outsourcing records] for: proactive risk that is management-owned across the organisation rather than only PSQ.1.c or only COP.12; integration with PSQ.1 and ROM.3.a rather than three unrelated files; failure-reporting systems implemented rather than PSQ.5 counted as this whole OE; outsourcing agreements that include service parameters; monitoring that produced an improvement; and no ISO certificate counted as implementation without the work.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a process failure was never reported, or when PSQ.1, PSQ.5, COP.12, ROM.3 or FMS that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable that management ensures the duties in this document.

Those responsible for governance (ROM.1) receive reporting of system and process failures as this hospital has defined that internal route, and they approve strategy (ROM.3.a) that this step 2 must integrate with.

Named leads operate the risk system, the failure-reporting systems, and outsourcing contracts as this hospital has defined them.

PSQ.1, PSQ.5, COP.12, MOM.7, PRE.6, HIC.4, HIC.5 and FMS (when drafted) remain the owning methods named in Scope.

The quality or accreditation coordinator audits the records at step 6.

All staff are expected to treat a quality-office risk file unused on the wards, an incident that never entered PSQ.5, and an outsourced service with no service parameters, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 7 ROM, standard ROM.4.
- Risk management -- Guidelines. ISO 31000:2018. International Organization for Standardization — chapter reference 38; framework, not a certified-system mandate.
- Alam, A. Y. (2016). Steps in the Process of Risk Management in Healthcare. Journal of Epidemiology and Preventive Medicine, 02(02) — chapter reference 1; framework.
- Kaya, G. K., Ward, J. R., & Clarkson, P. J. (2018). A framework to support risk assessment in hospitals. International Journal for Quality in Health Care, 31(5), 393-401 — chapter reference 26; framework.
- Kuhn, A. M. (2002). The need for risk management to evolve to assure a culture of safety. Quality and Safety in Health Care, 11(2), 158-162 — chapter reference 28; framework.
- Internal documents of {{HOSPITAL_NAME}}: the organisation-wide risk system; failure-reporting systems; outsourcing agreements; PSQ.1, PSQ.4, PSQ.5; COP.12; ROM.1, ROM.3; AAC.1.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with those responsible for governance and the quality or accreditation coordinator.

Copies issued to: named risk and outsourcing leads; department heads who report process failures.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder].

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

ROM — Responsibilities of Management (SHCO 3rd Edition Chapter 7)
QI — quality improvement
SLA — service-level agreement (used only if this hospital's outsourcing agreement uses that term)
ISO — International Organization for Standardization

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

The requirements in this document are accreditation requirements of the NABH SHCO 3rd Edition rather than duties under a named Act of Parliament. In particular those arising under no named Act of Parliament; the duties in this document are accreditation requirements of the NABH SHCO 3rd Edition are written here as accreditation method, not as a copied statute. This policy does not import the Consumer Protection Act, 2019, the Clinical Establishments Act, 2010, or the Mental Healthcare Act, 2017 as a checklist. Statutory duties that arise under other documents of {{HOSPITAL_NAME}} remain those documents. {{HOSPITAL_NAME}} is responsible for verifying any statutory duty that applies to it; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "ROM.4.a", "requirement": "Management ensures proactive risk management across the organisation.", "steps": "Steps 1, 6", "evidence": "The written organisation-wide proactive risk system showing management ownership across patient care and hospital management rather than a quality-office file unused on the wards; sample analyses that produced an improvement before harm; the recorded splits that PSQ.1.c owns quality-system patient-safety analysis, COP.12 owns bedside vulnerable/falls/PU/VTE tools, FMS (when drafted) owns facility rounds, and PSQ.5 owns after-the-fact incidents; the recorded use of ISO 31000:2018, Alam and Kaya (chapter references 38, 1 and 26) as frameworks not a certified-system or named-FMEA mandate; induction or briefing of named risk leads; the location of the system; the audit sample at step 6 of management-owned proactive work rather than one workshop", "responsible": "Head of the institution is accountable; named risk lead operates the system; PSQ.1.c/COP.12/PSQ.5/FMS remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "ROM.4.b", "requirement": "Management ensures integration between quality improvement, risk management and strategic planning within the organisation.", "steps": "Steps 2, 1, 6", "evidence": "The recorded method of integration and sample minutes or plans showing QI (PSQ.1), risk (this document) and strategy (ROM.3.a) talking to each other rather than three unrelated files; the audit sample at step 6", "responsible": "Head of the institution ensures integration; PSQ.1 and ROM.3.a remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "ROM.4.c", "requirement": "Management ensures implementation of systems for internal and external reporting of system and process failures.", "steps": "Steps 3, 6", "evidence": "The written internal and external reporting systems for system and process failures showing implementation (sample reports that left the organisation or reached governance) rather than a sentence in this policy; the recorded split that PSQ.5 is the incident SOP those clinical incidents use, PRE.6 is complaint redressal, MOM.7 is medication-event capture, and HIC.4/HIC.5 remain needlestick and HAI case-finding; the recorded refusal to print a mandatory 24-hour NABH clock or a universal named regulator; induction or briefing of staff who report failures; the location of the systems; the audit sample at step 6 of reports that actually travelled internally and, where defined, externally", "responsible": "Head of the institution ensures the systems are implemented; named reporters use them; PSQ.5/PRE.6/MOM.7/HIC remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "ROM.4.d", "requirement": "Management ensures that it has a documented agreement for all outsourced services that include service parameters.", "steps": "Steps 4, 6", "evidence": "The list of outsourced services against AAC.1 and the documented agreement for each including service parameters; recorded absences where nothing is outsourced; the recorded refusal to import Indian Contract Act 1872 as a NABH mandate; the audit sample at step 6", "responsible": "Head of the institution ensures agreements exist; named contracting lead holds them; quality or accreditation coordinator audits"}, {"oe_code": "ROM.4.e", "requirement": "Management monitors the quality of the outsourced services and improvements are made as required.", "steps": "Steps 5, 4, 6", "evidence": "Sample monitoring against the service parameters at step 4 and recorded improvements; the recorded split that HIC.6/AAC.4/AAC.5 own method where the work is CSSD, laboratory or imaging; the audit sample at step 6", "responsible": "Named monitor; owning clinical/IPC documents remain those methods; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. ROM.4 standard text and all five OEs were read from the official SHCO 3rd Edition PDF, Chapter 7, printed page 111 (PDF page index 117). Header: "Management ensures that patient-safety aspects and risk-management issues are an integral part of patient care and hospital management." PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Core, b Excellence, c Commitment, d Core, e Achievement.
   TWO OEs CARRY THE ASTERISK -- ROM.4.a and ROM.4.c. b, d, e are unasterisked (Tier 2). ROM.4.d is Core and still Tier 2 because it is unasterisked.
   Asterisks verified 2026-08-17 against the page and scripts/shco_oe_asterisks.json.

TIERING UNDER THE STANDING RULE
1. TWO OF FIVE OEs ARE TIER 1. Tier 1: a, c -- steps 1 and 3 carry the reasoning. Tier 2: b, d, e. Shallower treatment of b/d/e is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of ROM.4.a/c against PSQ.1.c, PSQ.5, COP.12, MOM.7, PRE.6, HIC.4/HIC.5.
   PSQ.1.c quality-system analysis vs this management risk duty -- HANDOFF ACCEPTED. Stated in Scope and step 1.
   COP.12 bedside programmes vs this organisation-wide duty -- HANDOFF ACCEPTED.
   PSQ.5 incident SOP vs ROM.4.c governance reporting systems -- HANDOFF ACCEPTED. Stated in Scope and step 3.
   PRE.6 complaints, MOM.7 medication events -- dual entry when definitions overlap; methods stay there.
3. FORWARD REFERENCES: FMS facility risk rounds; HRM not this document.
4. T2 QUICK CHECK: ROM.4.b vs PSQ.1 / ROM.3.a -- flagged. ROM.4.d/e outsourcing vs AAC.4/AAC.5/HIC.6 method -- flagged. AAC.1 unused outsourced services -- flagged.

STATUTORY AND EXTERNAL FACTS
5. No named Act is a numbered ROM chapter reference. P2 is accreditation-only. Indian Contract Act 1872 is not imported. ISO 31000:2018 is a framework, not a certification mandate.
6. Alam / Kaya / Kuhn -- frameworks, not pasted tools.
7. NO NUMBERS ARE STATED as requirements. No 24-hour NABH reporting clock.

EDITORIAL POSITIONS TAKEN
8. Accepting PSQ.1.c / COP.12 / PSQ.5 forward-refs without absorbing their methods.
9. Distinguishing ROM.4.c from PSQ.5 is required by two OEs in two chapters.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
10. P1/P3/P4 shared. P2 uses make_disclaimer_accreditation_only().

DELIBERATELY NOT INCLUDED
- PSQ.1 programme method. PSQ.5 incident SOP. COP.12 bedside tools. FMS fire plan.
- A named FMEA form. An ISO certificate as a substitute for the work. Indian Contract Act in P2.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 10 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 8 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 10; a search for "Hospital to define" without brackets finds all 10, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: organisation-wide proactive risk method; QI–risk–strategy integration method; internal and external failure-reporting systems; outsourcing agreements and parameters; outsourced-quality monitoring; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "17-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
