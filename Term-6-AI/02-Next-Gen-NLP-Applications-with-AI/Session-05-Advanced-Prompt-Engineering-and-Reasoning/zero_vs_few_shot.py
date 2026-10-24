"""Session 05 - Example 1: zero-shot vs few-shot prompting.

Zero-shot: describe the task only.
Few-shot : describe the task AND show a few solved examples first.
Run: python zero_vs_few_shot.py   (mock answers without OPENAI_API_KEY)
"""
from llm_client import ask_llm

review = "Delivery was late but the shirt quality is excellent."

# Step 1: zero-shot prompt - instructions only
zero_shot = f"""Classify the sentiment of the review as Positive, Negative or Mixed.
Review: {review}
Sentiment:"""

# Step 2: few-shot prompt - the same task with three solved examples
few_shot = f"""Classify the sentiment of each review as Positive, Negative or Mixed.

Review: The phone charges fast and looks great.
Sentiment: Positive

Review: The shoes tore after one week.
Sentiment: Negative

Review: Tasty food, but the waiter was rude.
Sentiment: Mixed

Review: {review}
Sentiment:"""

# Step 3: send both and compare
print("ZERO-SHOT:", ask_llm(zero_shot, mock_answer="The review is somewhat positive overall.", temperature=0))
print("FEW-SHOT :", ask_llm(few_shot, mock_answer="Mixed", temperature=0))
