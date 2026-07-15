# SHCO Quality Tools (Annexure 3) + Medication Chart Review Checklist
Source: NABH Accreditation Standards for Small Healthcare Organizations, 3rd Edition,
August 2022 — Medication Chart Review Checklist (pages 166-169, part of Annexure 2)
and Annexure 3 "Quality Tools" (pages 170-172). Official document.

This grounds AI answers about: (a) the 35-parameter medication chart review audit
form and how to count errors/opportunities, and (b) NABH-recognised quality
improvement tools (RCA, 5 Whys, Fishbone, Affinity, Histogram, FMEA).

NOTE: The medication error categorization (NCC-MERP A-I), algorithm, and root-cause
methodology are ALREADY in the deployed shco_medication_error_content.md (Annexure 2).
This file adds only the NEW content: the chart review checklist parameters and the
quality tools. Do not duplicate the categorization content.

---

## PART A — Medication Chart Review Checklist (35 parameters)

A structured audit form for reviewing medication charts. For each drug (up to 10 per
sheet), the auditor marks each parameter with the error category (A-I), or 0 for no
error, or NA if not applicable. Multiple errors can be recorded per cell.

Header fields: Auditor, Date of Audit, Location, UHID, Date of Admission, Primary
Consultant, Drug allergies documented (Yes/No).

**Doctors (parameters 1-13):**
1. Incorrect drug selection
2. No/wrong dose
3. No/wrong unit of measurement
4. No/wrong frequency
5. No/wrong route
6. No/wrong concentration
7. No/wrong rate of administration
8. Illegible handwriting
9. Non-approved abbreviations used
10. Non-usage of capital letters for drug names
11. Non-usage of generic names
12. Non-modification of drug dose keeping in mind drug-drug interaction
13. Non-modification of time of drug administration/dose/drug keeping in mind food-drug interaction

**Doctor and/or Nurse (parameters 14-16):**
14. Wrong formulation transcribed/indented
15. Wrong drug transcribed/indented
16. Wrong strength transcribed/indented

**Pharmacist (parameters 17-23):**
17. Wrong drug dispensed
18. Wrong dose dispensed
19. Wrong formulation dispensed
20. Expired/near-expiry drugs dispensed
21. No/wrong labelling
22. Delay in dispense beyond defined time
23. Generic or class substitute done without consulting the prescribing doctor

**Nurses (parameters 24-35):**
24. Wrong Patient
25. Dose Omission
26. Improper Dose
27. Wrong Drug
28. Wrong Formulation Administered
29. Wrong Route of Administration
30. Wrong Rate
31. Wrong Duration
32. Wrong Time*
33. No documentation of drug administration
34. Incomplete/Improper documentation by nursing staff**
35. Documentation without administration

---

## How to Count Errors and Opportunities (critical for KPI #2)

**Number of errors** = number of cells with a value between A and I.
Example: if drug 1 has a category-C error (doctors) and a category-B error
(pharmacists), and drug 4 has a category-C error (nurses) → numerator = 3.

**Number of opportunities** = number of cells with EITHER 0 OR a value A-I
(excluding NA cells).
Example: 10 drugs × 35 parameters = 350 cells = 350 opportunities (if all filled).
If 6 drugs and 24 cells marked NA → opportunities = (35 × 6) − 24 = 186.

**Selecting a category:** Choose only ONE category per error — the one that best fits.
Select the HIGHEST severity level that applies during the event. Example: if a patient
suffers a severe anaphylactic reaction (Category H) requiring treatment (Category F)
but recovers fully, code it as Category H (highest severity reached).

*Footnote on "Wrong Time": Deviation from the organisation's defined timeframe for
drug administration. The basis for "wrong time" must be evidence-based; the org may
adopt/adapt the ISMP Acute Care Guidelines for Timely Administration of Scheduled
Medications.

**Footnote on documentation: Incomplete = missing date, time, or signature.
Improper = wrong dose notation (e.g. writing "1 tablet of 250mg" when actually ½
tablet of 500mg was given), or not stating the actual brand in cases of brand
substitution.

