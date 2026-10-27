# evaluation_metrics.py - how good is a classifier? confusion matrix, precision, recall, F1

from sklearn.metrics import (accuracy_score, classification_report, confusion_matrix,
                             f1_score, precision_score, recall_score)

# Imagine a spam filter tested on 12 emails (1 = spam, 0 = not spam)
actual    = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
predicted = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]

# Confusion matrix layout for labels [0, 1]:
#                 predicted 0   predicted 1
#   actual 0         TN            FP
#   actual 1         FN            TP
matrix = confusion_matrix(actual, predicted)
print("Confusion matrix:\n", matrix)
tn, fp, fn, tp = matrix.ravel()
print(f"TP={tp}  TN={tn}  FP={fp}  FN={fn}\n")

# Calculate by hand to understand the formulas
print("Accuracy  (TP+TN)/all   :", round((tp + tn) / len(actual), 2))
print("Precision TP/(TP+FP)    :", round(tp / (tp + fp), 2))
print("Recall    TP/(TP+FN)    :", round(tp / (tp + fn), 2))

# The same numbers from scikit-learn
print("\nsklearn accuracy :", round(accuracy_score(actual, predicted), 2))
print("sklearn precision:", round(precision_score(actual, predicted), 2))
print("sklearn recall   :", round(recall_score(actual, predicted), 2))
print("sklearn F1       :", round(f1_score(actual, predicted), 2))

# A full report for every class at once
print("\n", classification_report(actual, predicted, target_names=["not spam", "spam"]))
