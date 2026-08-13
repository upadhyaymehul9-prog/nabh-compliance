# -*- coding: utf-8 -*-
"""Reconciliation 4/4: align the HIC.2 / HIC.4 post-exposure wording.

Todo items (scripts/master-policy-todos.md, "Specific divergences to resolve in that pass"):

  1. "Exposure first-aid: antiseptic wording. ... Both group *antiseptic* with caustic agents and
     prohibit it outright. CDC's position is narrower and three-part: caustic agents (bleach) are
     not applied; antiseptic or disinfectant is not *injected into* the wound; and antiseptics
     generally have no evidence of reducing transmission — which is 'not proven useful', not
     'prohibited'. ... as written both documents may contradict local practice (povidone-iodine
     after washing is common in Indian protocols). Fix is roughly one sentence in each, worded
     identically."

  2. "HIV PEP window: differing urgency. ... HIC.4's is the tighter and better-supported framing
     and is the likely target wording for both."

FACT-CHECK PERFORMED 2026-08-13, not taken on trust from the todo.

The todo's three-part characterisation of the antiseptic position is ACCURATE. Verified against
the US Public Health Service guideline (Kuhar et al., 2013), which reads:
  "Wounds and skin sites that have been in contact with blood or body fluids should be washed
   with soap and water; mucous membranes should be flushed with water."
  "There is no evidence that the use of antiseptics for wound care or expressing fluid by
   squeezing the wound further reduces the risk of HIV transmission."
  "The application of caustic agents (e.g. bleach) or the injection of antiseptics or
   disinfectants into the wound is not recommended."
The shared replacement sentence block below states exactly those three parts and is byte-identical
in both documents.

FINDING THAT CHANGES A PREMISE — FLAGGED, NOT SILENTLY ACTED ON. A 2025 revision of the PHS
guideline now exists (2025 US Public Health Service Guidelines for the Management of Occupational
Exposures to HIV, Infect Control Hosp Epidemiol). It says "Initiate PEP as soon as possible, up to
72 hours following the occupational exposure to HIV" and does NOT carry a "preferably within two
hours" figure. HIC.4's two-hour wording therefore rests on older guidance, not on the current
guideline. The instruction for this pass is to adopt HIC.4's wording in both, and that is what is
done here — it removes the divergence, which is the point of the pass, and "earlier is better" is
not clinically wrong. But the two-hour figure should not be described as coming from the current
guideline. The 2025 revision also adds a nuance NEITHER document carries: for exposures beyond
72 hours thought to represent a high risk of transmission, consult a provider with HIV treatment
expertise. Logged as a new item rather than folded in here, because it is new content and outside
the scope of this reconciliation.
"""
import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
DRAFTS = _HERE.parent / "drafts"

EM = "—"

# Byte-identical in both documents. This is the "one sentence in each, worded identically".
SHARED = (
    "The wound is not squeezed to express fluid, is not scrubbed and is not sucked, and no "
    "caustic agent such as bleach is applied to it. An antiseptic or disinfectant is never "
    "injected into the wound. Applying an antiseptic to the site after washing is not prohibited, "
    "and remains common practice in India, but there is no evidence that it reduces transmission "
    "and it is never a substitute for washing."
)

H2_OLD_FIRSTAID = (
    "1. Wash the site with soap and running water. Do not squeeze, scrub or apply a caustic agent "
    "such as bleach or antiseptic to the wound. Irrigate eyes or other mucous membranes with "
    "clean water or normal saline."
)
H2_NEW_FIRSTAID = (
    "1. Wash the site with soap and running water. " + SHARED + " Irrigate eyes or other mucous "
    "membranes with clean water or normal saline."
)

H4_OLD_FIRSTAID = (
    "- for a percutaneous injury, washes the site with soap and running water. The wound is not "
    "squeezed, not scrubbed, and not sucked, and no caustic agent, bleach, antiseptic or "
    "disinfectant is applied to it. Squeezing and caustics damage tissue and have no benefit;"
)
# SHARED ends in a full stop because HIC.2 uses it mid-paragraph. HIC.4's is a bullet in a
# semicolon-separated list, so the terminal stop is swapped for a semicolon rather than appended
# to it — "washing.;" was the first attempt and is what this rstrip prevents.
H4_NEW_FIRSTAID = (
    "- for a percutaneous injury, washes the site with soap and running water. "
    + SHARED.rstrip(".") + ";"
)

# HIC.4 keeps its wording; HIC.2 adopts it.
H2_OLD_HIV = (
    "- HIV: where prophylaxis is indicated, the first dose is given as soon as possible " + EM +
    " ideally within a few hours and certainly within 24 hours " + EM + " and is not started "
    "later than 72 hours after the exposure. The course runs for 28 days, with adherence support "
    "and follow-up testing."
)
H2_NEW_HIV = (
    "- HIV: where prophylaxis is indicated, the first dose is given as soon as possible, ideally "
    "within hours of the exposure and preferably within two, and is not started beyond 72 hours "
    "after the exposure, after which it is not considered effective. This is the same rule, in "
    "the same words, as the occupational health and post-exposure policy of {{HOSPITAL_NAME}}, "
    "which owns the detail; if either document changes it, the other is changed in the same pass. "
    "The course runs for 28 days, with adherence support and follow-up testing."
)

