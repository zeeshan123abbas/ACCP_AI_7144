// Run: node blocking-server.js, open /block in one tab and / in another
import http from "node:http";

http.createServer((req, res) => {
  if (req.url === "/block") {
    const end = Date.now() + 5000;
    while (Date.now() < end) {} // CPU-bound loop blocks the event loop for 5 s
    return res.end("Finished blocking work\n");
  }
  if (req.url === "/nonblock") {
    return setTimeout(() => res.end("Finished after 5 s without blocking\n"), 5000);
  }
  res.end("Hello! (Was I slow? Then someone hit /block)\n");
}).listen(3000, () => console.log("http://localhost:3000"));
