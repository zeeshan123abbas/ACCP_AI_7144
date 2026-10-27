"""Session 13 - Example 3: semantic search (meaning, not exact words).

Uses sentence-transformers if installed. Otherwise it falls back to
TF-IDF with a small synonym list, so the script always runs.
Install (optional): pip install sentence-transformers
Run: python semantic_search.py
"""
import numpy as np
from courses import COURSES

documents = [c["title"] + ". " + c["text"] for c in COURSES]
query = "teach a computer to talk with people"

try:
    # Option A: real embeddings
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
    doc_vectors = model.encode(documents, normalize_embeddings=True)
    query_vector = model.encode([query], normalize_embeddings=True)[0]
    scores = doc_vectors @ query_vector
    mode = "embeddings"
except ImportError:
    # Option B: fallback - expand the query with synonyms, then TF-IDF
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SYNONYMS = {"talk": "chatbots language text", "computer": "models", "websites": "web pages"}
    expanded = query + " " + " ".join(SYNONYMS.get(w, "") for w in query.split())
    vectorizer = TfidfVectorizer(stop_words="english")
    index = vectorizer.fit_transform(documents)
    scores = cosine_similarity(vectorizer.transform([expanded]), index)[0]
    mode = "TF-IDF + synonyms (install sentence-transformers for real embeddings)"

print("Mode :", mode)
print("Query:", query)
for i in np.argsort(scores)[::-1][:3]:
    print(f"  {scores[i]:.3f}  {COURSES[i]['title']}")
