import "dotenv/config";
import express from "express";
import mongoose from "mongoose";
import Course from "./models/Course.js";
import { recommend } from "./services/recommend.js";

const app = express();
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: false }));

app.get("/health", (req, res) => res.json({ ok: true, db: mongoose.connection.readyState === 1 }));

app.get("/", async (req, res) => {
  const courses = await Course.find().sort({ title: 1 });
  res.render("index", { courses });
});

app.post("/courses", async (req, res) => {
  const { title, level, tags } = req.body;
  if (title) {
    await Course.create({ title, level, tags: (tags || "").toLowerCase().split(",").map((t) => t.trim()).filter(Boolean) });
  }
  res.redirect("/");
});

app.post("/recommend", async (req, res) => {
  const interests = (req.body.interests || "").trim();
  const courses = await Course.find();
  const { source, results } = await recommend(courses, interests);
  res.render("recommend", { interests, source, results });
});

const PORT = process.env.PORT || 3000;
await mongoose.connect(process.env.MONGODB_URI);
console.log("Connected to MongoDB");
app.listen(PORT, () => console.log(`Running on http://localhost:${PORT}`));
