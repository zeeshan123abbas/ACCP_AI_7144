import "dotenv/config";
import express from "express";
import mongoose from "mongoose";
import helmet from "helmet";
import cors from "cors";
import { requireAuth } from "./auth.js";
import * as c from "./controllers.js";

const app = express();
app.use(helmet());
app.use(cors({ origin: process.env.CLIENT_ORIGIN || "*" }));
app.use(express.json({ limit: "10kb" }));

// wrap async controllers so errors reach the error handler (Express 4)
const wrap = (fn) => (req, res, next) => fn(req, res, next).catch(next);

app.get("/health", (req, res) => res.json({ ok: true }));
app.post("/api/auth/register", wrap(c.register));
app.post("/api/auth/login", wrap(c.login));

const tasks = express.Router();
tasks.use(requireAuth);
tasks.get("/", wrap(c.listTasks));
tasks.post("/", wrap(c.createTask));
tasks.patch("/:id", wrap(c.updateTask));
tasks.delete("/:id", wrap(c.deleteTask));
app.use("/api/tasks", tasks);

app.use((req, res) => res.status(404).json({ error: "Not found" }));
app.use((err, req, res, next) => {
  if (err.name === "ValidationError" || err.name === "CastError") return res.status(422).json({ error: err.message });
  console.error(err);
  res.status(500).json({ error: "Something went wrong" });
});

await mongoose.connect(process.env.MONGODB_URI || "mongodb://127.0.0.1:27017/taskmanager");
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Task API on http://localhost:${PORT}`));
