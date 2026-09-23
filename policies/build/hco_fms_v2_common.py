# -*- coding: utf-8 -*-
"""Shared helpers for HCO Full FMS.1–FMS.7 v2 builders.

Always pass draft_label via hco_document_control — never
pre_v2_common.document_control() (that still injects
\"not an approved master\").

HCO 6th Edition chapter name is FMS (Facility Management and Safety).
"""
from __future__ import annotations

from hco_cop_v2_common import DRAFT_LABEL, CHAPTER, VERSION, PROGRAMME, hco_document_control
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL

# Standards where Stop-work is proposed (judgment calls — see chapter notes).
STOP_WORK_PROPOSALS: dict[int, str] = {
    2: "Start or continue clinical care in an area without potable water or electricity (unless the FMS.7 emergency continuity plan is running)",
    3: "Use a hazardous material that is not identified, or for which there is no implemented spill plan",
    4: "Run critical utility equipment that has no implemented operational and maintenance plan, or that is known unsafe",
    5: "Use medical equipment that is past due preventive maintenance or calibration, or that is under an open recall or hazard notice",
    6: "Use a medical-gas outlet or manifold with a live leak, a silenced required alarm, or no required alternate source",
    7: "Occupy a patient-care floor without the required fire detection, abatement or evacuation provision, or without a displayed exit plan",
}


def stop_work_text(n: int) -> str:
    """Hospital-facing Stop-work section for flagged FMS standards."""
    eng = D("Engineering In-Charge")
    ms = D("Medical Superintendent")
    texts = {
        2: f"""Do not start or continue clinical care in an area that has no potable water or no electricity, unless the organisation has declared a FMS.7 emergency and the written service-continuity plan for that failure is running.

Stop-work applies to starting or continuing routine care in that area. Immediate life-saving care continues while water or power is restored or the patient is moved.

The person who stops tells the {eng} and the {ms} the same shift. Refusing to run care without water or power is not a disciplinary matter.""",
        3: f"""Do not use a hazardous material that has not been identified, or for which the spill plan is not implemented (no Material Safety Data Sheet path, no kit, or staff not trained for that material).

Stop-work applies to using that material. Immediate life-saving care that already depends on a stocked clinical product continues while the spill path is restored.

The person who stops tells the {eng} and the {ms} the same shift. Refusing an unidentified hazardous material is not a disciplinary matter.""",
        4: f"""Do not run critical utility equipment (as this hospital names it: at a minimum diesel generator, lifts, uninterruptible power supply, fire-related utility, reverse-osmosis plant for dialysis, water pumps) when there is no implemented operational and maintenance plan, or when the equipment is known unsafe.

Stop-work applies to starting or continuing that equipment. Life-saving care continues under the FMS.7 continuity plan.

The person who stops tells the {eng} and the {ms} the same shift. Refusing unsafe utility equipment is not a disciplinary matter.""",
        5: f"""Do not use medical equipment that is past the due date for preventive maintenance or calibration, or that is under an open manufacturer or regulatory recall or hazard notice.

Stop-work applies to putting that equipment into clinical use. Immediate life-saving care uses the next safe alternative and is documented.

The person who stops tells the {eng} and the {ms} the same shift. Refusing overdue or recalled equipment is not a disciplinary matter.""",
        6: f"""Do not use a medical-gas outlet or manifold when there is a live leak, a required alarm that has been silenced without a recorded reason, or no required alternate source for that gas, vacuum or compressed air.

Stop-work applies to using that outlet or manifold. Immediate life-saving care uses cylinders or the written alternate source.

The person who stops tells the {eng} and the {ms} the same shift. Refusing an unsafe gas outlet is not a disciplinary matter.""",
        7: f"""Do not occupy a patient-care floor when required fire detection, abatement or evacuation provision is not in place, or when the exit plan for that floor is not displayed.

Stop-work applies to placing or keeping patients on that floor as a planned location of care. Immediate life-saving evacuation and life-saving care continue.

The person who stops tells the {eng} and the {ms} the same shift. Refusing to occupy an unprotected floor is not a disciplinary matter.""",
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
