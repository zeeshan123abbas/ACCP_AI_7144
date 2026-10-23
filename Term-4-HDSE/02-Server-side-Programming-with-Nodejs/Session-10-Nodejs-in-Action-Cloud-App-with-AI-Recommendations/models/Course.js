import mongoose from "mongoose";

const courseSchema = new mongoose.Schema({
  title: { type: String, required: true, trim: true },
  level: { type: String, enum: ["beginner", "intermediate", "advanced"], default: "beginner" },
  tags: { type: [String], default: [] }, // e.g. ["react", "frontend"]
});

export default mongoose.model("Course", courseSchema);
