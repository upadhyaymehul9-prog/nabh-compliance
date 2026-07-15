# SHCO KPI Reference Content
Source: NABH Accreditation Standards for Small Healthcare Organizations, 3rd Edition,
August 2022, Annexure 1 (pages 151-159), official document.

This is the full, verified KPI annexure — 15 NABH-mandated KPIs with exact
definitions, formulas, units, and monitoring frequency. Use this to ground
the AI's answers when a user asks about a SPECIFIC KPI (e.g. "what is the
formula for medication error rate") — separate from the general "what is a
KPI" definition already in shco_general_info_content.md.

IMPORTANT: cross-check against your existing `kpis` Supabase table before
building — memory notes mention "15 NABH-mandated KPIs" for SHCO, which
matches this PDF's count exactly. If your kpis table already has this data
structured, USE THAT TABLE as the retrieval source instead of duplicating
it here — don't create a second source of truth for the same data. Only
use this file's content if the kpis table is missing/incomplete for SHCO.

---

## Why KPIs Matter (context, from Annexure 1 intro)

Key Performance Indicators (KPIs) help to systematically monitor, evaluate,
and continually improve service performance. By themselves, KPIs cannot
improve performance — they provide signposts that signal progress toward
goals and opportunities for sustainable improvement. Well-designed KPIs
help an organisation to: establish baseline information, set performance
standards/targets, measure and report improvements over time, compare
performance across locations, benchmark against regional/international
peers, and allow stakeholders to independently judge health sector
performance.

---

## The 15 KPIs (full table)

| # | Standard | Indicator | Formula | Unit | Frequency | Sampling |
|---|---|---|---|---|---|---|
| 1 | PSQ.2a | Time for initial assessment of indoor patients | Sum of assessment time / Total admissions (sample size) | Minutes | Monthly | Yes — stratified random |
| 2 | PSQ.2a | Incidence of medication errors | Total medication errors / Total opportunities × 100 | % | Monthly | Yes — stratified random |
| 3 | PSQ.2a | Percentage of transfusion reactions | Number of transfusion reactions / Number of units transfused × 100 | % | Monthly | No |
| 4 | PSQ.2a | Standardised Mortality Ratio for ICU | Actual ICU deaths / Predicted ICU deaths | Ratio | Monthly | No |
| 5 | PSQ.2a | Incidence of hospital-associated pressure ulcers after admission | New/worsening pressure ulcers / Total patient days × 1000 | per 1000 patient days | Monthly | No |
| 6 | PSQ.2b | Catheter-associated UTI rate | UTIs associated with urinary catheter (month) / Urinary catheter days × 1000 | per 1000 catheter days | Monthly | No |
| 7 | PSQ.2b | Ventilator-associated Pneumonia rate | VAP cases (month) / Ventilator days × 1000 | per 1000 ventilator days | Monthly | No |
| 8 | PSQ.2b | Central line-associated Blood stream infection rate | CLABSI cases (month) / Central line days × 1000 | per 1000 central line days | Monthly | No |
| 9 | PSQ.2b | Surgical site infection rate | SSIs (given month) / Surgeries performed (that month) × 100 | per 100 procedures | Monthly | No (special rolling/cumulative methodology — see note below) |
| 10 | PSQ.2b | Compliance to hand hygiene practice | Total hand hygiene actions performed / Total hand hygiene opportunities × 100 | % | Monthly | Yes — stratified random |
| 11 | PSQ.2b | % of cases receiving appropriate prophylactic antibiotics within specified timeframe | Patients who received appropriate antibiotic (dose+time) / Patients who underwent surgery × 100 | % | Monthly | No |
| 12 | PSQ.2c | Waiting time for diagnostics | Sum total time / Number of patients reported in diagnostics | Minutes | Monthly | No |
| 13 | PSQ.2c | Time taken for discharge | Sum of discharge time / Number of patients discharged | Minutes | Monthly | No |
| 14 | PSQ.2d | Incidence of patient falls | Number of patient falls / Total patient days × 1000 | per 1000 patient days | Monthly | No |
| 15 | PSQ.2d | Rate of needlestick injuries | Needlestick injuries / Occupied beds × 100 | per 100 occupied beds, cumulative YTD | Monthly (reported cumulative) | No |

---

## Important Special-Case Notes (don't drop these — they change how the KPI is interpreted)

**KPI #9 (Surgical Site Infection rate)** has a unique rolling/cumulative
methodology — the numerator updates over a 30 and then 90-day surveillance
window after the reporting month, so the "final" SSI rate for any given
month isn't known until ~90 days later. If a user asks about this KPI,
the AI should explain this timing nuance, not just give the formula.

**KPI #15 (Needlestick injury rate)** is reported cumulatively (year-to-date),
not as a standalone monthly figure — e.g. February's reported rate includes
January+February combined data, unlike all other KPIs which are monthly
snapshots.

**Sampling methodology**, when applicable (KPIs #1, #2, #10), uses stratified
random sampling — not convenience sampling — specifically to eliminate bias.

---

## Sample Size Calculation Table (for KPIs requiring sampling)

Uses Solvin's formula: n = N / (1 + Ne²) at 95% confidence interval.

| Screening Population (avg of preceding 3 months) | Required Sample Size |
|---|---|
| 50 | 44 |
| 100 | 79 |
| 150 | 108 |
| 200 | 132 |
| 500 | 217 |
| 1000 | 278 |
| 2000 | 322 |
| 5000 | 357 |
| 10000 | 370 |
| 20000 | 377 |

The "screening population" is the average of the previous three months for
the relevant metric (e.g. for "time for initial assessment," it's the average
monthly admissions over the prior 3 months).

---

## BUILD INSTRUCTIONS FOR CLAUDE CODE

1. FIRST — query the existing `kpis` table in Supabase. Check if these 15
   SHCO KPIs already exist there with formula/unit/frequency data. If yes,
   wire the AI's retrieval to query THAT table when a KPI question is asked
   — don't duplicate this content into a new table.

2. If the kpis table doesn't have this data (or doesn't exist for SHCO
   specifically), create the structured content as a JS constant or new
   table, following the same pattern as the general-info content from the
   previous session.

3. Update the retrieval logic in supabase/functions/ai-assistant/index.ts:
   add a branch that detects KPI-related questions (keyword match: "KPI",
   "indicator", a KPI name like "medication error rate", or a standard code
   like PSQ.2a/2b/2c/2d when asked in a KPI context) and retrieves from this
   KPI content instead of (or in addition to) the OE table.

4. System prompt addition: when answering a KPI question, ALWAYS include the
   formula and unit, not just a description — that's the part hospital staff
   actually need to implement tracking. Cite source as "Source: SHCO Full —
   KPI Annexure 1, [Indicator Name]".

5. Test questions: "what is the formula for medication error rate", "what
   is PSQ.2a", "how do I calculate surgical site infection rate", "what
   sample size do I need for 200 patients" — confirm grounded, formula-
   complete answers.
