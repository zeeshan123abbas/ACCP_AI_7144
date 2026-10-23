# Session 09: Node.js with MongoDB and Integrating AI Capabilities

> Module: Server-side Programming with Node.js · Term 4 (HDSE) · ⏱ ~2 hours

This session connects your Express server to a real database and to an AI service. First you will build CRUD APIs on MongoDB using Mongoose; then you will add AI features through an AI-as-a-Service provider and look at lightweight in-process ML libraries, ethics and privacy.

## 🎯 Learning Objectives

- Connect a Node.js application to MongoDB with Mongoose and environment variables
- Perform and expose CRUD operations on MongoDB as REST APIs
- Explain the role of AI in modern web backends and the AI-as-a-Service (AIaaS) model
- Connect Node.js to an AI API using both REST (`fetch`) and an official SDK
- Apply prompt design, security and response-validation best practices, and know where TensorFlow.js, Brain.js and ml.js fit
- Explain key ethical and privacy considerations for server-side AI

## 📖 Concepts Explained

### Part A - Node.js + MongoDB

**MongoDB** stores data as JSON-like **documents** in **collections**. Node can use the official `mongodb` driver or **Mongoose**, an ODM (Object Document Mapper) that adds schemas, validation and helpful methods.

| SQL term | MongoDB term | Mongoose |
|---|---|---|
| database | database | connection |
| table | collection | Model |
| row | document | document instance |
| column | field | schema path |

Connection string examples:
- Local: `mongodb://127.0.0.1:27017/term4`
- Atlas (cloud): `mongodb+srv://user:pass@cluster0.xxxxx.mongodb.net/term4`

| CRUD | Mongoose method |
|---|---|
| Create | `Model.create(data)` |
| Read | `Model.find(filter)`, `Model.findById(id)` |
| Update | `Model.findByIdAndUpdate(id, data, { new: true, runValidators: true })` |
| Delete | `Model.findByIdAndDelete(id)` |

```mermaid
flowchart LR
  C[Client] -->|HTTP JSON| E[Express route]
  E --> M[Mongoose model + validation]
  M -->|driver| DB[(MongoDB)]
  E -->|optional| AI[AI service]
```

### Part B - AI in web backends

AI turns ordinary backends into smart ones: summarising text, classifying support tickets, generating descriptions, recommendations, semantic search, moderation.

**AI as a Service (AIaaS):** instead of training models yourself, you call a provider's hosted model over HTTPS and pay per use.

| Provider | Strengths | Node.js integration |
|---|---|---|
| OpenAI | strong general LLMs, embeddings, images, speech | REST + official `openai` npm SDK |
| Google Gemini (AI Studio / Vertex AI) | multimodal, Google Cloud integration | REST + `@google/genai` SDK |
| Azure OpenAI / Azure AI services | enterprise security, regional hosting | REST + Azure SDKs |
| Anthropic Claude | long context, careful outputs | REST + `@anthropic-ai/sdk` |
| Hugging Face Inference | thousands of open models | REST + `@huggingface/inference` |

**REST vs SDK:** REST with `fetch` has no dependency and works with any provider; an SDK gives typed helpers, retries and streaming support.

**Lightweight in-process ML** (no external API, runs inside Node):

| Library | Good for |
|---|---|
| TensorFlow.js (`@tensorflow/tfjs-node`) | running/training neural networks, pre-trained models |
| Brain.js | simple neural networks for small classification tasks |
| ml.js | classic ML: regression, k-means, KNN, PCA |

### Best practices

| Area | Practice |
|---|---|
| Prompt design | clear role/instructions, give context, ask for a specific format (e.g. JSON), keep it short |
| Security | keys in env vars, rate-limit endpoints, never pass raw user input as system instructions (prompt injection) |
| Validation | parse and validate AI output (JSON schema / checks) before saving or showing it |
| Reliability | timeouts, retries with backoff, fallbacks when the provider is down |
| Cost | limit tokens, cache answers, use smaller models when possible |

### Ethics and privacy

- **Privacy:** do not send personal or sensitive data (CNIC numbers, health data) unless necessary and permitted; anonymise where possible.
- **Transparency:** tell users when content is AI-generated.
- **Bias and fairness:** AI may reflect biases; review outputs that affect people (grading, hiring).
- **Accuracy:** AI can "hallucinate"; keep a human in the loop for important decisions.
- **Compliance:** follow data-protection laws and the provider's usage policies; check where data is stored.

## 💻 Code Examples

### Example 1: Database connection module

📄 File: [`db.js`](db.js)

```js
import mongoose from "mongoose";

export async function connectDB(uri) {
  mongoose.connection.on("connected", () => console.log("✅ MongoDB connected"));
  mongoose.connection.on("error", (err) => console.error("MongoDB error:", err.message));
  await mongoose.connect(uri);
}
```

**How it works**

- `mongoose.connect` returns a Promise; the server starts only after it resolves (see `app.js`).
- Connection events help you see problems such as wrong passwords or a stopped MongoDB service.

### Example 2: Mongoose model with validation

📄 File: [`models/Product.js`](models/Product.js)

```js
import mongoose from "mongoose";

const productSchema = new mongoose.Schema(
  {
    name: { type: String, required: [true, "Name is required"], trim: true, maxlength: 100 },
    price: { type: Number, required: true, min: [0, "Price cannot be negative"] },
    category: { type: String, enum: ["mobile", "laptop", "accessory"], default: "accessory" },
    description: { type: String, default: "" },
    inStock: { type: Boolean, default: true },
  },
  { timestamps: true } // adds createdAt and updatedAt
);

export default mongoose.model("Product", productSchema);
```

