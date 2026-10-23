# Session 08: RESTful and HTTP APIs

> Module: Server-side Programming with Node.js · Term 4 (HDSE) · ⏱ ~2 hours

APIs are how your React frontend, mobile apps and other services talk to your Node.js backend. This session explains what an API is, the common API types, and the difference between a strict RESTful API and a simple HTTP API, then builds a well-designed REST API with Express.

## 🎯 Learning Objectives

- Describe an API and its purpose
- List common API types used with Node.js (REST, HTTP/RPC, GraphQL, WebSocket)
- Explain the features of RESTful and HTTP APIs and use them to manage data
- Identify the advantages and disadvantages of RESTful and HTTP APIs
- Design REST endpoints with correct methods, status codes, filtering and pagination

## 📖 Concepts Explained

### 1. What is an API?

An **Application Programming Interface** is a contract that lets one program use another program's features without knowing its internals.

> **Analogy:** a restaurant menu. You (the client) order from the menu (the API) and the kitchen (the server) prepares it. You never enter the kitchen.

### 2. Common API types in Node.js

| Type | Style | Typical use |
|---|---|---|
| **REST** | resources + HTTP methods (`GET /books/5`) | most web/mobile backends |
| **HTTP / RPC-style** | action endpoints (`POST /getBook`, `POST /sendInvoice`) | internal services, quick tools |
| **GraphQL** | single endpoint, client chooses fields | complex UIs needing flexible data |
| **WebSocket** | persistent two-way connection | chat, live scores, notifications |
| **Webhooks** | server calls *your* URL on events | payment confirmations, GitHub events |

### 3. RESTful API principles

REST (Representational State Transfer) is an architectural style:

- **Resources** identified by nouns in URLs: `/students`, `/students/7/courses`
- **HTTP methods** express the action
- **Stateless** - each request carries everything needed (e.g. a token); the server keeps no session per client
- **Uniform representations** - usually JSON
- **Proper status codes** and, ideally, cacheable responses

| Method | URL | Action | Success code |
|---|---|---|---|
| GET | `/students` | list | 200 |
| GET | `/students/7` | read one | 200 (404 if missing) |
| POST | `/students` | create | 201 + `Location` header |
| PUT | `/students/7` | replace entirely | 200 |
| PATCH | `/students/7` | update some fields | 200 |
| DELETE | `/students/7` | delete | 204 |

Status code families: **2xx** success, **3xx** redirect, **4xx** client error (400 bad input, 401 not authenticated, 403 forbidden, 404 not found, 409 conflict, 422 validation), **5xx** server error.

### 4. HTTP APIs (non-REST)

An "HTTP API" here means any API over HTTP that does not follow REST rules strictly: verbs in URLs, mostly `POST`, custom response shapes. It is quick to build but less predictable.

### 5. Comparison

| | RESTful API | HTTP (RPC-style) API |
|---|---|---|
| URL design | nouns: `/orders/5` | verbs: `/cancelOrder` |
| Methods | GET/POST/PUT/PATCH/DELETE | mostly GET/POST |
| Predictability | high; conventions are well known | varies by team |
| Caching | GET responses cache naturally | harder |
| Fits | CRUD over resources | actions that are not CRUD (e.g. `/reports/generate`) |
| Drawbacks | over/under-fetching, many endpoints, strict rules | inconsistent, harder to document and scale |

In practice many good APIs are "mostly REST" with a few action endpoints like `POST /orders/5/cancel`.

### 6. Good API design checklist

- Plural nouns, lowercase, hyphens: `/course-batches`
- Filtering, sorting, pagination via query: `?city=Karachi&sort=-createdAt&page=2&limit=10`
- Consistent error format: `{ "error": "message", "details": [...] }`
- Version your API: `/api/v1/...`
- Document it (OpenAPI/Swagger) and test it (Postman)

## 💻 Code Examples

### Example 1: A RESTful resource with filtering and pagination

📄 File: [`app.js`](app.js)

```js
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
```

**How it works**

