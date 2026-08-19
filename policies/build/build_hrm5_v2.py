# -*- coding: utf-8 -*-
"""HRM.5 v2 — staff well-being and occupational health.

Shape follows PRE v2 (section list and order only). Wording is built
from HRM.5 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 125 / PDF index 131.

No stop-work section. Four OEs mapped to four What-we-do subsections.
Owns general staff occupational health; cross-references HIC.4 for infection exposure.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.5"
CHAPTER = "HRM"
OE_CODES = [
    "HRM.5.a", "HRM.5.b", "HRM.5.c", "HRM.5.d",
]
POLICY_TITLE = "Staff Well-Being and Occupational Health"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HRM v2 template: PRE v2 shape, plain English, HR roles, four steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Staff well-being is promoted through identification of health problems and "
    "occupational health hazards, annual health checks, treatment for workplace injuries "
    "and measures to prevent and handle workplace violence — general occupational health "
    "owned here; infection-specific exposure response owned by HIC.4."
)

PURPOSE = f"""This policy describes how {HOSPITAL} promotes staff well-being through identification of health problems including occupational health hazards, conducts annual health checks, provides treatment for workplace-related injuries, and prevents and handles workplace violence.

It covers four elements: staff well-being and occupational hazard identification; annual health checks with documented findings; treatment for workplace injuries; and workplace violence prevention and handling.

HIC.4 owns infection-control occupational response (needlestick, sharps, splash, PEP). This policy owns general staff occupational health programmes. HRM.3.d owns occupational safety training delivery.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff at {HOSPITAL}: clinical, nursing, administrative and support. It applies to the {D('HR In-Charge / Personnel Officer')}, the {D('Medical Superintendent')}, department heads and the {D('Quality Coordinator')}.

It covers HRM.5.a–d. It does not cover infection-control occupational exposure response and PEP (HIC.4), occupational safety training delivery (HRM.3.d) or credentialing health status verification (HRM.6.b).

Boundaries with other policies of {HOSPITAL}:

- HIC.4 owns infection-control occupational response: needlestick, sharps injury, splash exposure and post-exposure prophylaxis. HRM.5 owns general staff health programmes, annual checks and workplace injury treatment.
- HRM.3.d owns training in occupational safety aspects. This policy owns the health programme and hazard identification.
- PSQ.5 may receive reports of violence-related incidents. This policy owns prevention and handling measures."""

POLICY_STATEMENT = f"""{HOSPITAL} promotes staff well-being through identification of health problems of staff, including occupational health hazards, in accordance with the organisation's policy.

Health checks of staff are done at least once a year and findings are documented. {HOSPITAL} provides treatment to staff who sustain workplace-related injuries.

{HOSPITAL} has measures in place for preventing and handling workplace violence."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. Occupational health hazards are identified and addressed per the organisation's policy — not only when a staff member falls ill.
2. Every active staff member receives a health check at least once a year — not only clinical staff.
3. Health check findings are documented and filed — not only verbal clearance to work.
4. Workplace-related injuries receive prompt treatment — not deferred to the staff member's own expense.
5. Workplace violence prevention and handling measures are documented and communicated — not only a reactive response after an event.

Staff who experience a workplace injury or violence report it immediately to the {D('HR In-Charge / Personnel Officer')} or the {D('Medical Superintendent')}. Infection-specific exposure follows HIC.4 immediately.

Staff who identify an unaddressed occupational hazard report it within the same working week."""

PROCEDURE_STEPS = [
f"""5.1 Staff well-being and occupational health hazard identification

Staff well-being is promoted through identification of health problems of the staff, including occupational health hazards, in accordance with the organisation's policy at {HOSPITAL}. The occupational health programme covers: hazard identification in each department; health surveillance for roles with known exposure (for example radiology, laboratory, operating areas); immunisation status tracking; and mental well-being awareness.

The {D('HR In-Charge / Personnel Officer')} maintains an occupational health hazard register updated {D('annually')} or when a new hazard is identified. Department heads report new hazards. Infection-specific exposure (needlestick, sharps, splash) is handled per HIC.4 — this step does not duplicate PEP procedures.""",

f"""5.2 Annual health checks

Health checks of staff are done at least once a year and the findings/results are documented at {HOSPITAL}. The annual check includes: general physical examination; {D('vision and hearing screening where role requires')}; {D('chest X-ray or PPD for high-risk roles')}; vaccination status review; and any role-specific tests defined in the hazard register.

Results are recorded on a standard health-check form filed in the personnel file (HRM.6). Abnormal findings are referred for follow-up treatment. Staff who cannot perform patient-facing duties due to health findings are reassigned per medical advice until cleared.""",

f"""5.3 Treatment for workplace-related injuries

Organisation provides treatment to staff who sustain workplace-related injuries at {HOSPITAL}. Workplace injuries include: slips and falls; manual handling injuries; chemical exposure (non-infection); and injuries from workplace violence.

The procedure covers: immediate first aid; medical assessment; treatment at {D("the hospital emergency service or a designated panel doctor")}; documentation of the injury; and return-to-work assessment. Injury records are filed in the personnel file and reported to the Medical Superintendent. Repeat injuries trigger review of the hazard register.""",

f"""5.4 Workplace violence prevention and handling

