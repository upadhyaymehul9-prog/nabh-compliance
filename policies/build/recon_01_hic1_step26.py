# -*- coding: utf-8 -*-
"""Reconciliation 1/4: reduce HIC.1 step 26 to a pointer at the surveillance policy.

Todo item (scripts/master-policy-todos.md, "HIC.5.d vs approved HIC.1 steps 25-26"):
  "the two outbreak definitions are consistent in substance but separately worded — make them
   identical, and reduce HIC.1 step 26 to a pointer once HIC.5 is approved. Also align HIC.1's
   'report to the ICO on the same day it is suspected' with HIC.5 step 31's 'on the day the
   suspicion arises' — same rule, different words."

TWO OF THE THREE SUB-TASKS WERE ALREADY DONE, verified 2026-08-13 rather than assumed:
  - The definitions are already BYTE-IDENTICAL. HIC.1 step 26 para 1 == HIC.5 step 30 para 1.
    HIC.5 step 30 says so in terms ("worded identically ... deliberately and not by coincidence"),
    because HIC.5 was drafted against approved HIC.1. Nothing to align.
  - The reporting wording is already identical too. The todo quotes HIC.5 step 31 as saying "on
    the day the suspicion arises"; the approved text actually reads "on the same day it is
    suspected", which is HIC.1 step 25's wording exactly. The todo is stale on this point.

So the only real work is the pointer. HIC.5's scope already claims the subject: "This policy owns
the identification and control of an outbreak within {{HOSPITAL_NAME}} — the thresholds that
define one, the duty to report a suspicion, the investigation, the control measures, and the
closure and report."

WHAT STAYS IN HIC.1, and why: the definition (so a reader of this policy alone knows what an
outbreak is without fetching another document), the same-day reporting duty, the IPCC's receipt
of the conclusion, and the feed into the annual risk assessment — all of which are programme
governance and belong here. What goes is the six-bullet response procedure, which HIC.5 steps
30-35 now carry in full.

KNOCK-ON, easy to miss: the HIC.1.a evidence authored earlier today cites "outbreak records under
step 26" in detail. Left alone it would promise an assessor investigation records that HIC.5 now
owns — the exact failure mode this reconciliation exists to prevent. Two evidence records are
therefore rewritten to match the reduced step.

The pointer idiom matches HIC.1's own existing usage at steps 8, 9 and 21 ("set out in the
hospital's <x> policy ... and are not restated here").
"""
import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
DRAFT = _HERE.parent / "drafts" / "hic1_draft.json"

EM = "—"

OLD_STEP_26 = """26. Recognising and responding to an outbreak within the hospital

An outbreak within {{HOSPITAL_NAME}} is any occurrence of infection above the expected level for that organism, area and period, or the appearance of an organism of particular significance even as a single case {EM} including a multidrug-resistant organism new to the hospital.

On suspicion, the Infection Control Team:

- confirms the cases against the surveillance definitions and establishes when and where they occurred;
- institutes control measures immediately, without waiting for the investigation to conclude, since delay to achieve certainty costs more than a precaution later found unnecessary;
- informs the Infection Control Officer and the head of the affected area, and convenes the IPCC or an emergency subgroup of it;
- investigates the source and route, involving the laboratory, and reviews practice, equipment, environment and staffing in the affected area;
- notifies the public health authority where step 25 requires it;
- records the sequence of events, the measures taken and the outcome, and reports the conclusion to the IPCC with the changes required to prevent recurrence.

The outbreak record is retained and the lessons are reflected in revisions to the relevant policy and in the next annual risk assessment.""".replace("{EM}", EM)

