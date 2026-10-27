# threshold_and_roc.py - change the decision threshold and measure ROC-AUC

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("loan_applications.csv")
X = df[["monthly_income_k", "loan_amount_k", "credit_score"]]
y = df["approved"].map({"No": 0, "Yes": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y)
model = LogisticRegression(max_iter=1000).fit(X_train, y_train)

# Probability of class 1 (approved) for each test applicant
probabilities = model.predict_proba(X_test)[:, 1]

# The default threshold is 0.5. A bank that fears bad loans may want 0.7
for threshold in [0.3, 0.5, 0.7]:
    predictions = (probabilities >= threshold).astype(int)
    print(f"threshold {threshold}: precision={precision_score(y_test, predictions):.2f} "
          f"recall={recall_score(y_test, predictions):.2f}")

# ROC-AUC: how well the model RANKS approved above rejected (1.0 perfect, 0.5 random)
print("\nROC-AUC:", round(roc_auc_score(y_test, probabilities), 3))
