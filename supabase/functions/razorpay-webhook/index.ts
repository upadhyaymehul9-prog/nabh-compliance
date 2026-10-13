// Razorpay webhook receiver. This is the ONLY place that flips a hospital's
// plan to 'paid' off a real payment — never trust a client call for that.
//
// verify_jwt is OFF for this function deliberately: Razorpay's webhook POST
// carries no Supabase apikey/Authorization header at all (it's an external
// server, not our frontend), so the platform JWT gate would reject every
// delivery with 401 before this code even runs. Authentication instead comes
// entirely from verifying the X-Razorpay-Signature header below — do not
// remove that check if you ever re-enable verify_jwt or refactor this.
//
// Configure in Razorpay Dashboard -> Settings -> Webhooks:
//   URL: https://<project-ref>.functions.supabase.co/razorpay-webhook
//   Active events: subscription.activated, subscription.charged,
//                   subscription.cancelled, subscription.halted,
//                   subscription.completed, subscription.expired
//   Secret: set the same value as RAZORPAY_WEBHOOK_SECRET below.
//
// Security: verifies the X-Razorpay-Signature header (HMAC-SHA256 of the raw
// body using the webhook secret) before trusting anything in the payload.
// Request bodies are read as raw text first — signature verification needs
// the exact bytes Razorpay signed, not a re-serialized JSON.parse() output.

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

async function verifySignature(rawBody: string, signature: string, secret: string): Promise<boolean> {
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const mac = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(rawBody));
  const expected = Array.from(new Uint8Array(mac)).map((b) => b.toString(16).padStart(2, "0")).join("");
  if (expected.length !== signature.length) return false;
  let diff = 0;
  for (let i = 0; i < expected.length; i++) diff |= expected.charCodeAt(i) ^ signature.charCodeAt(i);
  return diff === 0;
}

Deno.serve(async (req: Request) => {
  if (req.method !== "POST") return new Response("Method not allowed", { status: 405 });

  try {
    const webhookSecret = Deno.env.get("RAZORPAY_WEBHOOK_SECRET");
    const supabaseUrl = Deno.env.get("SUPABASE_URL");
    const serviceKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
    if (!webhookSecret) throw new Error("RAZORPAY_WEBHOOK_SECRET missing");
    if (!supabaseUrl) throw new Error("SUPABASE_URL missing");
    if (!serviceKey) throw new Error("SUPABASE_SERVICE_ROLE_KEY missing");

    const rawBody = await req.text();
    const signature = req.headers.get("X-Razorpay-Signature") ?? "";
    const valid = await verifySignature(rawBody, signature, webhookSecret);
    if (!valid) {
      console.error("Razorpay webhook: signature verification failed");
      return new Response("Invalid signature", { status: 401 });
    }

    const body = JSON.parse(rawBody);
    const dedupeKey: string = body?.id ?? `${body.event}:${body.created_at}:${JSON.stringify(body.payload).slice(0, 100)}`;

    const supabase = createClient(supabaseUrl, serviceKey);

    const { error: insertErr } = await supabase
      .from("razorpay_webhook_events")
      .insert({ id: dedupeKey, event: body.event, payload: body });
    if (insertErr) {
      if (insertErr.code === "23505") {
        return new Response("OK (already processed)", { status: 200 });
      }
      throw new Error(`Event log insert failed: ${insertErr.message}`);
    }

    const subscriptionEntity = body?.payload?.subscription?.entity;
    const hospitalId: string | undefined = subscriptionEntity?.notes?.hospital_id;
    const subscriptionId: string | undefined = subscriptionEntity?.id;

    if (!hospitalId) {
      console.warn(`Razorpay webhook ${body.event}: no hospital_id in subscription notes, skipping`, subscriptionId);
      return new Response("OK (no hospital_id to act on)", { status: 200 });
    }

    switch (body.event) {
      case "subscription.activated":
      case "subscription.charged": {
        const currentEndUnix: number | undefined = subscriptionEntity?.current_end;
        const accessUntil = currentEndUnix
          ? new Date(currentEndUnix * 1000).toISOString()
          : new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString();

        const { error } = await supabase
          .from("hospitals")
          .update({
            plan: "paid",
            access_until: accessUntil,
            subscription_status: subscriptionEntity.status,
            razorpay_subscription_id: subscriptionId,
          })
          .eq("id", hospitalId);
        if (error) throw new Error(`Failed to activate hospital ${hospitalId}: ${error.message}`);
        console.log(`Hospital ${hospitalId} marked paid, access_until=${accessUntil} (${body.event})`);
        break;
      }

      case "subscription.cancelled":
      case "subscription.halted":
      case "subscription.completed":
      case "subscription.expired": {
        const { error } = await supabase
          .from("hospitals")
          .update({ subscription_status: subscriptionEntity.status })
          .eq("id", hospitalId);
        if (error) throw new Error(`Failed to update status for hospital ${hospitalId}: ${error.message}`);
        console.log(`Hospital ${hospitalId} subscription status -> ${subscriptionEntity.status} (${body.event})`);
        break;
      }

      default:
        console.log(`Razorpay webhook: unhandled event ${body.event}, ignoring`);
    }

    return new Response("OK", { status: 200 });
  } catch (err) {
    console.error(err);
    return new Response((err as Error).message, { status: 500 });
  }
});
