"""Session 14 - Example 3: financial sentiment with a domain word list.

General sentiment tools get finance wrong: "liability" or "debt" is not
always negative, and "beat estimates" is very positive. A finance-specific
word list gives better results. (Research uses lists like Loughran-McDonald
or models like FinBERT.)
Run: python finance_sentiment.py
"""

POSITIVE = ["profit", "growth", "beat", "record", "surge", "upgrade", "dividend", "gain", "strong"]
NEGATIVE = ["loss", "decline", "miss", "default", "downgrade", "lawsuit", "plunge", "weak", "fraud"]

def finance_sentiment(headline):
    words = headline.lower().replace(",", "").split()
    # Step 1: count positive and negative finance words (handles "losses" via startswith)
    pos = sum(1 for w in words for p in POSITIVE if w.startswith(p))
    neg = sum(1 for w in words for n in NEGATIVE if w.startswith(n))
    # Step 2: turn the counts into a label
    score = pos - neg
    if score > 0:
        return "positive", score
    if score < 0:
        return "negative", score
    return "neutral", score

headlines = [
    "Bank reports record profit and higher dividend",
    "Cement maker posts quarterly loss as demand declines",
    "Textile exporter beats estimates despite weak rupee",
    "Company announces board meeting date",
]
for h in headlines:
    label, score = finance_sentiment(h)
    print(f"{label:<8} ({score:+d})  {h}")
