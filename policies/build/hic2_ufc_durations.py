# -*- coding: utf-8 -*-
"""Records the CDC Appendix A duration facts added to HIC.2 step 19 on 2026-08-13.

The HIC.2.c anchor introduced fact-stated discontinuation criteria into step 19. Under the
Tier 1 rule those facts must be recorded in universal_facts_checklist with their source, the
same as HIC.4-6 do. HIC.2's checklist numbers its facts 1-41 sequentially ACROSS sections, so
inserting into the existing TRANSMISSION-BASED PRECAUTIONS section would renumber 16-41. A new
dated section starting at 42 is appended instead; nothing renumbers.

Inserted BEFORE the "NABH-DERIVED POINTS" block, so the numbered facts stay contiguous and the
reviewer-flag block remains last.
"""
import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
DRAFT = _HERE.parent / "drafts" / "hic2_draft.json"

EM = "—"
ANCHOR = "NABH-DERIVED POINTS (not universal facts"

ADDITION = """TRANSMISSION-BASED PRECAUTIONS {EM} DURATION AND DISCONTINUATION (added 2026-08-13)
Source for facts 42-52: CDC, Guideline for Isolation Precautions: Preventing Transmission of Infectious Agents in Healthcare Settings (2007), Appendix A "Type and Duration of Precautions Recommended for Selected Infections and Conditions", current version dated 2 February 2025. Read from the source table directly rather than from a search summary or from recollection. These were added to step 19, which previously carried the BASIS for discontinuation but left every actual duration as "[Hospital to define]".
42. Measles {EM} airborne precautions until 4 days after onset of rash; duration of illness in an immunocompromised patient.
43. Chickenpox, and disseminated herpes zoster {EM} airborne plus contact precautions until all lesions are dry and crusted.
44. Pulmonary or laryngeal tuberculosis, CONFIRMED {EM} discontinue only when the patient is on effective therapy, is improving clinically, and has three consecutive sputum smears negative for acid-fast bacilli collected on separate days.
45. Pulmonary or laryngeal tuberculosis, SUSPECTED {EM} discontinue only when infectious tuberculosis is judged negligible and either another diagnosis explains the clinical syndrome or three acid-fast bacilli smears are negative, each specimen collected 8 to 24 hours apart with at least one an early morning specimen. Note the two entries differ; the draft carries both because a suspected case is the commoner situation on a ward.
46. Pertussis {EM} droplet precautions until 5 days after initiation of effective antibiotic therapy.
47. Meningococcal disease or meningitis, known or suspected {EM} droplet precautions until 24 hours after initiation of effective therapy.
48. Mumps {EM} droplet precautions until 5 days after onset of parotid swelling. Appendix A carries an explicit October 2017 update recording HICPAC's change from 9 days to 5; the 5-day figure is the current one.
49. Group A streptococcal pneumonia {EM} droplet precautions until 24 hours after initiation of effective therapy, with contact precautions added where skin lesions are present.
50. Clostridioides difficile {EM} contact precautions for the duration of illness; handwashing with soap and water preferred because alcohol is not sporicidal; hypochlorite for cleaning where transmission continues. Consistent with fact 5 already in this checklist.
51. Norovirus gastroenteritis {EM} contact plus standard precautions, with cohorting to separate air spaces and toilet facilities during an outbreak. Appendix A carries an April 2019 update changing the type of precaution from "Standard" to "Contact + Standard"; the draft states the updated position.
52. Multidrug-resistant organisms (MRSA, VRE, VISA/VRSA, ESBL producers, resistant S. pneumoniae) {EM} contact precautions, with NO fixed duration given. Appendix A leaves the duration to the infection control programme on local, state, regional or national recommendations, so the draft makes it a standing ICC decision rather than inventing a period.

REVIEWER TO NOTE {EM} A DELIBERATE OMISSION (2026-08-13)
Seasonal influenza is NOT given a duration in step 19, and that is deliberate rather than an oversight. The current Appendix A carries no duration entry for seasonal influenza {EM} the row reads "n/a" and refers the reader to separate CDC seasonal influenza guidance. The commonly quoted figure (7 days from onset, or 24 hours after fever resolves, whichever is longer) comes from that separate guidance and NOT from Appendix A. Rather than attribute a figure to a source that does not carry it, step 19 states the omission openly and leaves the criterion to the hospital at "[Hospital to define]", to be reconsidered each season. If a later revision wants a fixed figure, cite the seasonal influenza guidance specifically {EM} do not cite Appendix A for it.

"""


def main() -> None:
    draft = json.loads(DRAFT.read_text(encoding="utf-8"))
    text = draft["universal_facts_checklist"]

    if "added 2026-08-13" in text:
        raise SystemExit("addition already present — refusing to double-apply")
    if text.count(ANCHOR) != 1:
        raise SystemExit(f"anchor found {text.count(ANCHOR)} times — expected exactly 1")

    addition = ADDITION.format(EM=EM)
    draft["universal_facts_checklist"] = text.replace(ANCHOR, addition + ANCHOR)
    DRAFT.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"checklist: {len(text)} -> {len(draft['universal_facts_checklist'])} chars (LF)")
    print("facts 42-52 added; existing facts 1-41 unrenumbered")


if __name__ == "__main__":
    main()
