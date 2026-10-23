import { Router } from "express";
import mongoose from "mongoose";
import Product from "../models/Product.js";

const router = Router();
const validId = (req, res, next) =>
  mongoose.isValidObjectId(req.params.id) ? next() : res.status(400).json({ error: "Invalid id" });

router.get("/", async (req, res, next) => {
  try {
    const filter = req.query.category ? { category: req.query.category } : {};
    res.json(await Product.find(filter).sort({ createdAt: -1 }).limit(50));
  } catch (err) { next(err); }
});

router.get("/:id", validId, async (req, res, next) => {
  try {
    const p = await Product.findById(req.params.id);
    p ? res.json(p) : res.status(404).json({ error: "Not found" });
  } catch (err) { next(err); }
});

router.post("/", async (req, res, next) => {
  try { res.status(201).json(await Product.create(req.body)); }
  catch (err) { next(err); }
});

router.patch("/:id", validId, async (req, res, next) => {
  try {
    const p = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
    p ? res.json(p) : res.status(404).json({ error: "Not found" });
  } catch (err) { next(err); }
});

router.delete("/:id", validId, async (req, res, next) => {
  try {
    const p = await Product.findByIdAndDelete(req.params.id);
    p ? res.status(204).end() : res.status(404).json({ error: "Not found" });
  } catch (err) { next(err); }
});

export default router;
