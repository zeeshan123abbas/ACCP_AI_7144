"""Session 03 - Abstractive, prompt-based summarization with an instruction-tuned model.

Abstractive = write NEW sentences that capture the meaning.
Model: google/flan-t5-base (~1 GB, CPU ok). Swap to flan-t5-small for speed.
We control the output with the prompt (length, audience, format).
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)

ARTICLE = ("Karachi's new electric bus service started on two routes last year and now carries "
           "thousands of passengers daily. Riders say it is cleaner and cheaper than rickshaws. "
           "The city plans four more routes by next summer, but traffic experts say dedicated bus "
           "lanes and better footpaths are also needed to reduce congestion.")

def generate(prompt, max_new_tokens=60, **kwargs):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    out = model.generate(**inputs, max_new_tokens=max_new_tokens, **kwargs)
    return tokenizer.decode(out[0], skip_special_tokens=True)

prompts = {
    "one sentence": f"Summarize in one sentence: {ARTICLE}",
    "headline": f"Write a short news headline for this article: {ARTICLE}",
    "for a child": f"Explain this news to a 10 year old in one simple sentence: {ARTICLE}",
}
for name, p in prompts.items():
    print(f"[{name}] {generate(p, num_beams=4)}")

# Controllability via decoding: beam search (safe) vs sampling (creative)
print("\n[beam search ]", generate(prompts["one sentence"], num_beams=4))
print("[sampling t=1]", generate(prompts["one sentence"], do_sample=True, temperature=1.0, top_p=0.9))
