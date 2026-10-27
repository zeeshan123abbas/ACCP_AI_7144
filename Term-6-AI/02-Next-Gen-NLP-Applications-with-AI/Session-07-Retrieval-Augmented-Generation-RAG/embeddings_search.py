"""Session 07 - Example 4 (optional, needs a download): semantic retrieval with embeddings.

TF-IDF only matches the same WORDS. Embeddings match MEANING, so
"How much do I pay each month?" can find "The monthly fee is PKR 25,000".
Install: pip install sentence-transformers
Run:     python embeddings_search.py
"""
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Please install first:  pip install sentence-transformers")
    raise SystemExit

import numpy as np

sentences = [
    "The monthly fee for the ACCP AI programme is PKR 25,000.",
    "The centre is closed on Sundays and public holidays.",
    "Students may borrow two books for 14 days.",
]

# Step 1: load a small embedding model (about 90 MB, downloaded once)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: turn each sentence into a vector; normalize so dot product = cosine similarity
sentence_vectors = model.encode(sentences, normalize_embeddings=True)

# Step 3: embed a question that uses DIFFERENT words from the documents
question = "How much do I pay every month?"
question_vector = model.encode([question], normalize_embeddings=True)[0]

# Step 4: score and rank
scores = sentence_vectors @ question_vector
for i in np.argsort(scores)[::-1]:
    print(f"{scores[i]:.3f}  {sentences[i]}")
