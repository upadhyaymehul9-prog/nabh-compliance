// One-time (re-runnable) backfill job: generates embeddings for a SMALL
// batch of rows per call, then stops — call it repeatedly until it reports
// zero rows processed. This avoids exceeding free-tier Edge Function
// compute limits, which a single call processing all ~450+ rows in one
// loop hit (WORKER_RESOURCE_LIMIT).
//
// Uses Supabase's built-in gte-small model (free, runs in Edge Runtime,
// no external API key). Safe to re-run — only processes rows where
// embedding is null.
//
// Call repeatedly with: curl -X POST <function-url> -H "Authorization: Bearer <service-role-key>"
// Stop calling once the response shows shco_full_oes: 0, shco_kb: 0.

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const BATCH_SIZE = 5; // small — one call handles 5 OE rows + 5 kb rows max

Deno.serve(async (req: Request) => {
  try {
    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");

    const supabase = createClient(supabaseUrl, serviceKey);

    // @ts-ignore — Supabase.ai is injected globally in the Edge Runtime
    const model = new Supabase.ai.Session("gte-small");

    const embed = async (text: string): Promise<number[]> => {
      const output = await model.run(text, { mean_pool: true, normalize: true });
      return Array.from(output as Iterable<number>);
    };

    const results = { shco_full_oes: 0, shco_kb: 0, errors: [] as string[] };

    // --- shco_full_oes: ONE batch only, no outer loop ---
    {
      const { data: rows, error } = await supabase
        .from("shco_full_oes")
        .select("oe_code, text, interpretation")
        .is("embedding", null)
        .limit(BATCH_SIZE);
      if (error) throw new Error(`fetch shco_full_oes: ${error.message}`);

      for (const row of rows ?? []) {
        try {
          const inputText = [row.oe_code, row.text, row.interpretation]
            .filter(Boolean)
            .join(" — ");
          const vec = await embed(inputText);
          const { error: updErr } = await supabase
            .from("shco_full_oes")
            .update({ embedding: vec })
            .eq("oe_code", row.oe_code as string);
          if (updErr) throw updErr;
          results.shco_full_oes++;
        } catch (e) {
          results.errors.push(`shco_full_oes ${row.oe_code}: ${(e as Error).message}`);
        }
      }
    }

    // --- shco_kb: ONE batch only, no outer loop ---
    {
      const { data: rows, error } = await supabase
        .from("shco_kb")
        .select("id, title, content")
        .is("embedding", null)
        .limit(BATCH_SIZE);
      if (error) throw new Error(`fetch shco_kb: ${error.message}`);

      for (const row of rows ?? []) {
        try {
          const inputText = [row.title, row.content].filter(Boolean).join(" — ");
          const vec = await embed(inputText);
          const { error: updErr } = await supabase
            .from("shco_kb")
            .update({ embedding: vec })
            .eq("id", row.id as string);
          if (updErr) throw updErr;
          results.shco_kb++;
        } catch (e) {
          results.errors.push(`shco_kb ${row.id}: ${(e as Error).message}`);
        }
      }
    }

    return new Response(JSON.stringify(results, null, 2), {
      headers: { "Content-Type": "application/json" },
    });
  } catch (e) {
    return new Response(JSON.stringify({ error: (e as Error).message }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
});