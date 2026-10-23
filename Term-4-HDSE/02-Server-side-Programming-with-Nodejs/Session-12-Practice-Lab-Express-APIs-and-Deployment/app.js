import express from "express";
import mongoose from "mongoose";

const eventSchema = new mongoose.Schema({
  title: { type: String, required: true, trim: true },
  date: {
    type: Date,
    required: true,
    validate: { validator: (d) => d > new Date(), message: "Date must be in the future" },
  },
  capacity: { type: Number, required: true, min: 1 },
  booked: { type: Number, default: 0, min: 0 },
});
export const Event = mongoose.models.Event || mongoose.model("Event", eventSchema);

export const app = express();
app.use(express.json());
const wrap = (fn) => (req, res, next) => fn(req, res, next).catch(next);

app.get("/api/events", wrap(async (req, res) => {
  const filter = req.query.upcoming === "true" ? { date: { $gte: new Date() } } : {};
  res.json(await Event.find(filter).sort({ date: 1 }));
}));

app.post("/api/events", wrap(async (req, res) => {
  res.status(201).json(await Event.create(req.body));
}));

app.post("/api/events/:id/book", wrap(async (req, res) => {
  const updated = await Event.findOneAndUpdate(
    { _id: req.params.id, $expr: { $lt: ["$booked", "$capacity"] } },
    { $inc: { booked: 1 } },
    { new: true }
  );
  if (updated) return res.json({ message: "Seat booked", seatsLeft: updated.capacity - updated.booked });
  const exists = await Event.exists({ _id: req.params.id });
  res.status(exists ? 409 : 404).json({ error: exists ? "Event is full" : "Event not found" });
}));

app.post("/api/events/:id/promo", wrap(async (req, res) => {
  const ev = await Event.findById(req.params.id);
  if (!ev) return res.status(404).json({ error: "Event not found" });
  let text = `Join us for ${ev.title} on ${ev.date.toDateString()}! Only ${ev.capacity - ev.booked} seats left.`;
  if (process.env.OPENAI_API_KEY) {
    try {
      const r = await fetch("https://api.openai.com/v1/chat/completions", {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
        body: JSON.stringify({
          model: process.env.AI_MODEL || "gpt-4o-mini",
          max_tokens: 80,
          messages: [{ role: "user", content: `Write a 2-sentence promo for: ${text}` }],
        }),
        signal: AbortSignal.timeout(10000),
      });
      if (r.ok) text = (await r.json()).choices[0].message.content.trim();
    } catch { /* keep the template text */ }
  }
  res.json({ promo: text });
}));

app.delete("/api/events/:id", wrap(async (req, res) => {
  const ev = await Event.findByIdAndDelete(req.params.id);
  ev ? res.status(204).end() : res.status(404).json({ error: "Event not found" });
}));

app.use((err, req, res, next) => {
  const status = ["ValidationError", "CastError"].includes(err.name) ? 422 : 500;
  res.status(status).json({ error: err.message });
});
