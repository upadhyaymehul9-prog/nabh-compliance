#!/usr/bin/env python3
"""Build shco_annexure_kb.json from official SHCO 3rd Edition Annexures 1–3.

Content matches supabase/functions/ai-assistant/index.ts constants (book-sourced).
"""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "shco_annexure_kb.json"

KPI_ENTRIES = [
    {
        "title": "KPI 1 — Time for initial assessment of indoor patients",
        "section": "KPI 1",
        "content": (
            "Formula: Sum of time taken for assessment (minutes) / Total number of admissions (sample). "
            "Unit: Minutes. Frequency: Monthly. Sampling required: YES — stratified random sample. "
            "Linked standard: PSQ.2a."
        ),
        "book_page": 151,
    },
    {
        "title": "KPI 2 — Incidence of medication errors",
        "section": "KPI 2",
        "content": (
            "Formula: Total number of medication errors / Total number of opportunities × 100. "
            "Unit: % (percentage). Frequency: Monthly. Sampling required: YES — stratified random sample. "
            "Linked standard: PSQ.2a. See Annexure 2 for error counting methodology."
        ),
        "book_page": 151,
    },
    {
        "title": "KPI 3 — Percentage of transfusion reactions",
        "section": "KPI 3",
        "content": (
            "Formula: Number of transfusion reactions / Number of units transfused × 100. "
            "Unit: % (percentage). Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2a."
        ),
        "book_page": 152,
    },
    {
        "title": "KPI 4 — Standardised Mortality Ratio for ICU (SMR-ICU)",
        "section": "KPI 4",
        "content": (
            "Formula: Actual ICU deaths / Predicted ICU deaths. Unit: Ratio. Frequency: Monthly. "
            "Sampling required: No. Linked standard: PSQ.2a."
        ),
        "book_page": 152,
    },
    {
        "title": "KPI 5 — Incidence of hospital-associated pressure ulcers after admission",
        "section": "KPI 5",
        "content": (
            "Formula: Number of new or worsening pressure ulcers after admission / Total patient days × 1000. "
            "Unit: Per 1000 patient days. Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2a."
        ),
        "book_page": 152,
    },
    {
        "title": "KPI 6 — Catheter-associated UTI rate (CAUTI)",
        "section": "KPI 6",
        "content": (
            "Formula: Number of UTIs associated with urinary catheter in the month / "
            "Number of urinary catheter days in that month × 1000. Unit: Per 1000 catheter days. "
            "Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2b."
        ),
        "book_page": 153,
    },
    {
        "title": "KPI 7 — Ventilator-associated Pneumonia rate (VAP)",
        "section": "KPI 7",
        "content": (
            "Formula: Number of VAP cases in the month / Number of ventilator days in that month × 1000. "
            "Unit: Per 1000 ventilator days. Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2b."
        ),
        "book_page": 153,
    },
    {
        "title": "KPI 8 — Central line-associated Blood Stream Infection rate (CLABSI)",
        "section": "KPI 8",
        "content": (
            "Formula: Number of CLABSI cases in the month / Number of central line days in that month × 1000. "
            "Unit: Per 1000 central line days. Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2b."
        ),
        "book_page": 153,
    },
    {
        "title": "KPI 9 — Surgical site infection rate (SSI)",
        "section": "KPI 9",
        "content": (
            "Formula: Number of SSIs in a given month / Number of surgeries performed in that month × 100. "
            "Unit: Per 100 procedures. Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2b. "
            "SPECIAL NOTE: SSI has rolling/cumulative surveillance — numerator updates over 30-day then 90-day "
            "windows after the reporting month; final rate for a month may not be known for ~90 days."
        ),
        "book_page": 153,
    },
    {
        "title": "KPI 10 — Compliance to hand hygiene practice",
        "section": "KPI 10",
        "content": (
            "Formula: Total number of hand hygiene actions performed (compliant) / "
            "Total number of hand hygiene opportunities × 100. Unit: % (percentage). Frequency: Monthly. "
            "Sampling required: YES — stratified random sample. Linked standard: PSQ.2b."
        ),
        "book_page": 154,
    },
    {
        "title": "KPI 11 — Appropriate prophylactic antibiotics within specified timeframe",
        "section": "KPI 11",
        "content": (
            "Formula: Number of patients who received appropriate prophylactic antibiotic (correct dose and timing) / "
            "Number of patients who underwent surgery × 100. Unit: % (percentage). Frequency: Monthly. "
            "Sampling required: No. Linked standard: PSQ.2b."
        ),
        "book_page": 154,
    },
    {
        "title": "KPI 12 — Waiting time for diagnostics",
        "section": "KPI 12",
        "content": (
            "Formula: Sum total waiting time (minutes) / Number of patients reported in diagnostics. "
            "Unit: Minutes. Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2c."
        ),
        "book_page": 154,
    },
    {
        "title": "KPI 13 — Time taken for discharge",
        "section": "KPI 13",
        "content": (
            "Formula: Sum of time taken for discharge (minutes) / Number of patients discharged. "
            "Unit: Minutes. Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2c."
        ),
        "book_page": 154,
    },
    {
        "title": "KPI 14 — Incidence of patient falls",
        "section": "KPI 14",
        "content": (
            "Formula: Number of patient falls / Total patient days × 1000. "
            "Unit: Per 1000 patient days. Frequency: Monthly. Sampling required: No. Linked standard: PSQ.2d."
        ),
        "book_page": 155,
    },
    {
        "title": "KPI 15 — Rate of needlestick injuries",
        "section": "KPI 15",
        "content": (
            "Formula: Number of needlestick injuries / Number of occupied beds × 100. "
            "Unit: Per 100 occupied beds (cumulative year-to-date). Frequency: Monthly — reported as cumulative YTD. "
            "Sampling required: No. Linked standard: PSQ.2d. "
            "SPECIAL NOTE: Unlike other KPIs, needlestick rate is cumulative YTD (e.g. February includes January + February)."
        ),
        "book_page": 155,
    },
]

