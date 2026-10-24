"""Session 05 - Example 3: self-consistency = ask several times, take a majority vote.

One reasoning path can go wrong. If we sample 5 different paths
(temperature > 0) and pick the most common final answer, accuracy improves.
Run: python self_consistency.py
"""
from collections import Counter
from llm_client import ask_llm

question = ("Ali is older than Bilal. Bilal is older than Sana. "
            "Who is the youngest? Think step by step, then end with 'Answer: <name>'.")

# Sample answers for mock mode: four reasoning paths agree, one makes a mistake
mock_paths = [
    "Ali > Bilal > Sana, so the youngest is Sana. Answer: Sana",
    "Bilal is older than Sana, and Ali is older than Bilal. Answer: Sana",
    "Ali is oldest... I think Bilal. Answer: Bilal",
    "Order: Ali, Bilal, Sana. Answer: Sana",
    "Sana is younger than Bilal who is younger than Ali. Answer: Sana",
]

final_answers = []

# Step 1: ask the same question 5 times with some randomness
for i in range(5):
    reply = ask_llm(question, mock_answer=mock_paths[i], temperature=0.8)
    # Step 2: keep only the text after "Answer:"
    answer = reply.split("Answer:")[-1].strip().rstrip(".")
    final_answers.append(answer)
    print(f"Path {i + 1}: {answer}")

# Step 3: majority vote
votes = Counter(final_answers)
winner, count = votes.most_common(1)[0]
print(f"\nVotes: {dict(votes)}")
print(f"Self-consistent answer: {winner} ({count} of 5 votes)")