**How it works**

- The schema defines types, required fields, limits and allowed values.
- Mongoose rejects invalid data before it reaches MongoDB.
- The model name `Product` maps to the collection `products`.

### Example 3: CRUD routes

📄 File: [`routes/products.js`](routes/products.js)

```js
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
```

**How it works**

- Each route `await`s a Mongoose call and forwards errors with `next(err)`.
- `isValidObjectId` prevents cast errors from malformed ids.
- `runValidators: true` applies schema rules on updates too.

### Example 4: AI service: REST and SDK versions

📄 File: [`services/ai.js`](services/ai.js)

```js
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
```

**How it works**

- The REST version uses built-in `fetch` with a timeout via `AbortSignal.timeout`.
- The SDK version requests a JSON object and then **validates** the fields before returning them.
- User text is truncated to control cost; the system message is fixed by the server, not the user.

### Example 5: Wiring it all together

📄 File: [`app.js`](app.js)

```js
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
```

**How it works**

- Environment variables configure the database URI, AI key and port.
- Mongoose validation errors return 422; other errors 500.
- The server starts listening only after the database connection succeeds (top-level `await`).

### Example 6: Lightweight ML inside Node with Brain.js

📄 File: [`brain-demo.js`](brain-demo.js)

```js
// Optional: npm install brain.js   then  node brain-demo.js
import brain from "brain.js";

// Predict if a student is "at risk" from [attendance, assignmentsDone] scaled 0..1
const net = new brain.NeuralNetwork({ hiddenLayers: [3] });
net.train([
  { input: [0.95, 0.9], output: [0] },
  { input: [0.85, 0.8], output: [0] },
  { input: [0.5, 0.4], output: [1] },
  { input: [0.3, 0.2], output: [1] },
  { input: [0.7, 0.3], output: [1] },
  { input: [0.9, 0.6], output: [0] },
]);

const risk = net.run([0.55, 0.5])[0];
console.log(`At-risk probability: ${(risk * 100).toFixed(1)}%`);
```

**How it works**

- A tiny neural network learns a pattern from six examples, entirely offline with no API cost.
- Fine for simple experiments; real decisions need much more data and careful evaluation.

### ▶️ How to run

1. Install Node.js 20 LTS or newer and check with `node -v`.
2. Open a terminal in this session folder.
3. If a `package.json` is present, run `npm install` first.
4. Run a file with `node <filename>` (for example `node app.js`).
5. Start MongoDB locally (or create a free Atlas cluster), copy `.env.example` to `.env`, run `npm install` and `npm run dev`.
6. Test: `POST /api/products` with `{"name":"Wireless Earbuds","price":4500,"category":"accessory"}`, then `POST /api/products/<id>/ai-description`.

## 🧪 Lab Practice

1. Connect to local MongoDB and create three products through `POST /api/products`; view them in MongoDB Compass.
2. Send a product with a negative price and confirm the 422 validation error.
3. Add a `?minPrice=&maxPrice=` filter using `$gte` and `$lte`.
4. Add your AI key and generate a description for one product; then call `/api/ai/sentiment` with a positive and a negative review.
5. Write three versions of the description prompt (vague, specific, specific + format) and compare the outputs in a table.

## 📝 Assignment

Build a **Support Ticket API**: a `Ticket` model (title, description, email, status, priority, category). CRUD endpoints with validation, plus `POST /api/tickets/:id/triage` that asks an AI service to return JSON `{ "category": "...", "priority": "low|medium|high", "summary": "..." }`, validates it and saves it to the ticket. Remove the email before sending text to the AI and explain in your README which privacy risks you considered.

## ❓ Quick Quiz

**Q1.** What does Mongoose add on top of the MongoDB driver?

**Q2.** Which option makes `findByIdAndUpdate` return the updated document?

**Q3.** What is AI as a Service (AIaaS)?

**Q4.** Why validate AI responses before saving them?

**Q5.** Name one library for running ML inside Node.js without an external API.

<details>
<summary>Show answers</summary>

1. Schemas, validation, models, middleware and convenient query helpers.
2. `{ new: true }`
3. Using hosted AI models from a provider over an API and paying per use instead of building/hosting models yourself.
4. AI output can be malformed or incorrect; validation prevents bad data and security issues.
5. TensorFlow.js, Brain.js or ml.js.

</details>

## 💼 Interview Questions

**1. What is prompt injection and how do you reduce it?**

> User input that tries to override system instructions. Keep instructions in the system role, treat user text as data, restrict tools/permissions and validate outputs.

**2. When would you choose an SDK over plain REST for an AI provider?**

> When you want built-in retries, streaming helpers, types and less boilerplate; REST is better for minimal dependencies or unsupported languages.

**3. How do you keep MongoDB credentials safe in a Node app?**

> Store the connection string in environment variables or a secret manager, use least-privilege DB users and IP access lists, and never commit .env files.

## ✅ Summary

- Mongoose models give structure and validation to MongoDB documents.
- Express routes expose CRUD operations with proper errors and status codes.
- AIaaS providers add smart features via REST or SDKs.
- Good prompts, validation, timeouts and key protection make AI features reliable.
- Respect privacy, transparency and fairness when using AI on user data.

---

[⬅ Previous](../Session-08-RESTful-and-HTTP-APIs/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-10-Nodejs-in-Action-Cloud-App-with-AI-Recommendations/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
