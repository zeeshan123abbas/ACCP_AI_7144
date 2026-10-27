"""Session 07 - Example 2: find the most relevant chunks for a question (TF-IDF).

TF-IDF turns each chunk and the question into a vector of word weights.
Cosine similarity then tells us which chunks are closest to the question.
Install: pip install scikit-learn
Run:     python tfidf_retriever.py
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from chunk_documents import load_documents, chunk_text

# Step 1: build the list of chunks (the "knowledge base")
chunks = []
for filename, text in load_documents("docs").items():
    for piece in chunk_text(text):
        chunks.append({"source": filename, "text": piece})

# Step 2: learn the vocabulary and turn every chunk into a vector
vectorizer = TfidfVectorizer(stop_words="english")
chunk_vectors = vectorizer.fit_transform([c["text"] for c in chunks])


def retrieve(question, top_k=2):
    """Return the top_k chunks most similar to the question."""
    question_vector = vectorizer.transform([question])            # Step 3: embed the question
    scores = cosine_similarity(question_vector, chunk_vectors)[0]  # Step 4: compare with all chunks
    best = scores.argsort()[::-1][:top_k]                          # Step 5: highest scores first
    return [(round(float(scores[i]), 3), chunks[i]) for i in best]


if __name__ == "__main__":
    for question in ["What is the late fee?", "When is the centre closed?"]:
        print("\nQ:", question)
        for score, chunk in retrieve(question):
            print(f"  {score}  [{chunk['source']}] {chunk['text']}")
