import express from "express";

const app = express();
app.use(express.json());

let nextId = 4;
let books = [
  { id: 1, title: "Clean Code", author: "Robert Martin", year: 2008, available: true },
  { id: 2, title: "Eloquent JavaScript", author: "Marijn Haverbeke", year: 2018, available: false },
  { id: 3, title: "You Don't Know JS", author: "Kyle Simpson", year: 2015, available: true },
];

const findBook = (req, res, next) => {
  req.book = books.find((b) => b.id === Number(req.params.id));
  if (!req.book) return res.status(404).json({ error: "Book not found" });
  next();
};

// GET /api/v1/books?available=true&sort=-year&page=1&limit=2
app.get("/api/v1/books", (req, res) => {
  let result = [...books];
  if (req.query.available) result = result.filter((b) => String(b.available) === req.query.available);
  if (req.query.sort) {
    const field = req.query.sort.replace("-", "");
    const dir = req.query.sort.startsWith("-") ? -1 : 1;
    result.sort((a, b) => (a[field] > b[field] ? dir : -dir));
  }
  const page = Math.max(1, Number(req.query.page) || 1);
  const limit = Math.min(50, Number(req.query.limit) || 10);
  const data = result.slice((page - 1) * limit, page * limit);
  res.json({ page, limit, total: result.length, data });
});

app.get("/api/v1/books/:id", findBook, (req, res) => res.json(req.book));

app.post("/api/v1/books", (req, res) => {
  const { title, author, year } = req.body;
  if (!title || !author) return res.status(422).json({ error: "title and author are required" });
  const book = { id: nextId++, title, author, year: Number(year) || null, available: true };
  books.push(book);
  res.status(201).location(`/api/v1/books/${book.id}`).json(book);
});

app.put("/api/v1/books/:id", findBook, (req, res) => {
  const { title, author, year, available } = req.body;
  if (!title || !author) return res.status(422).json({ error: "PUT needs the full resource" });
  Object.assign(req.book, { title, author, year, available: Boolean(available) });
  res.json(req.book);
});

app.patch("/api/v1/books/:id", findBook, (req, res) => {
  const allowed = ["title", "author", "year", "available"];
  for (const key of allowed) if (key in req.body) req.book[key] = req.body[key];
  res.json(req.book);
});

app.delete("/api/v1/books/:id", findBook, (req, res) => {
  books = books.filter((b) => b !== req.book);
  res.status(204).end();
});

// HTTP/RPC-style action endpoint (not pure REST) for comparison
app.post("/api/v1/books/:id/borrow", findBook, (req, res) => {
  if (!req.book.available) return res.status(409).json({ error: "Already borrowed" });
  req.book.available = false;
  res.json({ message: `You borrowed "${req.book.title}"` });
});

app.listen(3000, () => console.log("Books API on http://localhost:3000/api/v1/books"));
