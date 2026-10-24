"""Session 02 - Example 3: transformer (BERT) NER with Hugging Face.

Setup: pip install transformers torch
The model dslim/bert-base-NER (~430 MB) downloads once, then is cached.
Run:   python ner_transformer.py
"""
from transformers import pipeline

# Step 1: create a ready-made NER pipeline.
# aggregation_strategy="simple" joins word pieces ("Ay", "##esha") into whole names.
ner = pipeline("token-classification", model="dslim/bert-base-NER",
               aggregation_strategy="simple")

text = "Ayesha Malik joined Microsoft in Seattle after studying at LUMS."

# Step 2: run the model
results = ner(text)

# Step 3: print each entity with its type and confidence score
for entity in results:
    print(f"{entity['entity_group']:<5} {entity['word']:<15} score={entity['score']:.2f}")
