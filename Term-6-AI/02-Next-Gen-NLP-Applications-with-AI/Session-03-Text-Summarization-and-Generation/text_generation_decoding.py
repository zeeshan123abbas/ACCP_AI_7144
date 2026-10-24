"""Session 03 - Example 4: how decoding settings change generated text.

Model: distilgpt2 (~350 MB), a small decoder-only language model.
Setup: pip install transformers torch
Run:   python text_generation_decoding.py
"""
from transformers import pipeline, set_seed

# Step 1: create a text-generation pipeline
generator = pipeline("text-generation", model="distilgpt2")
set_seed(42)                                   # same "random" results every run

prompt = "Artificial intelligence will help students"

# Step 2: greedy decoding - always pick the single most likely next word
greedy = generator(prompt, max_new_tokens=20, do_sample=False)
print("GREEDY  :", greedy[0]["generated_text"], "\n")

# Step 3: sampling with LOW temperature - safe, focused choices
low_temp = generator(prompt, max_new_tokens=20, do_sample=True, temperature=0.3)
print("TEMP 0.3:", low_temp[0]["generated_text"], "\n")

# Step 4: sampling with HIGH temperature - more creative (and more random)
high_temp = generator(prompt, max_new_tokens=20, do_sample=True, temperature=1.3)
print("TEMP 1.3:", high_temp[0]["generated_text"], "\n")

# Step 5: top-p (nucleus) sampling - choose only from the most likely words
top_p = generator(prompt, max_new_tokens=20, do_sample=True, top_p=0.9)
print("TOP-P   :", top_p[0]["generated_text"])
