"""Session 14 - Example 2: is a symptom present or NEGATED?

"No chest pain" must not be recorded as chest pain! This is a tiny version
of the well-known NegEx idea: look for a negation word shortly BEFORE the term.
Run: python negation_detection.py
"""
import re

SYMPTOMS = ["fever", "cough", "headache", "chest pain", "nausea", "sore throat"]
NEGATION_WORDS = ["no", "denies", "without", "not", "negative for"]
WINDOW = 4          # how many words before the symptom we check

def symptom_status(note):
    results = {}
    for sentence in re.split(r"[.;]", note.lower()):          # Step 1: one sentence at a time
        words = sentence.split()
        for symptom in SYMPTOMS:
            if symptom not in sentence:
                continue
            # Step 2: find the word position where the symptom starts
            first_word = symptom.split()[0]
            position = words.index(first_word)
            # Step 3: look at the few words before it for a negation
            before = " ".join(words[max(0, position - WINDOW):position])
            negated = any(re.search(rf"\b{neg}\b", before) for neg in NEGATION_WORDS)
            results[symptom] = "ABSENT" if negated else "PRESENT"
    return results

note = "Patient reports fever and cough. Denies chest pain. No nausea or headache today."
print("Note:", note)
for symptom, status in symptom_status(note).items():
    print(f"  {symptom:<11} -> {status}")
