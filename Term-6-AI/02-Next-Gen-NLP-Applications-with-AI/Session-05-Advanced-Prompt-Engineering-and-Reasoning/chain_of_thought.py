"""Session 05 - Example 2: chain-of-thought (CoT) prompting.

Asking the model to "think step by step" helps on maths and logic,
because it writes the middle steps instead of guessing the answer at once.
Run: python chain_of_thought.py
"""
from llm_client import ask_llm

question = ("A canteen had 23 samosas. It sold 15 in the morning and then made 12 more. "
            "How many samosas does it have now?")

# Step 1: direct prompt - asks only for the final answer
direct_prompt = f"{question}\nGive only the final number."

# Step 2: chain-of-thought prompt - asks for the steps, then the answer on its own line
cot_prompt = f"""{question}
Think step by step. Show each step on a new line.
Finish with a line in the form: Answer: <number>"""

cot_sample = "Start with 23.\nSold 15: 23 - 15 = 8.\nMade 12 more: 8 + 12 = 20.\nAnswer: 20"

print("DIRECT:\n", ask_llm(direct_prompt, mock_answer="20", temperature=0))
print("\nCHAIN OF THOUGHT:\n", ask_llm(cot_prompt, mock_answer=cot_sample, temperature=0))
