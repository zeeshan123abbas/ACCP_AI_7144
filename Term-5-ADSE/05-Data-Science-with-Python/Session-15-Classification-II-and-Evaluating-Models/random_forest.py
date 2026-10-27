# random_forest.py - many trees vote together (an ensemble)
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

data = load_breast_cancer(as_frame=True)
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=2, stratify=y)

# One deep tree vs a forest of 200 trees
single_tree = DecisionTreeClassifier(random_state=0).fit(X_train, y_train)
forest = RandomForestClassifier(n_estimators=200, random_state=0).fit(X_train, y_train)

print("Single tree  - train:", round(single_tree.score(X_train, y_train), 3),
      " test:", round(single_tree.score(X_test, y_test), 3))
print("Random forest - train:", round(forest.score(X_train, y_train), 3),
      " test:", round(forest.score(X_test, y_test), 3))

# Which features did the forest find most useful?
importance = pd.Series(forest.feature_importances_, index=X.columns)
top = importance.sort_values(ascending=False).head(8)
print("\nTop features:\n", top.round(3))

top.sort_values().plot(kind="barh", color="forestgreen", figsize=(7, 4),
                       title="Random forest: top 8 feature importances")
plt.tight_layout()
plt.savefig("feature_importance.png")
print("Saved feature_importance.png")
