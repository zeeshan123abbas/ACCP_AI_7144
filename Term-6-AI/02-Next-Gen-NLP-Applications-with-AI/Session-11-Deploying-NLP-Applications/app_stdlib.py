"""Session 11 - Example 4: the same API with ONLY the Python standard library.

Useful when you cannot install FastAPI. Good for learning; for real
production use FastAPI (Example 3) behind a proper server.
Run:  python app_stdlib.py      then in another terminal: python test_api.py
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from predict import predict_sentiment

class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, data):
        """Helper: send a Python dictionary as a JSON response."""
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):                                # GET /health
        if self.path == "/health":
            self.send_json(200, {"status": "ok"})
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):                               # POST /predict
        if self.path != "/predict":
            self.send_json(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            data = json.loads(self.rfile.read(length))
            self.send_json(200, predict_sentiment(data.get("text")))
        except (ValueError, AttributeError) as error:   # bad JSON or bad text
            self.send_json(400, {"error": str(error)})

if __name__ == "__main__":
    print("Serving on http://127.0.0.1:8000  (Ctrl+C to stop)")
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
