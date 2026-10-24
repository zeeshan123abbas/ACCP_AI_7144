"""Session 01 - A classic NLP pipeline with NLTK.

Stages: raw text -> tokenization -> normalization -> stop-word removal
        -> stemming vs lemmatization -> POS tagging -> named entities

First run downloads small NLTK data packages (one time only).
"""
import string
import nltk

for pkg in ["punkt_tab", "stopwords", "wordnet", "averaged_perceptron_tagger_eng",
            "maxent_ne_chunker_tab", "words"]:
    nltk.download(pkg, quiet=True)

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

text = ("Aptech students in Karachi are building chatbots this semester. "
        "Ali's team studied transformers, and their models were running on Google Colab!")

# 1) Tokenization
sentences = sent_tokenize(text)
tokens = word_tokenize(text)
print("Sentences:", sentences)
print("Tokens   :", tokens)

# 2) Normalization: lowercase and drop punctuation
normalized = [t.lower() for t in tokens if t not in string.punctuation]
print("Normalized:", normalized)

# 3) Stop-word removal
stops = set(stopwords.words("english"))
content_words = [t for t in normalized if t not in stops]
print("Without stop words:", content_words)

# 4) Stemming vs lemmatization
stemmer, lemmatizer = PorterStemmer(), WordNetLemmatizer()
print("\nword         stem        lemma(verb)")
for w in ["studied", "running", "models", "building", "better"]:
    print(f"{w:<12} {stemmer.stem(w):<11} {lemmatizer.lemmatize(w, pos='v')}")

# 5) Part-of-speech tagging
tags = nltk.pos_tag(tokens)
print("\nPOS tags:", tags)

# 6) Named Entity Recognition (classic chunker)
tree = nltk.ne_chunk(tags)
entities = [(" ".join(w for w, _ in st.leaves()), st.label())
            for st in tree if hasattr(st, "label")]
print("Entities:", entities)
