/**
 * generate_shco_tips.js
 * Generates 4 "How to Achieve" tips for each of the 408 SHCO Full OEs.
 *
 * Usage:
 *   set ANTHROPIC_API_KEY=sk-ant-...
 *   node scripts/generate_shco_tips.js
 *
 * Output: scripts/shco_tips_updates.sql  — run this in Supabase SQL Editor.
 */

const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ANTHROPIC_API_KEY;
if (!API_KEY) {
  console.error('\nERROR: ANTHROPIC_API_KEY environment variable not set.');
  console.error('Run:  set ANTHROPIC_API_KEY=sk-ant-...   then re-run this script.\n');
  process.exit(1);
}

// ── Parse OEs from shco_full_oes.sql ─────────────────────────────────────────
function parseOEs() {
  const sqlPath = path.join(__dirname, '..', 'shco_full_oes.sql');
  const sql = fs.readFileSync(sqlPath, 'utf8');

  // Each INSERT row looks like:
  // ('AAC', 'Access...', 'AAC.1', 'The org...', 'AAC.1.a', 'Commitment', 'The healthcare...'),
  // We extract lines between "insert into" and the end of the statement.
  const insertBlock = sql.match(/insert into public\.shco_full_oes[^;]+;/s)?.[0] || '';
  if (!insertBlock) throw new Error('Could not find INSERT block in SQL file');

  const oes = [];
  // Split on row boundaries — each row ends with '),\n' or ');\n'
  // Strategy: extract content between outer parens on each value line
  const lines = insertBlock.split('\n');
  let current = '';
  let inValues = false;

  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith('(\'AAC') || trimmed.startsWith('(\'COP') || trimmed.startsWith('(\'MOM') ||
        trimmed.startsWith('(\'PRE') || trimmed.startsWith('(\'HIC') || trimmed.startsWith('(\'PSQ') ||
        trimmed.startsWith('(\'ROM') || trimmed.startsWith('(\'FMS') || trimmed.startsWith('(\'HRM') ||
        trimmed.startsWith('(\'IMS')) {
      inValues = true;
      current = trimmed;
    } else if (inValues) {
      current += ' ' + trimmed;
    }

    if (inValues && (current.endsWith('),') || current.endsWith(');'))) {
      // Strip outer parens and trailing ,/;
      const inner = current.replace(/^\(/, '').replace(/[,;]$/, '').replace(/\)$/, '');
      const oe = parseSqlRow(current);
      if (oe) oes.push(oe);
      current = '';
      inValues = false;
    }
  }
  return oes;
}

function parseSqlRow(row) {
  // Strip leading ( and trailing ), or );
  let s = row.trim();
  if (s.startsWith('(')) s = s.slice(1);
  if (s.endsWith('),') || s.endsWith(');')) s = s.slice(0, -2);
  else if (s.endsWith(')')) s = s.slice(0, -1);

  // Split on ', ' boundaries respecting SQL '' escaping
  const fields = [];
  let i = 0;
  while (i < s.length) {
    // skip whitespace
    while (i < s.length && s[i] === ' ') i++;
    if (s[i] === "'") {
      i++; // skip opening quote
      let val = '';
      while (i < s.length) {
        if (s[i] === "'" && s[i+1] === "'") { val += "'"; i += 2; }
        else if (s[i] === "'") { i++; break; }
        else { val += s[i]; i++; }
      }
      fields.push(val);
      // skip comma+space
      while (i < s.length && (s[i] === ',' || s[i] === ' ')) i++;
    } else {
      // non-string field (shouldn't occur here)
      let val = '';
      while (i < s.length && s[i] !== ',') { val += s[i]; i++; }
      fields.push(val.trim());
      i++; // skip comma
    }
  }

  if (fields.length < 7) return null;
  return {
    chapter:       fields[0],
    chapter_name:  fields[1],
    standard_code: fields[2],
    standard_text: fields[3],
    oe_code:       fields[4],
    level:         fields[5],
    text:          fields[6],
  };
}

