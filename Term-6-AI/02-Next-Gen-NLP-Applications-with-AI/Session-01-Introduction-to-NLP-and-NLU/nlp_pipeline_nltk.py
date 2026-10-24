"""Session 01 - Example 1: the basic NLP pipeline with NLTK.

Steps: raw text -> sentences -> tokens -> lowercase -> remove punctuation -> remove stop words
Run:   python nlp_pipeline_nltk.py
"""
import string
import nltk

# Step 0: download the small data files NLTK needs (only the first time)
nltk.download("punkt_tab", quiet=True)    # sentence and word splitter
nltk.download("stopwords", quiet=True)    # list of common words like "the", "is"

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

text = "Aptech students in Karachi are building chatbots. The chatbots answer questions about fees!"

# Step 1: split the text into sentences
sentences = sent_tokenize(text)
print("1) Sentences :", sentences)

# Step 2: split the text into words and punctuation (tokens)
tokens = word_tokenize(text)
print("2) Tokens    :", tokens)

# Step 3: normalization - make every token lowercase
lower_tokens = [token.lower() for token in tokens]
print("3) Lowercase :", lower_tokens)

# Step 4: remove punctuation marks such as "." and "!"
no_punctuation = [token for token in lower_tokens if token not in string.punctuation]
print("4) No punct. :", no_punctuation)

# Step 5: remove stop words (very common words that carry little meaning)
english_stop_words = set(stopwords.words("english"))
content_words = [token for token in no_punctuation if token not in english_stop_words]
print("5) Content   :", content_words)
