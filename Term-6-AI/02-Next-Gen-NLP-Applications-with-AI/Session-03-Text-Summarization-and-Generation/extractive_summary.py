"""Session 03 - Example 1: extractive summarization by word frequency.

Extractive = choose the most important ORIGINAL sentences.
Idea: a sentence is important if it contains words that appear often in the article.
Run: python extractive_summary.py   (needs only Python)
"""
import re

ARTICLE = """Karachi's new electric bus service started on two routes last year.
The buses now carry thousands of passengers every day.
Passengers say the electric buses are cleaner and cheaper than rickshaws.
The city plans to add four more bus routes by next summer.
Some shopkeepers complained about lost parking spaces.
Experts say bus lanes are needed so the buses do not get stuck in traffic."""

STOP_WORDS = {"the", "a", "and", "are", "is", "to", "on", "by", "of", "in", "than",
              "so", "do", "not", "get", "say", "some", "about", "now", "every", "more"}

# Step 1: split the article into sentences
sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", ARTICLE) if s.strip()]

# Step 2: count how often each useful word appears in the whole article
word_counts = {}
for word in re.findall(r"[a-z']+", ARTICLE.lower()):
    if word not in STOP_WORDS:
        word_counts[word] = word_counts.get(word, 0) + 1

# Step 3: give every sentence a score = total count of its words
scores = []
for sentence in sentences:
    words = re.findall(r"[a-z']+", sentence.lower())
    score = sum(word_counts.get(word, 0) for word in words)
    scores.append(score)
    print(f"score {score:>2} | {sentence}")

# Step 4: pick the 2 best sentences, then keep them in their original order
best_positions = sorted(range(len(sentences)), key=lambda i: scores[i], reverse=True)[:2]
summary = [sentences[i] for i in sorted(best_positions)]

print("\nSUMMARY:")
print(" ".join(summary))
