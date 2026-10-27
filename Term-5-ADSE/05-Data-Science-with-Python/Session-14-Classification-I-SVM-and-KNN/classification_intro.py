# classification_intro.py - classification = predicting a CATEGORY (label)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Features (inputs) and label (output): will a student pass?
df = pd.DataFrame({
    "study_hours": [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 1.5, 6.5],
    "attendance":  [50, 60, 55, 65, 70, 80, 75, 85, 90, 95, 58, 88],
    "result":      ["Fail", "Fail", "Fail", "Fail", "Pass", "Pass",
                    "Pass", "Pass", "Pass", "Pass", "Fail", "Pass"],
})

X = df[["study_hours", "attendance"]]     # features: capital X (a table)
y = df["result"]                          # label: small y (one column)

# Split: the model learns from train, we check it on test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
print("Train rows:", len(X_train), "| Test rows:", len(X_test))

# Every scikit-learn model follows the same 3 steps
model = KNeighborsClassifier(n_neighbors=3)   # 1. create
model.fit(X_train, y_train)                   # 2. learn
predictions = model.predict(X_test)           # 3. predict

print("Predicted:", list(predictions))
print("Actual   :", list(y_test))
print("Accuracy :", model.score(X_test, y_test))

# Predict a brand-new student
new_student = pd.DataFrame({"study_hours": [4.5], "attendance": [72]})
print("New student ->", model.predict(new_student)[0])
