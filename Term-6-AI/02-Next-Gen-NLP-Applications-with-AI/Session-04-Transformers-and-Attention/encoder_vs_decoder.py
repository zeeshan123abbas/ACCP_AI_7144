"""Session 04 - Example 5: encoder-only (BERT) vs decoder-only (GPT-2) in practice.

Encoder (DistilBERT) reads the WHOLE sentence -> good at understanding (fill in the blank).
Decoder (DistilGPT-2) reads LEFT to RIGHT -> good at writing the next words.
Setup: pip install transformers torch   (two small models download once)
Run:   python encoder_vs_decoder.py
"""
from transformers import pipeline

# Step 1: encoder-only model fills a blank using words on BOTH sides
fill_mask = pipeline("fill-mask", model="distilbert-base-uncased")
print("ENCODER (DistilBERT): 'Students use Python to [MASK] machine learning models.'")
for guess in fill_mask("Students use Python to [MASK] machine learning models.")[:3]:
    print(f"   {guess['token_str']:<8} score={guess['score']:.2f}")

# Step 2: decoder-only model continues the text one token at a time
generator = pipeline("text-generation", model="distilgpt2")
result = generator("Students use Python to", max_new_tokens=12, do_sample=False)
print("\nDECODER (DistilGPT-2):")
print("  ", result[0]["generated_text"])
