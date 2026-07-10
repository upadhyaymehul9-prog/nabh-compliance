import { useState, useEffect } from "react";
import { supabase } from "../supabaseClient";

const HP = {
  brand: "#065F46", brandDark: "#064E3B", brandMid: "#047857", brandBg: "#ECFDF5",
  amber: "#D97706", text: "#1E293B", muted: "#475569", subtle: "#94A3B8", border: "#E2E8F0", white: "#FFFFFF",
  red: "#DC2626", redBg: "#FEF2F2", green: "#059669", greenBg: "#ECFDF9", brandLight: "#6EE7B7",
  boxBorder: "1.5px solid #000000",
};

// variant="page": full-screen standalone login (password recovery / expired-link fallback)
// variant="embedded": compact card meant to sit inside the homepage hero
export default function AuthForm({ onLogin, initialError, variant = "page", onBackToHomepage, initialMode }) {
  const embedded = variant === "embedded";
  const [email, setEmail] = useState(""); const [pass, setPass] = useState(""); const [whatsapp, setWhatsapp] = useState("");
  const [rememberMe, setRememberMe] = useState(false);
  const [mode, setMode] = useState(initialMode || "login"); const [error, setError] = useState(initialError || "");
  const [loading, setLoading] = useState(false); const [msg, setMsg] = useState("");
  const [showPricing, setShowPricing] = useState(false);
  const [showContact, setShowContact] = useState(false);
  useEffect(() => {
    if (!document.querySelector('link[data-login-figtree]')) {
      const link = document.createElement('link');
      link.rel = 'stylesheet'; link.setAttribute('data-login-figtree', '1');
      link.href = 'https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800&display=swap';
      document.head.appendChild(link);
    }
  }, []);
  useEffect(() => {
    const saved = localStorage.getItem('savedEmail');
    if (saved) { setEmail(saved); setRememberMe(true); }
  }, []);
  useEffect(() => {
    if (initialError) setError(initialError);
  }, [initialError]);
  const handle = async () => {
    setError(""); setMsg(""); setLoading(true);
    try {
      if (mode === "login") { const { data, error: err } = await supabase.auth.signInWithPassword({ email, password: pass }); if (err) throw err; if (rememberMe) { localStorage.setItem('savedEmail', email); } else { localStorage.removeItem('savedEmail'); } onLogin(data.user); }
      else if (mode === "signup") {
        const { data, error: err } = await supabase.auth.signUp({ email, password: pass }); if (err) throw err;
        if (whatsapp.trim() && data.user && data.session) { await supabase.from("profiles").upsert({ id: data.user.id, whatsapp_number: whatsapp.trim() }, { onConflict: "id" }); }
        await fetch("https://api.web3forms.com/submit", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ access_key: "2aaadfc3-c669-4b2b-92b8-6d6bee4faee1", subject: "New AccredReady Signup", name: "New User", email, message: `New signup:\nEmail: ${email}${whatsapp.trim() ? `\nWhatsApp: ${whatsapp.trim()}` : ""}`, }) });
        if (data.session) onLogin(data.user); else { setMsg("Account created. You can now sign in."); setMode("login"); }
      }
      else if (mode === "reset") { if (!email.trim()) throw new Error("Enter your email address first."); const { error: err } = await supabase.auth.resetPasswordForEmail(email, { redirectTo: "https://accredready.in" }); if (err) throw err; setMsg("Password reset email sent! Check your inbox."); setMode("login"); }
    } catch (e) { setError(e.message); }
    setLoading(false);
  };
  const signInWithGoogle = async () => {
    setError(""); setLoading(true);
    const { error: err } = await supabase.auth.signInWithOAuth({
      provider: "google",
      options: { redirectTo: "https://accredready.in" }
    });
    if (err) { setError(err.message); setLoading(false); }
  };
  if (mode === 'terms') return <TermsScreen onBack={() => setMode('login')} />;
  const inp = { width: "100%", padding: "12px 14px", borderRadius: 10, border: HP.boxBorder, background: "#f8fafc", color: HP.text, fontSize: 15, boxSizing: "border-box", fontFamily: "Inter,system-ui,sans-serif" };
  const lbl = { fontSize: 12, color: HP.muted, marginBottom: 6, fontWeight: 600, fontFamily: "Figtree,Inter,sans-serif" };
  const card = (
    <div style={embedded
      ? { position: "relative", background: HP.white, border: HP.boxBorder, borderRadius: 16, padding: "26px 24px", width: "100%", maxWidth: 420, boxShadow: "0 20px 50px rgba(6,78,59,.22)" }
      : { position: "relative", zIndex: 1, background: HP.white, border: HP.boxBorder, borderRadius: 16, padding: "36px 32px", width: "100%", maxWidth: 400, boxShadow: "0 20px 50px rgba(6,78,59,.22)" }
    }>
      {onBackToHomepage && (
        <button type="button" onClick={onBackToHomepage} style={{ display: "inline-flex", alignItems: "center", gap: 6, marginBottom: 20, background: "none", border: "none", padding: 0, cursor: "pointer", fontFamily: "Figtree,Inter,sans-serif", fontSize: 13, fontWeight: 600, color: HP.muted }}>
          ← Back to homepage
        </button>
      )}
      <div style={{ display: "flex", alignItems: "center", gap: 12, marginBottom: 24 }}>
        <div style={{ width: 42, height: 42, borderRadius: 10, background: HP.brand, border: HP.boxBorder, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Figtree,sans-serif", fontWeight: 800, fontSize: 20, color: HP.white, flexShrink: 0 }}>A</div>
        <div>
          <div style={{ fontFamily: "Figtree,sans-serif", fontSize: 20, fontWeight: 700, color: HP.text }}>Accred<span style={{ color: HP.brand }}>Ready</span></div>
          <div style={{ fontSize: 13, color: HP.muted, marginTop: 2 }}>{mode === "signup" ? "Create your account" : mode === "reset" ? "Reset password" : "Sign in to continue"}</div>
        </div>
      </div>
      {error && <div style={{ background: HP.redBg, border: HP.boxBorder, borderRadius: 10, padding: "10px 14px", marginBottom: 16, fontSize: 13, color: HP.red }}>{error}</div>}
      {msg && <div style={{ background: HP.greenBg, border: HP.boxBorder, borderRadius: 10, padding: "10px 14px", marginBottom: 16, fontSize: 13, color: HP.green }}>{msg}</div>}
      {!embedded && mode === "login" && (
        <div style={{ textAlign: "center", padding: "0 0 18px", marginBottom: 18, borderBottom: `1px solid ${HP.border}` }}>
          <div style={{ fontFamily: "Fraunces,Georgia,serif", fontSize: 15, fontStyle: "italic", color: HP.text, lineHeight: 1.8 }}>"Quality is not an act, it is a habit."</div>
          <div style={{ fontSize: 11, color: HP.subtle, marginTop: 6, letterSpacing: 2 }}>— ARISTOTLE</div>
        </div>
      )}
      <div style={{ marginBottom: 14 }}>
        <div style={lbl}>Email</div>
        <input value={email} onChange={e => setEmail(e.target.value)} placeholder="admin@hospital.com" type="email" style={inp} />
      </div>
      {mode === "signup" && <div style={{ marginBottom: 14 }}>
        <div style={lbl}>WhatsApp number (optional)</div>
        <input value={whatsapp} onChange={e => setWhatsapp(e.target.value)} placeholder="+91 98765 43210" type="tel" style={inp} />
      </div>}
      {mode !== "reset" && <div style={{ marginBottom: 20 }}>
        <div style={lbl}>Password</div>
        <input value={pass} onChange={e => setPass(e.target.value)} placeholder="••••••••" type="password" onKeyDown={e => e.key === "Enter" && handle()} style={inp} />
      </div>}
      {mode === "reset" && <div style={{ marginBottom: 20, fontSize: 13, color: HP.muted, lineHeight: 1.6 }}>Enter your email above and we'll send you a password reset link.</div>}
      {mode === "login" && <div style={{ display: "flex", alignItems: "center", gap: 8, margin: "8px 0 16px" }}>
        <input type="checkbox" id="rememberMe" checked={rememberMe} onChange={e => setRememberMe(e.target.checked)} style={{ width: 16, height: 16, accentColor: HP.brand, cursor: "pointer" }} />
        <label htmlFor="rememberMe" style={{ color: HP.muted, fontSize: 13, cursor: "pointer" }}>Remember me</label>
      </div>}
      <button onClick={handle} disabled={loading} style={{ width: "100%", padding: "13px", borderRadius: 10, background: HP.brand, border: HP.boxBorder, color: HP.white, fontSize: 15, fontWeight: 700, cursor: "pointer", opacity: loading ? 0.7 : 1, fontFamily: "Figtree,Inter,sans-serif", boxShadow: "0 2px 8px rgba(6,95,70,.28)" }}>
        {loading ? "Please wait…" : mode === "login" ? "Sign In →" : mode === "signup" ? "Create Account →" : "Send Reset Email →"}
      </button>
      <div style={{ fontSize: 11, color: HP.subtle, textAlign: "center", marginTop: 8 }}>🔒 Secured by Supabase · No spam, ever</div>
      {mode !== "reset" && (
        <>
          <div style={{ display: "flex", alignItems: "center", gap: 10, margin: "16px 0" }}>
            <div style={{ flex: 1, height: 1, background: HP.border }} />
            <div style={{ fontSize: 12, color: HP.muted, letterSpacing: 1 }}>OR</div>
            <div style={{ flex: 1, height: 1, background: HP.border }} />
          </div>
          <button onClick={signInWithGoogle} disabled={loading}
            style={{ width: "100%", padding: "12px", borderRadius: 10, background: HP.white, border: HP.boxBorder, color: HP.text, fontSize: 14, fontWeight: 600, cursor: "pointer", display: "flex", alignItems: "center", justifyContent: "center", gap: 10, opacity: loading ? 0.7 : 1, fontFamily: "Figtree,Inter,sans-serif" }}>
            <svg width="18" height="18" viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.08 17.74 9.5 24 9.5z" /><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z" /><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z" /><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.18 1.48-4.97 2.31-8.16 2.31-6.26 0-11.57-3.58-13.46-8.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z" /></svg>
            Continue with Google
          </button>
        </>
      )}
      {mode === "login" && (
        <>
          <div style={{ textAlign: "center", marginTop: 12, fontSize: 13, color: HP.muted }}>
            <span onClick={() => { setMode("reset"); setError(""); setMsg(""); }} style={{ color: HP.brandMid, cursor: "pointer", fontWeight: 600 }}>Forgot password?</span>
          </div>
          <div style={{ display: "flex", gap: 16, justifyContent: "center", marginTop: 14, flexWrap: "wrap" }}>
            <span onClick={() => setShowContact(true)} style={{ fontSize: 11, color: HP.muted, cursor: "pointer", letterSpacing: .5, textTransform: "uppercase", fontWeight: 600 }}>Contact</span>
            <span onClick={() => setMode("terms")} style={{ fontSize: 11, color: HP.muted, cursor: "pointer", letterSpacing: .5, textTransform: "uppercase", fontWeight: 600 }}>Terms</span>
            <a href="/privacy.html" target="_blank" rel="noopener noreferrer" style={{ fontSize: 11, color: HP.muted, letterSpacing: .5, textTransform: "uppercase", textDecoration: "none", fontWeight: 600 }}>Privacy</a>
          </div>
        </>
      )}
      <div style={{ textAlign: "center", marginTop: 10, fontSize: 13, color: HP.muted }}>
        {mode === "login" ? "Don't have an account? " : mode === "signup" ? "Already have an account? " : "Remember your password? "}
        <span onClick={() => { setMode(mode === "login" ? "signup" : "login"); setError(""); setMsg(""); }} style={{ color: HP.brand, cursor: "pointer", fontWeight: 700 }}>
          {mode === "login" ? "Sign up" : mode === "reset" ? "Sign in" : "Sign in"}
        </span>
      </div>
      {!embedded && !window.matchMedia("(display-mode: standalone)").matches && (
        <div style={{ textAlign: "center", marginTop: 14 }}>
          <div style={{ fontSize: 11, color: HP.subtle, marginBottom: 6 }}>Or get the Android app</div>
          <a href="https://play.google.com/store/apps/details?id=com.mktech.nabhcompliance" target="_blank" rel="noopener noreferrer" style={{ display: "inline-block" }}>
            <img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get it on Google Play" style={{ height: 44, width: "auto", display: "block", margin: "0 auto" }} />
          </a>
        </div>
      )}
      {!embedded && <div style={{ textAlign: "center", marginTop: 10, fontSize: 11, color: HP.subtle }}>Independent educational tool — Not affiliated with NABH/QCI</div>}
      <div style={{ textAlign: "center", marginTop: 10, paddingBottom: 4 }}>
        <span style={{ fontSize: 12, color: HP.muted }}>14-day free trial · No credit card · </span>
        <button onClick={() => setShowPricing(true)} style={{ fontSize: 12, color: HP.brand, cursor: "pointer", fontWeight: 700, background: "none", border: "none", padding: 0, fontFamily: "inherit" }}>View Pricing →</button>
      </div>
      {showPricing && (
        <div onClick={() => setShowPricing(false)} style={{ position: "fixed", inset: 0, zIndex: 2000, background: "rgba(6,30,20,.55)", display: "flex", alignItems: "center", justifyContent: "center", padding: 20 }}>
          <div onClick={e => e.stopPropagation()} style={{ background: HP.white, border: HP.boxBorder, borderRadius: 16, padding: "28px 24px", maxWidth: 400, width: "100%", textAlign: "center", position: "relative", boxShadow: "0 20px 50px rgba(0,0,0,.2)" }}>
            <button onClick={() => setShowPricing(false)} style={{ position: "absolute", top: 12, right: 14, background: "none", border: "none", color: HP.subtle, fontSize: 18, cursor: "pointer", lineHeight: 1 }}>✕</button>
            <div style={{ fontSize: 11, letterSpacing: 3, color: HP.brand, marginBottom: 8, fontWeight: 700 }}>ACCREDREADY</div>
            <div style={{ display: "flex", alignItems: "baseline", justifyContent: "center", gap: 4, marginBottom: 4 }}>
              <span style={{ fontSize: 38, fontWeight: 800, color: HP.text, fontFamily: "Figtree,sans-serif" }}>₹499</span>
              <span style={{ fontSize: 14, color: HP.muted }}>/month</span>
            </div>
            <div style={{ fontSize: 12, color: HP.muted, marginBottom: 20 }}>Per hospital · All features included</div>
            <div style={{ textAlign: "left", marginBottom: 22 }}>
              {["Full NABH compliance tracking", "Unlimited OE scoring", "KPI tracking and audit management", "Committee calendar and mock drills", "PDF gap reports", "No setup fee. Cancel anytime."].map((f, i) => (
                <div key={i} style={{ display: "flex", gap: 10, alignItems: "flex-start", marginBottom: 9 }}>
                  <span style={{ color: HP.brand, flexShrink: 0, fontWeight: 700 }}>✓</span>
                  <span style={{ fontSize: 13, color: HP.muted, lineHeight: 1.5 }}>{f}</span>
                </div>
              ))}
            </div>
            <a href="https://wa.me/918511180957?text=Hi%20Dr.%20Mehul%2C%20I%20want%20to%20subscribe%20to%20AccredReady%20for%20Rs.%20499%2Fmonth" target="_blank" rel="noopener noreferrer"
              style={{ display: "block", padding: "13px", borderRadius: 10, background: HP.amber, color: HP.white, fontSize: 15, fontWeight: 800, textDecoration: "none", boxShadow: "0 4px 14px rgba(217,119,6,.35)", fontFamily: "Figtree,sans-serif" }}>
              Get Started — WhatsApp Us
            </a>
            <div style={{ fontSize: 11, color: HP.subtle, marginTop: 12 }}>14-day free trial · Sign up to begin</div>
          </div>
        </div>
      )}
      {showContact && <ContactModal onClose={() => setShowContact(false)} />}
    </div>
  );
  if (embedded) return card;
  return (
    <div style={{ minHeight: "100vh", background: `linear-gradient(145deg,${HP.brandDark} 0%,${HP.brandMid} 42%,${HP.brandBg} 100%)`, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Inter,system-ui,sans-serif", padding: "24px 16px", position: "relative" }}>
      <div style={{ position: "absolute", inset: 0, backgroundImage: "radial-gradient(circle, rgba(255,255,255,.06) 1px, transparent 1px)", backgroundSize: "28px 28px", pointerEvents: "none" }} />
      {card}
    </div>
  );
}

function ContactModal({ onClose }) {
  const [name, setName] = useState(""); const [email, setEmail] = useState(""); const [phone, setPhone] = useState(""); const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false); const [success, setSuccess] = useState(false); const [err, setErr] = useState(false);
  const submit = async (e) => {
    e.preventDefault(); setLoading(true); setSuccess(false); setErr(false);
    try {
      const res = await fetch("https://api.web3forms.com/submit", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ access_key: "2aaadfc3-c669-4b2b-92b8-6d6bee4faee1", name, email, phone, message }) });
      const json = await res.json();
      if (res.ok && json.success) { setSuccess(true); setName(""); setEmail(""); setPhone(""); setMessage(""); }
      else setErr(true);
    } catch { setErr(true); }
    setLoading(false);
  };
  const inp = { width: "100%", boxSizing: "border-box", padding: "12px 14px", background: "#f8fafc", border: `1.5px solid ${HP.border}`, borderRadius: 10, color: HP.text, fontSize: 15, outline: "none", fontFamily: "inherit" };
  const lbl = { display: "block", color: HP.muted, fontSize: 13, marginBottom: 5, fontWeight: 600 };
  return (
    <div onClick={onClose} style={{ position: "fixed", inset: 0, zIndex: 3000, background: "rgba(6,30,20,.55)", display: "flex", alignItems: "center", justifyContent: "center", padding: 20 }}>
      <div onClick={e => e.stopPropagation()} style={{ background: HP.white, border: `1px solid ${HP.border}`, borderRadius: 16, padding: "28px 24px", maxWidth: 420, width: "100%", position: "relative", maxHeight: "90vh", overflowY: "auto", boxShadow: "0 20px 50px rgba(0,0,0,.2)" }}>
        <button onClick={onClose} style={{ position: "absolute", top: 12, right: 14, background: "none", border: "none", color: HP.subtle, fontSize: 20, cursor: "pointer", lineHeight: 1 }}>✕</button>
        <div style={{ fontSize: 11, letterSpacing: 3, color: HP.brand, marginBottom: 8, textTransform: "uppercase", fontWeight: 700 }}>AccredReady</div>
        <div style={{ fontSize: 20, fontWeight: 700, color: HP.text, marginBottom: 18, fontFamily: "Figtree,sans-serif" }}>Contact Us</div>
        {success && <div style={{ color: HP.green, fontSize: 15, padding: 14, background: HP.greenBg, borderRadius: 10, marginBottom: 16 }}>Thank you! We'll get back to you soon.</div>}
        {err && <div style={{ color: HP.red, fontSize: 14, padding: 12, background: HP.redBg, borderRadius: 10, marginBottom: 16 }}>Something went wrong, please try again.</div>}
        <form onSubmit={submit}>
          <div style={{ marginBottom: 14 }}><label style={lbl}>Name *</label><input type="text" required value={name} onChange={e => setName(e.target.value)} style={inp} /></div>
          <div style={{ marginBottom: 14 }}><label style={lbl}>Email *</label><input type="email" required value={email} onChange={e => setEmail(e.target.value)} style={inp} /></div>
          <div style={{ marginBottom: 14 }}><label style={lbl}>Mobile *</label><input type="tel" required value={phone} onChange={e => setPhone(e.target.value)} style={inp} /></div>
          <div style={{ marginBottom: 18 }}><label style={lbl}>Message *</label><textarea required rows={4} value={message} onChange={e => setMessage(e.target.value)} style={{ ...inp, resize: "vertical" }} /></div>
          <button type="submit" disabled={loading} style={{ width: "100%", padding: 12, background: HP.brand, border: "none", borderRadius: 10, color: HP.white, fontSize: 15, fontWeight: 600, cursor: "pointer", opacity: loading ? 0.7 : 1, fontFamily: "Figtree,inherit" }}>{loading ? "Sending…" : "Send Message"}</button>
        </form>
      </div>
    </div>
  );
}

function TermsScreen({ onBack }) {
  return (
    <div style={{ minHeight: '100vh', background: '#050e1a', color: '#c8dcea', fontFamily: 'Segoe UI,sans-serif', padding: '40px 24px', maxWidth: 720, margin: '0 auto' }}>
      <button onClick={onBack} style={{ background: 'transparent', border: '1px solid #0f2640', color: '#3a5870', padding: '6px 16px', borderRadius: 6, cursor: 'pointer', fontSize: 13, marginBottom: 32 }}>← Back to Login</button>
      <div style={{ color: '#c9a84c', fontSize: 12, letterSpacing: 3, marginBottom: 8, textTransform: 'uppercase' }}>AccredReady</div>
      <h1 style={{ fontFamily: 'Georgia,serif', fontSize: 28, fontWeight: 300, color: '#eef4f9', marginBottom: 6 }}>Terms & Conditions</h1>
      <div style={{ fontSize: 12, color: '#3a5870', letterSpacing: 1, marginBottom: 32 }}>Effective Date: 19 May 2026</div>
      {[
        ['1. Acceptance', 'By using AccredReady at accredready.in, you agree to these terms. If you disagree, do not use the platform.'],
        ['2. What AccredReady Is', 'AccredReady is an independent educational preparation tool for healthcare accreditation. It is not affiliated with, endorsed by, or officially connected to any accreditation body including any government authority.'],
        ['3. Your Account', 'You are responsible for keeping your login credentials secure. You agree to provide accurate information. We may suspend accounts that violate these terms.'],
        ['4. Subscription & Payment', 'Plan: ₹499/month per hospital, all features included. 14-day free trial for new users — no payment required. Payment via UPI or bank transfer. Cancel anytime by emailing upadhyay.mehul9@gmail.com. No refunds for partial months used.'],
        ['5. Acceptable Use', 'You agree not to share your account, attempt to access other users data, copy or reproduce platform content, or use the platform for any unlawful purpose.'],
        ['6. Intellectual Property', 'All content, design, and code is owned by AccredReady. No reproduction without written permission.'],
        ['7. Disclaimer', 'AccredReady does not guarantee accreditation outcomes. All accreditation decisions rest with the relevant accreditation body. Always verify content against official published standards.'],
        ['8. Limitation of Liability', 'AccredReady is not liable for any indirect, incidental, or consequential damages arising from use of the platform.'],
        ['9. Governing Law', 'These terms are governed by Indian law. Disputes are subject to courts in Gujarat, India.'],
        ['10. Changes', 'We may update these terms. Continued use after changes means acceptance.'],
        ['11. Contact', 'Email: upadhyay.mehul9@gmail.com'],
      ].map(([title, body]) => (
        <div key={title} style={{ marginBottom: 20 }}>
          <div style={{ fontSize: 13, fontWeight: 700, color: '#c9a84c', letterSpacing: 1, textTransform: 'uppercase', marginBottom: 6 }}>{title}</div>
          <div style={{ fontSize: 15, color: '#c8dcea', lineHeight: 1.8 }}>{body}</div>
        </div>
      ))}
    </div>
  );
}
