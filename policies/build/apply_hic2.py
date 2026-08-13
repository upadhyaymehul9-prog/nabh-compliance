# -*- coding: utf-8 -*-
"""Builds the HIC.2 edit locally: the HIC.2.c step expansions plus oe_mapping evidence.

Local-first. Writes the updated draft JSON only. Applying to Supabase is a separate,
reviewed step. Run:  python policies/build/apply_hic2.py
"""
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

from hic2_oe_evidence import HIC2_EVIDENCE                      # noqa: E402
from hic2_tbp_anchor import STEP_15_ADDITION, STEP_19_ADDITION  # noqa: E402

DRAFT = _HERE.parent / "drafts" / "hic2_draft.json"

# 1-based step numbers being expanded, and the text appended to each.
EXPANSIONS = {15: STEP_15_ADDITION, 19: STEP_19_ADDITION}


def main() -> None:
    draft = json.loads(DRAFT.read_text(encoding="utf-8"))
    steps = draft["procedure_steps"]
    mapping = draft["oe_mapping"]

    if len(steps) != 33:
        raise SystemExit(f"expected 33 steps, found {len(steps)} — do not proceed blind")

    for n, addition in EXPANSIONS.items():
        s = steps[n - 1]
        head = s.split("\n", 1)[0]
        if not head.startswith(f"{n}."):
            raise SystemExit(f"step {n} does not start with '{n}.' — numbering has shifted")
        if addition.strip()[:60] in s:
            raise SystemExit(f"step {n} already carries this addition — refusing to double-apply")
        steps[n - 1] = s + addition

    mapped = {m["oe_code"] for m in mapping}
    if mapped != set(HIC2_EVIDENCE):
        raise SystemExit(
            f"OE mismatch:\n  unauthored: {sorted(mapped - set(HIC2_EVIDENCE))}\n"
            f"  extra: {sorted(set(HIC2_EVIDENCE) - mapped)}"
        )

    for m in mapping:
        evidence, responsible = HIC2_EVIDENCE[m["oe_code"]]
        if any(not r.strip() for r in evidence.split(";")):
            raise SystemExit(f"{m['oe_code']}: evidence contains an empty record")
        m["evidence"] = evidence
        m["responsible"] = responsible

    # Step count must be unchanged: HIC.2 was renumbered once already and its six internal
    # cross-references rewritten. Inserting a step would silently invalidate them.
    if len(steps) != 33:
        raise SystemExit("step count changed — cross-references would be invalidated")

    # Placeholder integrity. A single-braced {HOSPITAL_NAME} is never substituted by the
    # renderer and prints literally in the DOCX. str.format() on template text produces exactly
    # that by collapsing the doubled braces, which is how it happened on 2026-08-13.
    blob = json.dumps(draft, ensure_ascii=False)
    doubled = blob.count("{{HOSPITAL_NAME}}")
    # "{HOSPITAL_NAME}" occurs ONCE inside each "{{HOSPITAL_NAME}}", not twice.
    single = blob.count("{HOSPITAL_NAME}") - doubled
    if single:
        raise SystemExit(
            f"{single} single-braced {{HOSPITAL_NAME}} found — these will render literally. "
            "Use .replace('{EM}', EM) on template text, never .format()."
        )
    print(f"placeholder check: {doubled} x {{{{HOSPITAL_NAME}}}}, 0 single-braced")

    DRAFT.write_text(json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    total = sum(len(m["evidence"].split(";")) for m in mapping)
    print(f"HIC.2: {len(mapping)} OEs, {total} records, {len(steps)} steps (unchanged)")
    for m in mapping:
        star = " *" if m["oe_code"] == "HIC.2.c" else "  "
        print(
            f" {star}{m['oe_code']}: {len(m['evidence'].split(';')):3d} records, "
            f"{len(m['evidence']):5d} ev chars, {len(m['responsible']):4d} rs chars"
        )
    for n in EXPANSIONS:
        print(f"  step {n}: now {len(steps[n-1])} chars")


if __name__ == "__main__":
    main()
