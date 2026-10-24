"""Session 02 - Example 2: statistical NER with a pre-trained spaCy model.

Setup: pip install spacy  and  python -m spacy download en_core_web_sm
Run:   python ner_spacy.py
"""
import spacy

# Step 1: load a model that was trained on thousands of labelled sentences
nlp = spacy.load("en_core_web_sm")

sentences = [
    "Ayesha Malik joined Microsoft in Seattle in March 2025.",
    "The Pakistan Cricket Board met in Lahore on Friday.",
]

# Step 2: run the model on each sentence and print the entities
for sentence in sentences:
    doc = nlp(sentence)
    print(sentence)
    for entity in doc.ents:
        print(f"   {entity.label_:<8} {entity.text}")
