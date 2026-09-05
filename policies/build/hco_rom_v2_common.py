# -*- coding: utf-8 -*-
"""Shared helpers for HCO Full ROM.1–ROM.6 v2 builders.

Always pass draft_label via hco_document_control — never
pre_v2_common.document_control() (that still injects
\"not an approved master\").

HCO 6th Edition chapter name is ROM (Responsibilities of Management).
"""
from __future__ import annotations

from hco_cop_v2_common import DRAFT_LABEL, CHAPTER, VERSION, PROGRAMME, hco_document_control
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL

# Standards where Stop-work is proposed (judgment calls — see chapter notes).
STOP_WORK_PROPOSALS: dict[int, str] = {
    6: "Start or continue an outsourced service without a documented agreement including service parameters; skip required internal/external reporting of a system or process failure",
}


def stop_work_text(n: int) -> str:
    """Hospital-facing Stop-work section for flagged ROM standards."""
    texts = {
        6: f"""Do not start or continue an outsourced service when there is no documented agreement that includes service parameters (quality, numbers, reports, timelines and how disputes are resolved).

Do not skip the organisation's internal or external reporting path for a system or process failure that the written guidance requires to be reported.

Stop-work applies to the outsourced-service start/continue and to delay of required failure reporting. Immediate life-saving care continues.

The person who stops tells the {D('Medical Superintendent')} the same shift. Refusing to start an unsigned outsourced service, or reporting a system failure, is not a disciplinary matter.""",
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
