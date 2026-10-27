# explore_csv.py - load a CSV file and explore it

import pandas as pd

df = pd.read_csv("sales.csv")

print("First 5 rows:\n", df.head(), "\n")
print("Last 3 rows:\n", df.tail(3), "\n")

# info(): columns, non-null counts and types (shows missing values!)
df.info()

# describe(): statistics for numeric columns
print("\n", df.describe())

# Count values in a text column
print("\nOrders per city:\n", df["city"].value_counts())

# Unique values
print("\nProducts:", df["product"].unique().tolist())
