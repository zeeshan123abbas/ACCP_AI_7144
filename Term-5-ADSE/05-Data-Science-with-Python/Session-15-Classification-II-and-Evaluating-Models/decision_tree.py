# decision_tree.py - a Decision Tree learns if/else questions from data
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

# Should the bank approve a loan?
df = pd.DataFrame({
    "income_k":   [30, 85, 45, 120, 25, 60, 95, 40, 150, 55, 35, 70],   # monthly income (Rs 000)
    "has_job":    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    "late_bills": [3, 0, 2, 0, 4, 1, 0, 3, 0, 2, 5, 0],                 # late payments last year
    "approved":   ["No", "Yes", "No", "Yes", "No", "Yes", "Yes", "No", "Yes", "No", "No", "Yes"],
})
X = df[["income_k", "has_job", "late_bills"]]
y = df["approved"]

# max_depth limits how many questions in a row (keeps the tree simple)
tree = DecisionTreeClassifier(max_depth=2, random_state=0)
tree.fit(X, y)

# The learned rules as text
print(export_text(tree, feature_names=list(X.columns)))

# Predict two new applicants
applicants = pd.DataFrame({"income_k": [50, 90], "has_job": [1, 1], "late_bills": [3, 0]})
print("Predictions:", list(tree.predict(applicants)))

# Draw the tree
plt.figure(figsize=(9, 5))
plot_tree(tree, feature_names=list(X.columns), class_names=list(tree.classes_),
          filled=True, rounded=True)
plt.savefig("decision_tree.png")
print("Saved decision_tree.png")
