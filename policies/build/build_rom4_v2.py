# -*- coding: utf-8 -*-
"""ROM.4 v2 — risk management, system-failure reporting and outsourced services.

Shape follows PRE.2 v2 (section list and order only). Wording is built
from ROM.4 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 111 / PDF index 117.
Chapter intent: printed page 109 / PDF index 115.

Does NOT overwrite rom4_draft.json or build_rom4.py. No SQL. No Supabase insert.
No stop-work section. Five OEs clustered into five What-we-do subsections.
Disclaimer P2 is accreditation-only.

ROM.4 is written as leadership/governance ownership of patient safety and risk
management. Cross-references PSQ (quality programme), HIC (infection), FMS
(facilities safety). Does NOT duplicate ward-level safety mechanics.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "ROM.4"
CHAPTER = "ROM"
OE_CODES = [
    "ROM.4.a", "ROM.4.b", "ROM.4.c", "ROM.4.d", "ROM.4.e",
]
POLICY_TITLE = "Risk Management, System-Failure Reporting and Outsourced Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "ROM v2 template: PRE v2 shape, plain English, governance roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Management ensures proactive risk management, integration between quality improvement "
    "and strategic planning, reporting of system and process failures, documented outsourced-service "
    "agreements, and monitoring of outsourced-service quality."
)

PURPOSE = f"""This policy establishes how management at {HOSPITAL} ensures proactive risk management, integrates quality improvement with risk management and strategic planning, implements reporting systems for system and process failures, maintains documented agreements for outsourced services, and monitors outsourced-service quality.

It covers five elements: proactive risk management; integration of quality improvement, risk management and strategic planning; internal and external reporting of system and process failures; documented outsourced-service agreements; and outsourced-service quality monitoring.

The chapter intent is that leaders ensure that patient-safety and risk-management issues are an integral part of patient care and hospital management.

This policy is written as governance and leadership ownership of risk management and outsourced services. Ward-level patient-safety mechanics remain with PSQ. Infection-control mechanics remain with HIC. Facilities safety mechanics remain with FMS.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the governing body, the Medical Superintendent, department and service heads, the Quality Coordinator, and any staff responsible for outsourced-service contracts at {HOSPITAL}.

It covers the five elements ROM.4.a–e name. It does not cover governance roles and mission (ROM.1), leader qualifications and performance (ROM.2), or strategic plans and service standards (ROM.3, though ROM.4.b integrates with ROM.3's strategic planning).

Boundaries with other policies of {HOSPITAL}:

- PSQ owns the quality-improvement programme, patient-safety goals, incident analysis and clinical indicators. This policy owns management's duty to ensure proactive risk management and to integrate quality improvement with strategic planning.
- HIC owns infection-prevention and -control mechanics. This policy owns management's risk-management oversight that includes infection risk.
- FMS owns facilities safety, fire safety and hazardous-materials management. This policy owns management's risk-management oversight that includes facilities risk.
- ROM.3 owns strategic and operational plans. This policy owns the integration of risk management into those plans (ROM.4.b).
- Outsourced-service operational supervision is the responsibility of the department that uses the service. This policy owns the documented agreement and quality monitoring at the management level."""

POLICY_STATEMENT = f"""{HOSPITAL} ensures proactive risk management across the organisation as a management responsibility, not only a quality-department activity.

Management integrates quality improvement, risk management and strategic planning. Systems for internal and external reporting of system and process failures are implemented. Outsourced services operate under documented agreements with service parameters, and their quality is monitored.

{HOSPITAL} does not treat a risk register that is never reviewed as proactive risk management, or an outsourced-service contract without service parameters as a documented agreement."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Operating without a documented risk-management programme that is reviewed by management {D('at least quarterly')}.
2. Treating quality improvement, risk management and strategic planning as unrelated activities with no documented integration.
3. Operating without a system for internal and external reporting of system and process failures.
4. Engaging an outsourced service without a documented agreement that includes service parameters.
5. Failing to monitor the quality of an outsourced service for more than {D('one review cycle')}.

Staff who see one of these acts report it the same day to the {D('Medical Superintendent')} or the {D('Quality Coordinator')}."""

PROCEDURE_STEPS = [
f"""5.1 Proactive risk management

Management ensures proactive risk management across the organisation. The {D('Medical Superintendent')} maintains a risk register that identifies risks across clinical, operational, financial and compliance domains.

The risk register is reviewed {D('quarterly')} by the Medical Superintendent and {D('half-yearly')} by the governing body. Each risk entry states the risk, the likelihood, the impact, the mitigation action, the responsible person and the review date.

This is management's ownership of risk. PSQ owns quality indicators and patient-safety goals. HIC owns infection risk at the operational level. FMS owns facilities risk at the operational level. ROM.4.a is the governance layer that ensures those risks are identified, registered and reviewed proactively.""",

f"""5.2 Integration of quality improvement, risk management and strategic planning

Management ensures integration between quality improvement, risk management and strategic planning within the organisation. The strategic plan (ROM.3.a) incorporates risk-management priorities and quality-improvement objectives.

The {D('Quality Coordinator')} maps quality-improvement priorities and risk-register items to the strategic plan {D('annually')} and presents the mapping to the Medical Superintendent. The governing body reviews the integration when approving the strategic plan.

This is not a separate quality plan. It is the documented link between what PSQ measures, what the risk register identifies, and what ROM.3's strategic plan commits to.""",

f"""5.3 Internal and external reporting of system and process failures

Management ensures implementation of systems for internal and external reporting of system and process failures. Internal reporting means {D('incident reports, near-miss reports and root-cause analyses submitted to the Quality Coordinator and reviewed by the Medical Superintendent')}.

External reporting means {D('mandatory notifications to regulatory bodies as required by applicable legislation — for example adverse-event reporting, notifiable-disease reporting, and any other external reporting obligation')}.

The {D('Quality Coordinator')} maintains the failure-reporting register. The Medical Superintendent reviews the register {D('monthly')} and presents a summary to the governing body {D('quarterly')}. PSQ owns the incident-analysis method. This step owns management's duty to ensure the reporting system exists and is used.""",

f"""5.4 Documented outsourced-service agreements

Management ensures that it has a documented agreement for all outsourced services that include service parameters. Each outsourced service at {HOSPITAL} operates under a written agreement that states {D('the scope of service, the service-level parameters (turnaround time, quality indicators, reporting requirements), the responsibilities of each party, the review mechanism and the termination clause')}.

The {D('Medical Superintendent')} or the designated contract holder maintains the agreement file. No outsourced service operates without a signed agreement.

The agreement is reviewed {D('before renewal')} and updated when service parameters change. A contract without service parameters is not a documented agreement under this policy.""",

f"""5.5 Outsourced-service quality monitoring

Management monitors the quality of the outsourced services and improvements are made as required. Each outsourced service is monitored against the service parameters defined in its agreement (section 5.4).

The {D('department or service head that uses the outsourced service')} collects monitoring data. The {D('Quality Coordinator')} compiles the data {D('quarterly')} and presents it to the Medical Superintendent. Non-conformances trigger corrective action with the service provider.

The governing body receives an annual summary of outsourced-service quality. An outsourced service that repeatedly fails to meet service parameters is escalated for contract review or termination.""",
]

