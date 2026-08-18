# -*- coding: utf-8 -*-
"""Builds the PSQ.1 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase until the
owner confirms.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

THIS CHAPTER IS PSQ (Patient Safety and Quality Improvement) in the SHCO 3rd
Edition. It replaced the 2nd Edition chapter titled Continuous Quality
Improvement (CQI). The two are not interchangeable. This draft is sourced
only from Chapter 6 of the 3rd Edition PDF.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): PSQ.1.a, PSQ.1.g, PSQ.1.h, PSQ.1.i
  Tier 2 (lighter pass):   PSQ.1.b, PSQ.1.c, PSQ.1.d, PSQ.1.e, PSQ.1.f

FOUR of nine OEs are asterisked. The draft builds deep blocks for a, g, h and i.
b-f are lean.

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 6 Patient Safety and Quality Improvement, standard
PSQ.1 and OEs PSQ.1.a-i, printed page 102, PDF page index 108. Chapter intent
and summary: printed page 101, PDF page index 107. References: printed pages
105-108, PDF indices 111-114.

Asterisks verified 2026-08-17: scripts/asterisk_extract.py against that PDF
(408 OEs, 132 asterisks, PSQ 28 OEs / 6 asterisks) and the PSQ.1 page read
directly. PSQ.1.a, PSQ.1.g, PSQ.1.h and PSQ.1.i carry the asterisk.

No named Act of Parliament is a numbered PSQ chapter reference.
"""
from policy_build_common import emit_and_verify, make_disclaimer_accreditation_only

STANDARD_CODE = "PSQ.1"
CHAPTER = "PSQ"
OE_CODES = [
    "PSQ.1.a", "PSQ.1.b", "PSQ.1.c", "PSQ.1.d", "PSQ.1.e",
    "PSQ.1.f", "PSQ.1.g", "PSQ.1.h", "PSQ.1.i",
]
TIER1_OES = ["PSQ.1.a", "PSQ.1.g", "PSQ.1.h", "PSQ.1.i"]

POLICY_TITLE = "Patient Safety Programme and Structured Quality Improvement Programme"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} develops, implements and maintains a patient-safety programme through a multi-disciplinary committee; how that programme identifies opportunities for improvement on review at pre-defined intervals; how the organisation performs proactive analysis of patient-safety risks and improves accordingly; how it adapts and implements national or international patient-safety goals or solutions; how a comprehensive quality-improvement programme is likewise developed, implemented and maintained by a multi-disciplinary committee, with a designated individual to coordinate it, and with review at pre-defined intervals; how audits are conducted at regular intervals as continuous monitoring; and how there is an established process to monitor and improve the quality of nursing care.

The chapter intent is an environment of patient safety and continual quality improvement, documented, involving all areas and all staff. A committee that meets once to adopt a downloaded plan, or a quality file that never changes what happens on the ward, is not that intent.

This document is the hospital-wide patient-safety and quality-improvement programmes. It is not the intensive-care quality-assurance programme, the theatre quality-assurance programme, HAI surveillance method, or the incident-management system. Those remain the documents that own them."""

SCOPE = """This policy applies to every area of {{HOSPITAL_NAME}} and to every staff member the programmes cover. It binds the multi-disciplinary committees, the designated quality-improvement coordinator, the people who audit, and the people who monitor nursing-care quality.