CHECKLIST_NOTE = (
    "\n\nRECONCILIATION PASS " + EM + " EXPOSURE FIRST AID AND PEP TIMING (added 2026-08-13)\n"
    "The first-aid sentence on antiseptics was rewritten and is now byte-identical in the "
    "infection prevention and control practices policy and the occupational health and "
    "post-exposure policy. Both previously grouped antiseptic with caustic agents and prohibited "
    "it outright, which overstated the source and risked contradicting local practice, since "
    "povidone-iodine after washing is common in Indian protocols.\n"
    "SOURCE, verified 2026-08-13 against the guideline itself: US Public Health Service, Updated "
    "US Public Health Service Guidelines for the Management of Occupational Exposures to Human "
    "Immunodeficiency Virus and Recommendations for Postexposure Prophylaxis (Kuhar et al., 2013). "
    "Its position is three-part and the documents now state all three: wounds and skin sites are "
    "washed with soap and water and mucous membranes flushed with water; there is no evidence that "
    "antiseptics for wound care, or expressing fluid by squeezing the wound, further reduce the "
    "risk of transmission; and the application of caustic agents such as bleach, or the injection "
    "of antiseptics or disinfectants into the wound, is not recommended. Note the distinction the "
    "documents now preserve: injecting antiseptic into the wound is not recommended, whereas "
    "applying antiseptic to the site is merely unproven, not prohibited.\n"
    "PEP TIMING. The first-dose wording is now identical in both documents: as soon as possible, "
    "ideally within hours and preferably within two, and not beyond 72 hours.\n"
    "REVIEWER TO NOTE " + EM + " THE TWO-HOUR FIGURE IS NOT FROM THE CURRENT GUIDELINE. A 2025 "
    "revision exists (2025 US Public Health Service Guidelines for the Management of Occupational "
    "Exposures to HIV, Infect Control Hosp Epidemiol). It states \"Initiate PEP as soon as "
    "possible, up to 72 hours following the occupational exposure to HIV\" and carries no "
    "\"within two hours\" figure. The two-hour wording was adopted across both documents on "
    "instruction, to remove a divergence between them, and it is not clinically wrong " + EM +
    " earlier is better " + EM + " but it should not be attributed to the 2025 guideline. The 2025 "
    "revision also adds a recommendation NEITHER document carries: where an exposure beyond 72 "
    "hours is thought to represent a high risk of transmission, consult a provider with expertise "
    "in HIV treatment rather than treating 72 hours as an absolute cut-off. Logged in "
    "scripts/master-policy-todos.md as a separate item."
)


def patch(name, edits, tail_note=True):
    path = DRAFTS / f"{name}_draft.json"
    draft = json.loads(path.read_text(encoding="utf-8"))
    steps = draft["procedure_steps"]
    for idx, old, new, label in edits:
        if steps[idx].count(old) != 1:
            raise SystemExit(f"{name} step {idx+1}: {label} not found exactly once")
        steps[idx] = steps[idx].replace(old, new)
    if tail_note:
        draft["universal_facts_checklist"] = draft["universal_facts_checklist"].rstrip("\n") + CHECKLIST_NOTE
    blob = json.dumps(draft, ensure_ascii=False)
    if blob.count("{HOSPITAL_NAME}") - blob.count("{{HOSPITAL_NAME}}"):
        raise SystemExit(f"{name}: single-braced placeholder present")
    # Compare without terminal punctuation: HIC.2 ends the block with a full stop, HIC.4 with
    # a semicolon because it is a bullet. The wording either side of it must still be identical.
    if SHARED.rstrip(".") not in blob:
        raise SystemExit(f"{name}: shared first-aid block missing after edit")
    path.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{name}: {len(edits)} step edit(s), {len(steps)} steps (unchanged)")


def main() -> None:
    patch("hic2", [
        (23, H2_OLD_FIRSTAID, H2_NEW_FIRSTAID, "first-aid sentence"),
        (23, H2_OLD_HIV, H2_NEW_HIV, "HIV PEP window"),
    ])
    patch("hic4", [
        (30, H4_OLD_FIRSTAID, H4_NEW_FIRSTAID, "first-aid bullet"),
    ])

    # The whole point is that the two blocks are identical. Prove it.
    h2 = json.loads((DRAFTS / "hic2_draft.json").read_text(encoding="utf-8"))["procedure_steps"][23]
    h4 = json.loads((DRAFTS / "hic4_draft.json").read_text(encoding="utf-8"))["procedure_steps"][30]
    core = SHARED.rstrip(".")
    if core not in h2 or core not in h4:
        raise SystemExit("shared block not present in both documents")
    print("shared first-aid block byte-identical in HIC.2 step 24 and HIC.4 step 31: OK")


if __name__ == "__main__":
    main()
