"""Session 06 - Example 5: prepare an instruction dataset for fine-tuning.

Fine-tuning data is usually a list of (instruction, input, output) records
saved as JSON Lines (.jsonl): one JSON object per line.
Run: python prepare_dataset.py   -> creates train.jsonl and test.jsonl
"""
import json
import random

# Step 1: a few hand-written examples (real projects use hundreds or thousands)
examples = [
    {"instruction": "Classify the complaint", "input": "My fee voucher shows the wrong amount.", "output": "billing"},
    {"instruction": "Classify the complaint", "input": "The parcel has not arrived after 10 days.", "output": "delivery"},
    {"instruction": "Classify the complaint", "input": "The laptop screen flickers.", "output": "product"},
    {"instruction": "Classify the complaint", "input": "I was charged twice this month.", "output": "billing"},
    {"instruction": "Classify the complaint", "input": "Courier left the box at the wrong house.", "output": "delivery"},
    {"instruction": "Classify the complaint", "input": "The charger stopped working in a week.", "output": "product"},
]

# Step 2: clean each record - strip spaces and drop empty ones
clean = []
for row in examples:
    row = {key: value.strip() for key, value in row.items()}
    if row["input"] and row["output"]:
        clean.append(row)

# Step 3: shuffle, then keep about 80% for training and 20% for testing
random.seed(42)
random.shuffle(clean)
split = int(len(clean) * 0.8)
train, test = clean[:split], clean[split:]

# Step 4: write JSON Lines files
def save_jsonl(rows, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")

save_jsonl(train, "train.jsonl")
save_jsonl(test, "test.jsonl")

# Step 5: show how one record becomes a single training prompt
first = train[0]
prompt = f"### Instruction:\n{first['instruction']}\n### Input:\n{first['input']}\n### Response:\n{first['output']}"
print(f"train: {len(train)} rows, test: {len(test)} rows")
print("\nOne formatted training example:\n" + prompt)
