import { useState, useEffect, useRef } from "react";

const ENDPOINT = "https://tbptllgcjtiiqspxqcde.supabase.co/functions/v1/ai-assistant";
const ANON_KEY =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRicHRsbGdjanRpaXFzcHhxY2RlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY2NjkzNjAsImV4cCI6MjA5MjI0NTM2MH0.4CPgNp6ytVNRmTU0FJbu2io94QJmsAow5im-vGtoRAU";

// trigger = { code: string|null, id: number }
// id increment = new auto-ask; allows same code to re-trigger
export default function AIAssistantWidget({ T, open, onOpen, onClose, trigger }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const bottomRef = useRef(null);

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

  const btnStyle = {
    position: "fixed",
    bottom: 216,
    right: 20,
    zIndex: 9996,
    width: 48,
    height: 48,
    borderRadius: 24,
    background: `linear-gradient(135deg, ${T.gold}, #f0d070)`,
    border: "none",
    color: T.bg,
    fontSize: 18,
    fontWeight: 900,
    cursor: "pointer",
    boxShadow: `0 4px 16px rgba(201,168,76,0.5)`,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    lineHeight: 1,
  };

  return (
    <>
      {/* Floating toggle button */}
      <button
        onClick={open ? onClose : onOpen}
        title={open ? "Close AI assistant" : "Ask AI about SHCO Full requirements"}
        style={btnStyle}
        aria-label="AI assistant"
      >
        {open ? "✕" : "AI"}
      </button>

      {/* Chat panel — slide up above the button */}
      {open && (
        <div
          style={{
            position: "fixed",
            bottom: 276,
            right: 20,
            zIndex: 9995,
            width: 360,
            maxHeight: 480,
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
                fontSize: 13,
                fontWeight: 900,
                color: T.bg,
                flexShrink: 0,
              }}
            >
              AI
            </span>
            <div style={{ flex: 1 }}>
              <div style={{ color: T.gold, fontWeight: 700, fontSize: 13 }}>
                AccredReady AI
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
              flex: 1,
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
                  marginTop: 48,
                  lineHeight: 1.8,
                }}
              >
                Ask anything about SHCO Full requirements.
                <br />
                <span style={{ color: T.gold, fontStyle: "italic" }}>
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
