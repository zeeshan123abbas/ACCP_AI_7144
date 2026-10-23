// chatbot-proxy.js — Node 20+, no packages needed
// Run: set OPENAI_API_KEY in your environment, then: node chatbot-proxy.js
import http from "node:http";

const SYSTEM_PROMPT =
  "You are a helpful assistant for a computer institute in Karachi. " +
  "Only answer questions about courses, timings and admissions. Keep answers short.";

const server = http.createServer(async (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "http://localhost:5500"); // your front-end only
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.end();
  if (req.method !== "POST" || req.url !== "/chat") {
    res.writeHead(404);
    return res.end();
  }

  let body = "";
  for await (const chunk of req) body += chunk;
  const { message } = JSON.parse(body || "{}");
  if (!message || message.length > 500) {
    res.writeHead(400, { "Content-Type": "application/json" });
    return res.end(JSON.stringify({ error: "Message required (max 500 chars)" }));
  }

  try {
    const aiRes = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${process.env.OPENAI_API_KEY}` // secret stays on the server
      },
      body: JSON.stringify({
        model: "gpt-4o-mini",
        messages: [
          { role: "system", content: SYSTEM_PROMPT },
          { role: "user", content: message }
        ],
        max_tokens: 200
      })
    });
    const data = await aiRes.json();
    const reply = data.choices?.[0]?.message?.content ?? "Sorry, I could not answer that.";
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ reply }));
  } catch (err) {
    res.writeHead(502, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "AI service unavailable" }));
  }
});

server.listen(3000, () => console.log("Chat proxy on http://localhost:3000/chat"));
