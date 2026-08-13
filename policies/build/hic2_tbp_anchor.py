# -*- coding: utf-8 -*-
"""The HIC.2.c transmission-based-precautions documented-evidence anchor.

Closes the deferred item in scripts/master-policy-todos.md: HIC.2.c is asterisked in the
official SHCO 3rd Edition PDF (printed p.93) but carries doc_required = false, and the flag
could not be flipped because the approved HIC.2 master had no block for an assessor to be
walked through.

WHAT THE TODO GOT RIGHT AND WHAT IT OVERSTATED (checked 2026-08-13 against live steps 15-19):
  - "no isolation signage record"        -> OVERSTATED. Step 15 already carries the entrance
                                            instruction card, showing required PPE and
                                            withholding the diagnosis.
  - "no category-assignment record"      -> OVERSTATED. Step 15 already carries the precaution
                                            assignment register with authoriser and dates.
  - "no record of who assigns/reviews"   -> PARTLY RIGHT. Initiation and ICN confirmation were
                                            present; no periodic REVIEW cadence existed.
  - "no PPE-by-category matrix"          -> RIGHT. PPE was stated per category in prose across
                                            steps 16-18 and never consolidated.
  - "no duration/discontinuation criteria" -> RIGHT. Step 19 carried the basis for stopping but
                                            every actual duration was "[Hospital to define]".

So the anchor is built by EXPANDING steps 15 and 19 in place. No step is inserted: HIC.2 was
already renumbered once (rev 2 -> rev 3, 34 steps -> 33) and its six internal cross-references
rewritten, so inserting mid-document would put every "steps 15-19" mapping and every in-prose
step reference at risk for no benefit.

DURATIONS ARE FACT-CHECKED, NOT WRITTEN FROM MEMORY. Source: CDC, Guideline for Isolation
Precautions: Preventing Transmission of Infectious Agents in Healthcare Settings (2007),
Appendix A "Type and Duration of Precautions Recommended for Selected Infections and
Conditions", current version dated 2 February 2025, read from the source table directly.
Note the deliberate omission of seasonal influenza: Appendix A carries NO duration entry for it
and refers instead to separate CDC seasonal-influenza guidance, so a fixed figure is not stated.
"""

EM = "—"

# Appended to the end of live procedure_steps[14] (step 15).
STEP_15_ADDITION = """

The personal protective equipment required by each category is consolidated here, so that the entrance card, the induction training and the audit tool all draw on one list rather than on three separate passages:

- Contact precautions {EM} gown and gloves, put on before entering the patient's environment and removed before leaving it.
- Droplet precautions {EM} a surgical mask, put on before entering and removed after leaving, with eye protection added where splashing or spraying towards the face is anticipated.
- Airborne precautions {EM} a fit-tested particulate respirator (N95 or equivalent) with a user seal check on every occasion, put on before entering and removed only after leaving the room and closing the door.
- Where more than one route of transmission applies, the requirements are cumulative and the most protective respiratory item governs.

Standard precautions continue to apply underneath every category. PPE is therefore still selected on the anticipated exposure under step 10 even where the category above does not call for it {EM} a category tells staff the minimum, never the maximum.

The assigned category is reviewed by the ICN at an interval of [Hospital to define], and additionally whenever the patient's clinical condition changes or a new microbiology result is available. Each review is recorded in the precaution assignment register with the date, the reviewer and the decision to continue, change or discontinue. A category that is never reviewed tends to outlive its indication: it holds isolation capacity that another patient needs, and it exposes the patient to the recognised harms of unnecessary isolation {EM} reduced clinical contact, delayed investigations and lower reported wellbeing.""".replace("{EM}", EM)

# Appended to the end of live procedure_steps[18] (step 19).
STEP_19_ADDITION = """

Reference criteria for discontinuation. {{HOSPITAL_NAME}} adopts the following as its standing criteria, taken from the CDC Guideline for Isolation Precautions, Appendix A. Where the treating doctor departs from a criterion for an individual patient, the departure and its reason are recorded in the case record and notified to the ICN.

- Measles {EM} airborne precautions until 4 days after the onset of rash, and for the whole duration of the illness in an immunocompromised patient.
- Chickenpox, and disseminated herpes zoster {EM} airborne and contact precautions until all lesions are dry and crusted.
- Pulmonary or laryngeal tuberculosis, confirmed {EM} airborne precautions discontinued only when the patient is on effective therapy, is improving clinically, and has three consecutive sputum smears negative for acid-fast bacilli collected on separate days.
- Pulmonary or laryngeal tuberculosis, suspected {EM} airborne precautions discontinued only when the likelihood of infectious tuberculosis is judged negligible and either another diagnosis explains the clinical syndrome or three sputum smears for acid-fast bacilli are negative, each specimen collected 8 to 24 hours apart with at least one taken in the early morning.
- Pertussis {EM} droplet precautions until 5 days after effective antibiotic therapy has started.
- Meningococcal disease or meningitis, known or suspected {EM} droplet precautions until 24 hours after effective therapy has started.
- Mumps {EM} droplet precautions until 5 days after the onset of parotid swelling.
- Group A streptococcal pneumonia {EM} droplet precautions until 24 hours after effective therapy has started, with contact precautions added where skin lesions are present.
- Clostridioides difficile {EM} contact precautions for the duration of the illness, with hands washed using soap and running water rather than handrub because alcohol is not sporicidal, and a hypochlorite agent used for environmental cleaning where transmission continues.
- Norovirus gastroenteritis {EM} contact precautions, with affected patients cohorted to separate air spaces and toilet facilities where an outbreak is in progress.
- Multidrug-resistant organisms {EM} contact precautions, with the duration determined by the infection control programme of {{HOSPITAL_NAME}} rather than by any fixed period, recorded as a standing decision of the ICC and reviewed when local resistance patterns shift.

Seasonal influenza is deliberately absent from the list above. The CDC appendix carries no duration entry for it and refers instead to separate seasonal influenza guidance, so {{HOSPITAL_NAME}} sets its own criterion at [Hospital to define] and reconsiders it each season rather than inheriting a figure that the source does not give.

For any organism not named above, the criterion applied is [Hospital to define], set by the ICN in consultation with the treating doctor and recorded in the precaution assignment register against that patient.""".replace("{EM}", EM)
# NB: .replace(), never .format(). str.format collapses the doubled braces in
# {{HOSPITAL_NAME}} to single braces, which the renderer then fails to substitute and prints
# literally. That bug reached the local draft on 2026-08-13 and was caught only by the
# post-apply hash check against the live row.
