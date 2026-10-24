# tokenise_text.py - splitting text into words and sentences (tokenisation)

import re
from collections import Counter

text = "Python is easy. Python is powerful! Is Python used in AI? Yes, it is."

# 1) Simple split on spaces (keeps punctuation attached)
print("split():", text.split())

# 2) Word tokens with regex: \w+ means "one or more letters/digits"
words = re.findall(r"\w+", text.lower())
print("Word tokens:", words)

# 3) Sentence tokens: split after . ! or ? followed by a space
sentences = re.split(r"(?<=[.!?])\s+", text)
print("Sentences:")
for s in sentences:
    print(" -", s)

# 4) Remove common "stop words" and count the rest
stop_words = {"is", "in", "it", "yes"}
keywords = [w for w in words if w not in stop_words]
print("Top keywords:", Counter(keywords).most_common(3))
