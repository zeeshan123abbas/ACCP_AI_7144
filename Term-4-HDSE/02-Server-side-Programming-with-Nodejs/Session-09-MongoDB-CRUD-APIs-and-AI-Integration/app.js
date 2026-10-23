import "dotenv/config";
import express from "express";
import { connectDB } from "./db.js";
import productRoutes from "./routes/products.js";
import Product from "./models/Product.js";
import { generateDescriptionREST, classifyReview } from "./services/ai.js";

const app = express();
app.use(express.json({ limit: "10kb" }));

app.use("/api/products", productRoutes);

// AI: generate and save a description for an existing product
app.post("/api/products/:id/ai-description", async (req, res, next) => {
  try {
    const product = await Product.findById(req.params.id);
    if (!product) return res.status(404).json({ error: "Not found" });
    product.description = await generateDescriptionREST(product);
    await product.save();
    res.json(product);
  } catch (err) { next(err); }
});

// AI: classify a review sent in the body
app.post("/api/ai/sentiment", async (req, res, next) => {
  try {
    if (!req.body.text) return res.status(400).json({ error: "text is required" });
    res.json(await classifyReview(req.body.text));
  } catch (err) { next(err); }
});

app.use((err, req, res, next) => {
  const status = err.name === "ValidationError" ? 422 : 500;
  res.status(status).json({ error: err.message });
});

await connectDB(process.env.MONGODB_URI || "mongodb://127.0.0.1:27017/term4");
app.listen(process.env.PORT || 3000, () => console.log("API ready on http://localhost:3000"));
