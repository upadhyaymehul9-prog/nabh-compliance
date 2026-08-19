import { useState, useEffect, useRef } from "react";
import { GennieHead, GennieFull } from "./GennieMascot";

const ENDPOINT = "https://tbptllgcjtiiqspxqcde.supabase.co/functions/v1/ai-assistant";
const ANON_KEY =
  "sb_publishable_tEu-kA8f9VLW-5uvU4E7ZA_PtaX59bw";

// Below this viewport height the panel at its normal anchor cannot show the
// whole greeting without scrolling: the greeting is 256px of content plus 108px
// of chrome (header 48 + input 60) = a 364px panel, while the normal anchor
// reserves 316px, so it needs 680px of viewport. Under the gate the panel drops
// 80px lower — stopping 8px above the tour "?" button — and the collapsed
// circle fades out, since at bottom:152 it would sit on top of the input bar.
// At or above the gate every value is exactly what shipped in adb2721.
const SHORT_VIEWPORT_GATE = 680;

// trigger = { code: string|null, id: number }
// id increment = new auto-ask; allows same code to re-trigger
export default function AIAssistantWidget({ T, open, onOpen, onClose, trigger }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [isShort, setIsShort] = useState(
    () => typeof window !== "undefined" && window.innerHeight < SHORT_VIEWPORT_GATE
  );
  const bottomRef = useRef(null);

  useEffect(() => {
    const onResize = () =>
      setIsShort(window.innerHeight < SHORT_VIEWPORT_GATE);
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);

  const ask = async (question) => {
    const q = question.trim();
    if (!q || loading) return;
    setMessages((prev) => [...prev, { role: "user", content: q }]);
    setInput("");
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(ENDPOINT, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${ANON_KEY}`,
        },
        body: JSON.stringify({ question: q }),
      });
      const data = await res.json();
      if (!res.ok || data.error) throw new Error(data.error || "Unknown error");
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: data.answer, sources: data.sources || [] },
      ]);
    } catch {
      setError("Couldn't get an answer — please try again.");
    } finally {
      setLoading(false);
    }
  };

  // Auto-ask when triggered by OE row click
  useEffect(() => {
    if (!trigger?.code || !trigger?.id) return;
    ask(`What do I need for ${trigger.code}?`);
  }, [trigger?.id]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleSubmit = (e) => {
    e.preventDefault();
    ask(input);
  };

  // Closed, Gennie floats free on the page — no card, border or backdrop — with
  // the greeting stacked beneath him. Open, he collapses back into the 56px
  // lamp-gold circle so the chat panel can claim the height.
  // Both states share bottom:164, which clears the relocated tour "?" button
  // (bottom:96, 48 tall) by 20px and never reaches the third-party chat widget
  // that owns bottom:14–68 at z-index 1000001.
  const launcherStyle = open
    ? {
        position: "fixed",
        bottom: 164,
        right: 20,
        zIndex: 9996,
        width: 56,
        height: 56,
        borderRadius: 28,
        background: `linear-gradient(135deg, ${T.gold}, #f0d070)`,
        border: "none",
        color: T.bg,
        cursor: "pointer",
        boxShadow: `0 4px 16px rgba(201,168,76,0.5)`,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        lineHeight: 1,
        overflow: "hidden",
        padding: 0,
        // On short viewports the panel drops to bottom:152 and would run the
        // input bar straight under this circle, so it fades out. The panel
        // header's ✕ is the close affordance there.
        opacity: isShort ? 0 : 1,
        pointerEvents: isShort ? "none" : "auto",
        transition: "opacity 0.15s",
      }
    : {
        position: "fixed",
        bottom: 164,
        right: 20,
        zIndex: 9996,
        width: 112,
        background: "transparent",
        border: "none",
        padding: 0,
        margin: 0,
        cursor: "pointer",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 8,
      };

  return (
    <>
      {/* Floating toggle button */}
      <button
        onClick={open ? onClose : onOpen}
        title={open ? "Close Gennie" : "Ask Gennie about SHCO Full requirements"}
        style={launcherStyle}
        aria-label="Gennie assistant"
      >
        {open ? (
          /* 48 inside the 56px circle: the hoop earrings sit at the very edge
             of the 130-wide viewBox, so a full-bleed 56 gets them clipped by
             the border-radius mask. 48 leaves them clear. */
          <GennieHead size={48} />
        ) : (
          <>
            {/* Wrapper carries the shadow — GennieFull takes no style prop, and
                drop-shadow() follows the SVG's alpha so it lifts the figure
                rather than boxing it. */}
            <span
              style={{
                display: "block",
                filter: "drop-shadow(0 4px 12px rgba(0,0,0,0.45))",
              }}
            >
              <GennieFull size={112} />
            </span>
            <span
              style={{
                color: T.gold,
                fontSize: 13,
                fontWeight: 700,
                lineHeight: 1.4,
                textAlign: "center",
              }}
            >
              Kya hukum hai mera aaka?
            </span>
          </>
        )}
      </button>

      {/* Chat panel — slide up above the button */}
      {open && (
        <div
          style={{
            position: "fixed",
            bottom: isShort ? 152 : 232,
            right: 20,
            zIndex: 9995,
            width: 360,
            // Viewport-relative ceiling so the panel never grows above the top
            // of the screen: bottom offset + ~84px top clearance (sticky header).
            // Normal — 232 + 84 = 316, sitting 12px above the collapsed circle.
            // Short  — 152 + 84 = 236, sitting 8px above the tour "?" button.
            // The offset is a fixed constant either way, so the panel only ever
            // grows upward and never reaches the third-party chat widget that
            // owns bottom 20–74 at z-index 1000002.
            maxHeight: isShort
              ? "min(480px, calc(100dvh - 236px))"
              : "min(480px, calc(100dvh - 316px))",
            display: "flex",
            flexDirection: "column",
            background: T.panel,
            border: `1px solid ${T.gold}55`,
            borderRadius: 16,
            boxShadow: "0 8px 40px rgba(0,0,0,0.6)",
            overflow: "hidden",
          }}
        >
          {/* Header */}
          <div
            style={{
              padding: "11px 14px",
              borderBottom: `1px solid ${T.border}`,
              background: T.panel2,
              display: "flex",
              alignItems: "center",
              gap: 10,
              flexShrink: 0,
            }}
          >
            <span
              style={{
                width: 28,
                height: 28,
                borderRadius: 14,
                background: `linear-gradient(135deg, ${T.gold}, #f0d070)`,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                flexShrink: 0,
                overflow: "hidden",
              }}
            >
              <GennieHead size={24} />
            </span>
            <div style={{ flex: 1 }}>
              <div style={{ color: T.gold, fontWeight: 700, fontSize: 13 }}>
                Gennie
              </div>
              <div style={{ color: T.muted, fontSize: 10 }}>
                SHCO Full — grounded on your OE database
              </div>
            </div>
            <button
              onClick={onClose}
              style={{
                background: "transparent",
                border: "none",
                color: T.muted,
                fontSize: 16,
                cursor: "pointer",
                padding: "2px 6px",
                borderRadius: 6,
              }}
            >
              ✕
            </button>
          </div>

          {/* Message list */}
          <div
            style={{
              flex: "1 1 auto",
              overflowY: "auto",
              padding: "12px 14px",
              display: "flex",
              flexDirection: "column",
              gap: 10,
              minHeight: 0,
            }}
          >
            {messages.length === 0 && !loading && (
              <div
                style={{
                  color: T.muted,
                  fontSize: 12,
                  textAlign: "center",
                  marginTop: 16,
                  lineHeight: 1.8,
                }}
              >
                <GennieFull size={72} />
                <div
                  style={{
                    color: T.gold,
                    fontSize: 15,
                    fontWeight: 700,
                    marginTop: 10,
                  }}
                >
                  Kya hukum hai mera aaka?
                </div>
                <div style={{ marginTop: 6 }}>
                  How can I help you stay compliant today? Ask me anything about
                  your OEs, committees, or gaps.
                </div>
                <span
                  style={{
                    color: T.gold,
                    fontStyle: "italic",
                    display: "inline-block",
                    marginTop: 8,
                  }}
                >
                  e.g. "What do I need for IMS.1.a?"
                </span>
              </div>
            )}

            {messages.map((msg, i) => (
              <div
                key={i}
                style={{
                  display: "flex",
                  flexDirection: "column",
                  alignItems: msg.role === "user" ? "flex-end" : "flex-start",
                  gap: 4,
                }}
              >
                <div
                  style={{
                    maxWidth: "88%",
                    padding: "8px 12px",
                    borderRadius:
                      msg.role === "user"
                        ? "12px 12px 2px 12px"
                        : "12px 12px 12px 2px",
                    background:
                      msg.role === "user" ? T.gold + "22" : T.panel2,
                    border: `1px solid ${
                      msg.role === "user" ? T.gold + "44" : T.border
                    }`,
                    color: T.text,
                    fontSize: 12,
                    lineHeight: 1.7,
                    whiteSpace: "pre-wrap",
                    wordBreak: "break-word",
                  }}
                >
                  {msg.content}
                </div>
                {msg.sources && msg.sources.length > 0 && (
                  <div
                    style={{
                      display: "flex",
                      gap: 4,
                      flexWrap: "wrap",
                      maxWidth: "88%",
                    }}
                  >
                    {msg.sources.map((src) => (
                      <span
                        key={src}
                        style={{
                          fontSize: 10,
                          padding: "1px 7px",
                          borderRadius: 8,
                          background: T.gold + "18",
                          border: `1px solid ${T.gold}44`,
                          color: T.gold,
                          fontFamily: "monospace",
                          fontWeight: 700,
                        }}
                      >
                        {src}
                      </span>
                    ))}
                  </div>
                )}
              </div>
            ))}

            {loading && (
              <div
                style={{
                  color: T.muted,
                  fontSize: 12,
                  display: "flex",
                  alignItems: "center",
                  gap: 8,
                }}
              >
                <span
                  style={{
                    display: "inline-block",
                    animation: "ai-spin 1s linear infinite",
                  }}
                >
                  ⏳
                </span>
                Thinking…
              </div>
            )}

            {error && (
              <div
                style={{
                  color: "#e05a5a",
                  fontSize: 12,
                  padding: "8px 12px",
                  background: "#18060644",
                  borderRadius: 8,
                  border: "1px solid #e05a5a33",
                }}
              >
                {error}
              </div>
            )}

            <div ref={bottomRef} />
          </div>

          {/* Input bar */}
          <form
            onSubmit={handleSubmit}
            style={{
              borderTop: `1px solid ${T.border}`,
              padding: "9px 12px",
              display: "flex",
              gap: 8,
              flexShrink: 0,
              background: T.panel2,
            }}
          >
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about any OE…"
              disabled={loading}
              style={{
                flex: 1,
                background: T.bg,
                border: `1px solid ${T.border}`,
                borderRadius: 8,
                padding: "7px 10px",
                color: T.text,
                fontSize: 12,
                outline: "none",
              }}
            />
            <button
              type="submit"
              disabled={loading || !input.trim()}
              style={{
                background: T.gold,
                border: "none",
                borderRadius: 8,
                padding: "7px 14px",
                color: T.bg,
                fontWeight: 800,
                fontSize: 14,
                cursor: loading || !input.trim() ? "default" : "pointer",
                opacity: loading || !input.trim() ? 0.45 : 1,
                transition: "opacity 0.15s",
              }}
            >
              →
            </button>
          </form>
        </div>
      )}
    </>
  );
}
