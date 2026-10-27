# lab5_save_and_load_model.py - save a trained model to a file and use it later
# joblib is installed together with scikit-learn

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# --- Part 1: train once and save ---
iris = load_iris()
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=500))
model.fit(iris.data, iris.target)
joblib.dump(model, "iris_model.joblib")
print("Model saved to iris_model.joblib")

# --- Part 2: later (e.g. inside a Flask app or Tkinter GUI) load and predict ---
loaded_model = joblib.load("iris_model.joblib")
flower = [[5.1, 3.5, 1.4, 0.2]]
species = iris.target_names[loaded_model.predict(flower)[0]]
print("Loaded model says the flower is:", species)