// ── Call Anthropic API ────────────────────────────────────────────────────────
async function generateTipsBatch(oes) {
  const oeList = oes.map(oe =>
    `OE_CODE: ${oe.oe_code}\nLEVEL: ${oe.level}\nCHAPTER: ${oe.chapter} — ${oe.chapter_name}\nSTANDARD: ${oe.standard_text}\nOE TEXT: ${oe.text}`
  ).join('\n\n');

  const prompt = `You are a NABH accreditation expert. Generate exactly 4 practical, actionable "How to Achieve" tips for each of the following NABH SHCO 3rd Edition Objective Elements.

Rules:
- Each tip must be 1-2 sentences, specific and immediately implementable by hospital staff
- Tips must NOT copy verbatim from the OE text — rephrase as actionable guidance
- For Core OEs: emphasise that assessors will examine records AND observe practice AND interview staff
- For Commitment OEs: focus on having an SOP, training staff, and maintaining records
- For Achievement OEs: focus on measurable outcomes, data collection, and improvement evidence
- For Excellence OEs: focus on innovation, benchmarking, and leadership
- Return ONLY a valid JSON object — no markdown, no explanation, no extra text
- Format: {"AAC.1.a": ["tip1","tip2","tip3","tip4"], "AAC.1.b": [...], ...}

OEs to process:
${oeList}`;

  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'x-api-key': API_KEY,
      'anthropic-version': '2023-06-01',
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-6',
      max_tokens: 8000,
      messages: [{ role: 'user', content: prompt }],
    }),
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(`API error ${response.status}: ${err}`);
  }

  const data = await response.json();
  const text = data.content?.[0]?.text || '';

  // Extract JSON — handle any leading/trailing whitespace or stray text
  const jsonMatch = text.match(/\{[\s\S]*\}/);
  if (!jsonMatch) throw new Error(`No JSON found in response: ${text.slice(0,200)}`);
  return JSON.parse(jsonMatch[0]);
}

// ── Sleep helper ──────────────────────────────────────────────────────────────
const sleep = ms => new Promise(r => setTimeout(r, ms));

// ── Main ──────────────────────────────────────────────────────────────────────
async function main() {
  console.log('\n📖 Parsing OEs from shco_full_oes.sql…');
  const oes = parseOEs();
  console.log(`   Found ${oes.length} OEs\n`);

  if (oes.length === 0) throw new Error('No OEs parsed — check SQL file path and format');

  const BATCH = 20;
  const allTips = {};
  const batches = Math.ceil(oes.length / BATCH);

  for (let b = 0; b < batches; b++) {
    const slice = oes.slice(b * BATCH, (b + 1) * BATCH);
    const codes = slice.map(o => o.oe_code).join(', ');
    console.log(`🔄 Batch ${b + 1}/${batches} — ${codes.slice(0, 60)}…`);

    let attempts = 0;
    while (attempts < 3) {
      try {
        const tips = await generateTipsBatch(slice);
        Object.assign(allTips, tips);
        console.log(`   ✅ Got tips for ${Object.keys(tips).length} OEs`);
        break;
      } catch (e) {
        attempts++;
        console.error(`   ⚠️  Attempt ${attempts} failed: ${e.message}`);
        if (attempts < 3) { console.log('   Retrying in 5s…'); await sleep(5000); }
        else throw e;
      }
    }

    // Rate limit: pause between batches
    if (b < batches - 1) await sleep(1500);
  }

  // ── Generate SQL UPDATE file ────────────────────────────────────────────────
  console.log('\n📝 Generating SQL update file…');

  let sql = `-- shco_tips_updates.sql
-- Generated by scripts/generate_shco_tips.js
-- Run this entire file in the Supabase SQL Editor.
-- Updates achieve_tips column for all ${oes.length} SHCO Full OEs.
-- Idempotent: safe to re-run.

`;

  let updated = 0;
  let missing = [];

  for (const oe of oes) {
    const tips = allTips[oe.oe_code];
    if (!tips || tips.length < 4) {
      missing.push(oe.oe_code);
      continue;
    }
    // Escape single quotes in tips for SQL
    const jsonStr = JSON.stringify(tips).replace(/'/g, "''");
    sql += `update public.shco_full_oes set achieve_tips = '${jsonStr}'::jsonb where oe_code = '${oe.oe_code}';\n`;
    updated++;
  }

  const outPath = path.join(__dirname, 'shco_tips_updates.sql');
  fs.writeFileSync(outPath, sql, 'utf8');

  console.log(`\n✅ Done!`);
  console.log(`   Updated: ${updated} OEs`);
  if (missing.length > 0) console.log(`   Missing: ${missing.join(', ')}`);
  console.log(`\n📄 SQL file written to: scripts/shco_tips_updates.sql`);
  console.log(`\nNext steps:`);
  console.log(`   1. Open Supabase SQL Editor`);
  console.log(`   2. Paste and run scripts/shco_tips_updates.sql`);
  console.log(`   3. Verify: SELECT COUNT(*) FROM shco_full_oes WHERE achieve_tips IS NOT NULL;`);
  console.log(`      (should return ${oes.length})\n`);
}

main().catch(e => { console.error('\n❌ Fatal:', e.message); process.exit(1); });
