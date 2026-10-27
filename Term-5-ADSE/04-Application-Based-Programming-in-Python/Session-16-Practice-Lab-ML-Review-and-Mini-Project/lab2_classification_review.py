# lab2_classification_review.py - full classifier with a Pipeline on a built-in dataset
# Breast cancer dataset: 30 measurements of a tumour -> malignant (0) or benign (1)

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=0, stratify=data.target)

# A Pipeline joins steps: scaling + model. fit() runs them in order, so the
# scaler is automatically fitted on training data only (no leakage).
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print("Confusion matrix:\n", confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions, target_names=data.target_names))
print("ROC-AUC:", round(roc_auc_score(y_test, probabilities), 3))
