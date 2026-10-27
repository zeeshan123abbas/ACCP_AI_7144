# compare_models_cv.py - compare 5 classifiers fairly with cross-validation and ROC AUC
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import RocCurveDisplay

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0, stratify=y)

models = {
    "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=7)),
    "SVM": make_pipeline(StandardScaler(), SVC(random_state=0)),
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=0),
    "Random Forest": RandomForestClassifier(n_estimators=200, random_state=0),
}

# 1. 5-fold cross-validated F1 on the training data
print("Model          | CV F1 (mean ± std)")
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")
    print(f"{name:<14} | {scores.mean():.3f} ± {scores.std():.3f}")

# 2. ROC curves on the test set (higher curve and AUC = better ranking of cases)
fig, ax = plt.subplots(figsize=(6, 5))
for name, model in models.items():
    model.fit(X_train, y_train)
    RocCurveDisplay.from_estimator(model, X_test, y_test, name=name, ax=ax)
ax.plot([0, 1], [0, 1], "k--", label="random guess")
ax.set_title("ROC curves on the test set")
ax.legend(loc="lower right", fontsize=8)
fig.savefig("roc_curves.png")
print("Saved roc_curves.png")
