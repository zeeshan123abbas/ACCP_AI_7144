# naive_bayes_spam.py - Naive Bayes classifies short messages as spam or ham (normal)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

messages = [
    "Congratulations you won a free iPhone click now",
    "Claim your free prize money today",
    "Win cash now limited offer",
    "Urgent your account is blocked send password",
    "Are we meeting for class tomorrow",
    "Please send me the lab notes",
    "Mama said dinner at 8 tonight",
    "The assignment deadline is Friday",
]
labels = ["spam", "spam", "spam", "spam", "ham", "ham", "ham", "ham"]

# Step 1: turn text into word counts (each word becomes a column)
vectorizer = CountVectorizer(lowercase=True)
X = vectorizer.fit_transform(messages)
print("Vocabulary size:", len(vectorizer.vocabulary_))

# Step 2: train Naive Bayes on the counts
model = MultinomialNB()
model.fit(X, labels)

# Step 3: classify new messages (use transform, NOT fit_transform, on new text)
new_messages = ["free cash prize click", "notes for tomorrow class", "send password now"]
X_new = vectorizer.transform(new_messages)
for text, label, probs in zip(new_messages, model.predict(X_new), model.predict_proba(X_new)):
    print(f"{text!r:<30} -> {label}  (P(ham)={probs[0]:.2f}, P(spam)={probs[1]:.2f})")
