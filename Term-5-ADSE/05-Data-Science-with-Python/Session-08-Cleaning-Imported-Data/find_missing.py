# find_missing.py - find and fix missing values
import pandas as pd

df = pd.read_csv("raw_customers.csv")
print(df, "\n")

# 1. Where are the blanks? (NaN = "Not a Number" = missing)
print("Missing per column:\n", df.isnull().sum(), "\n")

# 2. Which rows have any missing value?
print("Rows with blanks:\n", df[df.isnull().any(axis=1)], "\n")

# 3. Option A: drop rows that have a missing value
dropped = df.dropna()
print("After dropna:", len(dropped), "rows (was", len(df), ")")

# 4. Option B: impute (fill) missing values
filled = df.copy()
filled["age"] = filled["age"].fillna(filled["age"].median())          # middle value
filled["monthly_spend"] = filled["monthly_spend"].fillna(filled["monthly_spend"].mean())
print("\nAfter filling:\n", filled[["name", "age", "monthly_spend"]])
