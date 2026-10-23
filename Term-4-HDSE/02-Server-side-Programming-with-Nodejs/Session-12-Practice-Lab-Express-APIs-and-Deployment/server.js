import "dotenv/config";
import mongoose from "mongoose";
import { app } from "./app.js";

app.get("/health", (req, res) => res.json({ ok: true }));
await mongoose.connect(process.env.MONGODB_URI || "mongodb://127.0.0.1:27017/events");
app.listen(process.env.PORT || 3000, () => console.log("Events API running"));
