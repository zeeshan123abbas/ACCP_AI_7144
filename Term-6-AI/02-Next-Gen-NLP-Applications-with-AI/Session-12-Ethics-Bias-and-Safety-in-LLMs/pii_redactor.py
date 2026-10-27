"""Session 12 - Example 2: remove personal data (PII) before sending text to an LLM.

PII = Personally Identifiable Information: emails, phone numbers, ID numbers.
We replace them with placeholders using regular expressions.
Run: python pii_redactor.py
"""
import re

# Step 1: one pattern per type of personal data (Pakistani formats as examples)
PATTERNS = {
    "EMAIL": r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+",
    "CNIC":  r"\b\d{5}-\d{7}-\d\b",                       # 12345-1234567-1
    "PHONE": r"(?:\+92|0)3\d{2}[- ]?\d{7}\b",             # 0300-1234567 or +923001234567
    "CARD":  r"\b(?:\d{4}[- ]?){3}\d{4}\b",               # 16-digit card number
}

def redact(text):
    """Replace each match with a label like [EMAIL]; also return what was found."""
    found = []
    for label, pattern in PATTERNS.items():
        for match in re.findall(pattern, text):
            found.append(label)
        text = re.sub(pattern, f"[{label}]", text)
    return text, found

# Step 2: try it on a customer message
message = ("Hi, I am Sara. My CNIC is 42101-1234567-8, call me on 0300-1234567 "
           "or email sara.khan@example.com. My card 4111 1111 1111 1111 was charged twice.")

clean_text, found = redact(message)
print("Original:", message)
print("Redacted:", clean_text)
print("Removed :", found)
