"""Session 04 - Example 3: sinusoidal positional encoding.

Attention alone does not know word ORDER. We add a unique pattern of
sine and cosine values to each position so the model can tell
"dog bites man" from "man bites dog".
Run: python positional_encoding.py
"""
import numpy as np

num_positions = 5      # sentence length
d_model = 6            # size of each vector

encoding = np.zeros((num_positions, d_model))

# Step 1: fill the table one position and one dimension at a time
for pos in range(num_positions):
    for i in range(0, d_model, 2):
        angle = pos / (10000 ** (i / d_model))
        encoding[pos, i] = np.sin(angle)          # even columns use sine
        encoding[pos, i + 1] = np.cos(angle)      # odd columns use cosine

# Step 2: show the table - every row (position) is different
np.set_printoptions(precision=2, suppress=True)
print("Positional encoding (rows = positions 0..4):")
print(encoding)

# Step 3: in a transformer, this is ADDED to the word embeddings
word_embeddings = np.ones((num_positions, d_model))    # fake embeddings
model_input = word_embeddings + encoding
print("\nEmbedding + position for position 0 and 1:")
print(model_input[:2])
