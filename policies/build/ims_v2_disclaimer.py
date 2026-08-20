# -*- coding: utf-8 -*-
"""IMS v2 disclaimer helper.

Accreditation-only P2 plus one light data-protection forward-note. The note is the
hospital's duty to check current law, not a cited requirement of the 3rd Edition.
Does not name the DPDP Act 2023. P1/P3/P4 hashes stay byte-identical.
"""
from __future__ import annotations

from policy_build_common import make_disclaimer_accreditation_only

DATAPROTECTION_FORWARD_NOTE = (
    "{{HOSPITAL_NAME}} must verify its obligations under applicable data-protection "
    "law (data-protection law has evolved since 2022). That verification is the hospital's "
    "duty; it is not a cited requirement of this NABH SHCO 3rd Edition standard."
)


def make_ims_disclaimer() -> tuple[str, str]:
    """Return (disclaimer, statute_clause) for IMS v2 builders."""
    disclaimer, statute_clause = make_disclaimer_accreditation_only()
    p1, p2, p3, p4 = disclaimer.split("\n\n")
    p2 = p2 + " " + DATAPROTECTION_FORWARD_NOTE
    return "\n\n".join([p1, p2, p3, p4]), statute_clause