It covers: the patient-safety programme (committee, review, proactive risk analysis, adapted safety goals/solutions); the comprehensive quality-improvement programme (committee, designated individual, review); audits as continuous monitoring; and the process to monitor and improve quality of nursing care.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- Key indicators as tools for continual improvement are governed by PSQ.2 (sibling). This document owns the programmes that use those indicators. PSQ.2 owns which indicators are identified and monitored.
- Clinical audit and quality-improvement projects are governed by PSQ.3 (sibling). PSQ.1.h is audit as continuous monitoring of the programmes. PSQ.3 is clinical audit of patient care and named QI projects. They are not the same act.
- Management support, culture of safety, resources and workforce feedback are governed by PSQ.4 (sibling). This document owns the programmes; PSQ.4 owns that management supports them.
- Incident management, sentinel events, analysis, CAPA and informing stakeholders are governed by PSQ.5 (sibling). A finding from proactive analysis or from an audit may generate an incident; the incident system is PSQ.5.
- Intensive-care quality assurance is COP.6.d. Theatre quality assurance is COP.11.h. Those are unit programmes. This document is hospital-wide. Unit QA feeds this programme; it does not replace it, and this programme does not rewrite those unit methods.
- HAI surveillance method (case definitions, device-days, rates) is HIC.5. Infection-control practices are HIC.2/HIC.4. This document may use HIC figures as inputs. It does not redefine NHSN-style surveillance. Historical drafts that pointed HAI surveillance method at "CQI" were pointing at a 2nd Edition chapter name; under the 3rd Edition that method is HIC.5, and hospital-wide indicator monitoring of infection-control activities is PSQ.2.b, not this programme document.
- Vulnerable-patient, falls, pressure-ulcer and thrombosis programmes are COP.12. Proactive analysis of patient-safety risks here (PSQ.1.c) is organisation-level analysis, not the bedside identification COP.12 owns.
- Medication-error capture is MOM.7. This programme may review MOM.7 rates; it does not capture the event.
- Nursing assignment and nursing process are COP.4. PSQ.1.i owns monitoring and improving quality of nursing care as a quality-system process, not rewriting how a nurse is assigned.
- Patient-safety goals/solutions adapted here are not a second identity-check SOP (COP.1), a second injection-safety SOP (HIC.2), or a second medication-administration SOP (MOM.6). Those documents own the clinical method. This step owns that the hospital has adapted named goals/solutions and can show implementation.
- Organisation-wide risk management as a management duty is ROM.4 (not yet drafted). PSQ.1.c is the quality-system proactive analysis. ROM.4 must not silently become this analysis, and this analysis must not claim to be governance risk management.
- This chapter is PSQ, not CQI. Do not title, code or cite this document as Continuous Quality Improvement."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} develops, implements and maintains a patient-safety programme through a multi-disciplinary committee.

{{HOSPITAL_NAME}} reviews that programme at pre-defined intervals and identifies opportunities for improvement.

{{HOSPITAL_NAME}} performs proactive analysis of patient-safety risks and makes improvement accordingly.

{{HOSPITAL_NAME}} adapts and implements national or international patient-safety goals or solutions.

{{HOSPITAL_NAME}} develops, implements and maintains a comprehensive quality-improvement programme through a multi-disciplinary committee, with a designated individual to coordinate and implement it, and reviews that programme at pre-defined intervals.

{{HOSPITAL_NAME}} conducts audits at regular intervals as continuous monitoring.

{{HOSPITAL_NAME}} has an established process to monitor and improve the quality of nursing care.

{{HOSPITAL_NAME}} does not treat a downloaded plan, a committee that never meets, or a 2nd Edition "CQI" file retitled in ink, as these programmes."""

PROCEDURE_STEPS = [
"""1. Patient-safety programme developed, implemented and maintained by a multi-disciplinary committee

The patient safety programme is developed, implemented and maintained by a multi-disciplinary committee. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask who sits on the committee, what the programme actually does, and whether last month's work was the committee's or a quality officer's private file. The answer must be a living programme this hospital uses, not a 2nd Edition CQI manual with the cover changed to PSQ.

The reason this is the safety step is that patient safety that lives only with one coordinator is not a programme the chapter intent describes. The intent requires documentation and involvement of all areas and all staff. The common error is a committee whose minutes are apologies for absence, or a membership list of every head of department who never attends, counted as multi-disciplinary.

