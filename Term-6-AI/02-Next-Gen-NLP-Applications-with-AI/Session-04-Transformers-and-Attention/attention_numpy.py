"""Session 04 - Scaled dot-product attention and multi-head attention in NumPy.

Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V
"""
import numpy as np

np.random.seed(0)
tokens = ["the", "cat", "sat", "on", "mat"]
seq_len, d_model, n_heads = len(tokens), 8, 2
d_k = d_model // n_heads

X = np.random.randn(seq_len, d_model)          # pretend these are token embeddings

def softmax(x, axis=-1):
    e = np.exp(x - x.max(axis=axis, keepdims=True))
    return e / e.sum(axis=axis, keepdims=True)

def scaled_dot_product_attention(Q, K, V, mask=None):
    scores = Q @ K.T / np.sqrt(Q.shape[-1])     # similarity of every query with every key
    if mask is not None:
        scores = np.where(mask, scores, -1e9)   # block forbidden positions
    weights = softmax(scores)                   # each row sums to 1
    return weights @ V, weights

# ----- single head -----
Wq, Wk, Wv = (np.random.randn(d_model, d_k) for _ in range(3))
out, w = scaled_dot_product_attention(X @ Wq, X @ Wk, X @ Wv)
print("Attention weights (row = query token, columns = keys):")
print("       " + " ".join(f"{t:>5}" for t in tokens))
for t, row in zip(tokens, w):
    print(f"{t:>6} " + " ".join(f"{v:5.2f}" for v in row))

# ----- causal mask used by decoder-only models (GPT) -----
causal = np.tril(np.ones((seq_len, seq_len), dtype=bool))
_, w_causal = scaled_dot_product_attention(X @ Wq, X @ Wk, X @ Wv, mask=causal)
print("\nCausal weights for 'sat' (cannot see the future):", np.round(w_causal[2], 2))

# ----- multi-head attention -----
def multi_head_attention(X, n_heads):
    heads = []
    for h in range(n_heads):
        Wq, Wk, Wv = (np.random.randn(d_model, d_k) for _ in range(3))
        head_out, _ = scaled_dot_product_attention(X @ Wq, X @ Wk, X @ Wv)
        heads.append(head_out)
    Wo = np.random.randn(n_heads * d_k, d_model)
    return np.concatenate(heads, axis=-1) @ Wo   # concat heads, project back

mha = multi_head_attention(X, n_heads)
print("\nInput shape:", X.shape, "-> multi-head output shape:", mha.shape)
