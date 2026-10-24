"""Session 04 - Example 1: scaled dot-product attention, step by step in NumPy.

Formula:  Attention(Q, K, V) = softmax(Q x K^T / sqrt(d)) x V
Run: python attention_numpy.py   (needs only numpy)
"""
import numpy as np

np.random.seed(0)                       # same random numbers every run
tokens = ["the", "cat", "sat"]
d = 4                                   # size of each vector

# Step 1: pretend each token already has an embedding vector (3 tokens x 4 numbers)
X = np.random.randn(len(tokens), d)

# Step 2: make Query, Key and Value vectors with three weight matrices
W_query = np.random.randn(d, d)
W_key = np.random.randn(d, d)
W_value = np.random.randn(d, d)
Q = X @ W_query        # what each token is looking for
K = X @ W_key          # what each token offers
V = X @ W_value        # the information each token passes on

# Step 3: score how well every query matches every key (dot product)
scores = Q @ K.T

# Step 4: scale the scores so they do not get too large
scores = scores / np.sqrt(d)

# Step 5: softmax turns each row into weights that add up to 1
weights = np.exp(scores) / np.exp(scores).sum(axis=1, keepdims=True)

# Step 6: each output is a weighted mix of the Value vectors
output = weights @ V

print("Attention weights (row = token asking, column = token it looks at):")
print("        " + "  ".join(f"{t:>5}" for t in tokens))
for token, row in zip(tokens, weights):
    print(f"{token:>6}  " + "  ".join(f"{w:5.2f}" for w in row))
print("\nOutput shape:", output.shape, "(one new vector per token)")
