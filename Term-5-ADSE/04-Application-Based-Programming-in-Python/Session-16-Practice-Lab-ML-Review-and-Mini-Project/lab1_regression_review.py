# lab1_regression_review.py - compare regression models on a built-in medical dataset
# Diabetes dataset: 10 health measurements -> disease progression score after one year

from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True, as_frame=True)
print("Features:", list(X.columns))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Linear": LinearRegression(),
    "Ridge": Ridge(alpha=0.5),
    "Lasso": Lasso(alpha=0.1),
}

print(f"\n{'Model':<8} {'MAE':>6} {'R2':>6}")
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"{name:<8} {mean_absolute_error(y_test, predictions):6.1f} "
          f"{r2_score(y_test, predictions):6.3f}")

# Which features did Lasso switch off (weight exactly 0)?
lasso = models["Lasso"]
removed = [col for col, w in zip(X.columns, lasso.coef_) if w == 0]
print("\nFeatures removed by Lasso:", removed)
