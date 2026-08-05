import { useState, useEffect, useCallback } from "react";
import jsPDF from "jspdf";
import { supabase } from "../supabaseClient";

/**
 * Quick Checklist — a flat, read-only roll-up of the three things a hospital is
 * assessed on: OEs, KPIs and committees.
 *
 * This module never writes. It re-reads the same tables the scoring / KPI /
 * committee screens own and derives done / not-done from them, so it can never
 * drift out of step with those screens and can never corrupt them. The "done"
 * rules below are lifted verbatim from the existing screens — see each constant.
 *
 * Programme separation is absolute: every programme has its own catalogue table
 * and its own hospital-data table, and nothing is shared across programmes.
 */

// ── Done-rules (each mirrors an existing screen; do not diverge) ────────────
// Full programmes score OEs 1–5. NABH's own pass bar is 4 (get_final_decision).
const OE_DONE_SCORE = 4;
// ELC programmes use met / partial / not_met (see setElcScore in App.js).
const OE_DONE_STATUS = "met";
// KPIs need three months of data before NABH will look at a trend — this is the
// same threshold the KPI screens colour green on (trackingStatus / `tracked`).
const KPI_DONE_MONTHS = 3;
// A committee counts as active if it met at least once in the last 12 months —
// same rule as totalActive / meetingsInLast12 in the gap-report generators.
const COMMITTEE_DONE_WINDOW_DAYS = 365;

const PROGRAMMES = {
  "hco":       { label: "HCO Full Accreditation",             committeeProgramme: "HCO_FULL"  },
  "shco-full": { label: "SHCO Full Accreditation",            committeeProgramme: "SHCO_FULL" },
  "eco-full":  { label: "ECO Full Accreditation",             committeeProgramme: null        },
  "hco-elc":   { label: "HCO Entry Level Certification",      committeeProgramme: "HCO_ELC"   },
  "shco-elc":  { label: "SHCO Entry Level Certification",     committeeProgramme: "SHCO_ELC"  },
};

// ELC OE codes are stored compact (AAC1a) but read as dotted (AAC.1.a) everywhere
// they are shown to a user. Same transform the ELC gap lists use.
const toElcDotCode = (code) => code.replace(/^([A-Z]+)(\d+)([a-z]+)$/, "$1.$2.$3");

const distinctMonths = (rows) =>
  new Set(rows.map((r) => `${r.year}-${r.month}`)).size;

// ── Section loaders ────────────────────────────────────────────────────────
// Each returns [{ code, desc, done, status }] and never throws — a missing or
// empty table yields an empty section rather than breaking the whole checklist.

async function loadOeItems(programme, { hospitalId, assessmentId, refData }) {
  if (programme === "hco") {
    if (!assessmentId) return [];
    const [{ data: cat }, { data: scored }] = await Promise.all([
      supabase.from("objective_elements").select("id, chapter_id, text"),
      supabase.from("scores").select("oe_id, score").eq("assessment_id", assessmentId),
    ]);
    const scoreMap = {};
    (scored || []).forEach((s) => { scoreMap[s.oe_id] = s.score; });
    const order = refData?.CHAPTER_ORDER || {};
    return (cat || [])
      .slice()
      .sort((a, b) =>
        (order[a.chapter_id] || 999) - (order[b.chapter_id] || 999) ||
        a.id.localeCompare(b.id, undefined, { numeric: true, sensitivity: "base" }))
      .map((oe) => ({
        code: oe.id,
        desc: oe.text || "",
        done: (scoreMap[oe.id] || 0) >= OE_DONE_SCORE,
        status: scoreMap[oe.id] ? `Scored ${scoreMap[oe.id]}/5` : "Not scored",
      }));
  }

  if (programme === "shco-full" || programme === "eco-full") {
    if (!hospitalId) return [];
    const isShco = programme === "shco-full";
    const catTable   = isShco ? "shco_full_oes"    : "eco_full_oes";
    const scoreTable = isShco ? "shco_full_scores" : "eco_full_scores";
    const [{ data: cat }, { data: scored }] = await Promise.all([
      supabase.from(catTable).select("*").order("oe_code"),
      supabase.from(scoreTable).select("oe_code, score").eq("hospital_id", hospitalId),
    ]);
    const scoreMap = {};
    (scored || []).forEach((s) => { scoreMap[s.oe_code] = s.score; });
    return (cat || []).map((oe) => ({
      code: oe.oe_code,
      // The two catalogues name the text column differently.
      desc: (isShco ? oe.text : oe.oe_text) || "",
      done: (scoreMap[oe.oe_code] || 0) >= OE_DONE_SCORE,
      status: scoreMap[oe.oe_code] ? `Scored ${scoreMap[oe.oe_code]}/5` : "Not scored",
    }));
  }

  if (programme === "hco-elc" || programme === "shco-elc") {
    if (!hospitalId) return [];
    const scope = programme === "hco-elc" ? "HCO_ELC" : "SHCO_ELC";
    const { data: scored } = await supabase
      .from("elc_scores").select("oe_code, status")
      .eq("hospital_id", hospitalId).eq("programme", scope);
    const statusMap = {};
    (scored || []).forEach((s) => { statusMap[s.oe_code] = s.status; });
    return (refData?.HCO_ELC_OE_LIST || []).map((oe) => ({
      code: toElcDotCode(oe.code),
      desc: oe.text || "",
      done: statusMap[oe.code] === OE_DONE_STATUS,
      status: statusMap[oe.code]
        ? { met: "Met", partial: "Partial", not_met: "Not met" }[statusMap[oe.code]] || statusMap[oe.code]
        : "Not scored",
    }));
  }

  return [];
}

