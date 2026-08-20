# -*- coding: utf-8 -*-
"""Shared helpers for HCO Full COP.1–COP.20 v2 builders.

Always pass draft_label explicitly — never rely on the PRE default in
document_control(). Version line intentionally omits the legacy
\"not an approved master\" template leftover (renderer italic already cleaned).
"""
from __future__ import annotations

from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL

DRAFT_LABEL = "HCO Full v2 draft"
CHAPTER = "HCO"
VERSION = "2.0"
PROGRAMME = "HCO Full Accreditation, 6th Edition"


def hco_document_control(*, doc_no: str, prepared_by: str) -> str:
    """Document-control block with explicit HCO draft label and no leftover phrase."""
    return f"""Document number: {doc_no}
Issue number: {D('01')}
Version: {VERSION} ({DRAFT_LABEL})
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {prepared_by}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """


# Standards where Stop-work is proposed (judgment calls — see handoff).
# Values are short internal reasons, not hospital-facing text.
STOP_WORK_PROPOSALS: dict[int, str] = {
    2: "Emergency overcrowding / missing triage competence / dead-on-arrival pathway gaps",
    3: "Ambulance departure without functioning equipment, competent crew, or communication link",
    5: "CPR without named team roles, emergency drugs/equipment, or post-event documentation trigger",
    7: "Clinical procedure without clinical need, written guidance, or qualified performers",
    8: "Transfusion without two-identifier check, compatibility, or informed consent where required",
    9: "ICU/HDU admission beyond defined criteria / without competent staffing or monitoring",
    12: "Procedural sedation without pre-sedation assessment, monitoring, or recovery criteria",
    13: "Anaesthesia without documented pre-anaesthesia/pre-induction assessment or required monitoring",
    14: "Surgery without site/procedure verification or incomplete surgical safety checks",
    16: "High-risk care (falls/pressure/DVT/restraints/vulnerable) without identification and precautions",
}


def stop_work_text(n: int) -> str:
    """Hospital-facing Stop-work section for flagged COP standards."""
    texts = {
        2: f"""Do not receive and treat an emergency patient in an area that is not the identified emergency area, or when triage-competent personnel and basic resuscitation equipment are not available.

Do not leave overcrowding unmanaged when it blocks triage, resuscitation or safe holding.

Stop-work applies to unsafe emergency intake, not to immediate life-saving measures already under way — those continue while escalation happens.

The person who stops tells the {D('Emergency In-Charge')} and the {D('Medical Superintendent')} the same shift. Refusing unsafe emergency intake is not a disciplinary matter.""",
        3: f"""Do not dispatch or continue an ambulance transfer when the vehicle fails its readiness check, required equipment is non-functional, the driver is not licensed for the vehicle class, or the organisation/control-room communication link is down.

Stop-work applies to the transfer dispatch, not to on-scene life-saving measures.

The person who stops tells the {D('Ambulance / Transport In-Charge')} and the {D('Medical Superintendent')} the same shift. Refusing an unsafe ambulance dispatch is not a disciplinary matter.""",
        5: f"""Do not start a planned resuscitation response (or mock drill counted as CPR competence evidence) without a named CPR team with clear roles and without the minimum emergency medications and equipment available at the location.

Stop-work does not block an unexpected cardiac arrest already in progress — start CPR with available staff and escalate for equipment/team immediately.

The person responsible tells the {D('CPR Committee chair / Emergency In-Charge')} the same shift. Refusing to run a hollow CPR response is not a disciplinary matter.""",
        7: f"""Do not perform a clinical procedure that is not based on the patient's clinical need, or that lacks written guidance where required, or that is ordered/performed/assisted by personnel not qualified for that procedure.

Stop-work applies to the elective or non-emergent procedure start. Emergent life-saving procedures continue with the best available qualified help and are documented afterward.

The person who stops tells the {D('treating doctor')} and the {D('Medical Superintendent')} the same shift. Refusing an unsafe procedure is not a disciplinary matter.""",
        8: f"""Do not start transfusion of blood or blood components when patient identification (minimum two identifiers) is incomplete, compatibility checks are missing, or required informed consent has not been obtained (except where emergency transfusion rules documented by the organisation apply).

Stop-work applies to the transfusion start. Life-saving emergency transfusion follows the organisation's emergency-transfusion written guidance and is documented.

The person who stops tells the {D('Transfusion / Blood Bank In-Charge')} and the {D('treating doctor')} the same shift. Refusing an unsafe transfusion is not a disciplinary matter.""",
        9: f"""Do not admit a patient to ICU/HDU outside defined admission criteria, or when required monitoring and competent staffing for that level of care are not available.

Stop-work applies to the ICU/HDU bed allocation. Stabilisation in the best available supervised area continues while escalation for a safe bed happens.

The person who stops tells the {D('ICU In-Charge')} and the {D('Medical Superintendent')} the same shift. Refusing an unsafe critical-care admission is not a disciplinary matter.""",
        12: f"""Do not begin procedural sedation when pre-sedation assessment is incomplete, required monitoring is unavailable, or recovery/discharge criteria are not defined for the location.

Stop-work applies to sedation start, not to airway rescue already in progress.

The person who stops tells the {D('sedation privileged doctor')} and the {D('Medical Superintendent')} the same shift. Refusing unsafe sedation is not a disciplinary matter.""",
        13: f"""Do not induce anaesthesia when the pre-anaesthesia assessment and anaesthesia plan are not documented, when pre-induction assessment is not documented, or when required intra-operative monitoring (including ETCO2 where applicable) cannot be provided.

Stop-work applies to induction. Immediate life-saving operative care follows emergency anaesthesia rules documented by the organisation.

The person who stops tells the {D('Anaesthesiologist / OT In-Charge')} the same shift. Refusing unsafe induction is not a disciplinary matter.""",
        14: f"""Do not make the incision or start the interventional procedure when site/procedure/patient verification is incomplete or when required surgical-safety checks for the case are not done.

Stop-work applies to incision/start. Immediate life-saving surgery continues with verification completed at the earliest safe pause and documented.

The person who stops tells the {D('Surgeon / OT In-Charge')} the same shift. Refusing to start without verification is not a disciplinary matter.""",
        16: f"""Do not leave a patient identified as vulnerable, at fall risk, at pressure-ulcer risk, at DVT risk, or needing restraints without the precautions and monitoring required by the organisation's written guidance.

Do not apply or continue restraints without a documented clinical order and ongoing review.

Stop-work applies to missing precautions / unauthorised restraint — not to emergency physical intervention needed to prevent immediate harm, which is followed at once by documentation and medical review.

The person who stops tells the {D('treating doctor')} and the {D('Ward / ICU In-Charge')} the same shift. Refusing to leave high-risk patients unprotected is not a disciplinary matter.""",
    }
    return texts.get(n, "")


__all__ = [
    "BLANK",
    "D",
    "HOSPITAL",
    "HCO_EDITION_LABEL",
    "DRAFT_LABEL",
    "CHAPTER",
    "VERSION",
    "PROGRAMME",
    "hco_document_control",
    "STOP_WORK_PROPOSALS",
    "stop_work_text",
]
