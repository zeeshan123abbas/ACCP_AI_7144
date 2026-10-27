# lab2_compare_models.py - Lab 2: train five classifiers and compare them
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv("train.csv")                 # created by Lab 1
X_train = train.drop(columns="churn")
y_train = train["churn"]

models = {
    "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=9)),
    "SVM": make_pipeline(StandardScaler(), SVC()),
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=0),
    "Random Forest": RandomForestClassifier(n_estimators=200, max_depth=6, random_state=0),
}

# Recall matters: we want to FIND the customers who are about to leave
rows = []
for name, model in models.items():
    recall = cross_val_score(model, X_train, y_train, cv=5, scoring="recall").mean()
    f1 = cross_val_score(model, X_train, y_train, cv=5, scoring="f1").mean()
    accuracy = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy").mean()
    rows.append({"model": name, "accuracy": accuracy, "recall": recall, "f1": f1})

results = pd.DataFrame(rows).sort_values("f1", ascending=False).round(3)
print(results.to_string(index=False))
results.to_csv("model_comparison.csv", index=False)
print("\nBest by F1:", results.iloc[0]["model"])
