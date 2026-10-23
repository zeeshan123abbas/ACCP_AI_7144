import { User, Task } from "./models.js";
import { signToken } from "./auth.js";

export async function register(req, res) {
  const { name, email, password } = req.body;
  if (!name || !email || !password || password.length < 8) {
    return res.status(422).json({ error: "name, email and a password of 8+ characters are required" });
  }
  if (await User.exists({ email })) return res.status(409).json({ error: "Email already registered" });
  const user = await User.create({ name, email, password });
  res.status(201).json({ token: signToken(user), user: { id: user._id, name, email: user.email } });
}

export async function login(req, res) {
  const user = await User.findOne({ email: (req.body.email || "").toLowerCase() }).select("+password");
  if (!user || !(await user.checkPassword(req.body.password || ""))) {
    return res.status(401).json({ error: "Invalid email or password" });
  }
  res.json({ token: signToken(user) });
}

export async function listTasks(req, res) {
  const filter = { owner: req.user.id };
  if (req.query.done) filter.done = req.query.done === "true";
  res.json(await Task.find(filter).sort({ createdAt: -1 }));
}

export async function createTask(req, res) {
  const task = await Task.create({ title: req.body.title, dueDate: req.body.dueDate, owner: req.user.id });
  res.status(201).json(task);
}

export async function updateTask(req, res) {
  const { title, done, dueDate } = req.body;
  const task = await Task.findOneAndUpdate(
    { _id: req.params.id, owner: req.user.id },
    { title, done, dueDate },
    { new: true, runValidators: true } // Mongoose ignores undefined fields
  );
  task ? res.json(task) : res.status(404).json({ error: "Task not found" });
}

export async function deleteTask(req, res) {
  const task = await Task.findOneAndDelete({ _id: req.params.id, owner: req.user.id });
  task ? res.status(204).end() : res.status(404).json({ error: "Task not found" });
}
