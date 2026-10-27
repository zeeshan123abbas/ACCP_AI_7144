"""Session 13 - Example 2: ranked search with TF-IDF and cosine similarity.

Rare, specific words (like "pytorch") count more than common ones (like "learn").
Install: pip install scikit-learn
Run:     python tfidf_search.py
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from courses import COURSES

# Step 1: one document per course
documents = [c["title"] + ". " + c["text"] for c in COURSES]

# Step 2: build the TF-IDF index
vectorizer = TfidfVectorizer(stop_words="english")
index = vectorizer.fit_transform(documents)

def search(query, top_k=3):
    # Step 3: turn the query into a vector and compare with every course
    scores = cosine_similarity(vectorizer.transform([query]), index)[0]
    ranked = scores.argsort()[::-1][:top_k]
    return [(round(float(scores[i]), 3), COURSES[i]["title"]) for i in ranked if scores[i] > 0]

for query in ["python models", "build websites", "teach a computer to talk"]:
    print(f"\nQuery: {query}")
    print(search(query) or "  no results")
