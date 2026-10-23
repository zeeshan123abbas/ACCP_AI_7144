import { useEffect, useRef, useState } from "react";

export default function ChatBot() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hi! Ask me anything about React." },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const endRef = useRef(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  async function send(e) {
    e.preventDefault();
    const text = input.trim();
    if (!text || loading) return;
    const next = [...messages, { role: "user", content: text }];
    setMessages(next);
    setInput("");
    setLoading(true);
    setError("");
    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: next }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Request failed");
      setMessages((prev) => [...prev, { role: "assistant", content: data.reply }]);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section style={{ maxWidth: 520, border: "1px solid #ddd", borderRadius: 12, padding: 12 }}>
      <h2>🤖 React Tutor</h2>
      <div style={{ height: 300, overflowY: "auto", background: "#f8f9fa", padding: 8 }}>
        {messages.map((m, i) => (
          <p key={i} style={{ textAlign: m.role === "user" ? "right" : "left" }}>
            <span style={{ display: "inline-block", padding: "6px 10px", borderRadius: 10,
              background: m.role === "user" ? "#0d6efd" : "#e9ecef", color: m.role === "user" ? "white" : "black" }}>
              {m.content}
            </span>
          </p>
        ))}
        {loading && <p><em>Tutor is typing...</em></p>}
        <div ref={endRef} />
      </div>
      {error && <p style={{ color: "crimson" }}>{error}</p>}
      <form onSubmit={send} style={{ display: "flex", gap: 8, marginTop: 8 }}>
        <input style={{ flex: 1 }} value={input} onChange={(e) => setInput(e.target.value)} maxLength={1000} placeholder="Type a question" />
        <button disabled={loading}>Send</button>
      </form>
      <small>AI answers can be wrong. Verify important information.</small>
    </section>
  );
}
