"""Session 03 - Example 3: abstractive summary with a small open model on your laptop.

Model: google/flan-t5-small (~300 MB, runs on CPU, downloads once).
Setup: pip install transformers torch
Run:   python summarize_flan_t5.py
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-small"

# Step 1: load the tokenizer (text -> numbers) and the model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

article = ("The college library will stay open until 10 pm during exam week. "
           "Students must show their ID card at the entrance. "
           "Extra seats have been added on the second floor.")

# Step 2: FLAN-T5 follows instructions, so we start the input with "summarize:"
inputs = tokenizer("summarize: " + article, return_tensors="pt")

# Step 3: generate up to 40 new tokens using beam search (tries 4 options, keeps the best)
output_ids = model.generate(**inputs, max_new_tokens=40, num_beams=4)

# Step 4: turn the numbers back into text
print("Summary:", tokenizer.decode(output_ids[0], skip_special_tokens=True))
