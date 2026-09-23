# -*- coding: utf-8 -*-
"""HCO MOM.5 v2 — Uniform Medication Orders (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_mom_v2.py
Explicit draft_label via hco_mom_v2_common.hco_document_control.
Does NOT overwrite SHCO MOM, HCO AAC or HCO COP files.
"""
from __future__ import annotations

import sys
from generate_hco_mom_v2 import emit_standard

if __name__ == "__main__":
    sys.exit(emit_standard(5))