async function loadKpiItems(programme, { hospitalId, refData }) {
  if (!hospitalId) return [];

  // HCO Full and the two ELC programmes read their definitions from the shared
  // `kpis` catalogue, sliced by programme_scope. Their data tables stay separate.
  if (programme === "hco" || programme === "hco-elc" || programme === "shco-elc") {
    const dataTable =
      programme === "hco"      ? "kpi_data" :
      programme === "hco-elc"  ? "hco_elc_kpi_data" : "shco_elc_kpi_data";

    let defs = [];
    if (programme === "hco") {
      const { data } = await supabase.from("kpis").select("id, kpi_no, name, programme_scope").order("kpi_no");
      // ELC-scoped rows (the kpi_no 51–64 twins) belong to the ELC modules, not here.
      const isElcScoped = (k) =>
        Array.isArray(k.programme_scope) && k.programme_scope.some((s) => s === "HCO_ELC" || s === "SHCO_ELC");
      const override = refData?.HCO_KPI_OVERRIDE || {};
      defs = (data || []).filter((k) => !isElcScoped(k)).map((k) => ({ ...k, ...(override[k.kpi_no] || {}) }));
    } else {
      const scope = programme === "hco-elc" ? "HCO_ELC" : "SHCO_ELC";
      const { data } = await supabase
        .from("kpis").select("id, kpi_no, name, programme_scope")
        .contains("programme_scope", [scope]).order("kpi_no");
      defs = data || [];
    }

    const { data: rows } = await supabase
      .from(dataTable).select("kpi_id, month, year").eq("hospital_id", hospitalId);
    const all = rows || [];
    return defs.map((k) => {
      // kpi_id is compared as a string because `kpi_data` stores it loosely-typed.
      const months = distinctMonths(all.filter((d) => String(d.kpi_id) === String(k.id)));
      return {
        code: `KPI ${k.kpi_no}`,
        desc: k.name || "",
        done: months >= KPI_DONE_MONTHS,
        status: months === 0 ? "No data" : `${months} month${months > 1 ? "s" : ""}`,
      };
    });
  }

  // SHCO Full and ECO Full carry their KPI definitions in code, not in `kpis`.
  if (programme === "shco-full" || programme === "eco-full") {
    const isShco = programme === "shco-full";
    const defs = (isShco ? refData?.SHCO_KPIS : refData?.ECO_KPIS) || [];
    const { data: rows } = await supabase
      .from(isShco ? "shco_kpi_data" : "eco_kpi_data")
      .select("kpi_id, month, year").eq("hospital_id", hospitalId);
    const all = rows || [];
    return defs.map((k) => {
      const months = distinctMonths(all.filter((d) => String(d.kpi_id) === String(k.id)));
      return {
        code: `KPI ${k.id}`,
        desc: k.name || "",
        done: months >= KPI_DONE_MONTHS,
        status: months === 0 ? "No data" : `${months} month${months > 1 ? "s" : ""}`,
      };
    });
  }

  return [];
}

