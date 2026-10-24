"""Session 03 - Open-ended text generation and decoding strategies.

Model: distilgpt2 (~350 MB), a small decoder-only language model.
Compare greedy, beam search, top-k and nucleus (top-p) sampling.
"""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL)
prompt = "Artificial intelligence will help students"
inputs = tokenizer(prompt, return_tensors="pt")

strategies = {
    "greedy": dict(do_sample=False),
    "beam (5)": dict(do_sample=False, num_beams=5, no_repeat_ngram_size=2),
    "top-k (k=50)": dict(do_sample=True, top_k=50, temperature=0.9),
    "top-p (p=0.92)": dict(do_sample=True, top_p=0.92, top_k=0, temperature=0.9),
}
torch.manual_seed(42)
for name, cfg in strategies.items():
    out = model.generate(**inputs, max_new_tokens=25, pad_token_id=tokenizer.eos_token_id, **cfg)
    print(f"[{name:<14}] {tokenizer.decode(out[0], skip_special_tokens=True)!r}\n")

# Peek inside: the model's top 5 guesses for the very next token
with torch.no_grad():
    logits = model(**inputs).logits[0, -1]
probs = torch.softmax(logits, dim=-1)
top = torch.topk(probs, 5)
print("Next-token probabilities:")
for p, idx in zip(top.values, top.indices):
    print(f"  {tokenizer.decode(idx)!r:<12} {p.item():.3f}")