RESPONSIBILITY = f"""Governing body (owner(s) / board of directors / trustees)
- Reviews the risk register and risk-management programme.
- Receives reports on system and process failures and outsourced-service quality.
- Approves the integration of quality improvement, risk management and strategic planning.

Medical Superintendent (Head of the Institution)
- Maintains the risk register and reviews it quarterly.
- Ensures internal and external failure-reporting systems exist and are used.
- Holds or designates holding of outsourced-service agreements.
- Reviews outsourced-service quality data.

Quality Coordinator
- Maps quality-improvement priorities and risk items to the strategic plan.
- Maintains the failure-reporting register.
- Compiles outsourced-service monitoring data.
- Audits this policy {D('quarterly')} (see section 7).

Department / service heads
- Identify and escalate risks within their area to the risk register.
- Collect outsourced-service monitoring data for services they use.
- Report system and process failures through the internal reporting system."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Risk register current, reviewed and presented to management on schedule.
- Quality-improvement and risk-management integration documented in the strategic plan.
- Failure-reporting register maintained and reviewed monthly.
- Outsourced-service agreements on file with service parameters for every outsourced service.
- Outsourced-service quality monitoring data compiled and non-conformances addressed.

Root-cause analysis is required when the risk register is not reviewed on schedule, a failure-reporting gap is found, or an outsourced service operates without a documented agreement.

This policy is reviewed {D('annually')}, and sooner when the outsourced-service portfolio changes or a significant risk event occurs."""

