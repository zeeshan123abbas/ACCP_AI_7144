"""Session 02 - Rule-based and dictionary-based NER.

Fast, transparent and needs no training data, but brittle.
"""
import re

GAZETTEER = {   # dictionary (gazetteer) of known entities
    "LOC": ["Karachi", "Lahore", "Islamabad", "North Nazimabad", "Dubai"],
    "ORG": ["Aptech", "State Bank of Pakistan", "PTCL", "Hugging Face"],
}
PATTERNS = {    # regular-expression patterns
    "EMAIL": r"[\w.+-]+@[\w-]+\.[\w.]+",
    "PHONE": r"(?:\+92|0)3\d{2}-?\d{7}",
    "DATE": r"\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{4}\b",
    "MONEY": r"\b(?:Rs\.?|PKR)\s?[\d,]+\b",
}

def find_entities(text):
    found = []
    for label, names in GAZETTEER.items():
        for name in names:
            for m in re.finditer(re.escape(name), text):
                found.append((m.start(), m.end(), m.group(), label))
    for label, pattern in PATTERNS.items():
        for m in re.finditer(pattern, text):
            found.append((m.start(), m.end(), m.group(), label))
    # remove entities nested inside longer ones (e.g. 'Karachi' inside a longer match)
    found.sort(key=lambda e: (e[0], -(e[1] - e[0])))
    result, last_end = [], -1
    for e in found:
        if e[0] >= last_end:
            result.append(e); last_end = e[1]
    return result

text = ("Aptech North Nazimabad in Karachi will hold an AI seminar on 14 November 2026. "
        "Registration costs Rs. 2,500. Contact info@example.com or 0300-1234567.")
for start, end, span, label in find_entities(text):
    print(f"{label:<6} {span!r:<28} chars {start}-{end}")