- Each method on `/api/v1/books` maps to a CRUD action with the conventional status code.
- `findBook` middleware loads the resource once and returns 404 for every `/:id` route.
- PUT requires the full object; PATCH updates only fields that were sent (whitelisted).
- Query parameters provide filtering, sorting (`-year` = descending) and pagination with metadata.
- The `borrow` endpoint is an action, showing where a pragmatic HTTP-style route makes sense; 409 signals a conflict.

### Example 2: Testing the API with requests

📄 File: [`requests.http`](requests.http)

```http
### List available books, newest first
GET http://localhost:3000/api/v1/books?available=true&sort=-year

### Create
POST http://localhost:3000/api/v1/books
Content-Type: application/json

{ "title": "Node.js Design Patterns", "author": "Mario Casciaro", "year": 2020 }

### Partial update
PATCH http://localhost:3000/api/v1/books/1
Content-Type: application/json

{ "available": false }

### Action endpoint
POST http://localhost:3000/api/v1/books/3/borrow

### Delete
DELETE http://localhost:3000/api/v1/books/2
```

**How it works**

- Open this file in VS Code with the *REST Client* extension and click "Send Request" above each block, or copy the requests into Postman.

### ▶️ How to run

1. Install Node.js 20 LTS or newer and check with `node -v`.
2. Open a terminal in this session folder.
3. If a `package.json` is present, run `npm install` first.
4. Run a file with `node <filename>` (for example `node app.js`).
5. `npm install`, `npm run dev`, then send the requests in `requests.http`.

## 🧪 Lab Practice

1. Call every endpoint in `requests.http` and record the status code of each response.
2. Try to create a book without an author and confirm you get 422 with a clear message.
3. Add a `?q=` search that matches title or author case-insensitively.
4. Add a `POST /api/v1/books/:id/return` action endpoint and decide its status codes.
5. Design (on paper) REST URLs for a school: students, courses, enrolments, and a student's marks in a course.

## 📝 Assignment

Design and build a **Batch Management REST API** for an institute: resources `batches` and `students` (each student belongs to a batch). Implement full CRUD for both, nested route `GET /api/v1/batches/:id/students`, filtering/pagination on students, consistent error JSON and correct status codes. Include an `API.md` table documenting every endpoint, and a `requests.http` file to test it.

## ❓ Quick Quiz

**Q1.** Which HTTP method and status code fit creating a resource?

**Q2.** What is the difference between PUT and PATCH?

**Q3.** What does 'stateless' mean in REST?

**Q4.** Is `POST /deleteStudent` RESTful? What is the REST version?

**Q5.** Name one disadvantage of REST.

<details>
<summary>Show answers</summary>

1. POST with 201 Created.
2. PUT replaces the whole resource; PATCH changes only the fields provided.
3. Each request contains all information needed; the server stores no client session between requests.
4. No. REST uses `DELETE /students/:id`.
5. Over-fetching/under-fetching or needing many endpoints/round trips for complex screens.

</details>

## 💼 Interview Questions

**1. Which status code would you return for a duplicate email on signup?**

> 409 Conflict (some teams use 422/400), with a clear error message.

**2. How do you version an API and why?**

> Use a URL prefix (/api/v1) or a header so breaking changes can be released without breaking existing clients.

**3. REST vs GraphQL in one sentence each?**

> REST exposes many resource endpoints with fixed responses; GraphQL exposes one endpoint where the client queries exactly the fields it needs.

## ✅ Summary

- An API is a contract for programs to communicate.
- REST uses resource URLs, HTTP methods, statelessness and status codes.
- HTTP/RPC-style APIs use action endpoints; flexible but less consistent.
- Choose correct codes: 200, 201, 204, 400/422, 401, 403, 404, 409, 500.
- Support filtering, sorting, pagination, versioning and documentation.

---

[⬅ Previous](../Session-07-Asynchronous-Programming-and-the-Event-Loop/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-09-MongoDB-CRUD-APIs-and-AI-Integration/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
