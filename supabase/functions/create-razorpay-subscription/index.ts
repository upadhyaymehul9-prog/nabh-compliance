// Starts a Razorpay recurring subscription (₹499/month, UPI Autopay or card
// mandate) for the signed-in user's hospital, and returns the subscription_id
// the frontend hands to Razorpay Checkout to complete the mandate.
//
// The hospital is derived server-side from the caller's own JWT
// (profiles -> hospital_id), the same pattern used by the document paywall —
// never from a client-supplied hospital_id, so this can't be used to start a
// subscription against a hospital that isn't yours.
//
// Does NOT mark the hospital as paid. That only happens when the Razorpay
// webhook confirms an actual successful charge (see razorpay-webhook).

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const PROD_ORIGIN = "https://accredready.in";
const ALLOWED_ORIGINS = [PROD_ORIGIN, "http://localhost:3000"];

function corsFor(req: Request): Record<string, string> {
  const origin = req.headers.get("Origin") ?? "";
  return {
    "Access-Control-Allow-Origin": ALLOWED_ORIGINS.includes(origin) ? origin : PROD_ORIGIN,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization, apikey, x-client-info",
    "Vary": "Origin",
  };
}

Deno.serve(async (req: Request) => {
  const CORS = corsFor(req);
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });

  try {
    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    const razorpayKeyId = Deno.env.get("RAZORPAY_KEY_ID");
    const razorpayKeySecret = Deno.env.get("RAZORPAY_KEY_SECRET");
    const razorpayPlanId = Deno.env.get("RAZORPAY_PLAN_ID");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");
    if (!razorpayKeyId) throw new Error("RAZORPAY_KEY_ID missing");
    if (!razorpayKeySecret) throw new Error("RAZORPAY_KEY_SECRET missing");
    if (!razorpayPlanId) throw new Error("RAZORPAY_PLAN_ID missing — create a ₹499/month Plan in Razorpay first and set its plan_id here");

    const supabase = createClient(supabaseUrl, serviceKey);

    // Identify the caller and their hospital from the JWT — never trust a
    // client-supplied hospital_id for this.
    const authHeader = req.headers.get("Authorization");
    const jwt = authHeader?.replace(/^Bearer\s+/i, "");
    if (!jwt) {
      return Response.json({ error: "Sign in required." }, { status: 401, headers: CORS });
    }
    const { data: userData, error: userErr } = await supabase.auth.getUser(jwt);
    if (userErr || !userData?.user) {
      return Response.json({ error: "Your session has expired — sign in again." }, { status: 401, headers: CORS });
    }

    const { data: profile, error: profileErr } = await supabase
      .from("profiles")
      .select("hospital_id")
      .eq("id", userData.user.id)
      .maybeSingle();
    if (profileErr) throw new Error(`Profile lookup: ${profileErr.message}`);
    if (!profile?.hospital_id) {
      return Response.json({ error: "No hospital linked to this account." }, { status: 400, headers: CORS });
    }

    const { data: hospital, error: hospErr } = await supabase
      .from("hospitals")
      .select("id, name, plan, access_until")
      .eq("id", profile.hospital_id)
      .maybeSingle();
    if (hospErr) throw new Error(`Hospital lookup: ${hospErr.message}`);
    if (!hospital) {
      return Response.json({ error: "Hospital not found." }, { status: 404, headers: CORS });
    }

    // Already an active paying subscriber — refuse rather than spin up a
    // second, orphaned Razorpay subscription object alongside the real one.
    if (hospital.plan === "paid" && hospital.access_until && new Date(hospital.access_until) > new Date()) {
      return Response.json({ error: "This hospital already has an active subscription." }, { status: 409, headers: CORS });
    }

    // Create the subscription with Razorpay. notes.hospital_id is how the
    // webhook maps a payment event back to this hospital — Razorpay echoes
    // notes back on every subscription/payment webhook payload.
    const razorpayAuth = "Basic " + btoa(`${razorpayKeyId}:${razorpayKeySecret}`);
    const rpRes = await fetch("https://api.razorpay.com/v1/subscriptions", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Authorization": razorpayAuth },
      body: JSON.stringify({
        plan_id: razorpayPlanId,
        customer_notify: 1,
        total_count: 120, // 10 years of monthly cycles; subscription just runs until cancelled
        notes: {
          hospital_id: hospital.id,
          hospital_name: hospital.name,
        },
      }),
    });

    const rpBody = await rpRes.json();
    if (!rpRes.ok) {
      console.error("Razorpay subscription create failed:", rpBody);
      return Response.json(
        { error: rpBody?.error?.description || "Could not start subscription with Razorpay." },
        { status: 502, headers: CORS },
      );
    }

    // Record the pending subscription immediately so support can see an
    // attempt was made even if the user abandons the Checkout modal.
    const { error: updateErr } = await supabase
      .from("hospitals")
      .update({
        razorpay_subscription_id: rpBody.id,
        subscription_status: rpBody.status, // "created"
      })
      .eq("id", hospital.id);
    if (updateErr) console.error("Failed to record pending subscription:", updateErr.message);

    return Response.json(
      {
        subscription_id: rpBody.id,
        key_id: razorpayKeyId, // public key, safe to return — Checkout.js needs it client-side
      },
      { headers: CORS },
    );
  } catch (err) {
    console.error(err);
    return Response.json({ error: (err as Error).message }, { status: 500, headers: CORS });
  }
});
