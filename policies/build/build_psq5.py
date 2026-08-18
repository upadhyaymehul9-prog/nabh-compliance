# -*- coding: utf-8 -*-
"""Builds the PSQ.5 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase until the
owner confirms.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

THIS CHAPTER IS PSQ in the SHCO 3rd Edition, not 2nd Edition CQI.

Tier is decided by doc_required / the asterisk in the official PDF:
  Tier 1 (full treatment): PSQ.5.a, PSQ.5.b
  Tier 2 (lighter pass):   PSQ.5.c, PSQ.5.d, PSQ.5.e

TWO of five OEs are asterisked. The draft builds deep blocks for a and b.
c-e are lean.

Official source: NABH SHCO 3rd Edition PDF, Chapter 6, PSQ.5, printed page 104
(PDF page index 110). Intent printed page 101: robust incident reporting
system; sentinel events shall be defined; all incidents investigated;
appropriate action taken. Official PSQ.5.e uses "organization" (American
spelling).

Asterisks verified 2026-08-17: PSQ.5.a and PSQ.5.b carry the asterisk.
"""
from policy_build_common import emit_and_verify, make_disclaimer_accreditation_only

STANDARD_CODE = "PSQ.5"
CHAPTER = "PSQ"
OE_CODES = [
    "PSQ.5.a", "PSQ.5.b", "PSQ.5.c", "PSQ.5.d", "PSQ.5.e",
]
TIER1_OES = ["PSQ.5.a", "PSQ.5.b"]

POLICY_TITLE = "Incident Management"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} implements an incident management system; how it identifies sentinel events; how incidents are analysed; how corrective and preventive actions are taken from that analysis; and how various stakeholders are informed in case of a near miss, adverse event or sentinel event.

The chapter intent is a robust incident reporting system, defined sentinel events, investigation of all incidents, and appropriate action. A book that is never filled, a sentinel-event list copied from another hospital's specialties, or a medication error that is captured only in MOM.7 and never enters this system, is not that intent.

This document is the hospital-wide incident system. Specialty capture (medication events, transfusion reactions, unit QA findings, complaints) remains those documents; those events still enter this system when they are incidents."""

SCOPE = """This policy applies to every area of {{HOSPITAL_NAME}} in which an incident, near miss, adverse event or sentinel event can occur, and to everyone who reports, receives, analyses, acts or informs.

It covers: the incident management system; the mechanism to identify sentinel events; analysis of incidents; CAPA based on that analysis; and informing various stakeholders of a near miss, adverse event or sentinel event.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- MOM.7 owns capture, reporting and CAPA of near-miss, medication error and ADR as a medication process. A medication event is still an incident under this document when it meets this hospital's incident definition. MOM.7 does not replace this system; this system does not replace MOM.7 capture. Both records exist when the subject is a medication event.
- COP.5 owns transfusion-reaction pathway. A reaction is still an incident here when it meets the definition.
- COP.6.d and COP.11.h own unit quality-assurance programmes. A unit finding may generate an incident; unit QA is not the hospital incident system.
- COP.10.h owns that intra-operative adverse anaesthesia events are recorded and reviewed. That recording remains anaesthesia. This system still receives the event as an incident. COP.10's forward-ref to a future PSQ incident policy is landed here.
- COP.12 owns identification and management of vulnerable patients, falls, pressure ulcers, thrombosis and restraint. A fall or pressure ulcer that occurs is an incident here; COP.12 still owns the risk programme.
- PRE.6 (drafted UNAPPROVED on a sibling branch) owns patient/family complaints. A complaint may describe an incident; PRE.6 redresses the complaint; this document manages the incident. PRE.1.d/e own rights-violation reports. Neither replaces this system.
- HIC.4 owns occupational exposure / PEP. A needlestick is still an incident here; HIC.4 still owns the occupational pathway.
- HIC.5 owns HAI surveillance case-finding. An HAI counted for surveillance may also be an incident; this document does not redefine NHSN-style definitions.
- PSQ.1.c is proactive analysis before harm. This document is after an incident (and near miss). They feed each other; they are not the same act.
- ROM.4.c (when drafted) is management ensuring systems for internal and external reporting of system and process failures. This document is the incident system those reports use. ROM.4.c must not silently become this SOP, and this SOP must not claim to be governance reporting duty.
- WHO Patient Safety Incident Reporting and Learning Systems (chapter reference 26), AHRQ Reporting Patient Safety Events (chapter reference 31), Canadian Incident Analysis Framework (chapter reference 1) and RCA2 (chapter reference 30) are frameworks, not pasted protocols.
- This chapter is PSQ, not CQI. Do not code this system as a CQI incident module."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} implements an incident management system.

{{HOSPITAL_NAME}} has a mechanism to identify sentinel events.

