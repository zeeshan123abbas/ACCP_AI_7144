// node server.js   then: curl localhost:3000/notes
import http from "node:http";
import { addNote, loadNotes, removeNote } from "./store.js";

function readJson(req) {
  return new Promise((resolve, reject) => {
    let body = "";
    req.on("data", (chunk) => (body += chunk));
    req.on("end", () => {
      try { resolve(body ? JSON.parse(body) : {}); }
      catch { reject(new Error("Invalid JSON")); }
    });
  });
}

function send(res, status, data) {
  res.writeHead(status, { "Content-Type": "application/json" });
  res.end(JSON.stringify(data));
}

http.createServer(async (req, res) => {
  const { pathname, searchParams } = new URL(req.url, "http://localhost");
  try {
    if (req.method === "GET" && pathname === "/notes") {
      const q = (searchParams.get("q") || "").toLowerCase();
      const notes = await loadNotes();
      return send(res, 200, notes.filter((n) => n.text.toLowerCase().includes(q)));
    }
    if (req.method === "POST" && pathname === "/notes") {
      const { text } = await readJson(req);
      if (!text) return send(res, 400, { error: "text is required" });
      return send(res, 201, await addNote(text));
    }
    const match = pathname.match(/^\/notes\/(\d+)$/);
    if (req.method === "DELETE" && match) {
      const ok = await removeNote(Number(match[1]));
      return send(res, ok ? 200 : 404, ok ? { deleted: true } : { error: "Not found" });
    }
    send(res, 404, { error: "Route not found" });
  } catch (err) {
    send(res, 400, { error: err.message });
  }
}).listen(3000, () => console.log("Notes API on http://localhost:3000"));
