# lab3_salary_regression.py - predict salary with multiple linear regression
# Run lab1_clean_explore.py first

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("employees_clean.csv")

# Step 1: encode text columns
df["is_master"] = (df["education"] == "Master").astype(int)          # Bachelor=0, Master=1
df = pd.get_dummies(df, columns=["department"], dtype=int)           # one-hot

# Step 2: features and target
feature_columns = ["experience_years", "is_master",
                   "department_HR", "department_IT", "department_Sales"]
X = df[feature_columns]
y = df["salary_k"]

# Step 3: split, train, evaluate
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression().fit(X_train, y_train)
predictions = model.predict(X_test)
print("MAE:", round(mean_absolute_error(y_test, predictions), 2), "k Rs")
print("R2 :", round(r2_score(y_test, predictions), 3))

# Step 4: what each feature adds to salary
for name, weight in zip(feature_columns, model.coef_):
    print(f"  {name:<18} {weight:+.1f}")

# Step 5: predict for a new IT employee, 5 years, Master degree
new_person = pd.DataFrame([[5, 1, 0, 1, 0]], columns=feature_columns)
print("Predicted salary:", round(model.predict(new_person)[0]), "k Rs")
