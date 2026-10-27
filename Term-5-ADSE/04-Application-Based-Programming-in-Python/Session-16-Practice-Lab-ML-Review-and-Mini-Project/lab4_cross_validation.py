# lab4_cross_validation.py - a fairer score: test each model on 5 different splits

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

X, y = load_breast_cancer(return_X_y=True)

candidates = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "K-Nearest Neighbours": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=0),
}

# cv=5: split data into 5 parts; train on 4, test on 1; repeat 5 times
for name, model in candidates.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    print(f"{name:<22} mean={scores.mean():.3f}  (+/- {scores.std():.3f})")
