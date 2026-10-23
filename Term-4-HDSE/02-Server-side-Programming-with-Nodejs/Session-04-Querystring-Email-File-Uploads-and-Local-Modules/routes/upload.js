import { Router } from "express";
import multer from "multer";
import path from "node:path";
import crypto from "node:crypto";

const storage = multer.diskStorage({
  destination: "uploads/",
  filename: (req, file, cb) => {
    const ext = path.extname(file.originalname).toLowerCase();
    cb(null, `${crypto.randomUUID()}${ext}`); // random safe name
  },
});

const upload = multer({
  storage,
  limits: { fileSize: 2 * 1024 * 1024 }, // 2 MB
  fileFilter: (req, file, cb) => {
    const ok = ["image/png", "image/jpeg", "application/pdf"].includes(file.mimetype);
    cb(ok ? null : new Error("Only PNG, JPG or PDF allowed"), ok);
  },
});

const router = Router();

router.post("/upload", upload.single("document"), (req, res) => {
  if (!req.file) return res.status(400).json({ error: "No file received" });
  res.json({ saved: req.file.filename, sizeKB: Math.round(req.file.size / 1024) });
});

export default router;