Who sits on the committee, how often it meets, what written programme it maintains, and how implementation is evidenced in the areas this hospital actually runs, are [Hospital to define — the multi-disciplinary patient-safety committee (membership, meeting interval) and the written patient-safety programme it develops, implements and maintains]. A service the directory does not provide is a recorded absence, not a copied ICU safety SOP. WHO Patient Safety Solutions (chapter reference 27) and Leotsakos et al. on the WHO High 5s project (chapter reference 22) are frameworks for what a safety programme can contain; they are not pasted as this hospital's programme.

Implementation means the programme changes work: a goal adopted at step 4, a risk from step 3 acted on, an audit from step 7 that produced a change. Maintenance means the committee still owns it after the first year.""",

"""2. Patient-safety programme review at pre-defined intervals

The patient-safety programme identifies opportunities for improvement based on review at pre-defined intervals.

The interval, who reviews, and how opportunities are recorded, are [Hospital to define — the pre-defined interval at which the patient-safety programme is reviewed and how opportunities for improvement are recorded]. A review that only restates the programme text is not this OE.""",

"""3. Proactive analysis of patient-safety risks

The organisation performs proactive analysis of patient safety risks and makes improvement accordingly.

How that analysis is done (for example a periodic look at a process before harm, not only after an incident), which processes are in scope, and how an improvement is recorded, are [Hospital to define — how proactive analysis of patient-safety risks is performed and how resulting improvements are recorded]. This is organisation-level analysis. Bedside identification of a vulnerable patient, a fall risk or a pressure-ulcer risk remains COP.12. Incident investigation after the fact remains PSQ.5. Organisation-wide risk management as a management duty remains ROM.4 when drafted. AHRQ Detection of Safety Hazards (chapter reference 4) and NEJM Catalyst on risk management in healthcare (chapter reference 48) are frameworks, not pasted tools. This document does not print a named FMEA form as a NABH mandate.""",

"""4. National or international patient-safety goals or solutions

The organisation adapts and implements national/international patient-safety goals/solutions.

Which goals or solutions this hospital has adapted, how they are implemented here, and how that is recorded, are [Hospital to define — which national or international patient-safety goals or solutions this hospital adapts and how they are implemented]. Adaptation means this hospital chose and fitted them to the services it actually runs. Implementation is shown in the owning clinical or IPC documents (for example identity COP.1, injection safety HIC.2, medication administration MOM.6), not by reprinting those methods here. WHO Patient Safety Solutions (chapter reference 27) is a framework, not a mandated nine-item paste.""",

"""5. Comprehensive quality-improvement programme and designated coordinator

A comprehensive quality improvement programme is developed, implemented and maintained by a multi-disciplinary committee. There is a designated individual for coordinating and implementing the quality improvement programme.

The QI committee (it may be the same body as step 1, or a distinct body — the hospital says which), the written QI programme, and the named coordinator, are [Hospital to define — the multi-disciplinary quality-improvement committee, the written comprehensive QI programme, and the designated individual who coordinates and implements it]. Comprehensive means it covers the hospital, not a single ward project. PSQ.3 owns named QI projects and clinical audit; this step owns the programme those projects sit inside. IHI Quality Improvement Essentials Toolkit (chapter reference 28) and Hughes on tools and strategies (chapter reference 15) are frameworks, not pasted protocols.""",

"""6. Quality-improvement programme review at pre-defined intervals

The quality improvement programme identifies opportunities for improvement based on review at pre-defined intervals. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask when the QI programme was last reviewed and what changed. The answer must be a dated review that produced an opportunity, not the same PDF reprinted annually.

The reason this is written separately from step 5 is that a programme that is never reviewed is a filing exercise. Step 2 reviews the patient-safety programme. This step reviews the QI programme. They may share a meeting; the minutes must show both, or two reviews. The common error is one "quality meeting" that never distinguishes safety-programme review from QI-programme review, so neither OE can be shown.

The interval, who reviews, and how opportunities are recorded, are [Hospital to define — the pre-defined interval at which the quality-improvement programme is reviewed and how opportunities for improvement are recorded]. PSQ.2.e (data verification and analysis) feeds this review; it does not replace it.""",

"""7. Audits at regular intervals as continuous monitoring