{{HOSPITAL_NAME}} has an established process for analysis of incidents.

{{HOSPITAL_NAME}} takes corrective and preventive actions based on the findings of that analysis.

{{HOSPITAL_NAME}} has a process for informing various stakeholders in case of a near miss, adverse event or sentinel event.

{{HOSPITAL_NAME}} does not treat a specialty log (medication, transfusion, complaints) as a substitute for this system, and does not treat a 2nd Edition CQI incident file as this 3rd Edition standard."""

PROCEDURE_STEPS = [
"""1. Incident management system

The organisation implements an incident management system. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask how an incident is reported, who receives it, what counts as an incident, and whether yesterday's events entered the system. The answer must be a system staff actually use, not a quality-office register the wards do not know, and not MOM.7 or PRE.6 counted as the whole hospital system.

The reason this is the safety step is that without a single system, events live in specialty silos and the organisation cannot learn. The chapter intent names a robust incident reporting system. The common error is a form that can be submitted only to the person involved in the event, or a definition so narrow that near misses never enter. WHO (2020) incident reporting and learning systems (chapter reference 26) and AHRQ Reporting Patient Safety Events (chapter reference 31) are frameworks for a reporting-and-learning system. They are not pasted as a software specification, and they are not a mandate to buy a named incident application.

What counts as an incident (including near miss and adverse event as this hospital uses those terms), how it is reported, who receives it (a route that is not only the person involved), how it is recorded, and how specialty captures (MOM.7, COP.5, COP.10.h, HIC.4, PRE.6) also enter this system when they are incidents, are [Hospital to define — the incident management system, including what counts as an incident, how it is reported, who receives it, and how specialty captures also enter this system]. Implementation means events from the wards are in the register, not only assessment-week samples.

This document does not print a named software product or a mandatory 24-hour clock as a NABH mandate. The time frame for reporting is this hospital's defined method.""",

"""2. Mechanism to identify sentinel events

The organisation has a mechanism to identify sentinel events. This step is the documented-evidence anchor of a requirement the standard asterisks. An assessor will ask what this hospital treats as a sentinel event and how one is identified when it occurs. The answer must be a written definition this hospital uses, matching the services it actually runs, not a copied tertiary-hospital list that includes transplant or neonatal events this SHCO does not provide.

The reason this is written separately from step 1 is that a sentinel event is not merely a serious incident with a louder stamp. The chapter intent says sentinel events shall be defined. The common error is no definition, or a definition so wide that every complaint is labelled sentinel and the word means nothing, or so narrow that a wrong-site event would not qualify. Identification must work at the time of the event, not only at a quarterly meeting.

The mechanism — the written definition of a sentinel event at this hospital, how it is identified when it occurs, who may declare it, and how that identification is recorded — is [Hospital to define — the mechanism to identify sentinel events, including this hospital's definition, matching services it actually runs]. A class the service directory does not provide is a recorded absence, not a copied sentinel SOP. AHRQ and WHO materials in the chapter bibliography inform seriousness and learning; they are not a mandated national sentinel list pasted here.

A sentinel event enters the incident system at step 1 and is analysed at step 3. This step is identification.""",

"""3. Analysis of incidents

The organisation has an established process for analysis of incidents.

How incidents are analysed (including a deeper look for sentinel events), who analyses, and how the analysis is recorded, are [Hospital to define — the established process for analysis of incidents, including any distinct path for sentinel events]. Charles et al. (chapter reference 2), RCA2 (chapter reference 30) and ASQ on RCA (chapter reference 49) are frameworks. This document does not print a named RCA template as a NABH mandate. Proactive analysis before harm remains PSQ.1.c.""",

"""4. CAPA based on analysis

Corrective and preventive actions are taken based on the findings of such analysis.

How CAPA is decided, implemented and checked, is [Hospital to define — how corrective and preventive actions from incident analysis are taken and followed through]. MOM.7.e remains CAPA from medication-event analysis as a medication process; when the event also sat in this system, CAPA is coordinated, not duplicated as two unrelated actions, and not omitted because "MOM.7 already did it".""",

"""5. Informing stakeholders of near miss, adverse event or sentinel event

The organization shall have a process for informing various stakeholders in case of a near miss / adverse event / sentinel event.

Who the stakeholders are (patient/family, staff, leadership, and any external body this hospital has defined), when they are informed, and how that is recorded, are [Hospital to define — the process for informing various stakeholders in case of a near miss, adverse event or sentinel event]. Patient/family information about an event is not PRE.6 complaint redressal and is not PRE.3 consent. Professional or statutory external reporting, where it applies, remains the owning document (for example ROM.4.c when drafted). This document does not print a named regulator or a rupee disclosure as a NABH mandate.""",

