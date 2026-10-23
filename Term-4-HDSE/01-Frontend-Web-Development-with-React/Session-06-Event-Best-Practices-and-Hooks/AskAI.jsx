import { useCallback, useEffect, useState } from "react";
import { useDebounce } from "./useDebounce.js";

// Fake AI service so the demo runs without a key. Replace with fetch("/api/ai") later.
function fakeAI(prompt) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (prompt.toLowerCase().includes("error")) reject(new Error("AI service unavailable"));
      else resolve(`Suggestion for "${prompt}": try breaking it into smaller components.`);
    }, 900);
  });
}

export default function AskAI() {
  const [prompt, setPrompt] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const debouncedPrompt = useDebounce(prompt, 600);

  const ask = useCallback(async (text) => {
    if (text.trim().length < 3) return;
    setLoading(true);
    setError("");
    try {
      setAnswer(await fakeAI(text));
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  // live suggestion: fires only after the user stops typing
  useEffect(() => {
    ask(debouncedPrompt);
  }, [debouncedPrompt, ask]);

  return (
    <section>
      <h2>Ask the AI helper</h2>
      <input value={prompt} onChange={(e) => setPrompt(e.target.value)} placeholder="Describe your UI problem" />
      <button onClick={() => ask(prompt)} disabled={loading}>
        {loading ? "Thinking..." : "Ask now"}
      </button>
      {error && <p style={{ color: "crimson" }}>{error}</p>}
      {answer && !error && <blockquote>{answer}</blockquote>}
    </section>
  );
}