The organisation has measures in place for preventing and handling workplace violence at {HOSPITAL}. Prevention measures include: staff training on de-escalation (HRM.3.d); visible security measures; restricted access to high-risk areas; and a zero-tolerance policy communicated to patients and visitors.

Handling measures cover: immediate safety response; reporting to the Medical Superintendent and {D('local police where applicable')}; medical treatment for injured staff (step 5.3); incident documentation (cross-reference PSQ.5 for clinical incidents); support and counselling for affected staff; and review of prevention measures after each event.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Approves the occupational health policy and workplace violence measures.
- Ensures treatment is provided for workplace injuries.
- Reviews violence incidents and prevention effectiveness.

HR In-Charge / Personnel Officer
- Maintains occupational health hazard register and health-check schedule.
- Coordinates annual health checks and files results.
- Documents workplace injuries and violence incidents.

Department Heads
- Report occupational hazards in their areas.
- Ensure staff attend annual health checks.
- Support immediate response to violence incidents.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).

All Staff
- Attend annual health checks.
- Report workplace injuries and violence immediately.
- Follow infection-exposure procedures per HIC.4 when applicable."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers hazard identification, health checks, injury treatment and violence measures.

What is monitored each quarter:

- Occupational health hazard register current.
- All active staff received annual health check within the last {D('12 months')}.
- Health check findings documented and filed.
- Workplace injury records show prompt treatment provided.
- Workplace violence prevention measures communicated; any incidents handled per procedure.

Root-cause analysis is required when a staff member's annual health check is overdue by more than {D('three months')} or when a workplace injury was not treated promptly.

This policy is reviewed {D('annually')}, and sooner when HIC.4 exposure procedures change."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff are informed of the occupational health programme, annual health check requirement, injury reporting and workplace violence measures at induction (HRM.2.a) and {D('once a year')} after that.

Staff acknowledgement

I have read this Staff Well-Being and Occupational Health policy of {HOSPITAL}. I understand the annual health check requirement, how to report workplace injuries and the workplace violence prevention measures. I know that infection-specific exposure follows HIC.4.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The HR office holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/05"),
    version=VERSION,
    prepared_by=D("HR In-Charge / Personnel Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.5.
- Internal documents of {HOSPITAL}: occupational health hazard register; annual health check forms; workplace injury records; workplace violence prevention and handling procedure; infection-control occupational response (HIC.4)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the HR office.

Copies issued to: department heads; all staff areas.

The current version is available to all staff at the {D('HR office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """HIC — Hospital Infection Control (NABH SHCO chapter 4)
HRM — Human Resource Management (NABH SHCO chapter 8)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PEP — post-exposure prophylaxis
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HRM.5.a",
        "requirement": "Staff well-being is promoted through identification of health problems of the staff, including occupational health hazards, in accordance with the organisation's policy.",
        "steps": "Statement of intent; Section 3; 5.1 Staff well-being and occupational health hazard identification; Section 4 item 1",
        "responsible": "HR In-Charge / Personnel Officer (register); department heads (report hazards)",
        "records": [
            "Occupational health policy aligned with organisation's hazard identification approach.",
            "Occupational health hazard register updated annually or when new hazards identified.",
            "Cross-reference to HIC.4 for infection-specific exposure (not duplicated here).",
        ],
    },
    {
        "oe_code": "HRM.5.b",
        "requirement": "Health checks of staff are done at least once a year and the findings/results are documented.",
        "steps": "Section 3; 5.2 Annual health checks; Section 4 items 2 and 3",
        "responsible": "HR In-Charge / Personnel Officer (schedule and file); Medical Superintendent (abnormal findings)",
        "records": [
            "Annual health check schedule covering all active staff.",
            "Standard health check form with findings for each staff member.",
            "Follow-up and referral records for abnormal findings.",
        ],
    },
    {
        "oe_code": "HRM.5.c",
        "requirement": "Organisation provides treatment to staff who sustain workplace-related injuries.",
        "steps": "Section 3; 5.3 Treatment for workplace-related injuries; Section 4 item 4",
        "responsible": "Medical Superintendent (ensure treatment); HR In-Charge / Personnel Officer (document)",
        "records": [
            "Workplace injury reporting and treatment procedure.",
            "Injury records with first aid, medical assessment and treatment provided.",
            "Return-to-work assessment records.",
        ],
    },
    {
        "oe_code": "HRM.5.d",
        "requirement": "The organisation has measures in place for preventing and handling workplace violence.",
        "steps": "Section 3; 5.4 Workplace violence prevention and handling; Section 4 item 5",
        "responsible": "Medical Superintendent (approve measures); HR In-Charge / Personnel Officer (communicate and document)",
        "records": [
            "Workplace violence prevention and handling procedure.",
            "Staff training records on de-escalation and violence response.",
            "Incident documentation and post-event review records.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.5 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: HRM.5.a–d PDF index 131. No asterisked OEs. HRM.5.a/c Commitment; HRM.5.b/d Core.

SHAPE: Four What-we-do subsections (5.1–5.4). No stop-work. Disclaimer accreditation-only. HR roles only. HIC.4 boundary stated for infection-specific exposure; general occupational health owned here."""


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
        "template_test": "hrm_v2_adoptable_shape",
        "subtitle": "Staff well-being, health checks, injury treatment and violence prevention.",
        "doc_no": D("HRM/POL/05"),
    }
    emit_pre_v2(
        draft,
        "hrm5_v2_draft.json",
        "HRM.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
