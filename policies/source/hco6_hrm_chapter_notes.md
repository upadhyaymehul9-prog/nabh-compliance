# HCO Full Accreditation — HRM chapter OE inventory

## Sources

OE text, counts, levels, CORE/Commitment/Achievement/Excellence, and asterisks:
official portal **Standards** PDF (January 2025), local copy at
`/c/Users/SERVER/Desktop/NABH/NABH Hospital Accreditation Standard 6th Edition
January 2025.pdf` (same filename as the official portal URL named in the
drafting brief), `pdftotext -enc UTF-8 -layout` at
`policies/source/hco6_hrm_ocr.txt` (PDF pages 161–176 / printed 150–165).
Chapter 9 header confirmed on PDF page 161; Chapter 10 (Information Management
System) header confirmed on PDF page 177 — HRM body does not run past that.

**Encoding note (real bug caught before it shipped):** the first extraction
pass omitted `-enc UTF-8` and pdftotext silently mis-decoded the "fi"-ligature
glyph (`speci{fi}c` → raw byte 0xAE, not valid UTF-8, not the `` PUA
codepoint the existing `LIGATURE_MAP` expects). Re-ran with `-enc UTF-8`;
confirmed the ligature now decodes to the same `` PUA character FMS/ROM
already handle, so the existing ligature map needed no change.

**Parser format quirk (also caught, not inherited from FMS unmodified):** in
this chapter's `pdftotext -layout` output, OE level words are inconsistently
left-padded — `Commitment` OEs may carry a few leading spaces, `CORE` and
`Achievement` OEs often carry **none**, and several standard headers (e.g.
`HRM.2.        The organisation implements...`) start at column 0 with no
leading whitespace at all. The FMS-derived parser required `^\s+` (at least
one leading space); on this chapter that silently dropped every OE whose
level word starts at column 0 and let plain-English "Standard" title lines
bleed into the wrong OE. Fixed by loosening both patterns to `^\s*` and by
keying the standard-title trigger on the literal word "Standard" at the start
of a line (`^\s*Standard\b`) rather than requiring it to be alone on the
line — verified against the source text that "Standard" starts a line
exactly 13 times in the chapter body, once per standard, with no false
positives from body prose. `parse_hco_hrm_inventory.py` documents both fixes
inline.

Interpretation depth: scanned **Guidebook**
`policies/source/NABH 6th Edition Standards & Guidebook-1.pdf`.
**No text layer** — `pdftotext` (with or without `-enc/-raw`) returns nothing
for any page of this file, confirmed on pages 1–3 and again on HRM's own
pages. **No tesseract or pdftoppm binary is installed on this machine**
(`poppler-utils` here ships `pdftotext.exe` only; `pdftoppm` is absent; no
`tesseract`/`gs`/`magick`). `pip install pymupdf` needed no OS package and
rendered pages to PNG at 150 dpi locally; every HRM page (PDF 274–297) was
then read and transcribed visually against its own rendered image, OE by OE,
not run through a mechanical OCR pass. `hco6_hrm_guidebook_ocr.txt` documents
this in its own header and is therefore **not** noisy the way
`hco6_fms_guidebook_ocr.txt` is (no pipe-OCR, no dropped ligatures, no chrome
tails) — `extract_hco_hrm_interpretations.py` is a lighter script than its
FMS counterpart for exactly that reason; it still needed one real fix (next
paragraph).

**Verified HRM Intent at PDF page 274** (idx 273) — matches the FMS chapter
notes' forward pointer exactly. **Verified IMS (Chapter 10) Intent at PDF
page 302** (idx 301). References end PDF page 301 (idx 300, printed 292).

