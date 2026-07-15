# SHCO Medication Error Monitoring Reference (Annexure 2)
Source: NABH Accreditation Standards for Small Healthcare Organizations, 3rd Edition,
August 2022, Annexure 2 "Guidance On Monitoring Medication Errors" (pages 160-165),
official document. Categorization framework © 2001 NCC-MERP (National Coordinating
Council for Medication Error Reporting and Prevention).

Use this to ground the AI's answers when a user asks about medication error
CATEGORIZATION, harm levels, the classification algorithm, or how to monitor/
analyze medication errors. This supports the medication-audit OEs (MOM.3.f,
MOM.3.g) and KPI #2 (Incidence of medication errors).

---

## Definition of a Medication Error (NCC-MERP)

A medication error is any preventable event that may cause or lead to inappropriate
medication use or patient harm while the medication is in the control of the
healthcare professional, patient, or consumer. Such events may relate to professional
practice, healthcare products, procedures, and systems — including prescribing, order
communication, product labelling, packaging and nomenclature, compounding,
dispensing, distribution, administration, education, monitoring, and use.

---

## Categories of Medication Error (A through I)

The NCC-MERP index classifies errors into 4 harm levels and 9 categories:

**NO ERROR**
- Category A — Circumstances or events that have the capacity to cause error

**ERROR, NO HARM**
- Category B — An error occurred, but it did not reach the patient (note: an "error of omission" DOES reach the patient)
- Category C — An error occurred that reached the patient but did not cause harm
- Category D — An error reached the patient and required monitoring to confirm no harm resulted, and/or required intervention to preclude harm

**ERROR, HARM**
- Category E — An error that may have contributed to or resulted in temporary harm, requiring intervention
- Category F — An error that may have contributed to or resulted in temporary harm, requiring initial or prolonged hospitalization
- Category G — An error that may have contributed to or resulted in permanent patient harm
- Category H — An error that required intervention necessary to sustain life

**ERROR, DEATH**
- Category I — An error that may have contributed to or resulted in the patient's death

---

## Key Definitions (used in categorization)

- **Harm** — Impairment of the physical, emotional, or psychological function or structure of the body, and/or pain resulting therefrom.
- **Monitoring** — To observe or record relevant physiological or psychological signs.
- **Intervention** — May include change in therapy or active medical/surgical treatment.
- **Intervention Necessary to Sustain Life** — Includes cardiovascular and respiratory support (e.g. CPR, defibrillation, intubation).

---

## Classification Algorithm (decision tree, in words)

To categorize an error, work through these questions in order:

1. Did an actual error occur? → NO = Category A
2. Did the error reach the patient? → NO = Category B
3. Did the error contribute to or result in patient death? → YES = Category I
4. Was the patient harmed? → NO branch:
   - Was intervention to preclude harm or extra monitoring required? → YES = Category D, NO = Category C
5. If patient WAS harmed:
   - Did the error require intervention necessary to sustain life? → YES = Category H
   - Was the harm permanent? → YES = Category G
   - Was the harm temporary?
     - Did the error require initial or prolonged hospitalization? → YES = Category F, NO = Category E

---

## Methodology for Monitoring

Preferred methods: Chart Review, Audit, and Self-Reporting of medication errors
(for manually documented charts). Software programmes can be used where prescriptions
are generated online.

Important principles:
- Identifying personnel involved in errors is for proper ROOT CAUSE ANALYSIS and
  corrective/preventive action — NOT for punitive action. Process improvements are
  essential to reduce errors.
- Population for sample size = running average of the previous 3 months of admissions
  (per NABH's sample size calculation — see KPI Annexure 1).
- Files from ALL clinical specialities must be included; stratified sampling helps
  achieve this.
- Self-reported errors, errors found during audits, and errors found by any other
  methodology are ALL added to the numerator (total errors identified).

**Formula:** Total number of errors identified / Total number of opportunities × 100

---

## Immediate Correction (before full analysis)

While root-cause analysis is pending, immediate correction to mitigate the error:
- For Category A and B → Administer the drug within a reasonable timeframe
- For Category C and D → Consult the clinician and follow orders accordingly

---

## Analysis — Root Cause Categories

Data is collated by error category (A-I) against personnel (Doctors / Nurses /
Pharmacists). Possible root causes fall into 4 groups:

**People** — Casual attitude, inexperienced/new staff, untrained staff, shift-change/
hurry, emotionally or physically unfit, wrong indent/receiving, patient identification
error.

**Environment** — Pharmacy poor drug storage (ventilation/lighting/humidity), space
constraints for storage, manpower constraints for dispensing.

**Equipment** — Defective syringe pumps, inappropriate syringe/diluent.

**Process** — "Ten rights" not observed, wrong stocking, wrong labelling, no
cross-checking, stock-outs, unauthorized drug replacement, LASA (look-alike sound-
alike) medicine error, wrong dispensing, wrong distribution, illegible handwriting.

Common corrective actions: Training, manpower recruitment, pharmacy stock
rectification, equipment replacement/rectification.

---

## BUILD INSTRUCTIONS FOR CLAUDE CODE

1. Embed this as a constant (e.g. MEDICATION_ERROR_CONTENT) in the Edge Function
   supabase/functions/ai-assistant/index.ts — same pattern as GENERAL_INFO,
   GLOSSARY, and SHCO_KPI_CONTENT. Do NOT create a new table; this is static
   reference content.

2. Add a detection branch (e.g. isMedicationErrorQuestion()) that routes to this
   content when the question matches: "medication error", "category A/B/C...",
   "NCC-MERP", "harm level", "how to categorize/classify medication error",
   "root cause" + "medication", "LASA". Place it in the retrieval pipeline
   alongside the existing KPI/glossary/general-info branches.

3. System prompt: when answering medication-error categorization questions,
   include the specific category letter(s) and the harm level. Cite source as
   "Source: SHCO Full — Medication Error Monitoring (Annexure 2, NCC-MERP)".

4. Note the overlap: KPI #2 (medication error rate) is already in SHCO_KPI_CONTENT.
   Make sure a question like "what is the medication error rate formula" still
   routes to the KPI content (formula focus), while "how do I categorize a
   medication error" routes to THIS content (categorization focus). Test both
   to confirm they don't collide.

5. Test questions: "what is a category D medication error", "how do I categorize
   a medication error that reached the patient but caused no harm", "what are the
   harm levels for medication errors", "what's the difference between category E
   and F" — confirm grounded answers with correct category letters and source.
