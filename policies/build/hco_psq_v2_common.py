# -*- coding: utf-8 -*-
"""Shared helpers for HCO Full PSQ.1–PSQ.7 v2 builders.

Always pass draft_label via hco_document_control — never
pre_v2_common.document_control() (that still injects
\"not an approved master\").

HCO 6th Edition chapter name is PSQ (Patient Safety and Quality Improvement).
"""
from __future__ import annotations

from hco_cop_v2_common import DRAFT_LABEL, CHAPTER, VERSION, PROGRAMME, hco_document_control
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL

# Standards where Stop-work is proposed (judgment calls — see chapter notes).
STOP_WORK_PROPOSALS: dict[int, str] = {
    7: "Continue a process after a sentinel event without agreed controls; skip identification, reporting or analysis of a sentinel event",
}


def stop_work_text(n: int) -> str:
    """Hospital-facing Stop-work section for flagged PSQ standards."""
    texts = {
        7: f"""Do not leave a sentinel event unidentified or unreported once it is recognised.

Do not skip the organisation's analysis of a sentinel event (or of another incident the written guidance requires to be analysed).

Do not continue a process that analysis has shown caused a sentinel event until the agreed corrective action is in place, except immediate life-saving care.

Stop-work applies to delay of identification, reporting or analysis, and to continuing the unsafe process. Immediate life-saving care continues with the best available controls and is documented.

The person who stops tells the {D('Patient Safety Officer')} and the {D('Medical Superintendent')} the same shift. Reporting a sentinel event or refusing to continue an unsafe process is not a disciplinary matter.""",
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
