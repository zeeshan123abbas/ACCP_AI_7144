# ridge_lasso.py - regularised regression: Ridge and Lasso keep weights small

import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("houses.csv")

# Add a useless random column to see how each model treats it
df["random_noise"] = [(i * 37) % 11 for i in range(len(df))]

X = df[["area_sq_yd", "bedrooms", "age_years", "random_noise"]]
y = df["price_million"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Scale first so the penalty treats every feature fairly
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

models = {
    "Linear": LinearRegression(),
    "Ridge (alpha=1)": Ridge(alpha=1.0),     # shrinks all weights a little
    "Lasso (alpha=0.5)": Lasso(alpha=0.5),   # can push useless weights to exactly 0
}

for name, model in models.items():
    model.fit(X_train, y_train)
    weights = [round(float(w), 2) for w in model.coef_]
    score = model.score(X_test, y_test)      # score() = R2 for regression
    print(f"{name:<18} weights={weights}  test R2={score:.3f}")
