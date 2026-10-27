# lab1_word_counter.py - read a text file, tokenise it, count words
# Skills: files, exceptions, regex, dictionaries

import re

FILE_NAME = "story.txt"

# Step 1: read the file safely
try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        text = file.read()
except FileNotFoundError:
    print(f"Sorry, {FILE_NAME} was not found.")
    raise SystemExit

# Step 2: tokenise - make lowercase and keep only words (letters)
words = re.findall(r"[a-z]+", text.lower())
print("Total words:", len(words))

# Step 3: count each word in a dictionary
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# Step 4: sort by count (highest first) and show the top 5
top_words = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:5]
print("Top 5 words:")
for word, number in top_words:
    print(f"  {word:<10} {number}")

# Step 5: count sentences (split on . ! ?)
sentences = [s for s in re.split(r"[.!?]", text) if s.strip()]
print("Sentences:", len(sentences))
