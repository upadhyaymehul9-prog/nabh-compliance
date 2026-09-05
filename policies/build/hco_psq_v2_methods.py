# -*- coding: utf-8 -*-
"""Hospital-facing What-we-do methods for HCO PSQ.1–PSQ.7.

HCO 6th Edition chapter name is Patient Safety and Quality Improvement (PSQ).
Method notes from the Guidebook are attached separately by the generator.
"""
from __future__ import annotations


def method_bodies(*, D, HOSPITAL, BLANK) -> dict[str, str]:
    """Return method body text keyed by oe_code (without the 5.N title)."""
    pso = D("Patient Safety Officer")
    qc = D("Quality Coordinator")
    ms = D("Medical Superintendent")
    ns = D("Nursing Superintendent")
    qic = D("Quality Improvement Committee")
    psc = D("Patient Safety Committee")
    yearly = D("annually")
    quarterly = D("quarterly")
    monthly = D("monthly")

    return {
        "PSQ.1.a": f"""{HOSPITAL} documents a patient safety programme. A multi-disciplinary {psc} develops, implements and maintains it.

The {ms} constitutes the committee. Membership includes administration, clinical, nursing, quality and the {pso}. Terms of reference, quorum and meeting frequency ({D('at least monthly')}) are written. The current programme sits in the {D('Patient Safety Manual')}. Minutes-only notes are not this CORE asterisked element.""",

        "PSQ.1.b": f"""The programme covers the major patient-safety elements this hospital's scope requires: identification, communication, medication safety, procedure safety, falls and other high-risk care, infection-related safety (cross-reference IPC), and incident reporting.

The {psc} keeps a current element list in the manual. Staff who work in those areas are trained at induction and {yearly}.""",

        "PSQ.1.c": f"""The programme covers incidents from no-harm events through sentinel events. Written definitions of no-harm, near miss, adverse event and sentinel event sit in the manual (glossary plus local examples).

Every defined class can be reported through the incident system under PSQ.7. A programme that only tracks deaths is not comprehensive under this element.""",

        "PSQ.1.d": f"""The {ms} designates one or more patient safety officers to coordinate implementation. The {pso} is a doctor or nurse with experience applying risk management in clinical work, reports to top management, and has written roles.

The designation letter, time allocation and reporting line are on file. Champions in patient safety are named across departments. A title on a circular without time and duties is not designation.""",

        "PSQ.1.e": f"""The {psc} performs proactive analysis of patient-safety risks using tools such as HIRA, FMEA, HVA, fault-tree analysis or simulation, as the committee names for the process.

At a minimum, one patient-safety-related risk undergoes proactive analysis every year, and improvements from that analysis are made. Findings have owners and due dates. The {qc} holds the analysis file.""",

        "PSQ.1.f": f"""The {psc} reviews and updates the patient safety programme at least {yearly} and sooner after a sentinel event, a new service, or a change in national patient-safety goals.

An update is a dated change to the manual or element list. The {qc} holds the review minute.""",

        "PSQ.1.g": f"""{HOSPITAL} adapts and implements current national / international patient-safety goals, solutions or framework. At a minimum this is the current National Patient-Safety Framework, WHO Patient Safety Solutions and/or International Patient Safety Goals, as the {psc} adopts them for this hospital's scope.

The adopted list, local adaptations and how each goal is measured sit in the manual. This CORE element is evidenced by the current adopted list plus implementation records, not by a poster alone.""",

        "PSQ.2.a": f"""{HOSPITAL} documents a quality improvement and continuous monitoring programme. A multi-disciplinary {qic} develops, implements and maintains it.

The {ms} constitutes the committee. Membership includes administration, clinical, nursing and quality. Terms of reference, quorum and meeting frequency ({D('at least monthly')}) are written. The current programme sits in the {D('Quality Manual')}. This is a CORE asterisked element.""",

        "PSQ.2.b": f"""The quality improvement programme covers the major quality-assurance elements: indicator monitoring (PSQ.3), quality-improvement projects and tools (PSQ.4), clinical audit (PSQ.5), incident learning (PSQ.7), and department-level review.

The {qic} keeps a current element list. A programme that only lists indicators without review is not comprehensive under this asterisked element.""",

        "PSQ.2.c": f"""Quality-improvement work includes projects that improve process efficiency and effectiveness (time, waste, reliability of a defined process), not only clinical outcome counts.

Each such project has an aim, a measure and a before/after result held by the {qc}. This Excellence element is evidenced by completed projects with those measures.""",

        "PSQ.2.d": f"""Quality-improvement work includes projects that focus on appropriateness of clinical care (right care, indicated care, variation against agreed protocols).

The {qic} selects topics from clinical indicators, audits and incidents. Results go back to the clinical department. This Excellence element is evidenced by those topics and outcomes.""",

        "PSQ.2.e": f"""The {ms} designates an individual (default: the {qc}) to coordinate and implement the quality improvement programme. That person completes structured training in implementation of accreditation standards (NABH Programme on Implementation of NABH Standards) and has knowledge of hospital quality-improvement principles, evaluation methods and operations.

The designation letter, time allocation, written roles and reporting line to top management are on file. Champions in quality improvement are named across departments. This is an asterisked element.""",

        "PSQ.2.f": f"""The programme identifies opportunities for improvement from review at pre-defined intervals. The {qic} reviews the programme at least once in three months (and more often if the quality manual says so).

The review includes audits, organisational performance and key indicators. Minutes are kept. Each identified opportunity has an owner and a next step. This is an asterisked element.""",

        "PSQ.2.g": f"""The {qic} reviews and updates the quality improvement programme at least {yearly} and sooner after a major service change or a cluster of failed audits.

An update is a dated change to the manual, indicator set or audit calendar. The {qc} holds the review minute.""",

        "PSQ.2.h": f"""Audits are conducted at regular intervals as continuous monitoring. Choice and frequency cover priority areas and areas of concern from indicators or risk.

In addition, a hospital-wide internal audit covers all areas at least once in six months, done by identified staff or a multi-disciplinary team trained in NABH Accreditation Standards for Hospitals, assessing areas independent of their own work, against applicable standards and objective elements. Findings, CAPA and verification of changes are documented. A calendar without completed audits in the period is not this asterisked element.""",

        "PSQ.2.i": f"""There is an established process to monitor and improve the quality of nursing care: nursing audits and/or competency evaluation (written or witnessed demonstration) for key procedures, plus nursing quality indicators.

The {ns} and the {qc} keep the current process in writing and integrate it with the quality improvement programme. This CORE asterisked element is not met by a one-off lecture without monitoring.""",

        "PSQ.3.a": f"""The {qic} identifies and monitors key indicators for clinical structures, processes and outcomes matching this hospital's clinical scope. Any indicator mandated by the Government of India, the State Government or NABH is included. Specialty indicators from the NABH Key Performance Indicators set are used as they apply to the scope of services.

Each indicator has a defined numerator, denominator and multiplier (and definitions of terms where needed). Data are presented to the {qic} at the defined interval.""",

        "PSQ.3.b": f"""The {qic} identifies and monitors key indicators for infection prevention and control activities (cross-reference IPC.6 surveillance). Any indicator mandated by the Government of India or NABH is included. Healthcare-associated infection definitions follow the current CDC National Healthcare Safety Network definitions (CAUTI, CLABSI, SSI, VAP as applicable).

IPC indicator results are reviewed in the {qic} as well as the infection committee. This is a CORE element. Missing IPC indicators is a critical gap.""",

        "PSQ.3.c": f"""The {qic} identifies and monitors key indicators for managerial structures, processes and outcomes. Any indicator mandated by the Government of India, the State Government or NABH is included (including digital-health indicators as they apply).

Each indicator has a defined numerator, denominator and multiplier. Results go to the {qic} and to the relevant departmental leader.""",

        "PSQ.3.d": f"""The {qic} identifies and monitors key indicators for patient-safety activities (patient-safety goals and risk management). Any indicator mandated by the Government of India, the State Government or NABH is included.

Each indicator has a defined numerator, denominator and multiplier. This is a CORE element.""",

        "PSQ.3.e": f"""The quality team verifies indicator data regularly (default: {monthly} sample check of source vs reported figure, and a {quarterly} deeper verification of a rotating subset).

Verification notes sit with the indicator file. Unverified data are not used for public dashboards or management targets until checked.""",

        "PSQ.3.f": f"""There is a written mechanism to analyse indicator data (trend, target, outlier, comparison where defined) so that opportunities for improvement are identified.

Analysis is minuted at the {qic}. A spreadsheet without an identified opportunity or a documented 'no action needed' is not analysis under this element.""",

        "PSQ.3.g": f"""Improvements identified from indicator analysis are implemented and then evaluated (did the measure move as intended).

The {qc} tracks actions to closure. An action list without a later evaluation is incomplete under this element.""",

        "PSQ.3.h": f"""Feedback about care and service — rates, trends and improvement opportunities — is communicated to staff (department meetings, dashboards, huddles as the {qic} defines).

The {qc} keeps samples of what was shared and when. This Achievement element is evidenced by communication, not only by committee minutes.""",

        "PSQ.4.a": f"""{HOSPITAL} undertakes quality improvement projects. At a minimum, every year, the organisation undertakes two quality improvement projects. Each project has a definite purpose, a beginning and an end, and measurement of the parameters under improvement at the beginning and at the end.

The {qic} keeps a live project register with aim, owner, start date and status. This is a CORE element.""",

        "PSQ.4.b": f"""Quality improvement projects are centred on the six domains of healthcare quality: patient safety, cost-effectiveness, patient-centredness, timeliness, efficiency and equity.

The register tags how each project maps to those domains, including improvements in patient-care delivery and in hospital operations that affect cost and efficiency. This Achievement element is evidenced by completed projects covering those domains over the review period.""",

        "PSQ.4.c": f"""Projects use appropriate analytical, managerial and statistical tools (for example PDCA, run charts, Pareto, fishbone, 5-Why — the {qic} names the toolkit).

Project files show which tool was used and what it showed. A project that is only a memo without a tool is not this element.""",

        "PSQ.4.d": f"""{HOSPITAL} has a mechanism to capture patient-reported outcome measures (PROM) for defined conditions or pathways the {qic} names.

Collection method, frequency and how results feed improvement are written. A satisfaction survey alone is not PROM unless it includes defined outcome items the committee has accepted as PROM.""",

        "PSQ.5.a": f"""Clinical audits are performed to improve the quality of patient care, not only for documentation completeness and not as research projects.

The {qic} keeps a clinical-audit calendar. At a minimum the organisation conducts one clinical audit per clinical department once in two years, as per the scope of services. Topics may be disease-based, cost-based, community-based or morbidity-based (length of stay). Completed reports are filed.""",

        "PSQ.5.b": f"""Parameters to be audited are defined in writing before data collection: objectives, standards/criteria, sample, period and exclusions.

The audit lead agrees parameters with the {qc}. An audit started without predefined parameters is stopped and restarted against agreed criteria.""",

        "PSQ.5.c": f"""Medical and nursing staff participate in clinical audit: as audit leads, data collectors or in the results discussion for their specialty.

Attendance and role are recorded. An audit done only by the quality office with no clinical participation is not this Achievement element.""",

        "PSQ.5.d": f"""Patient and staff anonymity are maintained in clinical-audit reports and presentations. Identifiers are removed or coded; the key is held separately by the {qc}.

Reports used in open meetings do not name patients or staff. A named case discussion is a morbidity meeting, not this audit report.""",

        "PSQ.5.e": f"""Clinical audits are documented: protocol/parameters, data, findings, recommendations, attendees and date.

The {qc} files the pack. An undocumented verbal audit is not this element.""",

        "PSQ.5.f": f"""Remedial measures from clinical audit are implemented: each recommendation has an owner, due date and a later check that it was done.

The {qic} reviews open actions. A report without followed-up remedies is incomplete under this element.""",

        "PSQ.6.a": f"""Management creates a culture of safety: sharing information, reporting incidents, learning from analysis, a just (blame-free) culture, and collaboration across disciplines.

The {ms} signs the safety-culture statement in the patient-safety manual. Safety culture is measured at least {yearly} with a validated survey (for example MaPSaF, Safety Attitudes Questionnaire, or AHRQ SOPS) and management acts on the results. This Achievement element is evidenced by those actions, not by a poster alone.""",

        "PSQ.6.b": f"""Leaders at all levels are aware of the intent of the patient safety and quality improvement programme and the approach to implementation.

Department heads receive a briefing at induction to the role and {yearly}. The {qc} holds acknowledgement or attendance. A programme unknown to floor leaders is not this element.""",

        "PSQ.6.c": f"""Departmental leaders are involved in patient safety and quality improvement: they attend the relevant committee or send a named delegate, own department indicators and projects, and brief their teams.

Involvement is visible in minutes and department quality files.""",

        "PSQ.6.d": f"""The organisation earmarks adequate funds from its annual budget for the patient safety and quality programme (training, audit time, safety equipment, improvement projects, information systems as required).

The {ms} signs the budget line. Mid-year stock-out of a funded safety item is reported to management.""",

        "PSQ.6.e": f"""Management identifies organisational and department-level performance-improvement targets, monitors them at least once in three months, and modifies the target at least {yearly}.

Targets are shared with faculty and staff with regular feedback. This Achievement element is evidenced by the current target set plus review, not by an informal wish list.""",

        "PSQ.6.f": f"""Management uses workforce feedback (staff survey, safety huddle themes, suggestion scheme) to improve the patient safety and quality programme.

Feedback themes and resulting changes are minuted. This Excellence element is evidenced by a closed loop from staff input to a programme change.""",

        "PSQ.7.a": f"""{HOSPITAL} implements an incident management system covering identification, reporting, review and action. The system supports factual reporting and learning and is based on just culture. All incidents are captured without first filtering by severity or harm.

Written guidance, the reporting channel (form / digital), and who receives reports sit in the manual. The path is simple, clear, confidential and focused on process improvement. This CORE asterisked element is not met by a complaints box alone.""",

        "PSQ.7.b": f"""The organisation has a written mechanism to identify sentinel events: definition, examples for this hospital's scope, and who must be told immediately (default: {pso} and {ms}).

Recognised sentinel events are flagged in the incident system the same shift. Skipping identification or reporting is a stop-work trigger (section 6). This is an asterisked element.""",

        "PSQ.7.c": f"""Established processes analyse incidents: the {psc} is responsible; root-cause analysis is preferred; inputs are sought from the units concerned.

The immediate response is urgent care and support for those involved — that does not wait for analysis. For sentinel events, correction (if any) is initiated within {D('24 working hours')} of occurrence or reporting, and analysis is completed within {D('seven working days')} of occurrence or reporting. The {pso} tracks open analyses.""",

        "PSQ.7.d": f"""Corrective and preventive actions are taken from analysis findings. Actions have owners, due dates and a later effectiveness check.

Findings and recommendations are communicated to the personnel concerned. Continuing a process that analysis showed caused a sentinel event, before agreed controls are in place, is a stop-work trigger (section 6) except immediate life-saving care.""",

        "PSQ.7.e": f"""Risks identified in incident analysis are incorporated into the organisation's risk-management system (risk register update, residual risk, owner).

The {qc} or risk owner files the update. A CAPA without a risk-register entry when a new or changed risk was found is incomplete under this Achievement element.""",

        "PSQ.7.f": f"""There is a written process for informing stakeholders after a near miss, adverse event or sentinel event: who is told (patient/family as the organisation defines, treating team, leadership, and external agencies when required), by whom, and within what time.

The {pso} keeps a communication log for sentinel and defined serious events. This process sits beside, and does not replace, any statutory notification the hospital must make under other documents.""",
    }
