"""Session 01 - Example 3: POS tags, lemmas and named entities with spaCy.

Setup (one time):
    pip install spacy
    python -m spacy download en_core_web_sm
Run: python spacy_pipeline.py
"""
import spacy

# Step 1: load the small English model (tokenizer + tagger + parser + NER)
nlp = spacy.load("en_core_web_sm")

# Step 2: run the whole pipeline on a sentence with one call
doc = nlp("Sana booked a flight from Karachi to Dubai on Monday for 85,000 rupees.")

# Step 3: look at every token
print(f"{'TOKEN':<10}{'LEMMA':<10}{'POS':<7}STOP WORD?")
for token in doc:
    print(f"{token.text:<10}{token.lemma_:<10}{token.pos_:<7}{token.is_stop}")

# Step 4: look at the named entities spaCy found
print("\nNamed entities:")
for entity in doc.ents:
    print(f"  {entity.text:<15} {entity.label_:<8} ({spacy.explain(entity.label_)})")
