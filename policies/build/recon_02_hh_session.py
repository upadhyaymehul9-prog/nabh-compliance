# -*- coding: utf-8 -*-
"""Reconciliation 2/4: adopt HIC.2's hand hygiene session length in HIC.5.

Todo item (scripts/master-policy-todos.md, "HIC.5.b vs approved HIC.2 step 9"):
  "**Divergence:** HIC.2 states a session length ('approximately 20 minutes, plus or minus 10');
   HIC.5 step 20 deliberately states only 'a defined and limited length', to avoid creating a
   second and potentially divergent number. Not a contradiction — one specific, one general.
   Likely target wording is HIC.2's, adopted in both."

HIC.2 already carries the figure, so only HIC.5 changes. HIC.2 step 9 reads "each session runs
for approximately 20 minutes (plus or minus 10 minutes) so the observer can record accurately";
HIC.5 now states the same figure in its own sentence structure.

A cross-reference sentence is added for the same reason HIC.5 carries one on the outbreak
definition: the whole point of this pass is that two numbers in two policies of the same hospital
must not be allowed to drift apart silently. HIC.5's established name for HIC.2 is "the infection
prevention and control practices policy" — matched here rather than invented.
"""
import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
DRAFT = _HERE.parent / "drafts" / "hic5_draft.json"

OLD = (
    "Sessions are of a defined and limited length so that the observer records accurately, and "
    "are spread across shifts, days of the week and times of day rather than concentrated in the "
    "quiet hours of a weekday morning, which produces a flattering and useless figure."
)

NEW = (
    "Sessions run for approximately 20 minutes, plus or minus 10 minutes, so that the observer "
    "records accurately, and are spread across shifts, days of the week and times of day rather "
    "than concentrated in the quiet hours of a weekday morning, which produces a flattering and "
    "useless figure. That session length is the same figure, in the same words, as the infection "
    "prevention and control practices policy of {{HOSPITAL_NAME}}; if either document changes it, "
    "the other is changed in the same pass."
)


def main() -> None:
    draft = json.loads(DRAFT.read_text(encoding="utf-8"))
    steps = draft["procedure_steps"]

    if steps[19].count(OLD) != 1:
        raise SystemExit("HIC.5 step 20 sentence not found exactly once — re-read before editing")
    steps[19] = steps[19].replace(OLD, NEW)

    blob = json.dumps(draft, ensure_ascii=False)
    if blob.count("{HOSPITAL_NAME}") - blob.count("{{HOSPITAL_NAME}}"):
        raise SystemExit("single-braced {HOSPITAL_NAME} present — would render literally")

    DRAFT.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"HIC.5 step 20: {len(steps[19])} chars, {len(steps)} steps (unchanged)")


if __name__ == "__main__":
    main()
