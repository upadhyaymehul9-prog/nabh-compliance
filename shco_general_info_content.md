# SHCO General Reference Content
Source: NABH Accreditation Standards for Small Healthcare Organizations, 3rd Edition,
August 2022, ISBN 978-81-959676-1-2 (official document, fetched directly from
nabh-portal-live.s3.ap-south-1.amazonaws.com)

This is verbatim/close-paraphrase content from the official standards book, intended
to ground the AI assistant's answers to GENERAL questions about how SHCO/NABH works —
separate from OE-specific content already in shco_full_oes.

---

## What is NABH?

National Accreditation Board for Hospitals and Healthcare Providers (NABH) is a
constituent board of the Quality Council of India (QCI), set up to establish and
operate accreditation programs for healthcare organisations. NABH is accredited by
the International Society for Quality in Healthcare (ISQua).

---

## Assessment Modes — What They Are

There are three points in the accreditation cycle where NABH evaluates a hospital:

**Final Assessment** — The initial assessment before first accreditation is granted.
A team of assessors conducts an on-site evaluation. At this stage, only objective
elements at Core and Commitment level are scored (357 of 408 total OEs for SHCO).
Accreditation is awarded for 4 years if criteria are met.

**Surveillance Assessment** — Conducted 14–18 months after accreditation is granted
(midterm check during the 4-year cycle). At this stage, Core, Commitment, AND
Achievement level OEs are scored (392 of 408 total OEs). This checks whether the
hospital is improving and maintaining standards, not just passed once.

**Renewal/Re-accreditation Assessment** — Conducted before the 4-year accreditation
expires (apply at least 6 months prior to expiry). At this stage, ALL OE levels are
scored — Core, Commitment, Achievement, AND Excellence (all 408 OEs). This is the
full-cycle assessment for continued accreditation.

---

## Accreditation Decision Criteria by Assessment Type

| Criteria | Final | Surveillance | Re-accreditation |
|---|---|---|---|
| Overall compliance (cumulative score) | ≥80% | ≥80% | ≥80% |
| Commitment level compliance | ≥80% | ≥80% | ≥80% |
| Achievement level compliance | N/A | ≥80% | ≥80% |
| Excellence level compliance | N/A | N/A | ≥80% |
| Every Core OE score | ≥4 | ≥4 | ≥4 |
| Average score per standard | ≥4 | ≥4 | ≥4 |
| Average score per chapter | ≥4 | ≥4 | ≥4 |
| Improvement on OEs previously scored ≤2 | N/A | Required | Required |
| OEs scored ≤2 per standard (max allowed) | 1 | 1 | 0 — any OE ≤2 fails |
| OEs scored ≤3 need accepted action plan | Required | Required | Required |

**NOTE — internal book inconsistency on the "OEs ≤2 per standard" rule:**
The page 22 text states clearly that for Re-accreditation, "no individual
standard should have **any** objective element scored as 2 or less" (= 0
allowed, stricter than Final/Surveillance). However, the page 23 summary
table in the same book shows "1" for all three assessment types, which
contradicts this. If a user asks about this specific rule, acknowledge both
versions: the body text (p.22) says 0 for Re-accreditation; the summary
table (p.23) says 1 for all three. The safer / more conservative
interpretation for a hospital preparing for Re-accreditation is to treat
the limit as 0 (i.e., aim for no OE ≤2 in any standard).

---

## What is an OE Level (Core / Commitment / Achievement / Excellence)?

**CORE** — Standards the organisation MUST have in place to ensure quality of care
and safety. Mandatorily assessed at every assessment stage. Score must never be
below 4, at any assessment.

**Commitment** — Most objective elements sit here. These form the basis for
accreditation at the end of the Final Assessment.

**Achievement** — Reflects ongoing improvement beyond the basics. First assessed
at the Surveillance stage (14–18 months post-accreditation).

**Excellence** — The highest level, reflecting a mature quality system. Only
assessed at Re-accreditation (end of the 4-year cycle).

SHCO 3rd Edition breakdown: 408 total OEs = 100 Core + 257 Commitment + 35
Achievement + 16 Excellence, across 71 standards and 10 chapters.

---

## Scoring Scale (5-point, used in both self-assessment and official assessment)

| Score | Meaning | Criteria |
|---|---|---|
| 1 | No compliance | No systems in place; ≤20% of samples meet requirement; non-conformity exists |
| 2 | Poor compliance | Elementary systems in place; 21-40% of samples meet requirement; non-conformity exists |
| 3 | Partial compliance | Systems partially in place; 41-60% of samples meet requirement; non-conformity exists |
| 4 | Good compliance | Systems in place with evidence of implementation; 61-80% of samples meet requirement |
| 5 | Full compliance | Systems fully implemented across organisation; 81-100% of samples meet requirement; no non-conformity |

