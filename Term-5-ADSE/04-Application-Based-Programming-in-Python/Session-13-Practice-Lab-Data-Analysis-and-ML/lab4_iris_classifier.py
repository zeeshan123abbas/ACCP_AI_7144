# lab4_iris_classifier.py - classify flowers with Logistic Regression
# The Iris dataset is built into scikit-learn (no download needed)

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Step 1: load the data (150 flowers, 4 measurements, 3 species)
iris = load_iris()
X, y = iris.data, iris.target
print("Features:", iris.feature_names)
print("Species :", iris.target_names.tolist())

# Step 2: split 70% train / 30% test; stratify keeps species balanced
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# Step 3: train
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 4: evaluate
predictions = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, predictions) * 100, 1), "%")

# Step 5: predict a new flower (sepal length, sepal width, petal length, petal width in cm)
new_flower = [[6.0, 2.9, 4.5, 1.5]]
species_number = model.predict(new_flower)[0]
print("New flower is:", iris.target_names[species_number])
