"""Session 02 - NER with a generative LLM using a prompt (zero-shot).

Uses the small open model google/flan-t5-small (~300 MB, CPU friendly).
Larger instruction-tuned LLMs follow such prompts far more accurately;
the technique is exactly the same.
"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)

def ask(prompt, max_new_tokens=12):
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=max_new_tokens)
    return tokenizer.decode(output[0], skip_special_tokens=True)

text = "Bilal Ahmed works at Systems Limited in Lahore."
questions = {
    "PERSON": f"Who is the person mentioned in this text? Text: {text}",
    "ORGANIZATION": f"Which company is mentioned in this text? Text: {text}",
    "LOCATION": f"Which city is mentioned in this text? Text: {text}",
}
for label, prompt in questions.items():
    print(f"{label:<13} -> {ask(prompt)}")
