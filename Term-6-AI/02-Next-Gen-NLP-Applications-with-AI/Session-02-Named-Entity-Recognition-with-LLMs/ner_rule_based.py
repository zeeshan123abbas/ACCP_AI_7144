"""Session 02 - Example 1: rule-based NER (dictionary + regular expressions).

No training data needed. Fast and easy to explain, but it only finds
what you wrote rules for.
Run: python ner_rule_based.py
"""
import re

# Step 1: a dictionary (gazetteer) of names we already know
KNOWN_ENTITIES = {
    "Karachi": "LOCATION",
    "Lahore": "LOCATION",
    "Aptech": "ORGANIZATION",
    "State Bank of Pakistan": "ORGANIZATION",
}

# Step 2: patterns for entities that follow a fixed shape
PATTERNS = {
    "EMAIL": r"[\w.]+@[\w.]+\.\w+",                # name@site.com
    "PHONE": r"03\d{2}-\d{7}",                     # 0300-1234567
    "MONEY": r"Rs\. ?[\d,]+",                      # Rs. 2,500
}

text = ("Aptech in Karachi will hold an AI seminar. The fee is Rs. 2,500. "
        "Contact info@example.com or 0300-1234567.")

found = []

# Step 3: look for every known name in the text
for name, label in KNOWN_ENTITIES.items():
    if name in text:
        found.append((name, label))

# Step 4: look for every pattern in the text
for label, pattern in PATTERNS.items():
    for match in re.findall(pattern, text):
        found.append((match, label))

# Step 5: print the results
for entity, label in found:
    print(f"{label:<13} {entity}")