Audits are conducted at regular intervals as a means of continuous monitoring. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask which audits ran, at what interval, and what they monitored. The answer must be a schedule this hospital kept, not a single mock audit before assessment, and not clinical audit (PSQ.3) counted twice.

The reason this is distinct from PSQ.3 is that the book splits them. PSQ.1.h is audit as continuous monitoring of the safety and QI programmes — process, documentation, implementation. PSQ.3 is clinical audit of patient care against defined parameters, with medical and nursing participation and remedial measures. Using one file for both leaves one OE empty. The common error is to call every checklist an audit, or to paste a clinical-audit calendar here.

Which audits, the regular interval, who conducts them, and how findings enter the programmes at steps 1 and 5, are [Hospital to define — which audits are conducted at regular intervals as continuous monitoring, who conducts them, and how findings feed the patient-safety and QI programmes]. Unit QA (COP.6.d, COP.11.h) remains those unit programmes; their findings may be inputs. This step does not rewrite them.""",

"""8. Process to monitor and improve quality of nursing care

There is an established process in the organisation to monitor and improve quality of nursing care. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask how nursing-care quality is monitored and what improved. The answer must be a process used on the wards, not a COP.4 assignment roster counted as quality monitoring, and not an infection-control hand-hygiene rate counted as the whole of nursing quality.

The reason this is written separately is that nursing care is the work most patients actually receive, and a hospital-wide QI programme that never looks at it is not comprehensive. COP.4 owns how nursing care is assigned and documented as a care process. This step owns monitoring and improving its quality. The common error is to treat nurse-patient ratios, or a single indicator, as the process.

How quality of nursing care is monitored, by whom, which aspects, how improvement is recorded, and how it reports into the QI programme, are [Hospital to define — the established process to monitor and improve quality of nursing care]. This document does not print a named nursing-audit tool as a NABH mandate.""",

"""9. Records, review and the order of operations

The patient-safety programme and committee records, QI programme and coordinator records, review minutes, audit schedule and reports, and nursing-care quality monitoring records, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for patient-safety and QI programme records] for: a multi-disciplinary safety committee that implements, not only lists members; safety-programme review at the defined interval; proactive analysis that produced improvement; adapted goals/solutions implemented in owning clinical documents rather than reprinted here; a QI programme with a named coordinator; QI-programme review distinct enough to show; monitoring audits that are not only PSQ.3 clinical audits; a nursing-care quality process that is not only COP.4 assignment; and no file titled CQI offered as this 3rd Edition PSQ programme.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a committee existed only on paper, or a 2nd Edition CQI document was offered as PSQ.1, or when PSQ.2–5, COP.4, COP.6, COP.11, COP.12, HIC.5 or MOM.7 that this document hands work to are revised.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} maintaining a patient-safety programme and a comprehensive quality-improvement programme under this document.

The multi-disciplinary patient-safety committee owns the safety programme at steps 1-4. The multi-disciplinary QI committee owns the QI programme at steps 5-6. If they are the same body, minutes still show both functions.

The designated individual for coordinating and implementing the QI programme is named at step 5.

Nursing leadership operates the nursing-care quality process at step 8.

The quality or accreditation coordinator audits the records at step 9 and reports findings to the head of the institution.