**Extractor bug caught and fixed before writing the interpretations JSON:**
the first extraction pass (splitting the transcript on the literal token
`Interpretation:`) left the *next* OE's own "LEVEL letter. requirement text"
header line stuck onto the end of the *previous* OE's interpretation for
every same-standard OE-to-OE transition (this chapter's OEs don't have a
"Standard" line between them the way standard-to-standard transitions do, so
the existing `STANDARD_CUT` regex alone didn't catch it). Added a second cut
(`NEXT_OE_CUT`) on the next OE's level-word-plus-letter header pattern before
each block is finalized; re-ran and spot-checked the JSON — no OE's
interpretation still contains another OE's title text.

Cleaned notes: `policies/source/hco6_hrm_interpretations.json` (76 blocks,
1:1, verified — every value ends at the actual paragraph boundary against
the rendered page images, not by heuristic).

Official chapter name is **Human Resource Management (HRM)**. This is the
**HCO Full 6th Edition** chapter — a different edition and a different
programme from the already-deployed **SHCO 3rd Edition HRM** chapter that
already has its own `build_hrm1_v2.py`–`build_hrm9_v2.py`,
`policies/drafts/hrm*_v2_draft.json` and `policies/build/preview/HRM.*` (9
standards, different OE text, different lettering, different PDF, plain
`HRM/POL/NN` doc numbers with no `HCO/` prefix). Do not confuse the two — this
HCO output uses `HCO/HRM/POL/nn`, `HCO.HRM.n`, `hco_hrm{n}_v2_draft.json`,
and lands only in the `_hco` folders.

Do not re-derive OE counts/levels/asterisks from the Guidebook.

## Chapter totals (portal summary = body = Guidebook's own copy of the matrix)

- Standards: **13**
- Objective elements: **76**
- CORE 16 / Commitment 56 / Achievement 4 / Excellence 0

| Standard | OEs | letters | CORE | Achievement | * asterisks |
|---|---|---|---|---|---|
| HRM.1  | 7  | a–g | b        | c, g    | b, f |
| HRM.2  | 4  | a–d | a, c     | —       | a, d |
| HRM.3  | 10 | a–j | a        | —       | none |
| HRM.4  | 6  | a–f | a        | e, f    | a |
| HRM.5  | 6  | a–f | e        | —       | none |
| HRM.6  | 7  | a–g | e, f     | —       | none |
| HRM.7  | 5  | a–e | none     | —       | a |
| HRM.8  | 6  | a–f | d        | —       | a |
| HRM.9  | 4  | a–d | d        | —       | a, d |
| HRM.10 | 4  | a–d | none     | —       | none |
| HRM.11 | 6  | a–f | a, d     | —       | none |
| HRM.12 | 6  | a–f | a, d     | —       | none |
| HRM.13 | 5  | a–e | a, c     | —       | none |

Every column cross-checked letter-by-letter against the Guidebook's own copy
of the Objective-Element matrix (PDF page 275, printed 267) — full agreement,
no discrepancy, for all 76 OEs. Portal-PDF body and portal-PDF summary matrix
also agree with each other (verified by hand before writing the assertion
into `parse_hco_hrm_inventory.py`).

## Proposed judgment calls (defaults **written** into drafts)

### Stop-work

**Proposed default: stop-work on HRM.11, 12, 13. None on HRM.1–10.**

HRM's subject is workforce administration, not a piece of equipment or an
environment that can be switched off — so it does not carry the same kind of
mechanical go/no-go gate FMS or ROM standards do. The one place HRM does
create a hard, assessor-recognisable gate is credentialing and privileging:
each of HRM.11/12/13 is titled "...permitted to provide patient care
**without supervision**", and OE (a) in each is CORE "[professionals]
permitted by law, regulation and the organisation to provide patient care
without supervision **are identified**" — the standard's own wording already
implies that a professional not on that identified/privileged list does not
get to provide unsupervised care. That is the HRM equivalent of FMS's
equipment/infrastructure gates and is written as stop-work:

- **HRM.11** — a medical professional not on the organisation's identified
  and privileged list provides patient care without supervision.
- **HRM.12** — a nursing professional not on the organisation's identified
  and privileged list provides patient care without supervision.
- **HRM.13** — a para-clinical professional not on the organisation's
  identified and privileged list provides patient care without supervision.

Considered and rejected: HRM.3.a (induction training) and HRM.5.e / HRM.6.e /
HRM.6.f (CPR / disaster / fire training coverage) are ongoing training-coverage
metrics across the whole staff population, not a single controllable
point-of-care gate — the Guidebook itself allows induction "within a month of
joining", so a hard stop-work reading would contradict the source. HRM.1.c
(adequate staff number/mix) is a planning-level metric, not an event.
HRM.9.d (workplace-violence measures) is a programme-design requirement, not
a go/no-go at the point of care. Flag for approval: **if you want any of
these treated as stop-work triggers too, say so and I will add them** — the
current default is deliberately narrow to the one place the standard's own
language creates a hard gate.

### Statute P2

**Proposed default: statute P2 on HRM.12 only. Accreditation-only on
HRM.1–11 and HRM.13.**

- **HRM.12.a** Guidebook names a specific, on-point Act: "Refer to the Indian
  Nursing Council Act, 1947." Directly engages this standard's subject
  (identifying nursing professionals permitted to practise). **Written as
  P2.**
- **HRM.8.d** Guidebook says "Refer to relevant labour laws and CCS (CCA)
  rules" — CCS (Central Civil Services) Conduct/Classification-Control-Appeal
  rules govern central-government employees specifically and do not apply as
  a blanket statute to a private hospital's HR grievance procedure; "relevant
  labour laws" is a generic plural, not one named Act. Per the
  disclaimer-statute-matching standing rule (name only what the standard
  actually relies on, never a checklist import), this is written as a method
  note only, **not P2**. Flag for approval: if this hospital operates under
  CCS rules (e.g. a government/PSU hospital), the P2 default should change —
  say so and I will add the statute clause.
- **HRM.2.b** "in accordance with the law of the land" (pre-employment
  medical exam / HIV-testing consent) — no named Act. Method note only.
- **HRM.9.a** "in consonance with the law of the land" (staff health and
  safety policy) — no named Act. Method note only.
- **HRM.11** National Medical Commission's website is named as "a good
  reference" for verification (HRM.11.c) — a resource pointer, not a statute
  citation. No named Act anywhere in HRM.11. Accreditation-only.
- **HRM.13** No named Act anywhere. Accreditation-only.

### Wording kept as printed / flagged

None found. The portal-PDF OE and Standard-title wording for this chapter
parsed clean once the parser's leading-whitespace assumption was loosened
(see Sources above) — no grammar-as-printed quirks analogous to FMS's
"operate ... and promotes" needed preserving. Flagged instead: HRM.9.d's
Interpretation cross-references **FMS.3.a** ("The above should be part of
written guidance on security. Refer FMS.3.a.") — kept as a method-note
cross-reference only; FMS.3.a's own master policy is not edited.

### Prepared by

**Written default: HR In-Charge / Personnel Officer** for HRM.1–13. This
matches the designation the codebase's own (already-deployed, SHCO 3rd
Edition) HRM chapter already uses in `build_hrm1_v2.py`
(`D("HR In-Charge / Personnel Officer")`) — reused for naming consistency
only; no SHCO HRM content, wording or file is touched or copied.

## Cross-references noted (not folded in, not left silent)

Guidebook interpretations for this chapter point at OEs already owned by
other approved HCO policies. Recorded as method notes in the relevant HRM
step, per the same discipline used in earlier chapters — the owning
standard's master policy is not edited:

- HRM.5.a → COP.8 (blood transfusion services)
- HRM.5.b → COP.16.a (vulnerable patients)
- HRM.5.c → COP.16.e (control and restraint)
- HRM.5.d → PRE.8.e (healthcare communication)
- HRM.6.a → PSQ.1.a (safety programme)
- HRM.6.d → IPC.8.a (occupational safety / needle-stick etc.)
- HRM.9.d → FMS.3.a (workplace violence / security)

## OCR strips **written** into `hco6_hrm_interpretations.json` before generate

None needed. The source transcript (see Sources above) is a verified visual
read, not a mechanical OCR pass, so there is no pipe-OCR, ligature-drop or
chrome-tail corruption to strip. The one real defect found in extraction —
next-OE header text bleeding onto the end of the previous OE's interpretation
at same-standard transitions — was fixed in the extractor itself
(`NEXT_OE_CUT`), not patched after the fact in the JSON; see Sources above.

## File layout

  builders: policies/build/build_hco_hrm{N}_v2.py
  drafts: policies/drafts_hco/hco_hrm{N}_v2_draft.json
  masters: policies/build/masters_hco/HCO.HRM.{N}_v2_master.docx
  previews: policies/build/preview_hco/HCO.HRM.{N}_v2_preview.docx|.md
  doc_no: «HCO/HRM/POL/{NN}»
  programme: HCO Full Accreditation, 6th Edition

Do not write to SHCO folders. Do not touch AAC, COP, MOM, PRE, IPC, PSQ, ROM,
or FMS. Do not touch the SHCO 3rd Edition HRM chapter (`build_hrm*_v2.py`,
`policies/drafts/hrm*_v2_draft.json`, `policies/build/preview/HRM.*`) — a
separate, already-deployed programme with its own numbering.
