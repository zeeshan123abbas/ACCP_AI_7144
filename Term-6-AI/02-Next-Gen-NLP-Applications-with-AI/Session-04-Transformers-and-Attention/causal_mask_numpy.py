"""Session 04 - Example 2: the causal mask used by GPT-style (decoder) models.

When generating text, a token must not look at FUTURE tokens.
We block them by setting their scores to a very large negative number.
Run: python causal_mask_numpy.py
"""
import numpy as np

tokens = ["I", "love", "NLP", "class"]
n = len(tokens)

# Step 1: start with equal scores for every pair of tokens
scores = np.zeros((n, n))

# Step 2: build a lower-triangle mask: True = allowed to look, False = future
mask = np.tril(np.ones((n, n), dtype=bool))
print("Mask (1 = can see):")
print(mask.astype(int))

# Step 3: replace blocked positions with -1e9 so softmax gives them ~0 weight
scores = np.where(mask, scores, -1e9)

# Step 4: softmax row by row
weights = np.exp(scores) / np.exp(scores).sum(axis=1, keepdims=True)

print("\nAttention weights with the causal mask:")
for token, row in zip(tokens, weights):
    print(f"{token:>6}: " + "  ".join(f"{w:.2f}" for w in row))
