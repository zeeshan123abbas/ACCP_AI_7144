"""Session 11 - Example 5: call the running API and check the answers.

Start the server first (app_fastapi.py with uvicorn, or app_stdlib.py).
Run: python test_api.py
"""
import json
import urllib.error
import urllib.request

BASE_URL = "http://127.0.0.1:8000"

def post_json(path, data):
    """Send a JSON POST request and return (status code, response dictionary)."""
    request = urllib.request.Request(
        BASE_URL + path,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            return response.status, json.loads(response.read())
    except urllib.error.HTTPError as error:          # 4xx and 5xx responses
        return error.code, json.loads(error.read())

# Step 1: health check
with urllib.request.urlopen(BASE_URL + "/health", timeout=5) as response:
    print("health:", json.loads(response.read()))

# Step 2: a normal request
print(post_json("/predict", {"text": "The labs are great and the staff is helpful"}))

# Step 3: a bad request should return status 400, not crash the server
print(post_json("/predict", {"text": ""}))
