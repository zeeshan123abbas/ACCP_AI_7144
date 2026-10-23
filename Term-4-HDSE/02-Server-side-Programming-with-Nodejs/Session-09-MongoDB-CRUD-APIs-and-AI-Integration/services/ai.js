import OpenAI from "openai";

const MODEL = process.env.AI_MODEL || "gpt-4o-mini";

// Option 1: plain REST with fetch (works for any provider with an HTTP API)
export async function generateDescriptionREST(product) {
  const res = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
    body: JSON.stringify({
      model: MODEL,
      max_tokens: 120,
      messages: [
        { role: "system", content: "You write short, honest e-commerce product descriptions." },
        { role: "user", content: `Product: ${product.name}. Category: ${product.category}. Max 40 words.` },
      ],
    }),
    signal: AbortSignal.timeout(15000), // never wait forever
  });
  if (!res.ok) throw new Error(`AI request failed with ${res.status}`);
  const data = await res.json();
  return data.choices[0].message.content.trim();
}

// Option 2: official SDK, asking for structured JSON
const client = process.env.OPENAI_API_KEY ? new OpenAI() : null; // reads OPENAI_API_KEY

export async function classifyReview(text) {
  if (!client) throw new Error("OPENAI_API_KEY not set");
  const completion = await client.chat.completions.create({
    model: MODEL,
    response_format: { type: "json_object" },
    messages: [
      { role: "system", content: 'Classify the review. Reply only with JSON: {"sentiment":"positive|neutral|negative","score":0-1}' },
      { role: "user", content: text.slice(0, 2000) },
    ],
  });
  const parsed = JSON.parse(completion.choices[0].message.content);
  // validate the AI output before trusting it
  if (!["positive", "neutral", "negative"].includes(parsed.sentiment)) throw new Error("Unexpected AI output");
  return { sentiment: parsed.sentiment, score: Math.min(1, Math.max(0, Number(parsed.score) || 0)) };
}
