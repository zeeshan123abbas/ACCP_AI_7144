import express from "express";
import fs from "node:fs";
import { config } from "./config.js";
import { sendWelcomeEmail } from "./services/mailer.js";
import uploadRouter from "./routes/upload.js";

fs.mkdirSync("uploads", { recursive: true });
const app = express();
app.use(express.urlencoded({ extended: false })); // parse form posts

app.get("/", (req, res) => {
  res.send(`
    <h2>Register</h2>
    <form method="POST" action="/register">
      <input name="name" placeholder="Name" required>
      <input name="email" type="email" placeholder="Email" required>
      <button>Register</button>
    </form>
    <h2>Upload document</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
      <input type="file" name="document" required>
      <button>Upload</button>
    </form>`);
});

app.post("/register", async (req, res, next) => {
  try {
    const { name, email } = req.body;
    if (!name || !email) return res.status(400).send("Name and email required");
    const preview = await sendWelcomeEmail(email, name);
    res.send(`Email sent. Preview: <a href="${preview}" target="_blank">${preview}</a>`);
  } catch (err) {
    next(err);
  }
});

app.use(uploadRouter);

app.use((err, req, res, next) => {
  res.status(400).json({ error: err.message });
});

app.listen(config.port, () => console.log(`http://localhost:${config.port}`));
