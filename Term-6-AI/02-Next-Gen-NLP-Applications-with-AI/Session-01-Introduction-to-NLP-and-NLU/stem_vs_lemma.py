"""Session 01 - Example 2: stemming vs lemmatization.

Stemming chops word endings with simple rules (fast, sometimes not a real word).
Lemmatization uses a dictionary to find the real base word (slower, more accurate).
Run: python stem_vs_lemma.py
"""
import nltk

# Download the WordNet dictionary used by the lemmatizer (first time only)
nltk.download("wordnet", quiet=True)

from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["studies", "studying", "running", "better", "children", "went"]

print(f"{'WORD':<10} {'STEM':<10} {'LEMMA (as verb)':<16} LEMMA (as noun)")
for word in words:
    stem = stemmer.stem(word)                           # rule-based chopping
    lemma_verb = lemmatizer.lemmatize(word, pos="v")    # dictionary lookup, treat as verb
    lemma_noun = lemmatizer.lemmatize(word, pos="n")    # dictionary lookup, treat as noun
    print(f"{word:<10} {stem:<10} {lemma_verb:<16} {lemma_noun}")
