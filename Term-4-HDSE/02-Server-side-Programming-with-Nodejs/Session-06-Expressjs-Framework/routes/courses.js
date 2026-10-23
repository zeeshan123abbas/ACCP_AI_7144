import { Router } from "express";

const router = Router();
let courses = [
  { id: 1, title: "React", sessions: 12 },
  { id: 2, title: "Node.js", sessions: 12 },
  { id: 3, title: "MongoDB", sessions: 16 },
];

function validateCourse(req, res, next) {
  const { title, sessions } = req.body;
  if (!title || !Number.isInteger(sessions) || sessions < 1) {
    return res.status(400).json({ error: "title (string) and sessions (positive integer) are required" });
  }
  next();
}

// GET /api/courses?minSessions=13
router.get("/", (req, res) => {
  const min = Number(req.query.minSessions) || 0;
  res.json(courses.filter((c) => c.sessions >= min));
});

// GET /api/courses/2
router.get("/:id", (req, res, next) => {
  const course = courses.find((c) => c.id === Number(req.params.id));
  if (!course) {
    const err = new Error("Course not found");
    err.status = 404;
    return next(err);
  }
  res.json(course);
});

// POST /api/courses
router.post("/", validateCourse, (req, res) => {
  const course = { id: Date.now(), title: req.body.title, sessions: req.body.sessions };
  courses.push(course);
  res.status(201).json(course);
});

// DELETE /api/courses/2
router.delete("/:id", (req, res) => {
  const before = courses.length;
  courses = courses.filter((c) => c.id !== Number(req.params.id));
  res.status(before === courses.length ? 404 : 204).end();
});

export default router;
