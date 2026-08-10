# -*- coding: utf-8 -*-
"""Placeholder audit shared by the master-policy build scripts.

Why this exists: the HIC.4 build script originally counted placeholders as

    sum(s.count("[Hospital to define]") for s in PROCEDURE_STEPS)
      + DISTRIBUTION.count(...) + ABBREVIATIONS.count(...)

which was wrong twice over, and the two errors happened to cancel into a
plausible-looking number:

  1. It omitted rendered fields. `disclaimer` carries a placeholder and was
     never counted; purpose/scope/policy_statement/responsibility/references
     and the oe_mapping cells were never checked at all.
  2. It counted only the EXACT string "[Hospital to define]". The variant form
     "[Hospital to define — some guidance]" does NOT contain that substring, so
     every guidance-bearing placeholder was invisible to the count — including
     the intranet location in Distribution, which was therefore reported as
     having none.

A hospital filling this document searches for the blanks. If the count in the
build output disagrees with what they find, the inventory is worse than no
inventory. So: count every rendered field, and count both forms.

`universal_facts_checklist` is deliberately EXCLUDED — it is an internal review
field, not rendered into the docx (see _shared/policy-doc-template.ts, which has
no parameter for it). Counting it would inflate the figure with prose that
describes placeholders rather than being one.
"""
import json
import re

EXACT = "[Hospital to define]"

# Matches a placeholder in either form and captures the whole bracketed unit.
# Non-greedy up to the first closing bracket, which is why nesting is reported
# separately below rather than silently mis-measured.
ANY = re.compile(r"\[Hospital to define(?:[^\[\]]*)\]")
OPENER = re.compile(r"\[Hospital to define")
NESTED = re.compile(r"\[Hospital to define[^\[\]]*\[Hospital to define")

# Fields that reach the rendered docx. Mirrors the argument list passed to
# buildPolicyDocument() in supabase/functions/generate-hospital-policy/index.ts.
RENDERED_TEXT_FIELDS = [
    "policy_title", "purpose", "scope", "policy_statement",
    "responsibility", "references_text", "distribution",
    "abbreviations", "disclaimer",
    # optional five — counted when present, absent in HIC.1-4
    "definitions", "training_competency", "resources_required",
    "monitoring_audit", "exceptions",
]


def _counts(text):
    """(exact, variant) for one string. variant = opener present, exact form absent."""
    openers = len(OPENER.findall(text))
    exact = text.count(EXACT)
    return exact, openers - exact


def audit(draft, verbose=True):
    """Audit a draft dict. Returns (exact, variant, total, problems)."""
    rows = []
    problems = []

    for f in RENDERED_TEXT_FIELDS:
        v = draft.get(f)
        if not v:
            continue
        e, var = _counts(v)
        if e or var:
            rows.append((f, e, var))

    steps = draft.get("procedure_steps", [])
    se = sv = 0
    for i, s in enumerate(steps, start=1):
        e, var = _counts(s)
        se += e
        sv += var
        if NESTED.search(s):
            problems.append(
                f"step {i}: NESTED placeholder — a bracket inside a bracket cannot be "
                f"replaced as one unit and renders a stray ']'"
            )
    if se or sv:
        rows.append((f"procedure_steps ({len(steps)})", se, sv))

    om = json.dumps(draft.get("oe_mapping", []), ensure_ascii=False)
    e, var = _counts(om)
    if e or var:
        rows.append(("oe_mapping", e, var))

    exact = sum(r[1] for r in rows)
    variant = sum(r[2] for r in rows)

    if verbose:
        print()
        print(f"  {'field':34}{'exact':>7}{'variant':>9}{'total':>7}")
        print(f"  {'-' * 55}")
        for name, e_, v_ in rows:
            print(f"  {name:34}{e_:>7}{v_:>9}{e_ + v_:>7}")
        print(f"  {'-' * 55}")
        print(f"  {'TOTAL fillable blanks':34}{exact:>7}{variant:>9}{exact + variant:>7}")
        print()
        print(f"  A search for the exact string '{EXACT}' finds {exact} of {exact + variant}.")
        print(f"  A search for 'Hospital to define' (no brackets) finds all {exact + variant}.")
        if problems:
            print()
            for p in problems:
                print(f"  !! {p}")

    return exact, variant, exact + variant, problems
