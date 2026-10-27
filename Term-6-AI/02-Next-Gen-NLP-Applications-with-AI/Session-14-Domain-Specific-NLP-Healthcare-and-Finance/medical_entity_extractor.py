"""Session 14 - Example 1: pull medicines, doses and symptoms out of a clinical note.

Uses a small dictionary + regular expressions. Real systems use trained
medical NER models (e.g. scispaCy) and large vocabularies.
Run: python medical_entity_extractor.py
"""
import re

# Step 1: small dictionaries of known terms (lower case)
MEDICINES = ["paracetamol", "amoxicillin", "metformin", "ibuprofen", "omeprazole"]
SYMPTOMS = ["fever", "cough", "headache", "chest pain", "nausea", "sore throat"]

# Step 2: a pattern for doses like "500 mg", "5 ml", "1 g"
DOSE_PATTERN = r"\b\d+(?:\.\d+)?\s?(?:mg|ml|g|mcg)\b"
# and for frequencies like "twice daily" or "every 8 hours"
FREQUENCY_PATTERN = r"\b(?:once|twice|three times) (?:a day|daily)\b|\bevery \d+ hours\b"

def extract(note):
    text = note.lower()
    return {
        "medicines": [m for m in MEDICINES if m in text],
        "symptoms": [s for s in SYMPTOMS if s in text],
        "doses": re.findall(DOSE_PATTERN, text),
        "frequency": re.findall(FREQUENCY_PATTERN, text),
    }

note = ("Patient has fever and sore throat for 3 days. No chest pain. "
        "Start Amoxicillin 500 mg three times a day and Paracetamol 1 g every 8 hours if needed.")

print("Note:", note, "\n")
for key, values in extract(note).items():
    print(f"{key:<10}: {values}")
