"""Session 11 - Example 1: train a small sentiment model and save it to a file.

In production we train ONCE, save the model, and load the saved file in
the web API. Here: TF-IDF + Logistic Regression in one scikit-learn Pipeline.
Install: pip install scikit-learn joblib
Run:     python train_and_save_model.py   -> creates sentiment_model.joblib
"""
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Step 1: a small labelled dataset (1 = positive, 0 = negative)
texts = [
    "I love this course", "The teacher explains very well", "Great labs and helpful staff",
    "Amazing experience, highly recommended", "The notes are clear and useful",
    "Very bad service", "The class was boring and too long", "I hate the late timings",
    "Terrible internet in the lab", "The fee is too high for this quality",
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Step 2: a pipeline keeps the text-to-numbers step and the classifier together
model = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("classifier", LogisticRegression()),
])

# Step 3: train
model.fit(texts, labels)

# Step 4: save the whole pipeline in one file
joblib.dump(model, "sentiment_model.joblib")
print("Saved sentiment_model.joblib")

# Step 5: quick check that the saved model works after loading
loaded = joblib.load("sentiment_model.joblib")
print(loaded.predict(["the staff is helpful", "boring and bad"]))
