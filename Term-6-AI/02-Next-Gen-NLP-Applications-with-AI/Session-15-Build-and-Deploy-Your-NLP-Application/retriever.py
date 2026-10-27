"""Session 15 - Step 2: find the most relevant document for a question (TF-IDF).

Install: pip install scikit-learn
Run:     python retriever.py
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from knowledge_base import DOCUMENTS

class Retriever:
    def __init__(self, documents, min_score=0.1):
        self.documents = documents
        self.min_score = min_score                       # below this = "not found"
        texts = [d["title"] + ". " + d["text"] for d in documents]
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(texts)   # build the index once

    def search(self, question, top_k=2):
        """Return up to top_k (score, document) pairs above min_score."""
        scores = cosine_similarity(self.vectorizer.transform([question]), self.matrix)[0]
        ranked = scores.argsort()[::-1][:top_k]
        return [(float(scores[i]), self.documents[i]) for i in ranked if scores[i] >= self.min_score]

if __name__ == "__main__":
    retriever = Retriever(DOCUMENTS)
    for score, doc in retriever.search("When are certificates issued?"):
        print(f"{score:.2f}  {doc['title']}: {doc['text']}")
