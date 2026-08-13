# -*- coding: utf-8 -*-
"""Strengthens entry 4 of the HIC.1 universal_facts_checklist — the IPC staffing benchmark.

Raised on review 2026-08-13: the entry cited "the source" for the characterisation of
1:250 as a floor without naming which source carries that characterisation, and the
1:100 comparator used in step 16 ("facilities with high-acuity or high-turnover caseloads
commonly require a richer ratio") had no citation at all.

Verification performed 2026-08-13 against the WHO source PDF directly (text extracted with
pdfplumber, not read from a search summary):

  WHO. Minimum requirements for infection prevention and control programmes. Geneva:
  World Health Organization; 2019.

  p.23 / p.32, secondary care: "Trained IPC focal point (one full-time trained IPC officer
  [nurse or doctor]) as per the recommended ratio of 1:250 beds with dedicated time to carry
  out IPC activities in all facilities", with the worked example that a 120-bed facility
  requires one 50% full-time equivalent dedicated officer.

  p.23 / p.32, tertiary care: "At least one full-time trained IPC focal point (nurse or
  doctor) with dedicated time per 250 beds."

  p.35: "A minimum ratio of one full-time or equivalent IPC professional (nurse or doctor)
  per 250 beds or a higher ratio (one IPC professional per 100 beds) due to increased patient
  acuity and complexity, as well as the multiple roles and increasing responsibilities of the
  IPC professional."

The original attribution to WHO was therefore CORRECT, and p.35 is the specific sentence that
supports step 16's "floor rather than a target" wording. The lineage of both numbers is added
so a later reader does not have to re-derive it.

This edits universal_facts_checklist only. It is an internal review field and is not rendered
into the DOCX (policy-doc-template.ts has no parameter for it), so no document output changes.
"""
import json
from pathlib import Path

_HERE = Path(__file__).resolve().parent
DRAFT = _HERE.parent / "drafts" / "hic1_draft.json"
SQL_OUT = _HERE.parent / "sql" / "hic1_staffing_citation_update.sql"

EM = "—"

OLD = (
    "4. IPC staffing benchmark " + EM + " a minimum of one full-time equivalent trained "
    "infection prevention professional (nurse or doctor) per 250 beds, described in the "
    "source as a floor with a richer ratio argued for in higher-acuity settings. Used in "
    "step 16. Verified via WHO Minimum Requirements for Infection Prevention and Control "
    "Programmes (2019)."
)

NEW = (
    "4. IPC staffing benchmark " + EM + " a minimum of one full-time equivalent trained "
    "infection prevention professional (nurse or doctor) per 250 beds, described in the "
    "source as a floor with a richer ratio argued for in higher-acuity settings. Used in "
    "step 16. Verified via WHO, Minimum requirements for infection prevention and control "
    "programmes, Geneva: World Health Organization, 2019 " + EM + " re-verified 2026-08-13 "
    "against the source PDF itself rather than a secondary summary.\n"
    "   EXACT WORDING RELIED ON. Secondary care (p.23, p.32): \"Trained IPC focal point (one "
    "full-time trained IPC officer [nurse or doctor]) as per the recommended ratio of 1:250 "
    "beds with dedicated time to carry out IPC activities in all facilities\", with the worked "
    "example that a 120-bed facility requires one 50% full-time equivalent dedicated officer "
    + EM + " which is the arithmetic step 16 asks the hospital to perform for its own bed "
    "count. Tertiary care (p.23, p.32): \"At least one full-time trained IPC focal point (nurse "
    "or doctor) with dedicated time per 250 beds.\"\n"
    "   THE \"FLOOR, NOT A TARGET\" CHARACTERISATION IS WHO'S OWN, at p.35: \"A minimum ratio of "
    "one full-time or equivalent IPC professional (nurse or doctor) per 250 beds or a higher "
    "ratio (one IPC professional per 100 beds) due to increased patient acuity and complexity, "
    "as well as the multiple roles and increasing responsibilities of the IPC professional.\" "
    "This single sentence carries both halves of step 16 " + EM + " the 1:250 floor and the "
    "richer ratio for higher acuity " + EM + " so step 16 does not depend on any source outside "
    "WHO. WHO itself names 1:100 as the higher ratio.\n"
    "   LINEAGE OF THE TWO NUMBERS, recorded so it need not be re-derived. The 1:250 figure "
    "originates in the CDC Study on the Efficacy of Nosocomial Infection Control (SENIC), 1985, "
    "which associated one infection control professional per 250 occupied acute care beds with "
    "a 32% reduction in nosocomial infection. The 1:100 comparator originates in the APIC "
    "Delphi study " + EM + " O'Boyle C, Jackson M, Henly SJ, \"Staffing requirements for "
    "infection control programs in US health care facilities: Delphi project\", American Journal "
    "of Infection Control, October 2002 " + EM + " which recommended 0.8 to 1.0 infection control "
    "professionals per 100 occupied acute care beds, roughly 2.5 to 3 times the SENIC figure, on "
    "the ground that the scope of the role had expanded well beyond what SENIC measured.\n"
    "   REVIEWER TO NOTE: the professional-society literature treats 1:250 as outdated on its "
    "own, and published ratios in current practice run richer still. Step 16 is nonetheless "
    "correct as written and correctly sourced: it presents 1:250 as a floor, not as adequate "
    "staffing, and requires {{HOSPITAL_NAME}} to state and justify its own establishment rather "
    "than adopt the benchmark as its target. No change to step 16 is required."
)


def main() -> None:
    draft = json.loads(DRAFT.read_text(encoding="utf-8"))
    text = draft["universal_facts_checklist"]

    if OLD not in text:
        raise SystemExit("entry 4 not found verbatim — the checklist has changed; re-read before editing")
    if text.count(OLD) != 1:
        raise SystemExit("entry 4 matched more than once — refusing to edit ambiguously")

    draft["universal_facts_checklist"] = text.replace(OLD, NEW)
    DRAFT.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Live rows store CRLF; the local draft stores LF. Match the live convention.
    payload = draft["universal_facts_checklist"].replace("\n", "\r\n")
    literal = "'" + payload.replace("'", "''") + "'"
    SQL_OUT.write_text(
        "-- HIC.1: strengthen universal_facts_checklist entry 4 (IPC staffing benchmark citation).\n"
        "-- Internal review field only; not rendered into the DOCX. No document output changes.\n"
        "update public.shco_policy_masters\n"
        f"   set universal_facts_checklist = {literal}\n"
        " where standard_code = 'HIC.1';\n",
        encoding="utf-8",
    )
    print(f"entry 4: {len(OLD)} -> {len(NEW)} chars")
    print(f"checklist total: {len(text)} -> {len(draft['universal_facts_checklist'])} chars (LF)")
    print(f"wrote {SQL_OUT}")


if __name__ == "__main__":
    main()
