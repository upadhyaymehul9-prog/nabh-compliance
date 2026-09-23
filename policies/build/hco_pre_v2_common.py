# -*- coding: utf-8 -*-
"""Shared helpers for HCO Full PRE.1–PRE.8 v2 builders.

Always pass draft_label via hco_document_control — never
pre_v2_common.document_control() (that still injects
\"not an approved master\").
"""
from __future__ import annotations

from hco_cop_v2_common import DRAFT_LABEL, CHAPTER, VERSION, PROGRAMME, hco_document_control
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL

# Standards where Stop-work is proposed (judgment calls — see chapter notes).
STOP_WORK_PROPOSALS: dict[int, str] = {
    2: "Neglect or abuse; examination/procedure without privacy and dignity; listed invasive care without informed consent",
    4: "Start a listed procedure without valid informed consent from the person who may consent",
}


def stop_work_text(n: int) -> str:
    """Hospital-facing Stop-work section for flagged PRE standards."""
    texts = {
        2: f"""Do not continue an examination, procedure or treatment that exposes the patient beyond what the procedure requires, or that leaves the patient without privacy (screens, drapes, closed door or equivalent).

Do not leave a patient in a situation of neglect or abuse (unattended fall risk, unwarranted repeated examination, manhandling, or failure to protect a vulnerable patient). Stop the unsafe situation, protect the patient, and report it the same shift.

Do not start transfusion of blood or blood components, anaesthesia, surgery, a research protocol, or any other invasive / high-risk procedure / treatment without informed consent obtained under PRE.4 (except where this policy's documented emergency-life-saving rule applies).

Stop-work applies to the examination or procedure start. Immediate life-saving measures continue while escalation happens, and are documented.

The person who stops tells the {D('treating doctor')} and the {D('Medical Superintendent')} the same shift. Refusing an unsafe examination or a procedure without consent is not a disciplinary matter.""",
        4: f"""Do not start a procedure on the organisation's informed-consent list until valid informed consent has been obtained from the patient, or from the person who may consent when the patient is incapable of independent decision-making, in a language they can understand.

Do not accept a consent form signed by a nurse or clerk as the only consent when the person performing the procedure (or a doctor member of that team) has not explained the procedure, its risks, benefits, alternatives and who will perform it.

Stop-work applies to the procedure start. Immediate life-saving care when the patient is incapable and next of kin is not available follows the two-clinician emergency rule in section 5, and is documented the same shift.

The person who stops tells the {D('person performing the procedure')} and the {D('Medical Superintendent')} the same shift. Refusing to start without valid consent is not a disciplinary matter.""",
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
