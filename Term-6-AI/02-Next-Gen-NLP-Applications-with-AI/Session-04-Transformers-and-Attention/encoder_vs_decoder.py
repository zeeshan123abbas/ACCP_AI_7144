"""Session 04 - Encoder-only (BERT) vs decoder-only (GPT-2) models in practice.

BERT reads the whole sentence in both directions -> great for understanding (fill-mask).
GPT-2 reads left-to-right only -> great for generating the next words.
"""
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

fill = pipeline("fill-mask", model="distilbert-base-uncased")
print("ENCODER (DistilBERT) fills the blank using both sides of the sentence:")
for r in fill("Students use Python to [MASK] machine learning models.")[:3]:
    print(f"  {r['token_str']:<10} score={r['score']:.3f}")

tok = AutoTokenizer.from_pretrained("distilgpt2")
gpt = AutoModelForCausalLM.from_pretrained("distilgpt2")
ids = tok("Students use Python to", return_tensors="pt")
out = gpt.generate(**ids, max_new_tokens=12, do_sample=False, pad_token_id=tok.eos_token_id)
print("\nDECODER (DistilGPT-2) continues the text left-to-right:")
print(" ", tok.decode(out[0], skip_special_tokens=True))

print("\nTokenization differs too:")
print("  BERT :", fill.tokenizer.tokenize("Transformers are unbelievable"))
print("  GPT-2:", tok.tokenize("Transformers are unbelievable"))
