"""Session 01 - A complete (small) supervised ML workflow.

Scenario: a microfinance company wants to predict whether a loan
application should be approved. We create a synthetic dataset so the
script runs offline, then follow the standard ML workflow:
collect -> prepare -> split -> train -> evaluate -> predict.
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1) Collect data (synthetic, reproducible)
rng = np.random.default_rng(42)
n = 500
df = pd.DataFrame({
    "monthly_income_k": rng.integers(30, 400, n),     # PKR thousands
    "existing_loans": rng.integers(0, 4, n),
    "years_employed": rng.integers(0, 20, n),
    "credit_score": rng.integers(300, 850, n),
})
# Hidden "true" rule + a little noise creates the label
score = (df.monthly_income_k / 400) + (df.credit_score - 300) / 550 \
        + df.years_employed / 40 - df.existing_loans * 0.25
df["approved"] = ((score + rng.normal(0, 0.15, n)) > 1.0).astype(int)

print("First rows of the dataset:")
print(df.head(), "\n")
print("Label balance:\n", df.approved.value_counts(), "\n")

# 2) Prepare: features (X) and label (y)
X = df.drop(columns="approved")
y = df["approved"]

# 3) Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0, stratify=y)

# 4) Train a model
model = DecisionTreeClassifier(max_depth=4, random_state=0)
model.fit(X_train, y_train)

# 5) Evaluate on unseen data
pred = model.predict(X_test)
print(f"Test accuracy: {accuracy_score(y_test, pred):.2%}")
print(classification_report(y_test, pred, target_names=["rejected", "approved"]))

# 6) Use the model for a new applicant
new_applicant = pd.DataFrame([{"monthly_income_k": 180, "existing_loans": 1,
                               "years_employed": 6, "credit_score": 710}])
decision = model.predict(new_applicant)[0]
print("New applicant ->", "APPROVED" if decision else "REJECTED")

# Which features mattered most?
for name, imp in sorted(zip(X.columns, model.feature_importances_), key=lambda t: -t[1]):
    print(f"  {name:<18} importance = {imp:.2f}")
