"""Session 02 - Example 5: measuring NER with precision, recall and F1.

Precision = of the entities we predicted, how many were right?
Recall    = of the real entities, how many did we find?
F1        = one number that balances both
Run: python ner_evaluation.py
"""

# Step 1: the correct answers (gold labels) written by a human
gold = {("Imran", "PERSON"), ("Lahore", "LOCATION"), ("World Bank", "ORGANIZATION"),
        ("Friday", "DATE")}

# Step 2: what our system predicted
predicted = {("Imran", "PERSON"), ("Lahore", "LOCATION"), ("Bank", "ORGANIZATION")}

# Step 3: count matches and mistakes using set operations
true_positives = len(gold & predicted)       # in both sets: correct
false_positives = len(predicted - gold)      # predicted but wrong
false_negatives = len(gold - predicted)      # real entity we missed

# Step 4: apply the formulas
precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)
f1 = 2 * precision * recall / (precision + recall)

print("Correct (TP):", true_positives, "| Wrong (FP):", false_positives, "| Missed (FN):", false_negatives)
print(f"Precision = {precision:.2f}")
print(f"Recall    = {recall:.2f}")
print(f"F1 score  = {f1:.2f}")