"""6. Records, review and the order of operations

The incident system, sentinel-event definition and identifications, analyses, CAPA, and stakeholder-information records, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for incident-management records] for: incidents actually entering the system from the wards; specialty events (medication, transfusion, anaesthesia, needlestick, complaint-described harm) also present here when they meet the definition; sentinel events identified against this hospital's definition; analysis and CAPA; stakeholders informed; no 2nd Edition CQI incident module offered as PSQ.5; and no named software counted as implementation without reports.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a sentinel event was not identified, or a medication error never entered this system, or when MOM.7, COP.10, COP.12, PRE.6 or PSQ.1 that this document hands work to are revised.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} implementing the incident management system and identifying sentinel events.

The named lead for incident management authors and keeps current the system, the sentinel-event definition and the analysis/informing methods. The named lead is [Hospital to define — the named lead for incident management].

Staff report incidents. The receiver is not only the person involved. Specialty leads (medication, transfusion, anaesthesia, IPC, complaints) ensure those events also enter this system when they are incidents.

The quality or accreditation coordinator audits the records at step 6 and reports findings to the head of the institution.

All staff are expected to treat an unused register, a copied sentinel list for services this hospital does not run, and a specialty log offered as the whole system, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 6 PSQ, standard PSQ.5. This is not the 2nd Edition CQI chapter.
- Patient safety incident reporting and learning systems: technical report and guidance (2020). World Health Organization — chapter reference 26; framework, not a software specification.
- Reporting Patient Safety Events (2019). AHRQ Patient Safety Network — chapter reference 31; framework.
- Canadian Incident Analysis Framework (2012). Canadian Patient Safety Institute — chapter reference 1; framework.
- RCA2 Improving Root Cause Analyses and Actions to Prevent Harm (2015). National Patient Safety Foundation — chapter reference 30; framework, not a mandated template.
- Charles, R., et al. (2016). How to perform a root cause analysis for workup and future prevention of medical errors — chapter reference 2; framework.
- Internal documents of {{HOSPITAL_NAME}}: the incident system; the sentinel-event definition; analysis and CAPA records; stakeholder-information method; MOM.7; COP.5, COP.6, COP.10, COP.11, COP.12; HIC.4/HIC.5; PRE.6; PSQ.1."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: every ward and the emergency area; the operation theatre and anaesthesia; pharmacy; IPC; the named incident receiver; and the named lead.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The incident-reporting method — the working document this policy requires — is held where staff can actually use it.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

PSQ — Patient Safety and Quality Improvement (SHCO 3rd Edition Chapter 6; not CQI)
CAPA — corrective and preventive action
RCA — root cause analysis
ADR — adverse drug reaction

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PSQ.5.a",
        "requirement": "The organisation implements an incident management system.",
        "steps": "Steps 1, 6",
        "evidence": "The written incident management system (what counts as an incident including near miss and adverse event as this hospital uses those terms, how reported, who receives on a route that is not only the person involved, how recorded) showing implementation on the wards rather than a quality-office register unused except at assessment; sample incidents against the unique identification number; the recorded method by which MOM.7 medication events, COP.5 transfusion reactions, COP.10.h anaesthesia events, HIC.4 needlesticks and PRE.6 complaint-described harm also enter this system when they meet the definition, without those specialty documents being replaced; the recorded use of WHO 2020 incident-reporting guidance and AHRQ Reporting Patient Safety Events (chapter references 26 and 31) as frameworks not a named software mandate; the recorded refusal to print a mandatory 24-hour NABH clock or a 2nd Edition CQI incident module as this system; induction or briefing of staff who report; the location of the system so staff can use it; the audit sample at step 6 of incidents that actually entered from the wards",
        "responsible": "Named lead holds the system; staff report; specialty leads ensure dual entry when required; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.5.b",
        "requirement": "The organisation has a mechanism to identify sentinel events.",
        "steps": "Steps 2, 1, 6",
        "evidence": "The written sentinel-event definition matching services this hospital actually runs, with recorded absences for classes the service directory does not provide rather than a copied tertiary list; the identification method at the time of the event (who may declare, how recorded) rather than only a quarterly retrospective stamp; sample identifications entering the incident system; the recorded refusal to treat every complaint as sentinel or to leave the term undefined; the location of the definition; induction or briefing of staff who may recognise a sentinel event; the audit sample at step 6 of identification against this hospital's definition",
        "responsible": "Named lead holds the definition and mechanism; staff who recognise a sentinel event apply it; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.5.c",
        "requirement": "The organisation has an established process for analysis of incidents.",
        "steps": "Steps 3, 2, 6",
        "evidence": "The written analysis process including any distinct path for sentinel events; sample analyses; the recorded split that PSQ.1.c is proactive analysis before harm; RCA2/Charles/ASQ used as frameworks not mandated templates; the audit sample at step 6",
        "responsible": "Named analysers; named lead holds the process; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.5.d",
        "requirement": "Corrective and preventive actions are taken based on the findings of such analysis.",
        "steps": "Steps 4, 3, 6",
        "evidence": "Sample CAPA from incident analysis followed through; the recorded coordination with MOM.7.e when the event was also a medication event, neither omitted nor duplicated as unrelated actions; the audit sample at step 6",
        "responsible": "Named CAPA owners; MOM.7.e remains medication CAPA; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PSQ.5.e",
        "requirement": "The organization shall have a process for informing various stakeholders in case of a near miss / adverse event / sentinel event.",
        "steps": "Steps 5, 2, 6",
        "evidence": "The written informing process naming stakeholders as this hospital defines them; sample records of informing; the recorded splits that PRE.6 is complaint redressal and ROM.4.c will own governance external-reporting duty; the audit sample at step 6",
        "responsible": "Named informer; PRE.6/ROM.4 remain those documents; quality or accreditation coordinator audits",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. PSQ.5 standard text and all five OEs were read from the official SHCO 3rd Edition PDF, Chapter 6, printed page 104 (PDF page index 110). Header: "Incidents are collected and analysed to ensure continual quality improvement" (no terminal period in the book). Official PSQ.5.e uses "organization". PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Core, b Commitment, c Commitment, d Commitment, e Excellence.
   TWO OEs CARRY THE ASTERISK -- PSQ.5.a and PSQ.5.b. c-e are unasterisked (Tier 2).
   This is PSQ, not 2nd Edition CQI.

TIERING UNDER THE STANDING RULE
1. TWO OF FIVE OEs ARE TIER 1. Tier 1: a, b -- steps 1 and 2 carry the reasoning. Tier 2: c, d, e. Shallower treatment of c-e is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-17) of PSQ.5.a/b against HIC masters and AAC/COP/MOM drafts. Search terms: incident, sentinel, near miss, adverse event, RCA, medication error, complaint.
   MOM.7 -- CRITICAL SPLIT. Medication-event capture remains MOM.7; the event also enters this system when it is an incident. Stated in Scope and step 1.
   COP.10.h -- forward-ref to this policy landed. Anaesthesia records the event; this system receives it as an incident.
   COP.5 / COP.6.d / COP.11.h / COP.12 / HIC.4 / HIC.5 / PRE.6 -- specialty or unit or complaint pathways. Stated in Scope.
   PSQ.1.c -- proactive vs after-the-fact. Stated in Scope and step 3.
   ROM.4.c -- governance reporting duty, undrafted. Flagged.
3. FORWARD REFERENCES: ROM.4.c.
4. T2 QUICK CHECK: PSQ.5.d vs MOM.7.e CAPA coordination -- flagged. PSQ.5.e vs PRE.6 -- flagged.

STATUTORY AND EXTERNAL FACTS
5. No named Act of Parliament is a numbered PSQ chapter reference for incident management. P2 is accreditation-only. Do not force CPA 2019 onto this standard; PRE.6 already uses CPA for consumer grievance where that subject lives.
6. WHO 2020, AHRQ reporting primer, Canadian framework, RCA2 -- chapter refs 26, 31, 1, 30 -- frameworks, not pasted software or templates.
7. NO NUMBERS ARE STATED as requirements. No mandatory 24-hour NABH clock. No named software.

EDITORIAL POSITIONS TAKEN
8. Dual entry of specialty events (MOM.7 etc.) into this system is an editorial position required so silos do not empty PSQ.5.
9. Sentinel-event definition left to the hospital, fenced to AAC.1 services, is an editorial position; the standard requires a mechanism, not a national list.
10. Refusal to code this as CQI is required by the owner's instruction.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
11. make_disclaimer_accreditation_only(). AAC.1 defaulted-statute bug refused. BMW/FSS out of P2.

DELIBERATELY NOT INCLUDED
- Proactive risk analysis -- PSQ.1.c. Indicator monitoring -- PSQ.2. Clinical audit -- PSQ.3.
- Medication-event capture method -- MOM.7. Transfusion-reaction pathway -- COP.5. Anaesthesia recording -- COP.10.h. Falls programme -- COP.12. Complaint redressal -- PRE.6. HAI definitions -- HIC.5. PEP -- HIC.4.
- A named incident application. A pasted national sentinel list. A 2nd Edition CQI incident module.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 11 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 9 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 11; a search for "Hospital to define" without brackets finds all 11, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: incident system; sentinel-event mechanism; analysis process; CAPA method; stakeholder-informing process; named lead; audit interval; review interval; intranet location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 6 PSQ, printed page 104.
-- TWO OEs CARRY THE ASTERISK -- PSQ.5.a and PSQ.5.b. NOT 2nd Edition CQI.
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
        json_name="psq5_draft.json",
        sql_name="psq5_insert.sql",
    )
