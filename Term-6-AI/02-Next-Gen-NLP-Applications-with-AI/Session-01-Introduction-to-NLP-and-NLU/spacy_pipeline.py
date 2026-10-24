"""Session 01 - The same pipeline in one call with spaCy.

Setup (one time):
    pip install spacy
    python -m spacy download en_core_web_sm
"""
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Sana booked a flight from Karachi to Dubai on Monday for 85,000 rupees "
          "because Emirates offered a student discount.")

print(f"{'TOKEN':<10}{'LEMMA':<10}{'POS':<7}{'STOP':<6}DEPENDENCY")
for tok in doc:
    print(f"{tok.text:<10}{tok.lemma_:<10}{tok.pos_:<7}{str(tok.is_stop):<6}{tok.dep_} -> {tok.head.text}")

print("\nNamed entities:")
for ent in doc.ents:
    print(f"  {ent.text:<15} {ent.label_:<8} ({spacy.explain(ent.label_)})")

print("\nNoun chunks:", [chunk.text for chunk in doc.noun_chunks])
