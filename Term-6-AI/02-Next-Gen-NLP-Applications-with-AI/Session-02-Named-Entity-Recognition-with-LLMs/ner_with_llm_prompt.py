"""Session 02 - Example 4: NER with a large language model (zero-shot prompt).

We describe the task in plain English and ask for JSON back.
Works live with OPENAI_API_KEY, or prints a mock answer without it.
Run: python ner_with_llm_prompt.py
"""
import json
from llm_client import ask_llm

text = "Bilal Ahmed works at Systems Limited in Lahore and earns Rs. 300,000 a month."

# Step 1: write a clear prompt with the labels and the output format we want
prompt = f"""Extract named entities from the text.
Use only these labels: PERSON, ORGANIZATION, LOCATION, MONEY.
Return JSON only, as a list of objects with "text" and "label".

Text: {text}"""

# Step 2: this is what a good answer looks like (used only in mock mode)
sample = ('[{"text": "Bilal Ahmed", "label": "PERSON"}, '
          '{"text": "Systems Limited", "label": "ORGANIZATION"}, '
          '{"text": "Lahore", "label": "LOCATION"}, '
          '{"text": "Rs. 300,000", "label": "MONEY"}]')

# Step 3: ask the model (temperature 0 = most consistent answer)
answer = ask_llm(prompt, mock_answer=sample, temperature=0)
print("Raw answer:", answer)

# Step 4: turn the JSON text into Python objects so a program can use it
json_text = answer.replace("(mock) ", "").strip()
json_text = json_text.removeprefix("```json").removesuffix("```").strip()   # some models wrap JSON
try:
    entities = json.loads(json_text)
    for item in entities:
        print(f"{item['label']:<13} {item['text']}")
except json.JSONDecodeError:
    print("The model did not return valid JSON. Try a stricter prompt.")
