# -*- coding: utf-8 -*-
"""Reconciliation 3/4: narrow HIC.3's environmental surface sampling to match HIC.5.

Todo item (scripts/master-policy-todos.md, "HIC.3 promises a record the hospital does not
routinely produce — environmental surface swabs"):
  "Narrow HIC.3's HIC.3.c evidence list to the objective cleaning-outcome monitoring HIC.5 step 27
   actually produces (fluorescent marker or ATP pass rates), and re-point HIC.3's environmental
   sampling text at the trigger list in HIC.5 step 28 rather than describing it as routine."
  "HIC.5's position is the better-supported one and should win."

THE CONTRADICTION SITS IN THREE PLACES, not the two the todo names. Verified 2026-08-13:
  1. HIC.3.c evidence ends "...; environmental surface swab results"        <- todo names this
  2. HIC.3 step 5 bullet: routine "surface swab sampling ... at an interval" <- todo names this
  3. HIC.3.a evidence: "environmental air AND SURFACE sampling results"      <- todo does NOT
Leaving (3) would mean the pass did not actually resolve the contradiction, so it is fixed too.
Surface culturing does not belong under engineering controls in any case.

WHAT IS DELIBERATELY KEPT. HIC.5 step 28 expressly routes the parameters and frequencies for
critical-system monitoring — OT air, ventilation validation, dialysis water, potable water — to
"the support services policy and the facility policies", i.e. to HIC.3, and says HIC.5 "receives
the results and trends them rather than setting the parameters". So HIC.3 step 5 keeps its air
sampling, temperature and humidity, pressure differential and water sampling bullets untouched.
Only surface culturing is narrowed. The todo's own closing note says the same: "Do not move them."

PLACEHOLDER COUNT KNOCK-ON. Removing the routine surface-swab interval removes one
"[Hospital to define]". HIC.3's checklist already claimed a wrong figure — it said 38 when the
true count was 40 (a separate deferred item in this same file, logged 2026-08-06). Rather than
leave a number that is now wrong for two independent reasons, the figure is set to the correct
post-edit value of 39. That closes the separate item as a side effect.
"""
import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
DRAFT = _HERE.parent / "drafts" / "hic3_draft.json"

EM = "—"

OLD_STEP_5 = """5. Environmental surveillance of critical areas

{{HOSPITAL_NAME}} monitors the environment of its critical areas so that deterioration is detected before it causes infection rather than after.

Environmental surveillance comprises:

- microbiological air sampling of operating theatres and other critical areas at an interval of [Hospital to define], with the sampling method, plate positions and acceptance limits stated in writing before sampling begins;
- surface swab sampling in operating theatres, critical care and procedure rooms at an interval of [Hospital to define], concentrated on high-touch surfaces and on equipment in contact with patients;
- continuous or logged monitoring of temperature and relative humidity in theatres and critical care, reviewed daily;
- verification of pressure differentials and air change rates as set out in step 4;
- water sampling as set out in step 6.

Results are reported to the Infection Control Team and reviewed at the Infection Prevention and Control Committee alongside infection data, so that an environmental trend and a clinical trend can be read against each other.

An out-of-limit result is not a filing matter. It generates a recorded investigation of the probable cause, a corrective action with a named owner and a date, and a repeat sample confirming the correction. Where the result concerns an area in active clinical use, the Infection Control Officer decides whether use continues meanwhile and records the decision and its basis.

Routine environmental sampling is a monitoring tool, not a substitute for cleaning and maintenance; {{HOSPITAL_NAME}} does not treat a passing plate count as evidence that its procedures are being followed."""

NEW_STEP_5 = """5. Environmental surveillance of critical areas

{{HOSPITAL_NAME}} monitors the environment of its critical areas so that deterioration is detected before it causes infection rather than after.

Environmental surveillance comprises:

- microbiological air sampling of operating theatres and other critical areas at an interval of [Hospital to define], with the sampling method, plate positions and acceptance limits stated in writing before sampling begins;
- continuous or logged monitoring of temperature and relative humidity in theatres and critical care, reviewed daily;
- verification of pressure differentials and air change rates as set out in step 4;
- water sampling as set out in step 6.

Surface culturing is deliberately absent from that list. {{HOSPITAL_NAME}} does not perform routine untargeted surface sampling: a colony count taken from a general surface has no established relationship to patient infection, there is no agreed action threshold for most surfaces, and a low count is not evidence that cleaning is being carried out {EM} which is precisely the inference a routine swabbing schedule invites. Surface sampling is performed only against a defined trigger: an outbreak investigation that has generated a hypothesis naming the organism sought in advance; clearance after construction, renovation or a repair affecting a critical area; suspected contamination of a product, device or process; or direction by the competent health authority. Those triggers, and the record required with every sample taken, are set out in the hospital's surveillance policy, which owns this subject, and are not restated here.

Whether the housekeeping procedure at steps 13 to 19 is actually being carried out is measured instead by objective thoroughness monitoring {EM} a fluorescent marking gel or adenosine triphosphate bioluminescence, read as a pass rate by area and by surface type {EM} which the hospital's surveillance policy owns and this policy does not duplicate.

Results are reported to the Infection Control Team and reviewed at the Infection Prevention and Control Committee alongside infection data, so that an environmental trend and a clinical trend can be read against each other.

An out-of-limit result is not a filing matter. It generates a recorded investigation of the probable cause, a corrective action with a named owner and a date, and a repeat sample confirming the correction. Where the result concerns an area in active clinical use, the Infection Control Officer decides whether use continues meanwhile and records the decision and its basis.

Environmental sampling is a monitoring tool, not a substitute for cleaning and maintenance; {{HOSPITAL_NAME}} does not treat a passing plate count as evidence that its procedures are being followed.""".replace("{EM}", EM)

