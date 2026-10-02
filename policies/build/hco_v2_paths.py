# -*- coding: utf-8 -*-
"""Physical output paths for HCO Full (6th Edition) v2 masters.

HCO files must never share folders with SHCO. SHCO keeps:

- policies/drafts/
- policies/build/preview/
- policies/build/masters/

HCO writes only to the ``*_hco`` siblings. Import these constants from HCO
builders and generators; do not hard-code the old mixed folders.
"""
from __future__ import annotations

from pathlib import Path

from policy_build_common import POLICIES

HCO_DRAFTS = POLICIES / "drafts_hco"
HCO_PREVIEW = POLICIES / "build" / "preview_hco"
HCO_MASTERS = POLICIES / "build" / "masters_hco"

# Relative POSIX paths for Deno / shell (repo-root relative).
HCO_DRAFTS_REL = "policies/drafts_hco/"
HCO_PREVIEW_REL = "policies/build/preview_hco/"
HCO_MASTERS_REL = "policies/build/masters_hco/"
