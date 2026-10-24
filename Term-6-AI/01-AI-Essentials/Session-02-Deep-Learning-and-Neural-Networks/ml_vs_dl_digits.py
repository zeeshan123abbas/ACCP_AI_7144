"""Session 02 - Classic ML vs a neural network on handwritten digits.

The 8x8 digits dataset ships with scikit-learn, so no download is needed.
We compare a linear model with a multi-layer perceptron (MLP).
"""
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

X, y = load_digits(return_X_y=True)          # 1797 images, 64 pixels each
print("Data shape:", X.shape)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=7, stratify=y)
scaler = StandardScaler().fit(X_tr)
X_tr, X_te = scaler.transform(X_tr), scaler.transform(X_te)

linear = LogisticRegression(max_iter=2000).fit(X_tr, y_tr)
mlp = MLPClassifier(hidden_layer_sizes=(128, 64), activation="relu",
                    max_iter=300, random_state=7).fit(X_tr, y_tr)

print(f"Logistic Regression accuracy : {accuracy_score(y_te, linear.predict(X_te)):.2%}")
print(f"Neural network (MLP) accuracy: {accuracy_score(y_te, mlp.predict(X_te)):.2%}")
print("MLP layers (weights shapes):", [w.shape for w in mlp.coefs_])
print("Total trainable parameters:",
      sum(w.size for w in mlp.coefs_) + sum(b.size for b in mlp.intercepts_))