Note: the basis for scoring is implementation. If documentation is inadequate even
when implementation is good, the score can be downgraded by one point.

---

## What is a KPI in the NABH context?

KPI = Key Performance Indicator. Per Annexure 1 of the official SHCO 3rd Edition
standards book: Key Performance Indicators help to systematically monitor,
evaluate, and continually improve service performance. By themselves, KPIs don't
improve performance — they provide signposts that signal progress toward goals
and opportunities for improvement.

Well-designed KPIs help an organisation to:
- Establish baseline information (current state of performance)
- Set performance standards and targets to motivate continual improvement
- Measure and report improvements over time
- Compare performance across locations
- Benchmark against regional/international peers or norms
- Allow stakeholders to independently judge health sector performance

Each KPI in the NABH framework has a standardised definition, formula
(numerator/denominator), unit, and defined monitoring frequency. KPIs are
separate from OE scoring — they're tracked on an ongoing basis (not scored
1-5 like OEs) and are reviewed for trends over time.

[NOTE FOR BUILD: This is the general definition only. Your app's actual KPI data
(the 50 KPI definitions/formulas) lives in a separate `kpis` table not yet wired
into this AI assistant — flagged as a separate future feature. The full KPI list
with formulas is in Annexure 1 of the source PDF, starting page 151 — extract
separately if/when building the KPI-specific feature.]

---

## What is a Standard vs an Objective Element?

**Standard** — A statement of expectation defining structures/processes that must
be in place. Numbered serially: first 3 letters = chapter code, number = order
within chapter (e.g. AAC.1 = first standard of the AAC chapter).

**Objective Element (OE)** — The measurable component of a standard, scored on
the 1-5 scale during assessment. Numbered with a letter after the standard number
(e.g. AAC.1.c = third OE of the first AAC standard).

---

## The 10 SHCO Chapters

1. AAC — Access, Assessment and Continuity of Care (48 OEs)
2. COP — Care of Patients (82 OEs)
3. MOM — Management of Medication (52 OEs)
4. PRE — Patient Rights and Education (39 OEs)
5. HIC — Hospital Infection Control (36 OEs)
6. PSQ — Patient Safety and Quality Improvement (28 OEs)
7. ROM — Responsibilities of Management (19 OEs)
8. FMS — Facility Management and Safety (29 OEs)
9. HRM — Human Resource Management (45 OEs)
10. IMS — Information Management System (30 OEs)

(Verified against the complete 188-page official PDF: the book itself uses "HIC"
consistently as the chapter abbreviation throughout — confirmed in the Table of
Contents, chapter overview, and all standard/OE numbering. Note: the book is
slightly inconsistent on the FULL chapter name — Table of Contents says "Hospital
Infection Control (HIC)" while the "How to read the standard" section says
"Hospital Infection Prevention and Control (HIC)". Either full name is
book-accurate; the abbreviation HIC is correct either way. Still confirm this
matches the actual chapter column value in your live shco_full_oes table before
deploying — do not assume without checking, per the earlier IC/IPC mismatch
caught in testing.)

---

## Glossary — Official NABH Terminology
Source: SHCO 3rd Edition standards book, pages 138-150 (full 188-page document,
not the partial earlier fetch). Extracted via pdfplumber from the user-uploaded
PDF and cross-checked against the previous partial draft.

**FLAG FOR MANUAL VERIFICATION (per CLAUDE.md PDF extraction rule):** This text
has known ligature-stripping artifacts from PDF extraction — words like "denes"
(defines), "specic" (specific), "qualication" (qualification), "uid" (fluid),
"signicant" (significant), "rst" (first), "ll/full" (fill), "denition"
(definition) are missing letters where the original PDF used ligatures (fi, fl)
that didn't extract cleanly. The MEANING is intact and unambiguous in every case,
but a human pass to clean the spelling before this goes into a production system
prompt is recommended — do not deploy without at least a skim-read, since this is
exactly the kind of unverified extraction your own content rules flag.

The official preamble states: "The commonly-used terminologies in the NABH
standards are briefly described and explained herein to remove any ambiguity
regarding their comprehension. The definitions narrated have been taken from
various authentic sources as stated, wherever possible. Notwithstanding the
accuracy of the explanations given, in the event of any discrepancy with a legal
requirement enshrined in the law of the land, the provisions of the latter shall
apply."

