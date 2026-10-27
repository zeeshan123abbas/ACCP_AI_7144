# choose_degree.py - too simple vs too complex: underfitting and overfitting
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

# Made-up data that truly follows a curve, plus noise
rng = np.random.default_rng(seed=0)
x = rng.uniform(0, 10, 60)
y = 3 + 2 * x - 0.3 * x**2 + rng.normal(0, 1.5, 60)
X = x.reshape(-1, 1)

# Keep 30% of the data aside to TEST on data the model has never seen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print("degree | train R2 | test R2")
for degree in [1, 2, 3, 6, 12]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    train_r2 = r2_score(y_train, model.predict(X_train))
    test_r2 = r2_score(y_test, model.predict(X_test))
    print(f"{degree:>6} | {train_r2:8.3f} | {test_r2:7.3f}")

print("\nPick the degree with the best TEST score, not the best train score.")
