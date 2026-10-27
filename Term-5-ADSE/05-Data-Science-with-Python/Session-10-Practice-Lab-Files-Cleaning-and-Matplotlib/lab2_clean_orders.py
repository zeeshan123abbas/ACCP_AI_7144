# lab2_clean_orders.py - Lab 2: clean the combined orders
import pandas as pd

orders = pd.read_pickle("orders_combined.pkl")      # created by Lab 1
print("Before cleaning:", orders.shape)
print("Missing:\n", orders.isnull().sum())

# Task 1: remove exact duplicates
orders = orders.drop_duplicates()

# Task 2: one spelling style for cities
orders["city"] = orders["city"].str.strip().str.title()

# Task 3: quantity can never be negative -> treat as missing
orders.loc[orders["qty"] < 0, "qty"] = None

# Task 4: fill missing quantity with 1 (most orders are single items)
orders["qty"] = orders["qty"].fillna(1).astype(int)

# Task 5: real dates and a revenue column
orders["date"] = pd.to_datetime(orders["date"])
orders["revenue"] = orders["qty"] * orders["price"]

print("\nAfter cleaning:", orders.shape)
print(orders)
orders.to_csv("orders_clean.csv", index=False)
print("\nSaved orders_clean.csv")