async function loadCommitteeItems(programme, { hospitalId }) {
  const scope = PROGRAMMES[programme]?.committeeProgramme;
  if (!scope || !hospitalId) return [];

  let committees = [];
  if (scope === "HCO_FULL") {
    // committee_programme_map has no HCO_FULL rows yet, so HCO Full reads the
    // flat catalogue — same fallback CommitteesScreen uses.
    const { data } = await supabase.from("committees").select("id, name, chapter_ref").order("id");
    committees = data || [];
  } else {
    const { data } = await supabase
      .from("committee_programme_map").select("chapter_ref, committees(*)").eq("programme", scope);
    committees = (data || [])
      .map((r) => (r.committees ? { ...r.committees, chapter_ref: r.chapter_ref || r.committees.chapter_ref } : null))
      .filter(Boolean);
  }

  const { data: meetings } = await supabase
    .from("committee_meetings").select("committee_id, meeting_date")
    .eq("hospital_id", hospitalId).eq("programme", scope);
  const all = meetings || [];
  const cutoff = Date.now() - COMMITTEE_DONE_WINDOW_DAYS * 24 * 60 * 60 * 1000;

  return committees.map((c) => {
    const mine = all.filter((m) => m.committee_id === c.id);
    const recent = mine.filter((m) => new Date(m.meeting_date).getTime() >= cutoff);
    const last = mine
      .slice()
      .sort((a, b) => new Date(b.meeting_date) - new Date(a.meeting_date))[0];
    return {
      code: c.chapter_ref || `COM ${c.id}`,
      desc: c.name || "",
      done: recent.length > 0,
      status: last
        ? `Last met ${new Date(last.meeting_date).toLocaleDateString("en-IN", { day: "2-digit", month: "short", year: "numeric" })}`
        : "No meetings recorded",
    };
  });
}

// ── PDF text sanitising ────────────────────────────────────────────────────
/**
 * jsPDF's built-in Helvetica is a standard-14 font limited to WinAnsi. Any code
 * point outside it is silently truncated to its low byte, so U+2264 "≤" prints
 * as 0x64 "d" — which is why KPI targets like "≤90 minutes" came out as
 * "d90 minutes".
 *
 * We translate rather than embed a Unicode TTF: a font subset would have to be
 * base64'd into a bundle already flagged as oversized, and "<=90 minutes" reads
 * correctly in a plain-text checklist. Note this only makes the PDF safe — the
 * in-app view is HTML and renders the original characters as authored.
 *
 * Much of the text reaching this function comes from Supabase rather than from
 * constants in this repo, so the map is a best-effort translation and anything
 * unmapped falls through to a compatibility decomposition, not a mystery glyph.
 */
const PDF_CHAR_MAP = {
  // Comparison / maths — the ones that actually break NABH KPI targets
  "≤": "<=", "≥": ">=", "≠": "!=", "±": "+/-", "×": "x", "÷": "/", "≈": "~",
  "⁄": "/", "∞": "inf", "√": "sqrt", "∑": "sum", "µ": "u",
  // Dashes and minus signs
  "–": "-", "—": "-", "―": "-", "‐": "-", "‑": "-", "‒": "-", "−": "-",
  // Quotes
  "“": '"', "”": '"', "„": '"', "‟": '"', "‘": "'", "’": "'", "‚": "'", "‛": "'",
  "«": '"', "»": '"',
  // Punctuation and bullets
  "…": "...", "•": "*", "‣": "*", "·": "-", "∙": "-", "°": " deg",
  "→": "->", "←": "<-", "↑": "^", "↓": "v", "↔": "<->",
  // Symbols and currency
  "™": "(TM)", "®": "(R)", "©": "(C)", "§": "S", "¶": "P",
  "₹": "Rs.", "€": "EUR", "£": "GBP", "¥": "JPY", "¢": "c",
  // Fractions
  "½": "1/2", "⅓": "1/3", "⅔": "2/3", "¼": "1/4", "¾": "3/4",
  // Ligatures (these appear in text pasted out of PDFs)
  "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl",
  // Invisible / exotic whitespace
  " ": " ", " ": " ", " ": " ", " ": " ", " ": " ",
  "​": "", "‌": "", "‍": "", "﻿": "",
};

