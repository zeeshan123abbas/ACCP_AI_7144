function keywordRecommend(courses, interests) {
  const words = interests.toLowerCase().split(/[\s,]+/).filter(Boolean);
  return courses
    .map((c) => ({
      course: c,
      score: c.tags.filter((t) => words.includes(t)).length,
      reason: "Matched your keywords",
    }))
    .filter((r) => r.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 3);
}

async function aiRecommend(courses, interests) {
  const catalogue = courses.map((c) => ({ id: String(c._id), title: c.title, tags: c.tags }));
  const res = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
    body: JSON.stringify({
      model: process.env.AI_MODEL || "gpt-4o-mini",
      response_format: { type: "json_object" },
      messages: [
        { role: "system", content: 'Recommend up to 3 courses from the catalogue. Reply JSON: {"picks":[{"id":"...","reason":"..."}]}. Use only ids from the catalogue.' },
        { role: "user", content: `Interests: ${interests.slice(0, 300)}\nCatalogue: ${JSON.stringify(catalogue)}` },
      ],
    }),
    signal: AbortSignal.timeout(15000),
  });
  if (!res.ok) throw new Error(`AI error ${res.status}`);
  const { picks } = JSON.parse((await res.json()).choices[0].message.content);
  const byId = new Map(catalogue.map((c, i) => [c.id, courses[i]]));
  const valid = (picks || []).filter((p) => byId.has(p.id)).slice(0, 3);
  if (valid.length === 0) throw new Error("AI returned no valid ids");
  return valid.map((p) => ({ course: byId.get(p.id), reason: p.reason }));
}

export async function recommend(courses, interests) {
  if (process.env.OPENAI_API_KEY) {
    try {
      return { source: "AI", results: await aiRecommend(courses, interests) };
    } catch (err) {
      console.warn("AI failed, using fallback:", err.message);
    }
  }
  return { source: "keywords", results: keywordRecommend(courses, interests) };
}
