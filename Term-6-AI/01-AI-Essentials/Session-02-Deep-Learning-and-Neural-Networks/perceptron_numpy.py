"""Session 02 - A single artificial neuron and a tiny neural network, from scratch.

Part A: a perceptron learns the AND gate (linearly separable).
Part B: a 2-layer network with sigmoid learns XOR (NOT linearly separable),
        which a single neuron cannot do. This is why we need hidden layers.
"""
import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)

# ---------------- Part A: perceptron for AND ----------------
y_and = np.array([0, 0, 0, 1])
w, b, lr = np.zeros(2), 0.0, 0.1
for epoch in range(20):
    for xi, target in zip(X, y_and):
        out = 1 if xi @ w + b > 0 else 0       # step activation
        err = target - out
        w += lr * err * xi                      # perceptron update rule
        b += lr * err
print("AND weights:", w, "bias:", round(b, 2))
print("AND predictions:", [1 if xi @ w + b > 0 else 0 for xi in X])

# ---------------- Part B: 2-layer network for XOR ----------------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

y_xor = np.array([[0], [1], [1], [0]], dtype=float)
rng = np.random.default_rng(1)
W1, b1 = rng.normal(0, 1, (2, 4)), np.zeros((1, 4))   # input -> hidden (4 neurons)
W2, b2 = rng.normal(0, 1, (4, 1)), np.zeros((1, 1))   # hidden -> output
lr = 1.0

for epoch in range(5000):
    # forward pass
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)
    # backward pass (gradient of mean squared error)
    d_out = (out - y_xor) * out * (1 - out)
    d_h = (d_out @ W2.T) * h * (1 - h)
    W2 -= lr * h.T @ d_out
    b2 -= lr * d_out.sum(axis=0, keepdims=True)
    W1 -= lr * X.T @ d_h
    b1 -= lr * d_h.sum(axis=0, keepdims=True)
    if epoch % 1000 == 0:
        print(f"epoch {epoch:4d}  loss = {np.mean((out - y_xor) ** 2):.4f}")

print("XOR outputs:", out.round(2).ravel(), "-> rounded:", out.round().astype(int).ravel())
