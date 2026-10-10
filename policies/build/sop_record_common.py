# -*- coding: utf-8 -*-
"""Shared builder for SHCO SOP + Record master .docx files.

Introduced with the FMS chapter (Oct 2026). The AAC/COP/HRM/ROM chapters
were each hand-built with one-off python-docx scripts -- no reusable module
existed. This factors out the structure every one of those files already
shared (verified against SOP_COP.13.*.docx and its Records/*.docx on
2026-10-10: same heading set, same "Table Grid" style, same yellow
FFF2CC worked-example-row shading, same page/margin defaults), so every
later chapter (PSQ, MOM, IPC, PRE, HRM additions, etc.) builds from one
place instead of re-deriving the template by eye each time.

Nothing here invents new structure. It only encodes what the already-
approved files already do, so this module is itself verifiable against
them -- see policies/build/verify_sop_record_template.py.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt

WORKED_EXAMPLE_FILL = "FFF2CC"


def _shade_row(row, fill: str = WORKED_EXAMPLE_FILL) -> None:
    for cell in row.cells:
        tcPr = cell._tc.get_or_add_tcPr()
        shd = tcPr.makeelement(qn("w:shd"), {
            qn("w:val"): "clear",
            qn("w:color"): "auto",
            qn("w:fill"): fill,
        })
        tcPr.append(shd)


def _add_single_cell_table(doc: Document, text: str) -> None:
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    t.rows[0].cells[0].text = text
    doc.add_paragraph("")


# ---------------------------------------------------------------- SOP -----

@dataclass
class ProcedureBlock:
    heading: str          # e.g. "4.1 Patients in pain are effectively managed (COP.13.a)"
    why_it_matters: str
    steps: list[str]      # already-numbered strings, "1. ...", "2. ..."
    technical_sources: list[str] | None = None  # bare APA-style lines, bulleted


@dataclass
class SOPSpec:
    sop_no: str                 # "SOP-FMS.1"
    title: str                  # "Planned Facilities, Utilities and Environment-Friendly Measures"
    standard_code_range: str    # "FMS.1.a-f"
    what_is_this_for: str
    worked_example: str
    why_nabh_asks: str
    purpose: str
    scope: str
    responsibilities: list[tuple[str, str]]   # (role, text)
    blocks: list[ProcedureBlock]
    records_note: str
    related_documents: list[str]
    verified_sources: list[str]
    review_text: str
    effective_date_placeholder: str = "«________»"
    version: str = "1.0"


def build_sop(spec: SOPSpec, out_path: Path) -> None:
    doc = Document()

    doc.add_paragraph("Standard Operating Procedure")
    doc.add_paragraph(spec.title)
    doc.add_paragraph(f"«Hospital Name» — Supports {spec.standard_code_range}")
    doc.add_paragraph("")
    doc.add_paragraph("")
    doc.add_paragraph("")

    _add_single_cell_table(doc, spec.what_is_this_for)
    _add_single_cell_table(doc, spec.worked_example)
    _add_single_cell_table(doc, spec.why_nabh_asks)

    ctrl = doc.add_table(rows=2, cols=4)
    ctrl.style = "Table Grid"
    ctrl.rows[0].cells[0].text = "SOP No."
    ctrl.rows[0].cells[1].text = spec.sop_no
    ctrl.rows[0].cells[2].text = "Version"
    ctrl.rows[0].cells[3].text = spec.version
    ctrl.rows[1].cells[0].text = "Effective Date"
    ctrl.rows[1].cells[1].text = spec.effective_date_placeholder
    ctrl.rows[1].cells[2].text = "Review Frequency"
    ctrl.rows[1].cells[3].text = "Annual, or on change"
    doc.add_paragraph("")

    doc.add_heading("1. Purpose", level=1)
    doc.add_paragraph(spec.purpose)

    doc.add_heading("2. Scope", level=1)
    doc.add_paragraph(spec.scope)

    doc.add_heading("3. Responsibility", level=1)
    for role, text in spec.responsibilities:
        doc.add_paragraph(f"{role}: {text}")

    doc.add_heading("4. Procedure", level=1)
    for i, block in enumerate(spec.blocks, start=1):
        doc.add_heading(block.heading, level=2)
        doc.add_paragraph(f"Why this step matters: {block.why_it_matters}")
        for step in block.steps:
            doc.add_paragraph(step)
        if block.technical_sources:
            doc.add_paragraph("Technical source(s) for these steps: ")
            for src in block.technical_sources:
                doc.add_paragraph(f"• {src}", style="List Paragraph")

    doc.add_heading("5. Records", level=1)
    doc.add_paragraph(spec.records_note)

    doc.add_heading("6. Related Documents", level=1)
    for rd in spec.related_documents:
        doc.add_paragraph(rd, style="List Paragraph")

    doc.add_heading("7. Where This SOP's Requirements Come From (Verified Sources)", level=1)
    for src in spec.verified_sources:
        doc.add_paragraph(f"• {src}", style="List Paragraph")

    doc.add_heading("8. Review", level=1)
    doc.add_paragraph(spec.review_text)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))


# -------------------------------------------------------------- Record -----

@dataclass
class RecordSpec:
    oe_code: str
    oe_requirement: str
    record_title: str           # "FMS.1 Record 1 -- Space-to-service-directory alignment record"
    what_is_this: str
    real_example: str
    why_nabh_asks: str
    how_to_fill: list[tuple[str, str]]   # (column_name, instruction)
    verified_sources: list[str]
    column_headers: list[str]
    worked_example_row: list[str]
    extra_blank_rows: int = 7


def build_record(spec: RecordSpec, out_path: Path) -> None:
    doc = Document()

    doc.add_paragraph(f"{spec.oe_code} — {spec.oe_requirement}")
    doc.add_paragraph(spec.record_title)
    doc.add_paragraph("")
    doc.add_paragraph("")
    doc.add_paragraph("")

    _add_single_cell_table(doc, f"What is this record, in plain terms?\n{spec.what_is_this}")
    _add_single_cell_table(doc, f"A real example of when you'd use this\n{spec.real_example}")
    _add_single_cell_table(doc, f"Why does NABH ask for this?\n{spec.why_nabh_asks}")

    doc.add_paragraph("How to fill this in — column by column")
    for col, instr in spec.how_to_fill:
        doc.add_paragraph(f"{col}: {instr}")
    doc.add_paragraph(
        "The first data row below (shaded yellow, and marked WORKED EXAMPLE "
        "in the row itself) is a worked example already filled in correctly. "
        "Delete it or overwrite it once you start using this record for real "
        "— don't leave the example row mixed in with real entries. Add "
        "more blank rows as needed; don't create a second copy of this file."
    )
    doc.add_paragraph("")

    doc.add_paragraph("Where this requirement comes from (verified, clickable sources)")
    for src in spec.verified_sources:
        doc.add_paragraph(f"• {src}", style="List Paragraph")
    doc.add_paragraph("")
    doc.add_paragraph("")
    doc.add_paragraph("")

    n_cols = len(spec.column_headers)
    total_rows = 1 + 1 + 1 + spec.extra_blank_rows  # header + spacer + example + blanks
    t = doc.add_table(rows=total_rows, cols=n_cols)
    t.style = "Table Grid"
    for j, h in enumerate(spec.column_headers):
        t.rows[0].cells[j].text = h
    _shade_row(t.rows[1])
    for j in range(n_cols):
        t.rows[1].cells[j].text = ""
    _shade_row(t.rows[2])
    for j, v in enumerate(spec.worked_example_row):
        t.rows[2].cells[j].text = v

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))
