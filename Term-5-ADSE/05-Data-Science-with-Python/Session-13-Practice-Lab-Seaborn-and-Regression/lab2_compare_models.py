# lab2_compare_models.py - Lab 2: linear vs polynomial vs logarithmic for size -> rent
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

df = pd.read_csv("karachi_rent.csv")
df = df[df["area"] == "Gulshan"]                    # one area, so only size matters
X = df[["size_sqyd"]]
y = df["rent"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

results = {}

# Model 1: straight line
linear = LinearRegression().fit(X_train, y_train)
results["linear"] = r2_score(y_test, linear.predict(X_test))

# Model 2: polynomial degree 2
poly = make_pipeline(PolynomialFeatures(2), LinearRegression()).fit(X_train, y_train)
results["polynomial (2)"] = r2_score(y_test, poly.predict(X_test))

# Model 3: logarithmic curve with curve_fit
def log_curve(x, a, b):
    return a + b * np.log(x)

(a, b), _ = curve_fit(log_curve, X_train["size_sqyd"], y_train)
results["logarithmic"] = r2_score(y_test, log_curve(X_test["size_sqyd"], a, b))

print("Test R2 for each model:")
for name, score in results.items():
    print(f"  {name:<15} {score:.3f}")
print("Best model:", max(results, key=results.get))
