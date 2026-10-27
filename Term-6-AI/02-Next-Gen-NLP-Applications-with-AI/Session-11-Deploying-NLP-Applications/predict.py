"""Session 11 - Example 2: one small function that the API will call.

Keeping prediction logic in its own file means the web server, tests and
command line can all reuse it.
Run: python predict.py "the labs are great"
"""
import sys
import joblib

MAX_CHARS = 1000                                 # reject very long inputs
_model = None                                    # loaded once, then reused

def get_model():
    """Load the model the first time it is needed (lazy loading)."""
    global _model
    if _model is None:
        _model = joblib.load("sentiment_model.joblib")
    return _model

def predict_sentiment(text):
    """Return a dictionary that is easy to turn into JSON."""
    # Step 1: validate the input
    if not isinstance(text, str) or not text.strip():
        raise ValueError("text must be a non-empty string")
    if len(text) > MAX_CHARS:
        raise ValueError(f"text must be at most {MAX_CHARS} characters")

    # Step 2: predict the label and its probability
    model = get_model()
    probability_positive = float(model.predict_proba([text])[0][1])
    label = "positive" if probability_positive >= 0.5 else "negative"
    return {"text": text, "label": label, "confidence": round(max(probability_positive, 1 - probability_positive), 3)}

if __name__ == "__main__":
    sentence = sys.argv[1] if len(sys.argv) > 1 else "the teacher is very helpful"
    print(predict_sentiment(sentence))
