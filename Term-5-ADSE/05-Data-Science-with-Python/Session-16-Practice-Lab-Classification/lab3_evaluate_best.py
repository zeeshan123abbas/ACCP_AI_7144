# lab3_evaluate_best.py - Lab 3: final test of the chosen model + business output
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
X_train, y_train = train.drop(columns="churn"), train["churn"]
X_test, y_test = test.drop(columns="churn"), test["churn"]

# Chosen model: Naive Bayes won Lab 2 on F1 (change it if your Lab 2 result differs)
model = GaussianNB()
model.fit(X_train, y_train)

# 1. Final, one-time check on the untouched test set
pred = model.predict(X_test)
print(classification_report(y_test, pred, target_names=["stays", "leaves"]))

ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=["stays", "leaves"],
                                        cmap="Oranges")
plt.title("Churn model (Naive Bayes) - test set")
plt.savefig("churn_confusion_matrix.png")
plt.close()

# 2. Risk list for the retention team: probability of leaving for each test customer
risk = X_test.copy()
risk["leave_probability"] = model.predict_proba(X_test)[:, 1].round(2)
top_risk = risk.sort_values("leave_probability", ascending=False).head(5)
print("Top 5 customers to call:\n",
      top_risk[["months", "monthly_bill", "complaints", "leave_probability"]])

# 3. What drives churn? Naive Bayes has no importance scores,
#    so we ask a random forest to explain which features matter most
forest = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=0)
forest.fit(X_train, y_train)
importance = pd.Series(forest.feature_importances_, index=X_train.columns).sort_values()
print("\nFeature importance (from random forest):\n", importance.round(3))
print("\nSaved churn_confusion_matrix.png")
