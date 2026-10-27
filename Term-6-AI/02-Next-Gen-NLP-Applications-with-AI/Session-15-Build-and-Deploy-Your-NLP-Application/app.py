"""Session 15 - Step 5: serve the assistant as a web API.

Install: pip install fastapi "uvicorn[standard]" scikit-learn
Run:     uvicorn app:app --reload
Test:    open http://127.0.0.1:8000/docs and try POST /ask
"""
import logging
import time
from fastapi import FastAPI
from pydantic import BaseModel
from assistant import answer
from guard import redact

logging.basicConfig(filename="requests.log", level=logging.INFO, format="%(asctime)s %(message)s")
app = FastAPI(title="Campus Help Desk Assistant", version="1.0")

class Question(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(body: Question):
    start = time.perf_counter()
    result = answer(body.question)                               # all logic lives in assistant.py
    latency_ms = round((time.perf_counter() - start) * 1000)
    # log WITHOUT personal data
    logging.info("status=%s latency_ms=%s question=%r", result["status"], latency_ms, redact(body.question))
    return {**result, "latency_ms": latency_ms}
