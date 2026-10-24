"""Session 02 - Statistical (spaCy) vs transformer (BERT) NER, with evaluation.

Setup:
    pip install spacy transformers torch
    python -m spacy download en_core_web_sm
The BERT model (~430 MB) downloads on first run from the Hugging Face Hub.
"""
import spacy
from transformers import pipeline

sentences = [
    "Imran Khan visited Lahore with officials from the World Bank.",
    "Ayesha Malik joined Microsoft in Seattle after studying at LUMS.",
    "The Pakistan Cricket Board met in Karachi on Friday.",
]
# Gold (correct) annotations to evaluate against: (text, type)
gold = [
    {("Imran Khan", "PER"), ("Lahore", "LOC"), ("World Bank", "ORG")},
    {("Ayesha Malik", "PER"), ("Microsoft", "ORG"), ("Seattle", "LOC"), ("LUMS", "ORG")},
    {("Pakistan Cricket Board", "ORG"), ("Karachi", "LOC")},
]

SPACY_MAP = {"PERSON": "PER", "GPE": "LOC", "LOC": "LOC", "ORG": "ORG", "NORP": "MISC"}
nlp = spacy.load("en_core_web_sm")
bert_ner = pipeline("token-classification", model="dslim/bert-base-NER",
                    aggregation_strategy="first")    # merge word pieces into whole words/entities

def spacy_entities(s):
    ents = set()
    for e in nlp(s).ents:
        if e.label_ in SPACY_MAP:
            text = e.text[4:] if e.text.lower().startswith("the ") else e.text  # drop leading "the"
            ents.add((text, SPACY_MAP[e.label_]))
    return ents

def bert_entities(s):
    return {(e["word"], e["entity_group"]) for e in bert_ner(s)}

def evaluate(pred_sets):
    tp = sum(len(p & g) for p, g in zip(pred_sets, gold))
    fp = sum(len(p - g) for p, g in zip(pred_sets, gold))
    fn = sum(len(g - p) for p, g in zip(pred_sets, gold))
    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
    return precision, recall, f1

for name, fn in [("spaCy (statistical)", spacy_entities), ("BERT (transformer)", bert_entities)]:
    preds = [fn(s) for s in sentences]
    print(f"\n{name}")
    for s, p in zip(sentences, preds):
        print("  ", sorted(p))
    p, r, f = evaluate(preds)
    print(f"   precision={p:.2f} recall={r:.2f} F1={f:.2f}")
