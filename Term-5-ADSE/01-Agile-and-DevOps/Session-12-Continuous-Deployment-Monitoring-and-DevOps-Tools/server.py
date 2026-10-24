"""Minimal HTTP service with a /health endpoint for monitoring.
Uses only the standard library. Run: python server.py  then open http://localhost:8000/grade?marks=72
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from app import grade


class Handler(BaseHTTPRequestHandler):
    def _send(self, status: int, body: dict) -> None:
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/health":
            self._send(200, {"status": "ok"})
        elif url.path == "/grade":
            try:
                marks = int(parse_qs(url.query).get("marks", ["-1"])[0])
                self._send(200, {"marks": marks, "grade": grade(marks)})
            except ValueError as err:
                self._send(400, {"error": str(err)})
        else:
            self._send(404, {"error": "not found"})


if __name__ == "__main__":
    print("Serving on http://localhost:8000")
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
