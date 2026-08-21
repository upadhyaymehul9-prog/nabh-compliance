# -*- coding: utf-8 -*-
"""Shared helpers for HCO Full HRM.1–HRM.13 v2 builders.

Always pass draft_label via hco_document_control — never
pre_v2_common.document_control() (that still injects
\"not an approved master\").

HCO 6th Edition chapter name is HRM (Human Resource Management). Do not
confuse with the already-deployed SHCO 3rd Edition HRM chapter
(build_hrm1_v2.py..build_hrm9_v2.py, policies/drafts/hrm*_v2_draft.json) —
separate programme, separate edition, separate OE set.
"""
from __future__ import annotations

from hco_cop_v2_common import DRAFT_LABEL, CHAPTER, VERSION, PROGRAMME, hco_document_control
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL

# Standards where Stop-work is proposed (judgment calls — see chapter notes).
# HRM's subject is workforce administration, not equipment or environment, so
# it does not carry FMS/ROM-style mechanical gates. The one place the
# standard's own wording creates a hard go/no-go is credentialing and
# privileging: HRM.11-13 are each titled "...permitted to provide patient
# care without supervision", and CORE OE (a) in each requires that those
# professionals be identified.
STOP_WORK_PROPOSALS: dict[int, str] = {
    11: "A medical professional not on the organisation's identified and privileged list provides patient care without supervision",
    12: "A nursing professional not on the organisation's identified and privileged list provides patient care without supervision",
    13: "A para-clinical professional not on the organisation's identified and privileged list provides patient care without supervision",
}


def stop_work_text(n: int) -> str:
    """Hospital-facing Stop-work section for flagged HRM standards."""
    hr = D("HR In-Charge / Personnel Officer")
    ms = D("Medical Superintendent")
    texts = {
        11: f"""Do not let a medical professional provide patient care without supervision unless the {hr} and the credentialing file show that professional identified and privileged for that care under HRM.11.

Stop-work applies to starting or continuing unsupervised care by that professional. Care already under way is handed to a privileged professional or brought under supervision; immediate life-saving care is not withdrawn while that handover happens.

The person who stops tells the {hr} and the {ms} the same shift. Refusing to let an uncredentialed or unprivileged professional practise unsupervised is not a disciplinary matter.""",
        12: f"""Do not let a nursing professional provide patient care without supervision unless the {hr} and the credentialing file show that professional identified and privileged for that care under HRM.12.

Stop-work applies to starting or continuing unsupervised care by that professional. Care already under way is handed to a privileged professional or brought under supervision; immediate life-saving care is not withdrawn while that handover happens.

The person who stops tells the {hr} and the {ms} the same shift. Refusing to let an uncredentialed or unprivileged professional practise unsupervised is not a disciplinary matter.""",
        13: f"""Do not let a para-clinical professional provide patient care without supervision unless the {hr} and the credentialing file show that professional identified and privileged for that care under HRM.13.

Stop-work applies to starting or continuing unsupervised care by that professional. Care already under way is handed to a privileged professional or brought under supervision; immediate life-saving care is not withdrawn while that handover happens.

The person who stops tells the {hr} and the {ms} the same shift. Refusing to let an uncredentialed or unprivileged professional practise unsupervised is not a disciplinary matter.""",
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
