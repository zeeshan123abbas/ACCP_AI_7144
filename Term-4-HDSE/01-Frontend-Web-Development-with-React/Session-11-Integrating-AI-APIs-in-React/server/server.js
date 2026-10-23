// Node 20+. Run: cd server && npm init -y && npm install express dotenv && node server.js
import "dotenv/config";
import express from "express";

const app = express();
app.use(express.json({ limit: "20kb" }));

app.post("/api/chat", async (req, res) => {
  const { messages } = req.body;
  if (!Array.isArray(messages) || messages.length === 0) {
    return res.status(400).json({ error: "messages array required" });
  }
  const trimmed = messages.slice(-10).map((m) => ({
    role: m.role === "assistant" ? "assistant" : "user",
    content: String(m.content).slice(0, 1000),
  }));

  try {
    const r = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
      },
      body: JSON.stringify({
        model: process.env.AI_MODEL || "gpt-4o-mini",
        messages: [{ role: "system", content: "You are a friendly React tutor. Answer briefly." }, ...trimmed],
      }),
    });
    if (!r.ok) return res.status(r.status).json({ error: `AI provider error ${r.status}` });
    const data = await r.json();
    res.json({ reply: data.choices[0].message.content });
  } catch (err) {
    res.status(500).json({ error: "Could not reach AI provider" });
  }
});

app.listen(5000, () => console.log("AI proxy on http://localhost:5000"));
