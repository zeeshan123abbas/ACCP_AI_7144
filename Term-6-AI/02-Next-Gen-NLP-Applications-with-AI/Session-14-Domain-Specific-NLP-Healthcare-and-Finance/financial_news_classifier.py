"""Session 14 - Example 4: train a classifier to label financial news topics.

Domain models learn from domain data. We train TF-IDF + Logistic Regression
on a few labelled headlines and predict new ones.
Install: pip install scikit-learn
Run:     python financial_news_classifier.py
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Step 1: labelled training headlines (real projects use thousands)
train = [
    ("Central bank raises policy rate by 100 basis points", "monetary_policy"),
    ("State bank keeps interest rate unchanged", "monetary_policy"),
    ("Inflation slows, rate cut expected next month", "monetary_policy"),
    ("Oil company reports 20 percent rise in quarterly earnings", "earnings"),
    ("Bank profit falls on higher provisions", "earnings"),
    ("Fertilizer firm announces final dividend and earnings growth", "earnings"),
    ("Stock index hits all-time high in heavy trading", "markets"),
    ("Shares slide as investors book profits", "markets"),
    ("Rupee gains against the dollar in interbank market", "markets"),
]
texts = [t for t, _ in train]
labels = [label for _, label in train]

# Step 2: build and train the model
model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2)), LogisticRegression(max_iter=1000))
model.fit(texts, labels)

# Step 3: predict topics for new headlines, with the model's confidence
new_headlines = [
    "Policy rate cut by 150 basis points",
    "Cement company earnings jump on strong sales",
    "Shares rally as index crosses new record",
]
for headline in new_headlines:
    probabilities = model.predict_proba([headline])[0]
    best = probabilities.argmax()
    print(f"{model.classes_[best]:<16} {probabilities[best]:.0%}  {headline}")