[FULL GLOSSARY TEXT — Accreditation through Workplace violence — to be inserted
from /mnt/user-data/outputs/glossary_final_chunk.txt, ~80 terms, alphabetical,
covering: Accreditation, Accreditation assessment, Advance life support, Adverse
drug reaction, Adverse event, Anaesthesia Death, Assessment, Barrier nursing,
Basic life support, Breakdown maintenance, Byelaws, Calibration, Care Plan,
Citizen's charter, Clinical audit, Clinical autopsy, Clinical care pathway,
Clinical practice guidelines, Competence, Confidentiality, Consent, Control
Charts, Correction, Corrective action, Credentialing, Data, Discharge summary,
Disciplinary procedure, Drug dispensing, Drug Administration, Effective
communication, Employees, End-of-life Care, Enhanced communication, Ethics,
Evidence-based medicine, Family, Failure Mode and Effect Analysis (FMEA),
Formulary, Goal, Grievance-handling procedures, Hazardous materials, Hazardous
waste, Healthcare-associated infection, Healthcare organisation, High-dependency
unit, High Risk/High Alert Medications, Incident reporting, In-service
education/training, Indicator, Information, Intent, Inventory control, Isolation,
Job description, Job specification, Maintenance, Medical equipment, Medication
error, Medication Order, Mission, Monitoring, Multidisciplinary, Near-miss, No
harm, Notifiable disease, Nursing empowerment, Objective, Objective element,
Occupational health hazard, Operational plan, Organogram, Outsourcing,
Patient-care setting, Patient record/medical record/clinical record,
Patient-reported experience measures (PREMs), Patient-reported outcome measures
(PROMs), Patient Satisfaction, Patient Experience, Performance appraisal, Point
of care equipment, Policies, Preventive action, Preventive maintenance,
Prescription, Privileging, Privileged communication, Procedural sedation,
Procedure, Process, Programme, Protocol, Quality, Quality assurance, Quality
improvement, Radiation Safety, Re-assessment, Reconciliation of medications,
Resources, Restraints, Risk abatement, Risk assessment, Risk management, Risk
mitigation, Risk reduction, Root Cause Analysis (RCA), Safety, Safety programme,
Scope of services, Security, Sedation (3 levels: minimal/moderate/deep), Sentinel
events, Social responsibility, Sound clinical practice, Special Educational needs
of the patient, Staff, Standard precautions, Standards, Sterilisation, Strategic
plan, Surveillance, Table-top exercise, Traceability, Transfusion reaction,
Triage, Turn-around-time, Unstable patient, Validated tool, Validation, Values,
Verbal order, Verification, Vision, Vulnerable patient, Workplace violence —
each with full official definition text.]

---

## BUILD INSTRUCTIONS FOR CLAUDE CODE (next session)

0. TWO FILES needed for this build:
   - shco_general_info_content.md (this file) — assessment modes, scoring,
     decision criteria, chapter structure, KPI definition, glossary summary
   - glossary_final_chunk.txt — full ~80-term official glossary, separate file
     because of its length. Read BOTH before building.
   - IMPORTANT: skim glossary_final_chunk.txt for the ligature artifacts
     flagged above before using it verbatim in a system prompt — at minimum,
     fix obvious words if you have time; if not, deploy as-is since meaning
     is intact, but note it in the commit message as "extraction not yet
     manually proofread."

1. Create a new table `shco_general_info` OR embed this as a structured JSON/
   constant in the Edge Function — given this is small, static content, a JS
   constant may be simpler than a new table (matches the pattern used for
   ELC_OE_TIPS). Glossary terms should be a separate keyed object (term →
   definition) for clean lookup, distinct from the assessment-mode/scoring
   content.

2. Update the retrieval logic in supabase/functions/ai-assistant/index.ts:
   - If the question matches an oe_code pattern → query shco_full_oes (existing
     behavior, unchanged)
   - If the question matches general-info keywords (assessment mode, KPI,
     scoring, what is core/commitment/achievement/excellence, what is a
     standard, what is an objective element) → pull from this new general
     content instead
   - If neither matches → existing keyword fallback against shco_full_oes,
     then existing no-match response (unchanged)

3. Update the system prompt to allow citing this general content as a SEPARATE
   source type from OE content — e.g. "Source: SHCO Full — General Reference
   (NABH 3rd Edition Standards Book)" instead of an oe_code citation, so it's
   clear to the user this isn't OE-specific guidance.

4. IMPORTANT: verify the HIC vs IPC chapter code discrepancy against the live
   shco_full_oes table before deploying — do not assume the official book's
   chapter codes exactly match what's in the database without checking first.

5. Test questions: "what is a KPI", "what is final assessment", "what does
   core mean", "what is the difference between surveillance and re-accreditation"
   — confirm grounded answers from this new content, not from Sonnet's general
   training knowledge.