const ASCII_MAX = 0x7f;
const isAscii = (ch) => ch.codePointAt(0) <= ASCII_MAX;

export function sanitizeForPdf(value) {
  if (value === null || value === undefined) return "";
  // Array.from walks by code point, so astral characters (emoji) arrive whole
  // rather than as two lone surrogates. A code-point walk is used instead of a
  // regex range because the natural range here spans control characters.
  return Array.from(String(value), (ch) => {
    if (isAscii(ch)) return ch;
    const mapped = PDF_CHAR_MAP[ch];
    if (mapped !== undefined) return mapped;
    // Unmapped: fold accented Latin to its base letter (e-acute -> e) and drop
    // anything with no ASCII form at all (emoji, CJK) rather than emitting a
    // byte that a reader would show as some other character.
    return Array.from(ch.normalize("NFKD")).filter(isAscii).join("");
  })
    .join("")
    // OE text out of the database carries hard line breaks; collapse so a row
    // stays one line and the width measurement matches what is drawn.
    .replace(/\s+/g, " ")
    .trim();
}

// ── PDF export ─────────────────────────────────────────────────────────────

function buildChecklistPDF({ sections, programmeLabel, hospitalName, showCompleted }) {
  const doc = new jsPDF({ unit: "pt", format: "a4" });
  const W = doc.internal.pageSize.getWidth();
  const H = doc.internal.pageSize.getHeight();
  const M = 40;
  const BOX_X = M + 2;
  const CODE_X = M + 18;
  const DESC_X = M + 96;
  const DESC_W = W - M - DESC_X;
  const BOTTOM = H - 46;

  const today = new Date();
  // Every string handed to doc.text goes through S() — including the labels
  // authored here, which contain en-dashes and middots of their own.
  const S = sanitizeForPdf;
  let y = 0;
  let page = 0;

  const footer = () => {
    doc.setFont("helvetica", "normal").setFontSize(7.5).setTextColor(150);
    doc.text(S("AccredReady — Quick Checklist"), M, H - 26);
    doc.text(S(`Page ${page}`), W - M, H - 26, { align: "right" });
  };

  const newPage = (first) => {
    if (!first) { footer(); doc.addPage(); }
    page += 1;
    y = M;
  };

  newPage(true);

  // Title block
  doc.setFont("helvetica", "bold").setFontSize(15).setTextColor(30);
  doc.text(S("Quick Checklist"), M, y + 4);
  y += 20;
  doc.setFont("helvetica", "normal").setFontSize(10).setTextColor(70);
  doc.text(S(hospitalName || "Hospital"), M, y);
  y += 13;
  doc.setFontSize(8.5).setTextColor(120);
  doc.text(
    S(`${programmeLabel}  ·  Generated ${today.toLocaleDateString("en-IN", { day: "2-digit", month: "long", year: "numeric" })}` +
      `  ·  ${showCompleted ? "All items" : "Outstanding items only"}`),
    M, y
  );
  y += 14;
  doc.setDrawColor(200).setLineWidth(0.7).line(M, y, W - M, y);
  y += 16;

  sections.forEach((section) => {
    const rows = showCompleted ? section.items : section.items.filter((i) => !i.done);
    if (section.items.length === 0) return;

    if (y > BOTTOM - 40) newPage(false);
    doc.setFont("helvetica", "bold").setFontSize(10.5).setTextColor(30);
    doc.text(S(section.title.toUpperCase()), M, y);
    doc.setFont("helvetica", "normal").setFontSize(8.5).setTextColor(120);
    doc.text(S(`${section.doneCount} of ${section.items.length} complete`), W - M, y, { align: "right" });
    y += 6;
    doc.setDrawColor(225).setLineWidth(0.5).line(M, y, W - M, y);
    y += 13;

    if (rows.length === 0) {
      doc.setFont("helvetica", "italic").setFontSize(8.5).setTextColor(120);
      doc.text(S("All items complete."), CODE_X, y);
      y += 20;
      return;
    }

    rows.forEach((item) => {
      if (y > BOTTOM) {
        newPage(false);
        doc.setFont("helvetica", "bold").setFontSize(9).setTextColor(120);
        doc.text(S(`${section.title.toUpperCase()} (continued)`), M, y);
        y += 16;
      }
      // Checkbox
      doc.setDrawColor(item.done ? 90 : 140).setLineWidth(0.7);
      doc.rect(BOX_X, y - 6.5, 8, 8);
      if (item.done) {
        doc.setDrawColor(40).setLineWidth(1.1);
        doc.line(BOX_X + 1.6, y - 2.6, BOX_X + 3.3, y - 0.8);
        doc.line(BOX_X + 3.3, y - 0.8, BOX_X + 6.5, y - 5.2);
      }
      // Code
      doc.setFont("courier", "bold").setFontSize(7.8).setTextColor(item.done ? 130 : 40);
      doc.text(S(item.code).slice(0, 13), CODE_X, y);
      // Description — one line, truncated to the column width. Sanitise before
      // splitting so the measured width matches the glyphs actually drawn.
      doc.setFont("helvetica", "normal").setFontSize(8.5).setTextColor(item.done ? 140 : 55);
      const lines = doc.splitTextToSize(S(item.desc), DESC_W - 4);
      doc.text(lines.length > 1 ? `${lines[0].replace(/\s+\S*$/, "")}...` : (lines[0] || ""), DESC_X, y);
      y += 13.5;
    });
    y += 10;
  });

  footer();

  const stamp =
    String(today.getDate()).padStart(2, "0") +
    String(today.getMonth() + 1).padStart(2, "0") +
    today.getFullYear();
  const cleanHospital = (hospitalName || "Hospital").replace(/\s+(New|Trial|Active|Expired)$/i, "").trim();
  doc.save(`QuickChecklist_${cleanHospital.replace(/[^a-z0-9]+/gi, "_")}_${stamp}.pdf`);
}

