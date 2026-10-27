"""Session 11 - Example 3: serve the model as a REST API with FastAPI.

Install: pip install fastapi "uvicorn[standard]" scikit-learn joblib
Run:     uvicorn app_fastapi:app --reload
Open:    http://127.0.0.1:8000/docs   (interactive docs to test the API)
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from predict import predict_sentiment

app = FastAPI(title="Sentiment API", version="1.0")

# Step 1: describe the JSON body we expect: {"text": "..."}
class Review(BaseModel):
    text: str

# Step 2: a health check so servers and load balancers know the app is alive
@app.get("/health")
def health():
    return {"status": "ok"}

# Step 3: the prediction endpoint
@app.post("/predict")
def predict(review: Review):
    try:
        return predict_sentiment(review.text)
    except ValueError as error:                      # bad input -> HTTP 400
        raise HTTPException(status_code=400, detail=str(error))