NEW_STEP_26 = """26. Recognising an outbreak within the hospital

An outbreak within {{HOSPITAL_NAME}} is any occurrence of infection above the expected level for that organism, area and period, or the appearance of an organism of particular significance even as a single case {EM} including a multidrug-resistant organism new to the hospital.

That definition is kept here in full rather than replaced by a cross-reference, so that a reader of this policy alone can tell what an outbreak is without fetching another document. It is worded identically to the definition in the hospital's surveillance policy, deliberately and not by coincidence: two policies of the same hospital that define an outbreak differently will, sooner or later, disagree about whether one is happening. If either document is revised, the other is revised in the same pass.

A cluster of infection among patients or staff of {{HOSPITAL_NAME}} is reported to the Infection Control Officer on the same day it is suspected. Any member of staff may make that report, of any grade, without going through a line manager and without waiting for evidence, a diagnosis or an organism.

What happens after that suspicion is raised is not set out here. The identification, investigation, control, closure and reporting of an outbreak within {{HOSPITAL_NAME}} {EM} the thresholds that require the outbreak route to be entered, the Infection Control Officer's standing authority to act without waiting for a committee, the immediate control measures, the line list and epidemic curve, any decision to cohort patients, restrict admission or close a unit, the declaration of closure, and the written outbreak report {EM} are set out in the hospital's surveillance policy, which owns this subject and carries the documented-evidence anchor for it. They are not restated here. This policy states that the programme must have that capability, must staff it and must fund it.

Two related subjects do stay with this policy and are not displaced by the surveillance policy: participation of {{HOSPITAL_NAME}} in outbreaks and pandemics in the surrounding community, under step 24, and statutory notification of communicable disease to the public health authorities, under step 25.

The Infection Prevention and Control Committee receives the conclusion of every outbreak together with the changes required to prevent recurrence, and the lessons are reflected in revisions to the relevant policy and in the next annual infection risk assessment under step 6.""".replace("{EM}", EM)

# --- HIC.1.a evidence records that must move with the step -------------------------------
OLD_EV_1 = (
    "outbreak records under step 26 showing the cases confirmed against the surveillance "
    "definitions with when and where they occurred, the time control measures began relative to "
    "the time suspicion arose, the notification to the Infection Control Officer and the head of "
    "the affected area, the convening of the IPCC or its emergency subgroup, the investigation of "
    "source and route with laboratory involvement and the review of practice, equipment, "
    "environment and staffing in the affected area, the sequence of events, the measures taken "
    "and the outcome"
)
NEW_EV_1 = (
    "the outbreak definition in force under step 26, evidenced as worded identically to the "
    "definition in the hospital's surveillance policy, with the record that any revision to one "
    "was made in the same pass as the other"
)

OLD_EV_2 = (
    "the outbreak conclusion reported to the IPCC with the changes required to prevent "
    "recurrence, and evidence that the lessons reached both the revision of the relevant policy "
    "and the next annual risk assessment"
)
NEW_EV_2 = (
    "records of clusters of infection among patients or staff reported to the Infection Control "
    "Officer on the same day they were suspected, by staff of any grade and without going through "
    "a line manager; "
    "the IPCC minute receiving the conclusion of every outbreak with the changes required to "
    "prevent recurrence, and evidence that the lessons reached both the revision of the relevant "
    "policy and the next annual infection risk assessment {EM} the identification, investigation, "
    "control and closure records themselves being held under the hospital's surveillance policy, "
    "which owns that procedure and carries its documented-evidence anchor"
).replace("{EM}", EM)


def main() -> None:
    draft = json.loads(DRAFT.read_text(encoding="utf-8"))
    steps = draft["procedure_steps"]

    if steps[25] != OLD_STEP_26:
        raise SystemExit("step 26 does not match the expected approved text — re-read before editing")
    steps[25] = NEW_STEP_26

    a = next(m for m in draft["oe_mapping"] if m["oe_code"] == "HIC.1.a")
    for old, new in ((OLD_EV_1, NEW_EV_1), (OLD_EV_2, NEW_EV_2)):
        if a["evidence"].count(old) != 1:
            raise SystemExit(f"evidence record not found exactly once: {old[:60]}...")
        a["evidence"] = a["evidence"].replace(old, new)

    blob = json.dumps(draft, ensure_ascii=False)
    doubled = blob.count("{{HOSPITAL_NAME}}")
    if blob.count("{HOSPITAL_NAME}") - doubled:
        raise SystemExit("single-braced {HOSPITAL_NAME} present — would render literally")

    DRAFT.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"step 26: {len(OLD_STEP_26)} -> {len(NEW_STEP_26)} chars")
    print(f"HIC.1.a evidence: {len(a['evidence'].split(';'))} records")
    print(f"steps: {len(steps)} (unchanged)")


if __name__ == "__main__":
    main()
