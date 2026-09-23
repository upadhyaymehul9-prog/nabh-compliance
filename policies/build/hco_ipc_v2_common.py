# -*- coding: utf-8 -*-
"""Shared helpers for HCO Full IPC.1–IPC.8 v2 builders.

Always pass draft_label via hco_document_control — never
pre_v2_common.document_control() (that still injects
\"not an approved master\").

HCO 6th Edition chapter name is IPC (Infection Prevention and Control).
Do not use HIC in HCO output.
"""
from __future__ import annotations

from hco_cop_v2_common import DRAFT_LABEL, CHAPTER, VERSION, PROGRAMME, hco_document_control
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL

# Standards where Stop-work is proposed (judgment calls — see chapter notes).
STOP_WORK_PROPOSALS: dict[int, str] = {
    3: "Start a procedure without standard precautions / hand hygiene / safe injection; restricted antimicrobial without the stewardship path",
    4: "Handle BMW without required segregation or PPE; start construction/renovation without the infection-risk plan",
    5: "Insert a urinary catheter, central line, or start ventilation / an operation without the HAI-prevention bundle in place",
    7: "Issue an item when sterilisation validation failed or a recall is in effect",
    8: "Continue duty against a work restriction; skip post-exposure prophylaxis after a blood/body-fluid exposure",
}


def stop_work_text(n: int) -> str:
    """Hospital-facing Stop-work section for flagged IPC standards."""
    texts = {
        3: f"""Do not start a clinical procedure when standard precautions are not in place (PPE, sharps safety, cough etiquette as the situation requires), when hand hygiene has not been done at the required moment, or when injection/infusion practice would reuse a needle or syringe.

Do not start a restricted antimicrobial without the organisation's antimicrobial-stewardship path (documented indication and, where required, approval).

Stop-work applies to the procedure or first dose start. Immediate life-saving care continues with the best available precautions and is documented.

The person who stops tells the {D('treating doctor')} and the {D('Infection Prevention and Control Officer')} the same shift. Refusing an unsafe start is not a disciplinary matter.""",
        4: f"""Do not handle biomedical waste without the required colour-coded segregation and PPE.

Do not start construction or renovation in a patient-care area until the infection-risk plan for that work has been completed and the {D('Infection Prevention and Control Officer')} has agreed the controls.

Stop-work applies to the waste-handling act and to the construction/renovation start. Emergency repair that cannot wait follows the documented emergency-works IPC controls and is recorded.

The person who stops tells the {D('Infection Prevention and Control Officer')} and the {D('Medical Superintendent')} the same shift. Refusing unsafe waste handling or unplanned works is not a disciplinary matter.""",
        5: f"""Do not insert an indwelling urinary catheter, insert a central line, start invasive ventilation, or make a surgical incision unless the organisation's prevention bundle for that HAI (CAUTI, CLABSI, VAP or SSI) is in place for this patient.

Stop-work applies to the device insertion or incision. Life-saving airway or haemorrhage control continues with the best available precautions and the bundle is completed as soon as the patient is stable.

The person who stops tells the {D('treating doctor')} and the {D('Infection Prevention and Control Officer')} the same shift. Refusing an insertion without the bundle is not a disciplinary matter.""",
        7: f"""Do not issue an instrument, device or pack from sterile storage when validation of that sterilisation load has failed, or when a recall of that load or machine is in effect.

Stop-work applies to issue from CSSD / sterile store. Immediate life-saving use of the only available item is documented and the {D('CSSD In-Charge')} is told the same shift.

The person who stops tells the {D('CSSD In-Charge')} and the {D('Infection Prevention and Control Officer')} the same shift. Refusing to issue a failed or recalled load is not a disciplinary matter.""",
        8: f"""Do not continue clinical duty when a work restriction for a transmissible infection applies to you.

Do not leave a blood or body-fluid exposure (including a needle-stick) without starting the organisation's post-exposure path the same shift.

Stop-work applies to the restricted duty and to delay of PEP. Immediate first aid at the exposure site starts at once.

The person who stops (or the colleague who sees the restriction being ignored) tells the {D('Occupational Health Physician')} and the {D('Infection Prevention and Control Officer')} the same shift. Reporting an exposure or observing a restriction is not a disciplinary matter.""",
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
