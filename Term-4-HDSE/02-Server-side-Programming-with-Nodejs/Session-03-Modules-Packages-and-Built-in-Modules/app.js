// Run: node app.js  ->  http://localhost:3000/api/marks?values=70,85,90
import http from "node:http";
import os from "node:os";
import average, { percentage } from "./math.js";

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const send = (status, data) => {
    res.writeHead(status, { "Content-Type": "application/json" });
    res.end(JSON.stringify(data));
  };

  if (req.method === "GET" && url.pathname === "/api/marks") {
    const values = (url.searchParams.get("values") ?? "")
      .split(",")
      .map(Number)
      .filter((n) => !Number.isNaN(n));
    return send(200, {
      values,
      average: average(values),
      percentOfMax: percentage(average(values), 100),
    });
  }

  if (url.pathname === "/api/system") {
    return send(200, { host: os.hostname(), cpus: os.cpus().length, freeMemMB: Math.round(os.freemem() / 1e6) });
  }

  send(404, { error: `No route for ${req.method} ${url.pathname}` });
});

server.listen(3000, () => console.log("http://localhost:3000"));
