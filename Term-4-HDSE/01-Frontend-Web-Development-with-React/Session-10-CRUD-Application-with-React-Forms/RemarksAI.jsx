import { useState } from "react";

// Expects a backend route POST /api/improve -> { text } (built in Session 11)
export default function RemarksAI() {
  const [remarks, setRemarks] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    const text = remarks.trim().slice(0, 500); // validate + limit length
    if (!text) return;
    setLoading(true);
    try {
      const res = await fetch("/api/improve", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      const data = await res.json();
      setResult(data.text ?? "No response");
    } catch {
      setResult("AI service not available. Start the proxy from Session 11.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Improve teacher remarks with AI</h2>
      <textarea rows={3} value={remarks} onChange={(e) => setRemarks(e.target.value)} maxLength={500} />
      <br />
      <button disabled={loading}>{loading ? "Improving..." : "Improve"}</button>
      {result && <p><strong>AI:</strong> {result}</p>}
    </form>
  );
}
