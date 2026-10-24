"""Session 01 - The three types of learning in one file.

1. Supervised   : learn from labelled examples (classification)
2. Unsupervised : find groups in unlabelled data (clustering)
3. Reinforcement: learn by trial, error and reward (Q-learning)
"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

# ---------- 1. Supervised learning ----------
X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=1)
clf = LogisticRegression(max_iter=500).fit(X_tr, y_tr)
print(f"[Supervised]   Iris species accuracy: {clf.score(X_te, y_te):.2%}")

# ---------- 2. Unsupervised learning ----------
# Customers described by (visits per month, average bill in PKR hundreds)
customers = np.array([[2, 5], [3, 4], [2, 6], [12, 30], [14, 28],
                      [13, 35], [6, 15], [7, 14], [5, 16]])
km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(customers)
print("[Unsupervised] Customer groups:", km.labels_.tolist())

# ---------- 3. Reinforcement learning ----------
# A robot walks on a 1-D corridor of 5 cells. Cell 4 holds the reward.
# Actions: 0 = left, 1 = right.
n_states, n_actions = 5, 2
Q = np.zeros((n_states, n_actions))
alpha, gamma, epsilon = 0.5, 0.9, 0.2
rng = np.random.default_rng(0)

for episode in range(200):
    state = 0
    while state != 4:
        if rng.random() < epsilon:
            action = rng.integers(n_actions)           # explore
        else:
            action = int(np.argmax(Q[state]))          # exploit
        nxt = max(0, state - 1) if action == 0 else min(4, state + 1)
        reward = 10 if nxt == 4 else -1
        Q[state, action] += alpha * (reward + gamma * Q[nxt].max() - Q[state, action])
        state = nxt

policy = ["L" if np.argmax(q) == 0 else "R" for q in Q[:4]]
print("[Reinforcement] Learned policy for cells 0-3:", policy)