TRAINING_ACKNOWLEDGEMENT = f"""The Medical Superintendent, department heads, the Quality Coordinator and staff responsible for outsourced-service contracts are trained on this policy at induction and {D('once a year')} after that. Training covers risk management, failure reporting, outsourced-service agreements and quality monitoring.

Staff acknowledgement

I have read this Risk Management, System-Failure Reporting and Outsourced Services policy of {HOSPITAL}. I understand the risk-management and outsourced-service requirements.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Medical Superintendent holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("ROM/POL/04"),
    version=VERSION,
    prepared_by=D("Medical Superintendent"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Responsibilities of Management chapter, standard ROM.4.
- Internal documents of {HOSPITAL}: risk register; quality-improvement programme (PSQ); strategic plan (ROM.3); failure-reporting register; outsourced-service agreements and monitoring records; infection-control programme (HIC); facilities safety programme (FMS)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: governing body members; department and service heads; nursing administration; quality office; staff responsible for outsourced-service contracts.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
FMS — Facility Management and Safety (NABH SHCO chapter 6)
HIC — Hospital Infection Control (NABH SHCO chapter 5)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 9)
ROM — Responsibilities of Management (NABH SHCO chapter 7)
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "ROM.4.a",
        "requirement": "Management ensures proactive risk management across the organisation.",
        "steps": "Statement of intent; Section 3; 5.1 Proactive risk management; Section 4 items 1, 6",
        "responsible": "Medical Superintendent (risk register); governing body (review); department heads (escalate risks)",
        "records": [
            "Risk register with risk, likelihood, impact, mitigation, responsible person and review date.",
            "Quarterly risk-register review records signed by the Medical Superintendent.",
            "Half-yearly governing-body review of the risk-management programme.",
            "Quarterly audit sample showing the register is current and reviewed.",
        ],
    },
    {
        "oe_code": "ROM.4.b",
        "requirement": "Management ensures integration between quality improvement, risk management and strategic planning within the organisation.",
        "steps": "Section 3; 5.2 Integration of quality improvement, risk management and strategic planning; Section 4 item 2",
        "responsible": "Quality Coordinator (mapping); Medical Superintendent (present); governing body (approve integration)",
        "records": [
            "Documented mapping of quality-improvement priorities and risk items to the strategic plan.",
            "Annual update of the mapping presented to the Medical Superintendent.",
            "Governing-body review record when approving the strategic plan.",
        ],
    },
    {
        "oe_code": "ROM.4.c",
        "requirement": "Management ensures implementation of systems for internal and external reporting of system and process failures.",
        "steps": "Statement of intent; Section 3; 5.3 Internal and external reporting of system and process failures; Section 4 item 3",
        "responsible": "Quality Coordinator (register); Medical Superintendent (review); PSQ (incident-analysis method)",
        "records": [
            "Failure-reporting register with incident reports, near-miss reports and root-cause analyses.",
            "Monthly review of the register by the Medical Superintendent.",
            "Quarterly summary presented to the governing body.",
            "Evidence of external reporting to regulatory bodies where required.",
        ],
    },
    {
        "oe_code": "ROM.4.d",
        "requirement": "Management ensures that it has a documented agreement for all outsourced services that include service parameters.",
        "steps": "Section 3; 5.4 Documented outsourced-service agreements; Section 4 item 4",
        "responsible": "Medical Superintendent or contract holder (agreement file); department heads (operational supervision)",
        "records": [
            "Signed agreement for each outsourced service with scope, service parameters and review mechanism.",
            "Agreement file maintained and accessible.",
            "Review records before renewal or when parameters change.",
        ],
    },
    {
        "oe_code": "ROM.4.e",
        "requirement": "Management monitors the quality of the outsourced services and improvements are made as required.",
        "steps": "Section 3; 5.5 Outsourced-service quality monitoring; Section 4 item 5",
        "responsible": "Department heads (collect data); Quality Coordinator (compile); Medical Superintendent (review)",
        "records": [
            "Quarterly outsourced-service monitoring data against service parameters.",
            "Non-conformance records and corrective actions with the service provider.",
            "Annual summary of outsourced-service quality presented to the governing body.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """ROM.4 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Chapter intent PDF index 115. ROM.4.a–e PDF page 117. Asterisked OEs: ROM.4.a, ROM.4.c. ROM.4.c and ROM.4.d are Core, ROM.4.b is Excellence, ROM.4.e is Achievement, ROM.4.a is Commitment.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. Governance roles only. Cross-references PSQ, HIC, FMS without duplicating ward-level mechanics."""


def main() -> int:
    draft = {
        "standard_code": STANDARD_CODE,
        "chapter": CHAPTER,
        "oe_codes": OE_CODES,
        "policy_title": POLICY_TITLE,
        "purpose": PURPOSE,
        "scope": SCOPE,
        "policy_statement": POLICY_STATEMENT,
        "procedure_steps": PROCEDURE_STEPS,
        "responsibility": RESPONSIBILITY,
        "references_text": REFERENCES,
        "distribution": DISTRIBUTION,
        "abbreviations": ABBREVIATIONS,
        "disclaimer": DISCLAIMER,
        "oe_mapping": OE_MAPPING,
        "universal_facts_checklist": UNIVERSAL_FACTS_CHECKLIST,
        "version": VERSION,
        "revision_history": REVISION_HISTORY,
        "status": "draft",
        "definitions": STATEMENT_OF_INTENT,
        "exceptions": NON_NEGOTIABLES,
        "monitoring_audit": MONITORING_AUDIT,
        "training_competency": TRAINING_ACKNOWLEDGEMENT,
        "resources_required": DOCUMENT_CONTROL,
        "template_test": "rom_v2_adoptable_shape",
        "subtitle": "Risk management, failure reporting and outsourced-service governance.",
        "doc_no": D("ROM/POL/04"),
    }
    emit_pre_v2(
        draft,
        "rom4_v2_draft.json",
        "ROM.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
