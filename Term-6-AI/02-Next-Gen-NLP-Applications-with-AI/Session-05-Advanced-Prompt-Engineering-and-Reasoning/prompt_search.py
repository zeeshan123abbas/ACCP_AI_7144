"""Session 05 - Example 5: automatic prompt optimization (simple prompt search).

Instead of guessing which prompt is best, we TEST several candidate prompts
on a small labelled set and keep the one with the highest accuracy.
Run: python prompt_search.py
"""
from llm_client import ask_llm, is_live

# Step 1: a small labelled test set
test_set = [
    ("I love this phone", "Positive"),
    ("Worst service ever", "Negative"),
    ("Battery life is amazing", "Positive"),
    ("The parcel arrived broken", "Negative"),
]

# Step 2: candidate prompt templates ({text} is replaced with each review)
candidates = [
    "What do you think about this review? {text}",
    "Is this review Positive or Negative? {text}",
    "Classify the review as Positive or Negative. Reply with one word only.\nReview: {text}",
]

def mock_model(prompt, text):
    """Offline stand-in: follows the format only if the prompt clearly asks for it."""
    guess = "Positive" if any(w in text.lower() for w in ["love", "amazing"]) else "Negative"
    if "one word" in prompt:
        return guess
    if "Positive or Negative" in prompt:
        return f"I would say it is {guess}."
    return "This review shares the customer's opinion."

# Step 3: score every candidate prompt
best_prompt, best_score = None, -1
for template in candidates:
    correct = 0
    for text, label in test_set:
        prompt = template.format(text=text)
        answer = ask_llm(prompt, mock_answer=mock_model(template, text), temperature=0)
        answer = answer.replace("(mock) ", "").strip().rstrip(".")
        if answer == label:                       # strict check: exact label only
            correct += 1
    accuracy = correct / len(test_set)
    print(f"accuracy {accuracy:.0%} | {template[:60]!r}")
    if accuracy > best_score:
        best_prompt, best_score = template, accuracy

# Step 4: report the winner
print("\nMode:", "LIVE" if is_live() else "MOCK")
print("Best prompt:", repr(best_prompt))