OLD_EV_C = "supervisor and Infection Control Nurse inspection reports; environmental surface swab results"
NEW_EV_C = (
    "supervisor and Infection Control Nurse inspection reports; objective cleaning-thoroughness "
    "results using a fluorescent marking gel or adenosine triphosphate bioluminescence, expressed "
    "as a pass rate by area and by surface type, with the method in use and any numeric threshold "
    "stated alongside the result"
)

OLD_EV_A = "environmental air and surface sampling results with corrective actions"
NEW_EV_A = "environmental air sampling results with corrective actions"

OLD_UFC = "HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] " + EM + " 38 occurrences across:"
NEW_UFC = (
    "HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] " + EM + " 39 occurrences across:"
)

# A fourth reference the todo did not name: the checklist's provenance note recording what step 5
# absorbed from the tracker when HIC.3 was drafted. It still listed "surface swabs", which is now
# untrue of step 5. Amended with a dated note rather than silently deleted, because it is a
# historical record of how the document was built and the change is worth seeing.
OLD_PROV = (
    "environmental surveillance (OT air sampling, HEPA integrity, temperature and humidity "
    "monitoring, surface swabs), which the HIC.1 draft carried as a pointer only and which is now "
    "written out at step 5 under HIC.3.a engineering controls."
)
NEW_PROV = (
    "environmental surveillance (OT air sampling, HEPA integrity, temperature and humidity "
    "monitoring), which the HIC.1 draft carried as a pointer only and which is now written out at "
    "step 5 under HIC.3.a engineering controls. AMENDED 2026-08-13 in the reconciliation pass: "
    "step 5 originally also carried routine surface swab sampling on a fixed interval. That "
    "contradicted the approved HIC.5 step 28, which states that {{HOSPITAL_NAME}} does not perform "
    "routine untargeted environmental culturing and restricts surface sampling to defined "
    "triggers. HIC.5's position is the better-supported one " + EM + " CDC environmental infection "
    "control guidance establishes no relationship between general-area surface counts and patient "
    "infection, and there are no agreed action thresholds for most surfaces " + EM + " so step 5 "
    "was narrowed to match it and now points at HIC.5 for the trigger list. Objective "
    "cleaning-thoroughness monitoring (fluorescent marker or ATP pass rate) replaced surface swab "
    "results in the HIC.3.c evidence column, and 'and surface' was struck from the HIC.3.a "
    "evidence column. The placeholder figure above moved from 40 to 39 because the routine "
    "surface-swab interval was removed; it had also been recorded incorrectly as 38, which is "
    "corrected in the same edit."
)


def main() -> None:
    draft = json.loads(DRAFT.read_text(encoding="utf-8"))
    steps = draft["procedure_steps"]

    if steps[4] != OLD_STEP_5:
        raise SystemExit("HIC.3 step 5 does not match the approved text — re-read before editing")
    steps[4] = NEW_STEP_5

    for code, old, new in (("HIC.3.c", OLD_EV_C, NEW_EV_C), ("HIC.3.a", OLD_EV_A, NEW_EV_A)):
        m = next(x for x in draft["oe_mapping"] if x["oe_code"] == code)
        if m["evidence"].count(old) != 1:
            raise SystemExit(f"{code}: evidence fragment not found exactly once")
        m["evidence"] = m["evidence"].replace(old, new)

    for old, new, label in (
        (OLD_UFC, NEW_UFC, "placeholder figure"),
        (OLD_PROV, NEW_PROV, "provenance note"),
    ):
        if draft["universal_facts_checklist"].count(old) != 1:
            raise SystemExit(f"checklist {label} not found exactly once — re-read before editing")
        draft["universal_facts_checklist"] = draft["universal_facts_checklist"].replace(old, new)

    blob = json.dumps(draft, ensure_ascii=False)
    if blob.count("{HOSPITAL_NAME}") - blob.count("{{HOSPITAL_NAME}}"):
        raise SystemExit("single-braced {HOSPITAL_NAME} present — would render literally")
    # Police the OPERATIVE content only. universal_facts_checklist is an internal review field,
    # is not rendered into the DOCX, and legitimately describes what was removed and why — so the
    # phrase is expected there and nowhere else.
    operative = json.dumps(
        {"procedure_steps": draft["procedure_steps"], "oe_mapping": draft["oe_mapping"]},
        ensure_ascii=False,
    )
    if "surface swab" in operative.lower():
        raise SystemExit(
            "'surface swab' still present in procedure_steps or oe_mapping — contradiction not closed"
        )

    DRAFT.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"step 5: {len(OLD_STEP_5)} -> {len(NEW_STEP_5)} chars")
    print(f"steps: {len(steps)} (unchanged)")


if __name__ == "__main__":
    main()
