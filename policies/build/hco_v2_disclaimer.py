# -*- coding: utf-8 -*-
"""HCO Full v2 disclaimer helper (6th Edition).

Accreditation-only P2 by default (names HCO Full Accreditation 6th Edition).
Imaging standards pass a statute_clause into make_disclaimer() for AERB /
PC-PNDT where the guidebook names them.
"""
from __future__ import annotations

from policy_build_common import (
    DISCLAIMER_P1,
    DISCLAIMER_P3,
    DISCLAIMER_P4,
    make_disclaimer,
)


def make_hco_disclaimer_accreditation_only() -> tuple[str, str]:
    """P2 for HCO standards whose References do not rely on a named Act."""
    statute_clause = "not duties under a named Act of Parliament"
    p2 = (
        "The requirements in this document are accreditation requirements of the NABH "
        "Full Accreditation Standards for Hospitals, 6th Edition, "
        f"{statute_clause}. This policy does not import the Consumer Protection Act, "
        "2019, the Clinical Establishments Act, 2010, or the Mental Healthcare Act, "
        "2017 as a checklist. Statutory duties that arise under other documents of "
        "{{HOSPITAL_NAME}} remain those documents. {{HOSPITAL_NAME}} is responsible "
        "for verifying any statutory duty that applies to it; this document does not "
        "constitute legal advice."
    )
    return "\n\n".join([DISCLAIMER_P1, p2, DISCLAIMER_P3, DISCLAIMER_P4]), statute_clause


def make_hco_disclaimer_statute(statute_clause: str) -> tuple[str, str]:
    return make_disclaimer(statute_clause), statute_clause