// ── View ───────────────────────────────────────────────────────────────────

export default function QuickChecklistTab({ T, programme, hospitalId, assessmentId, hospitalName, refData }) {
  const [sections, setSections] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCompleted, setShowCompleted] = useState(false);
  const [pdfLoading, setPdfLoading] = useState(false);
  const [error, setError] = useState(null);

  const cfg = PROGRAMMES[programme];

  const load = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const [oes, kpis, committees] = await Promise.all([
        loadOeItems(programme, { hospitalId, assessmentId, refData }),
        loadKpiItems(programme, { hospitalId, refData }),
        loadCommitteeItems(programme, { hospitalId }),
      ]);
      setSections([
        { key: "oes", title: "Objective Elements", items: oes },
        { key: "kpis", title: "Key Performance Indicators", items: kpis },
        { key: "committees", title: "Committees", items: committees },
      ].map((s) => ({ ...s, doneCount: s.items.filter((i) => i.done).length })));
    } catch (e) {
      setError(e?.message || "Could not load the checklist.");
    }
    setLoading(false);
  }, [programme, hospitalId, assessmentId, refData]);

  useEffect(() => { load(); }, [load]);

  const exportPDF = () => {
    setPdfLoading(true);
    try {
      buildChecklistPDF({
        sections,
        programmeLabel: cfg?.label || "",
        hospitalName,
        showCompleted,
      });
    } catch (e) {
      alert("Could not generate the PDF: " + (e?.message || "unknown error"));
    }
    setPdfLoading(false);
  };

  const totalItems = sections.reduce((a, s) => a + s.items.length, 0);
  const totalDone = sections.reduce((a, s) => a + s.doneCount, 0);
  const anyData = totalItems > 0;

  if (loading) {
    return <div style={{ textAlign: "center", color: T.muted, padding: 40 }}>Loading checklist…</div>;
  }

  return (
    <div style={{ padding: "16px 16px 60px" }}>
      {/* Header */}
      <div style={{
        display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap",
        marginBottom: 14, paddingBottom: 12, borderBottom: `1px solid ${T.border}`,
      }}>
        <div style={{ flex: 1, minWidth: 200 }}>
          <div style={{ fontSize: 15, fontWeight: 700, color: T.text }}>Quick Checklist</div>
          <div style={{ fontSize: 11, color: T.muted, marginTop: 3 }}>
            {cfg?.label}
            {anyData && <> · {totalDone} of {totalItems} complete</>}
          </div>
        </div>

        <label style={{
          display: "flex", alignItems: "center", gap: 6,
          fontSize: 12, color: T.muted, cursor: "pointer", userSelect: "none",
        }}>
          <input
            type="checkbox"
            checked={showCompleted}
            onChange={(e) => setShowCompleted(e.target.checked)}
            style={{ cursor: "pointer" }}
          />
          Show completed
        </label>

        <button
          onClick={exportPDF}
          disabled={pdfLoading || !anyData}
          style={{
            padding: "6px 14px", borderRadius: 7, border: `1px solid ${T.gold}`,
            background: "transparent", color: T.gold, fontSize: 12, fontWeight: 700,
            cursor: pdfLoading || !anyData ? "default" : "pointer",
            opacity: pdfLoading || !anyData ? 0.5 : 1, whiteSpace: "nowrap",
          }}
        >
          {pdfLoading ? "⏳ Generating…" : "⬇ Export PDF"}
        </button>
      </div>

      {error && (
        <div style={{
          padding: "10px 14px", borderRadius: 8, marginBottom: 14,
          background: `${T.red}18`, border: `1px solid ${T.red}55`, color: T.red, fontSize: 12,
        }}>
          {error}
        </div>
      )}

      {!anyData && !error && (
        <div style={{ color: T.muted, fontSize: 13, padding: "24px 0" }}>
          Nothing to show yet. Score some OEs, log KPI data, or record a committee meeting
          and they will appear here.
        </div>
      )}

      {sections.map((section) => {
        if (section.items.length === 0) return null;
        const rows = showCompleted ? section.items : section.items.filter((i) => !i.done);
        return (
          <div key={section.key} style={{ marginBottom: 26 }}>
            <div style={{
              display: "flex", alignItems: "baseline", gap: 10,
              paddingBottom: 6, borderBottom: `1px solid ${T.border}`, marginBottom: 4,
            }}>
              <div style={{ fontSize: 12, fontWeight: 700, letterSpacing: 1, color: T.text }}>
                {section.title.toUpperCase()}
              </div>
              <div style={{ fontSize: 11, color: T.muted, marginLeft: "auto" }}>
                {section.doneCount} of {section.items.length} complete
              </div>
            </div>

            {rows.length === 0 ? (
              <div style={{ fontSize: 12, color: T.muted, fontStyle: "italic", padding: "10px 2px" }}>
                All items complete.
              </div>
            ) : rows.map((item) => (
              <div
                key={`${section.key}-${item.code}`}
                title={item.desc}
                style={{
                  display: "flex", alignItems: "center", gap: 10,
                  padding: "7px 2px", borderBottom: `1px solid ${T.border}44`,
                  opacity: item.done ? 0.55 : 1,
                }}
              >
                <span style={{
                  flexShrink: 0, width: 13, height: 13, borderRadius: 3,
                  border: `1px solid ${item.done ? T.green : T.border}`,
                  background: item.done ? T.green : "transparent",
                  color: "#fff", fontSize: 10, lineHeight: "12px", textAlign: "center",
                }}>
                  {item.done ? "✓" : ""}
                </span>
                <span style={{
                  flexShrink: 0, minWidth: 78, fontFamily: "monospace",
                  fontSize: 11.5, fontWeight: 700, color: item.done ? T.muted : T.text,
                }}>
                  {item.code}
                </span>
                <span style={{
                  flex: 1, minWidth: 0, fontSize: 12.5, color: item.done ? T.muted : T.text,
                  whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis",
                }}>
                  {item.desc}
                </span>
                <span style={{ flexShrink: 0, fontSize: 10.5, color: T.muted, whiteSpace: "nowrap" }}>
                  {item.status}
                </span>
              </div>
            ))}
          </div>
        );
      })}
    </div>
  );
}
