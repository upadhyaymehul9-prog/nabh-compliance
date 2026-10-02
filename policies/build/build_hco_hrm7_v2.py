# -*- coding: utf-8 -*-
"""HCO HRM.7 v2 — Staff Performance Appraisal (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_hrm_v2.py
Explicit draft_label via hco_hrm_v2_common.hco_document_control.
Does NOT overwrite SHCO (including SHCO's own HRM chapter), HCO AAC, HCO COP,
HCO MOM, HCO PRE, HCO IPC, HCO PSQ, HCO ROM or HCO FMS files.
"""
from __future__ import annotations

import sys
from generate_hco_hrm_v2 import emit_standard

if __name__ == "__main__":
    sys.exit(emit_standard(7))
