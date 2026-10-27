# loan_classifier.py - full classification project: will a loan be approved?

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("loan_applications.csv")

# Step 1: feature engineering
df["loan_to_income"] = df["loan_amount_k"] / df["monthly_income_k"]

# Step 2: encode categorical columns
df["approved"] = df["approved"].map({"No": 0, "Yes": 1})
education_order = {"Matric": 0, "Intermediate": 1, "Bachelor": 2, "Master": 3}
df["education"] = df["education"].map(education_order)
df = pd.get_dummies(df, columns=["employment", "city"], drop_first=True, dtype=int)

# Step 3: features (X) and target (y) - app_id is just a number, so drop it
X = df.drop(columns=["app_id", "approved"])
y = df["approved"]
print("Features used:", list(X.columns), "\n")

# Step 4: split, then scale (fit on train only)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=7, stratify=y)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: train and evaluate
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Test accuracy:", round(accuracy_score(y_test, predictions) * 100, 1), "%")

# Step 6: which features push towards approval (+) or rejection (-)?
weights = pd.Series(model.coef_[0], index=X.columns).sort_values()
print("\nFeature weights:\n", weights.round(2))
