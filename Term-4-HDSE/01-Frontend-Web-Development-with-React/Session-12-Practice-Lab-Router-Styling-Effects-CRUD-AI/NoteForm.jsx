import { useState } from "react";
import styles from "./Notes.module.css";

export default function NoteForm({ initial = { title: "", body: "" }, onSave }) {
  const [form, setForm] = useState(initial);
  const [error, setError] = useState("");
  const [aiText, setAiText] = useState("");
  const [loading, setLoading] = useState(false);

  const change = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  function submit(e) {
    e.preventDefault();
    if (!form.title.trim()) return setError("Title is required");
    onSave({ ...form, title: form.title.trim() });
  }

  async function summarise() {
    setLoading(true);
    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: [{ role: "user", content: `Summarise in 2 lines: ${form.body}` }] }),
      });
      const data = await res.json();
      setAiText(res.ok ? data.reply : data.error);
    } catch {
      setAiText("AI proxy not running - start it from Session 11.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={submit} className={styles.form}>
      <input name="title" value={form.title} onChange={change} placeholder="Title" />
      {error && <small className={styles.error}>{error}</small>}
      <textarea name="body" rows={6} value={form.body} onChange={change} placeholder="Write your note" />
      <div>
        <button type="submit">Save</button>{" "}
        <button type="button" onClick={summarise} disabled={loading || form.body.length < 20}>
          {loading ? "Summarising..." : "✨ AI summary"}
        </button>
      </div>
      {aiText && <p className={styles.ai}>{aiText}</p>}
    </form>
  );
}