All staff are expected to treat a paper committee, a monitoring audit that is only a clinical-audit file, and a document coded CQI offered as this programme, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Safety and Quality Improvement chapter (Chapter 6), standard PSQ.1. This is not the 2nd Edition Continuous Quality Improvement (CQI) chapter.
- Patient Safety Solutions (2017). World Health Organization — chapter reference 27; used as a framework for adapted goals/solutions; not pasted as a mandated list.
- Leotsakos, A., et al. (2014). Standardization in patient safety: the WHO High 5s project. International Journal for Quality in Health Care, 26(2), 109-116 — chapter reference 22; framework, not pasted.
- Quality Improvement Essentials Toolkit. Institute for Healthcare Improvement — chapter reference 28; framework for the QI programme, not pasted as a protocol.
- Hughes, R. (2008). Tools and Strategies for Quality Improvement and Patient Safety. In Patient Safety and Quality: An Evidence-based Handbook for Nurses — chapter reference 15; framework.
- Detection of Safety Hazards (2019). AHRQ Patient Safety Primers — chapter reference 4; framework for proactive analysis.
- Internal documents of {{HOSPITAL_NAME}}: the patient-safety programme; the QI programme; committee terms and minutes; the designated coordinator's role; the monitoring-audit schedule; the nursing-care quality process; PSQ.2–5; COP.4, COP.6, COP.11, COP.12; HIC.5; MOM.7."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: the patient-safety and QI committees; nursing administration; every in-patient ward; and the designated QI coordinator.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The written programmes — the working documents this policy requires — are held where the committees work.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