SAMPLING_BLOCK = {
    "kb_type": "annexure_kpi",
    "section": "KPI sampling methodology",
    "title": "KPI sampling — Solvin's formula (Annexure 1)",
    "content": (
        "KPIs must be tracked monthly. Assessors verify at least 3 months of data before accreditation. "
        "KPIs are separate from OE scoring — tracked as numbers/rates over time, not rated 1–5. "
        "Stratified random sampling required for KPIs 1, 2, and 10 only — NOT convenience sampling. "
        "Sample size: Solvin's formula n = N / (1 + Ne²) at 95% CI, where N = average of preceding 3 months. "
        "Sample size table: N=50→44, 100→79, 150→108, 200→132, 500→217, 1000→278, 2000→322, 5000→357, "
        "10000→370, 20000→377."
    ),
    "source_label": "SHCO Full — Annexure 1 KPI Sampling (NABH 3rd Edition, pp.151–152)",
    "book_page": 151,
}

MED_ERROR_BLOCK = {
    "kb_type": "annexure_med_error",
    "section": "Medication error categories",
    "title": "Medication error monitoring — NCC-MERP categories A–I (Annexure 2)",
    "content": (
        "DEFINITION (NCC-MERP): A medication error is any preventable event that may cause or lead to "
        "inappropriate medication use or patient harm while the medication is in the control of the healthcare "
        "professional, patient, or consumer. "
        "NO ERROR — Category A: Circumstances or events that have the capacity to cause error. "
        "ERROR NO HARM — B: Error occurred but did NOT reach the patient; C: Reached patient, no harm; "
        "D: Reached patient, monitoring/intervention to preclude harm. "
        "ERROR HARM — E: Temporary harm, intervention; F: Temporary harm, hospitalization; G: Permanent harm; "
        "H: Intervention necessary to sustain life. ERROR DEATH — I: May have contributed to or resulted in death. "
        "Formula: Total number of errors identified / Total number of opportunities × 100 (KPI #2). "
        "Personnel identification is for RCA and corrective action — NOT punitive action."
    ),
    "source_label": "SHCO Full — Annexure 2 Medication Error Monitoring (NABH 3rd Edition, pp.160–165)",
    "book_page": 160,
}

CHART_REVIEW_BLOCK = {
    "kb_type": "annexure_chart_review",
    "section": "Medication chart audit",
    "title": "Medication chart review checklist — 35 parameters (Annexure 2)",
    "content": (
        "Structured audit form: up to 10 drugs per sheet; mark each parameter with error category A–I, 0, or NA. "
        "Doctors (1–13): drug selection, dose, unit, frequency, route, concentration, rate, handwriting, "
        "abbreviations, capitals for drug names, generic names, drug-drug interaction, food-drug interaction. "
        "Doctor/Nurse (14–16): wrong formulation/drug/strength transcribed. "
        "Pharmacist (17–23): wrong drug/dose/formulation, expired drugs, labelling, delay, unauthorized substitute. "
        "Nurses (24–35): wrong patient, omission, improper dose, wrong drug/formulation/route/rate/duration/time, "
        "documentation issues. "
        "ERRORS = cells with A–I. OPPORTUNITIES = cells with 0 or A–I (exclude NA). "
        "Choose ONE category per error — highest severity that applies."
    ),
    "source_label": "SHCO Full — Annexure 2 Chart Review Checklist (NABH 3rd Edition, pp.166–169)",
    "book_page": 166,
}

QUALITY_TOOLS_BLOCK = {
    "kb_type": "annexure_quality_tools",
    "section": "Quality improvement tools",
    "title": "Quality tools — RCA, 5 Whys, Fishbone, Affinity, Histogram, FMEA (Annexure 3)",
    "content": (
        "NABH recognises six tools for QI data analysis: "
        "Root Cause Analysis (RCA) — systematic analysis using 5 Whys or Cause and Effect Diagram; "
        "5 Whys — sequential why questions to root cause; "
        "Cause and Effect Diagram (Ishikawa/Fishbone) — causes grouped under Materials, Methods, Equipment, "
        "Environment, People; "
        "Affinity Diagram — same purpose as Fishbone, different layout; "
        "Histogram — bar chart of continuous data variation; "
        "FMEA — proactive failure modes/effects analysis for risk mitigation before harm occurs."
    ),
    "source_label": "SHCO Full — Annexure 3 Quality Tools (NABH 3rd Edition, pp.170–172)",
    "book_page": 170,
}


def main() -> None:
    entries = [SAMPLING_BLOCK, MED_ERROR_BLOCK, CHART_REVIEW_BLOCK, QUALITY_TOOLS_BLOCK]
    for kpi in KPI_ENTRIES:
        entries.append(
            {
                "kb_type": "annexure_kpi",
                "section": kpi["section"],
                "title": kpi["title"],
                "content": kpi["content"],
                "source_label": f"SHCO Full — Annexure 1 {kpi['title']} (NABH 3rd Edition, p.{kpi['book_page']})",
                "book_page": kpi["book_page"],
            }
        )
    OUT.write_text(json.dumps(entries, indent=2))
    print(f"Wrote {len(entries)} annexure KB entries to {OUT}")


if __name__ == "__main__":
    main()
