# evaluate_classifier.py - confusion matrix, precision, recall and F1
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, classification_report, ConfusionMatrixDisplay)

X, y = load_breast_cancer(return_X_y=True)
# In this dataset 0 = malignant (cancer), 1 = benign. We care about catching cancer,
# so we flip the labels: 1 = malignant (the "positive" class we want to find)
y = 1 - y
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=4, stratify=y)

model = GaussianNB().fit(X_train, y_train)          # Naive Bayes for number features
pred = model.predict(X_test)

# The confusion matrix counts each kind of right and wrong answer
tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
print(f"True positives : {tp}  (cancer found)")
print(f"True negatives : {tn}  (healthy correctly cleared)")
print(f"False positives: {fp}  (false alarm)")
print(f"False negatives: {fn}  (cancer MISSED - the dangerous mistake)")

print("\nAccuracy :", round(accuracy_score(y_test, pred), 3))
print("Precision:", round(precision_score(y_test, pred), 3), " = TP / (TP + FP)")
print("Recall   :", round(recall_score(y_test, pred), 3), " = TP / (TP + FN)")
print("F1 score :", round(f1_score(y_test, pred), 3), " = balance of precision and recall")

print("\n", classification_report(y_test, pred, target_names=["benign", "malignant"]))

ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=["benign", "malignant"],
                                        cmap="Blues")
plt.title("Confusion matrix - Naive Bayes")
plt.savefig("confusion_matrix.png")
print("Saved confusion_matrix.png")
