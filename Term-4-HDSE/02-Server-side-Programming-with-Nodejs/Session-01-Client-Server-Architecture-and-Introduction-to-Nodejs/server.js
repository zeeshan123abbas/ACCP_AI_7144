// Run: node server.js  then open http://localhost:3000
import http from "node:http";

const server = http.createServer((req, res) => {
  console.log(`${req.method} ${req.url}`);

  if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end("<h1>Welcome to my first Node server</h1><a href='/api/time'>Server time</a>");
  } else if (req.url === "/api/time") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ serverTime: new Date().toISOString() }));
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("404 - Not found");
  }
});

server.listen(3000, () => console.log("Server running at http://localhost:3000"));
