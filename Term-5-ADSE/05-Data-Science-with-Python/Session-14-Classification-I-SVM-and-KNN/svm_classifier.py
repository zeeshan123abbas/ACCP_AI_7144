# svm_classifier.py - Support Vector Machine with linear and RBF kernels
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline

# 569 tumour samples, 30 measurements, label 0 = malignant, 1 = benign
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1, stratify=y)

# SVM needs scaled features, so we always put a scaler in front
for kernel in ["linear", "rbf"]:
    model = make_pipeline(StandardScaler(), SVC(kernel=kernel, C=1.0))
    model.fit(X_train, y_train)
    print(f"{kernel:<6} kernel accuracy: {model.score(X_test, y_test):.3f}")

# The C setting: small C = wider, softer margin; large C = tries to classify every point
for c in [0.01, 1, 100]:
    model = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=c)).fit(X_train, y_train)
    print(f"C = {c:<5} test accuracy: {model.score(X_test, y_test):.3f}")
