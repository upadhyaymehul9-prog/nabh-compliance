import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const CORS = {
  "Access-Control-Allow-Origin": "https://accredready.in",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: CORS });
  }

  const _step = { current: "parse" };

  try {
    const { question } = await req.json();
    if (!question || typeof question !== "string") {
      return Response.json({ error: "Missing question" }, { status: 400, headers: CORS });
    }

    _step.current = "env-check";
    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    const anthropicKey = Deno.env.get("ANTHROPIC_API_KEY");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");
    if (!anthropicKey) throw new Error("ANTHROPIC_API_KEY missing");

    _step.current = "supabase-init";
    const supabase = createClient(supabaseUrl, serviceKey);

    // Step 1: try oe_code match — normalize user input to canonical DB format
    // DB format: CHAPTER.NUMBER.letter  e.g. "AAC.1.a", "PRE.2.g"
    // Handles: "aac1a", "aac 1 a", "AAC-1-A", "AAC .1.a", "aac.1.a" → "AAC.1.a"
    _step.current = "db-oe_code-search";
    const normalizeOeCode = (q: string): string => {
      // Strip all whitespace first, then try to extract a code pattern
      const compact = q.replace(/\s+/g, "");
      // Match: 2-4 uppercase letters, optional separator, 1-2 digits, optional separator, 1 letter
      const match = compact.match(/^([A-Za-z]{2,4})[.\-]?(\d{1,2})[.\-]?([A-Za-z])$/i);
      if (match) {
        return `${match[1].toUpperCase()}.${match[2]}.${match[3].toLowerCase()}`;
      }
      return compact;
    };
    const oeCodeQuery = normalizeOeCode(question.trim());
    const { data: codeRows, error: codeErr } = await supabase
      .from("shco_full_oes")
      .select("oe_code, chapter, standard_code, level, text, achieve_tips")
      .ilike("oe_code", `%${oeCodeQuery}%`)
      .limit(12);
    if (codeErr) throw new Error(`DB oe_code search: ${codeErr.message}`);

    let rows = codeRows && codeRows.length > 0 ? codeRows : null;
    let isKeywordFallback = false;

    // Step 2: fall back to keyword search against text column
    if (!rows) {
      _step.current = "db-keyword-search";
      const keywords = question
        .split(/\s+/)
        .filter((w) => w.length > 3)
        .slice(0, 8);

      if (keywords.length > 0) {
        const filter = keywords.map((w) => `text.ilike.%${w}%`).join(",");
        const { data: kwRows, error: kwErr } = await supabase
          .from("shco_full_oes")
          .select("oe_code, chapter, standard_code, level, text, achieve_tips")
          .or(filter)
          .limit(12);
        if (kwErr) throw new Error(`DB keyword search: ${kwErr.message}`);
        if (kwRows && kwRows.length > 0) {
          rows = kwRows;
          isKeywordFallback = true;
        } else {
          rows = [];
        }
      } else {
        rows = [];
      }
    }

    _step.current = "build-context";
    const contextBlock = rows.length > 0
      ? rows
          .map((r) => {
            const tips = Array.isArray(r.achieve_tips) && r.achieve_tips.length > 0
              ? r.achieve_tips.join(" | ")
              : "—";
            return `${r.oe_code} | ${r.level} | ${r.text} | ${tips}`;
          })
          .join("\n")
      : "";

    const systemPrompt =
      `You are AccredReady's NABH SHCO Full compliance assistant. You answer ONLY` +
      ` using the Objective Element (OE) content provided below in <context>. You` +
      ` have no other knowledge of NABH standards, KPIs, or accreditation` +
      ` requirements — anything not in the provided context is outside what you know.\n\n` +
      `Rules:\n` +
      `1. If the answer is fully contained in <context>, answer clearly and cite` +
      ` the exact oe_code(s) you used.\n` +
      `2. If <context> is empty or doesn't address the question, say: 'I couldn't` +
      ` find a matching SHCO Full requirement for that — try rephrasing, or check` +
      ` with your AccredReady admin.' Do NOT guess or use general NABH knowledge.\n` +
      `3. Never state OE counts, chapter totals, fees, or validity periods unless` +
      ` they appear verbatim in <context>.\n` +
      `4. Keep answers practical and specific — hospital staff need to know what to` +
      ` DO, not just what the rule says.\n` +
      `5. Always end your answer with the source: 'Source: SHCO Full — [oe_code]'\n` +
      `6. When you cannot find a match, state ONLY that no matching SHCO Full` +
      ` requirement was found, and suggest the user rephrase or check with their` +
      ` AccredReady admin. Do NOT speculate about which chapter, standard, or OE` +
      ` might contain the answer, do NOT guess chapter names or codes, and do NOT` +
      ` describe NABH structure beyond what is explicitly in <context>. If <context>` +
      ` is empty, your entire response must be limited to the refusal sentence —` +
      ` nothing else.\n\n` +
      `<context>\n${contextBlock}\n</context>`;

    _step.current = "anthropic-fetch";
    const anthropicRes = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": anthropicKey.trim(),
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: "claude-sonnet-4-6",
        max_tokens: 600,
        system: systemPrompt,
        messages: [{ role: "user", content: question }],
      }),
    });

    _step.current = "anthropic-parse";
    if (!anthropicRes.ok) {
      const body = await anthropicRes.text();
      throw new Error(`Anthropic API error: ${anthropicRes.status} — ${body}`);
    }

    const anthropicData = await anthropicRes.json();
    const answer = anthropicData.content?.[0]?.text ?? "";
    const sources = (!isKeywordFallback && rows.length > 0)
      ? rows.map((r) => r.oe_code)
      : [];
    const suggestions = (isKeywordFallback || rows.length === 0)
      ? [
          "What are the requirements for infection control programme documentation?",
          "Who approves antibiotic usage in SHCO standards?",
          "What are the safe injection practices required?",
          "What does the IC committee need to do and how often does it meet?",
        ]
      : [];

    return Response.json({ answer, sources, suggestions }, { headers: CORS });
  } catch (err) {
    console.error(`[${_step.current}]`, err);
    return Response.json(
      { error: "Something went wrong. Please try again." },
      { status: 500, headers: CORS },
    );
  }
});
