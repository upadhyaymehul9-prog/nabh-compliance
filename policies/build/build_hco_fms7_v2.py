# -*- coding: utf-8 -*-
"""HCO FMS.7 v2 — Fire and Non-Fire Emergencies (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_fms_v2.py
Explicit draft_label via hco_fms_v2_common.hco_document_control.
Does NOT overwrite SHCO, HCO AAC, HCO COP, HCO MOM, HCO PRE, HCO IPC, HCO PSQ or HCO ROM files.
"""
from __future__ import annotations

import sys
from generate_hco_fms_v2 import emit_standard

if __name__ == "__main__":
    sys.exit(emit_standard(7))