---

## PART B — Quality Tools (Annexure 3)

QI data should be analysed using statistical/quality tools to assess compliance with
targets and identify areas for improvement. NABH recognises the following tools:

**Root Cause Analysis (RCA):** A systematic, extensive, in-depth analysis of a problem
to get to its underlying cause. Used to establish causality when adverse trends are
noted for any parameter, or in the case of errors/incidents. Carried out using either
the 5 Whys tool or the Cause and Effect Diagram.

**5 Whys (Taiichi Ohno):** Asks "Why?" five times sequentially, each in response to
the previous answer, until reaching the root cause. Shifts focus (blame) from
individuals to the process. A problem may have multiple root causes; different people
seeing different parts of the system may answer differently. The 5 Whys has been
criticised for over-simplifying complex problems — best used in conjunction with a
Cause and Effect Diagram.

**Cause and Effect Diagram (Ishikawa / Fishbone):** Graphically displays the
relationship of many causes to an effect and to each other. A horizontal line runs
from tail to head of the "fish," where the effect is written. Causes are grouped under
categories such as Materials, Methods, Equipment, Environment, and People (or as
required). Used extensively to reach the root cause of deviations from any policy/
procedure/protocol, for outliers in indicator data, and for detailed analysis of
incidents and adverse events.

**Affinity Diagram:** Serves the same purpose as the Ishikawa chart, but the visual
presentation differs.

**Histogram:** A bar chart displaying variation in continuous data (time, weight, size,
temperature). Helps recognise and analyse patterns not apparent in data tables or from
averages/medians, and highlights the most frequently occurring interval.

**Failure Modes and Effects Analysis (FMEA):** A tool for systematic, PROACTIVE
analysis of a process where harm may occur — preventing it by correcting processes
proactively rather than reacting to adverse events after failures. FMEA prompts teams
to review, evaluate, and record:
- Steps in the process
- Failure modes (what could go wrong?)
- Failure causes (why would the failure happen?)
- Failure effects (consequences — severity and frequency — of each failure)
- How the failure can be prevented

FMEA forms the core of risk assessment and risk mitigation.

---

## BUILD INSTRUCTIONS FOR CLAUDE CODE

1. Embed as a constant (e.g. QUALITY_TOOLS_CONTENT) in the Edge Function
   supabase/functions/ai-assistant/index.ts — same pattern as GENERAL_INFO,
   GLOSSARY, SHCO_KPI_CONTENT, MEDICATION_ERROR_CONTENT. No new table.

2. Add a detection branch for: "quality tool", "RCA", "root cause analysis",
   "5 whys", "fishbone", "ishikawa", "cause and effect diagram", "affinity
   diagram", "histogram", "FMEA", "failure mode", "chart review checklist",
   "how to count opportunities", "medication audit form".

3. IMPORTANT OVERLAP CHECK — there are now THREE medication-related content blocks:
   - KPI #2 (medication error RATE/formula) → SHCO_KPI_CONTENT
   - Categorization (NCC-MERP A-I, algorithm) → MEDICATION_ERROR_CONTENT
   - Chart review checklist + opportunity counting → THIS content
   Test that "medication error rate formula" → KPI, "categorize a medication
   error" → Annexure 2, "how do I count opportunities in a chart review" → THIS.
   These must not collide.

4. System prompt: cite source as "Source: SHCO Full — Quality Tools (Annexure 3)"
   for QI tools, and "Source: SHCO Full — Medication Chart Review Checklist
   (Annexure 2)" for the checklist content.

5. Test questions:
   - "what is FMEA" → proactive analysis tool, the 5 review points, source
   - "what is the 5 whys" → root cause tool, shifts blame to process, criticism noted
   - "what quality tools does NABH recognise" → lists all 6
   - "how do I count opportunities in a medication chart review" → the cells-minus-NA
     rule, with the 186 example
   - "what parameters do nurses get audited on in chart review" → parameters 24-35
   - Overlap: "medication error rate formula" must still → KPI content (not this)
