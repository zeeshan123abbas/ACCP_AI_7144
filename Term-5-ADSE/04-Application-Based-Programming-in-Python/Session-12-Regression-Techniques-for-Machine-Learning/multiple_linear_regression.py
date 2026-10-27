# multiple_linear_regression.py - predict house price from several features
# Uses houses.csv (area, bedrooms, age -> price in million Rs)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Step 1: load data and choose features (X) and target (y)
df = pd.read_csv("houses.csv")
X = df[["area_sq_yd", "bedrooms", "age_years"]]
y = df["price_million"]

# Step 2: keep 25% of the houses aside for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 3: train
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: what did it learn? one weight (coefficient) per feature
for feature, weight in zip(X.columns, model.coef_):
    print(f"{feature:<12} weight = {weight:+.3f}")
print(f"intercept    = {model.intercept_:.3f}\n")

# Step 5: evaluate on the TEST set
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)
print(f"MAE  : {mae:.2f} million (average mistake)")
print(f"RMSE : {rmse:.2f} million (punishes big mistakes more)")
print(f"R2   : {r2:.3f} (1.0 = perfect)\n")

# Step 6: compare a few predictions with real prices
comparison = pd.DataFrame({"actual": y_test.values, "predicted": predictions.round(1)})
print(comparison.head())

# Step 7: predict a new house: 200 sq yd, 3 bedrooms, 5 years old
new_house = pd.DataFrame([[200, 3, 5]], columns=X.columns)
print(f"\nNew house price: about {model.predict(new_house)[0]:.1f} million Rs")
