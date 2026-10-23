import express from "express";
import coursesRouter from "./routes/courses.js";

const app = express();

// 1. Built-in middleware
app.use(express.json());                 // parse JSON bodies into req.body
app.use(express.static("public"));       // serve files from /public

// 2. Custom middleware: request logger with timing
app.use((req, res, next) => {
  const start = Date.now();
  res.on("finish", () => console.log(`${req.method} ${req.originalUrl} ${res.statusCode} ${Date.now() - start}ms`));
  next();
});

// 3. Routes
app.get("/api/health", (req, res) => res.json({ status: "ok", time: new Date() }));
app.use("/api/courses", coursesRouter);

// 4. 404 handler (no route matched)
app.use((req, res) => res.status(404).json({ error: `Cannot ${req.method} ${req.originalUrl}` }));

// 5. Error handler (four parameters)
app.use((err, req, res, next) => {
  console.error(err);
  res.status(err.status || 500).json({ error: err.message || "Server error" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Express running on http://localhost:${PORT}`));