PSQ — Patient Safety and Quality Improvement (SHCO 3rd Edition Chapter 6; not CQI)
QI — quality improvement
CQI — Continuous Quality Improvement (SHCO 2nd Edition chapter name only; not a code in this edition)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PSQ.1.a",
        "requirement": "The patient safety programme is developed, implemented and maintained by a multi-disciplinary committee.",
        "steps": "Steps 1, 2, 9",
        "evidence": "The written patient-safety programme and the multi-disciplinary committee's current membership, meeting interval and minutes showing the committee develops, implements and maintains the programme rather than a quality officer's private file or a 2nd Edition CQI manual retitled PSQ; sample implementation in areas this hospital actually runs, with a recorded absence against the service directory for a service it does not provide; the recorded use of WHO Patient Safety Solutions and High 5s (chapter references 27 and 22) as frameworks not pasted programmes; induction or briefing of committee members; the location of the programme; the audit sample at step 9 of a living committee rather than a membership list of absentees",
        "responsible": "Multi-disciplinary patient-safety committee owns the programme; head of the institution is accountable; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.1.b",
        "requirement": "The patient-safety programme identifies opportunities for improvement based on review at pre-defined intervals.",
        "steps": "Steps 2, 1, 9",
        "evidence": "The written pre-defined review interval; sample reviews that recorded opportunities rather than restating the programme text; the audit sample at step 9",
        "responsible": "Patient-safety committee reviews; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.1.c",
        "requirement": "The organisation performs proactive analysis of patient safety risks and makes improvement accordingly.",
        "steps": "Steps 3, 9",
        "evidence": "The written proactive-analysis method; sample analyses that produced an improvement; the recorded split that COP.12 owns bedside vulnerable/falls/PU identification, PSQ.5 owns after-the-fact incident analysis, and ROM.4 will own management risk duty; the audit sample at step 9",
        "responsible": "Named lead or committee performs analysis; COP.12/PSQ.5/ROM.4 remain those documents; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.1.d",
        "requirement": "The organisation adapts and implements national/international patient-safety goals/solutions.",
        "steps": "Steps 4, 1, 9",
        "evidence": "The written list of goals/solutions this hospital has adapted, matching services it actually runs; evidence of implementation in owning clinical/IPC documents rather than a reprint of COP.1, HIC.2 or MOM.6; the audit sample at step 9",
        "responsible": "Patient-safety committee adapts; owning clinical/IPC policies implement; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.1.e",
        "requirement": "A comprehensive quality improvement programme is developed, implemented and maintained by a multi-disciplinary committee.",
        "steps": "Steps 5, 6, 9",
        "evidence": "The written comprehensive QI programme and QI committee records (or the same body as step 1 with minutes that show the QI function); the recorded split that PSQ.3 owns named projects and clinical audit; the audit sample at step 9",
        "responsible": "QI committee owns the programme; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.1.f",
        "requirement": "There is a designated individual for coordinating and implementing the quality improvement programme.",
        "steps": "Steps 5, 9",
        "evidence": "The named designated individual and role; sample work showing that person coordinates implementation rather than an unnamed quality office; the audit sample at step 9",
        "responsible": "Designated QI coordinator; QI committee; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.1.g",
        "requirement": "The quality improvement programme identifies opportunities for improvement based on review at pre-defined intervals.",
        "steps": "Steps 6, 5, 9",
        "evidence": "The written pre-defined QI-programme review interval and sample dated reviews that produced an opportunity rather than an annual reprint of the same file; minutes that distinguish this review from the patient-safety-programme review at step 2 even when they share a meeting; the recorded split that PSQ.2.e data analysis feeds this review and does not replace it; the recorded refusal to treat a 2nd Edition CQI annual report as this 3rd Edition OE; induction or briefing of the QI committee on the review method; the location of review records; the audit sample at step 9 of a review that changed the programme",
        "responsible": "QI committee reviews; designated coordinator prepares; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.1.h",
        "requirement": "Audits are conducted at regular intervals as a means of continuous monitoring.",
        "steps": "Steps 7, 9",
        "evidence": "The written monitoring-audit schedule (which audits, regular interval, who conducts) showing continuous monitoring of the safety and QI programmes rather than a single pre-assessment mock audit; sample audit reports whose findings entered the programmes at steps 1 and 5; the recorded split that PSQ.3 owns clinical audit of patient care and that this step is not that file counted twice; the recorded split that COP.6.d and COP.11.h remain unit QA and may feed this step as inputs; the location of the schedule; the audit sample at step 9 of monitoring audits that ran at the stated interval",
        "responsible": "Named auditors conduct monitoring audits; QI/safety committees receive findings; PSQ.3 owns clinical audit; quality or accreditation coordinator audits the schedule",
    },
    {
        "oe_code": "PSQ.1.i",
        "requirement": "There is an established process in the organisation to monitor and improve quality of nursing care.",
        "steps": "Steps 8, 5, 9",
        "evidence": "The written established process to monitor and improve quality of nursing care, showing aspects monitored, who monitors, and recorded improvements, rather than a COP.4 assignment roster or a single HIC hand-hygiene rate counted as the whole process; sample ward records of that monitoring reporting into the QI programme; the recorded split that COP.4 owns nursing assignment and the nursing process as care; the recorded refusal to print a named nursing-audit tool as a NABH mandate; induction or briefing of nursing leads; the location of the process; the audit sample at step 9 of monitoring that produced an improvement",
        "responsible": "Nursing leadership operates the process; QI programme receives findings; COP.4 owns assignment; quality or accreditation coordinator audits",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. PSQ.1 standard text and all nine OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 6 Patient Safety and Quality Improvement, printed page 102 (PDF page index 108). Header: "The organisation implements a patient-safety programme and a structured quality improvement programme." Chapter intent printed page 101 (PDF page index 107). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Core, b Commitment, c Core, d Core, e Core, f Commitment, g Commitment, h Commitment, i Core.
   FOUR OEs CARRY THE ASTERISK -- PSQ.1.a, g, h, i. PSQ.1.b-f are unasterisked (Tier 2).
   Verified 2026-08-17: asterisk_extract.py against the download (408 OEs, 132 asterisks, PSQ 28/6) and the PSQ.1 page read directly.
   EDITION FLAG: the 3rd Edition forward (PDF index 2) states the chapter on Continuous Quality Improvement is now replaced with Patient Safety and Quality Improvement. This draft is PSQ, not CQI.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. FOUR OF NINE OEs ARE TIER 1. Tier 1: a, g, h, i -- steps 1, 6, 7, 8 carry the reasoning. Tier 2: b, c, d, e, f. Shallower treatment of b-f is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of PSQ.1.a/g/h/i against HIC masters and AAC/COP/MOM drafts (PRE drafts exist UNAPPROVED on a sibling branch). Search terms: quality, audit, nursing quality, committee, CQI, patient safety programme.
   PSQ.2 / PSQ.3 / PSQ.4 / PSQ.5 -- siblings. Stated in Scope.
   COP.6.d / COP.11.h -- unit QA vs hospital-wide programme. Stated in Scope and step 7.
   COP.4 -- nursing assignment vs nursing-care quality monitoring. Stated in Scope and step 8.
   HIC.5 -- HAI surveillance method. Historical HIC.1/HIC.3 drafts still say method "belongs to CQI". Under 3rd Edition the method is HIC.5; this programme does not take it. Flagged; HIC.1/HIC.3 not patched in this pass.
3. FORWARD REFERENCES: ROM.4 management risk; PRE.6 complaints (not this programme).
4. T2 QUICK CHECK: PSQ.1.c vs COP.12 vs ROM.4 -- flagged. PSQ.1.d vs COP.1 / HIC.2 / MOM.6 -- flagged. PSQ.1.e vs PSQ.3 projects -- flagged.

STATUTORY AND EXTERNAL FACTS
5. No named Act of Parliament is a numbered PSQ chapter reference. P2 is accreditation-only. CPA/CEA/MHCA are not a checklist. BMW/FSS are not in P2.
6. WHO Patient Safety Solutions, High 5s, IHI QI toolkit, AHRQ safety-hazard primer -- chapter refs 27, 22, 28, 4 -- frameworks, not pasted.
7. NO NUMBERS ARE STATED as requirements. No named FMEA form or nursing-audit tool as a NABH mandate.

EDITORIAL POSITIONS TAKEN
8. Distinguishing PSQ.1.h monitoring audits from PSQ.3 clinical audits is an editorial position required by two OEs in the same chapter.
9. Refusal to treat 2nd Edition CQI documents as this programme is an editorial position required by the owner's instruction that CQI and PSQ are not interchangeable.
10. Same-body-or-two-committees choice at step 5 is left to the hospital.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
11. P1/P3/P4 shared. P2 uses make_disclaimer_accreditation_only(). AAC.1 defaulted-statute bug refused.

DELIBERATELY NOT INCLUDED
- Indicator list -- PSQ.2. Clinical audit and QI projects -- PSQ.3. Management support -- PSQ.4. Incident system -- PSQ.5.
- Unit QA methods -- COP.6.d / COP.11.h. Nursing assignment -- COP.4. HAI surveillance method -- HIC.5.
- A 2nd Edition CQI programme copied forward. A named FMEA or nursing tool as a mandate.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 13 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 11 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 13; a search for "Hospital to define" without brackets finds all 13, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: safety committee and programme; safety-programme review interval; proactive-analysis method; which goals/solutions; QI committee, programme and designated individual; QI-programme review interval; monitoring-audit schedule; nursing-care quality process; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 6 PSQ, printed page 102
-- (PDF page index 108). NOT the 2nd Edition CQI chapter.
-- FOUR OEs CARRY THE ASTERISK -- PSQ.1.a, g, h, i.
-- UNAPPROVED DRAFT. Do not run this insert until the owner confirms the write.
"""

if __name__ == "__main__":
    emit_and_verify(
        standard_code=STANDARD_CODE,
        chapter=CHAPTER,
        oe_codes=OE_CODES,
        policy_title=POLICY_TITLE,
        purpose=PURPOSE,
        scope=SCOPE,
        policy_statement=POLICY_STATEMENT,
        procedure_steps=PROCEDURE_STEPS,
        responsibility=RESPONSIBILITY,
        references_text=REFERENCES,
        distribution=DISTRIBUTION,
        abbreviations=ABBREVIATIONS,
        disclaimer=DISCLAIMER,
        oe_mapping=OE_MAPPING,
        universal_facts_checklist=UNIVERSAL_FACTS_CHECKLIST,
        version=VERSION,
        revision_history=REVISION_HISTORY,
        tier1_oes=TIER1_OES,
        statute_clause=STATUTE_CLAUSE,
        sql_header=SQL_HEADER,
        json_name="psq1_draft.json",
        sql_name="psq1_insert.sql",
    )
