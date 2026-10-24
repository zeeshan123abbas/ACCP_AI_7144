"""Session 03 - Extractive summarization with TF-IDF sentence scoring.

Extractive = pick the most important ORIGINAL sentences.
No neural network needed; runs instantly with scikit-learn.
"""
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ARTICLE = """
Karachi's public transport is changing quickly. The new electric bus service started on two
routes last year and now carries thousands of passengers every day. Commuters say the buses
are cleaner and cheaper than rickshaws. The city government plans to add four more routes by
next summer. However, traffic experts warn that buses alone cannot fix congestion. They argue
that dedicated bus lanes and better footpaths are also needed. Some shopkeepers along the
routes complained about lost parking spaces. Officials replied that more customers now arrive
by bus. A survey found that most riders would leave their motorbikes at home if service were
more frequent. The project is being watched closely by other cities in Pakistan.
"""

def summarize(text, n_sentences=3):
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    tfidf = TfidfVectorizer(stop_words="english").fit_transform(sentences)
    # Score 1: how important the words in each sentence are
    word_score = np.asarray(tfidf.sum(axis=1)).ravel()
    # Score 2: how similar each sentence is to the document as a whole (centrality)
    centroid = np.asarray(tfidf.mean(axis=0))
    centrality = cosine_similarity(tfidf, centroid).ravel()
    score = 0.5 * word_score / word_score.max() + 0.5 * centrality / centrality.max()
    top = sorted(np.argsort(score)[-n_sentences:])          # keep original order
    return [sentences[i] for i in top], score

summary, scores = summarize(ARTICLE)
print("Sentence scores:", np.round(scores, 2))
print("\nSUMMARY:")
for s in summary:
    print(" -", s)
original_words = len(ARTICLE.split())
summary_words = sum(len(s.split()) for s in summary)
print(f"\nCompression: {original_words} -> {summary_words} words")
