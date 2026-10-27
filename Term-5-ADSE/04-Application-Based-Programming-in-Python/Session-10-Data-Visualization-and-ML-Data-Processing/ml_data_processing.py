# ml_data_processing.py - prepare raw data for a machine learning model
# Install once:  pip install pandas scikit-learn

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Raw data: has missing values, text columns and very different number ranges
df = pd.DataFrame({
    "age":    [22, 25, None, 30, 28, 35, 40, None, 23, 31],
    "salary": [40000, 52000, 61000, None, 58000, 90000, 120000, 75000, 43000, 66000],
    "city":   ["Karachi", "Lahore", "Karachi", "Islamabad", "Lahore",
               "Karachi", "Islamabad", "Lahore", "Karachi", "Lahore"],
    "bought": ["no", "no", "yes", "yes", "no", "yes", "yes", "yes", "no", "yes"],
})
print("RAW DATA:\n", df, "\n")

# STEP 1: fill missing numbers with the column mean
imputer = SimpleImputer(strategy="mean")
df[["age", "salary"]] = imputer.fit_transform(df[["age", "salary"]])

# STEP 2: encode text -> numbers
# 2a) the target yes/no becomes 1/0
df["bought"] = df["bought"].map({"no": 0, "yes": 1})
# 2b) city has no order, so use one-hot encoding (one 0/1 column per city)
df = pd.get_dummies(df, columns=["city"], dtype=int)
print("AFTER IMPUTING + ENCODING:\n", df, "\n")

# STEP 3: split features (X) and target (y)
X = df.drop(columns=["bought"])
y = df["bought"]

# STEP 4: split into training and testing sets (80% / 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print("Train rows:", len(X_train), "| Test rows:", len(X_test))

# STEP 5: scale numbers so age (20s) and salary (100,000s) are comparable
scaler = StandardScaler()                         # result: mean 0, std 1
X_train[["age", "salary"]] = scaler.fit_transform(X_train[["age", "salary"]])
X_test[["age", "salary"]] = scaler.transform(X_test[["age", "salary"]])  # only transform!
print("\nSCALED TRAINING DATA:\n", X_train.round(2))

# Bonus: MinMaxScaler squeezes values into the range 0..1
print("\nMin-max scaled salary:",
      MinMaxScaler().fit_transform(df[["salary"]]).round(2).ravel())
