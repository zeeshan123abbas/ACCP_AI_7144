# clean_and_group.py - fix missing values and duplicates, then summarise

import pandas as pd

df = pd.read_csv("sales.csv")

# 1) Find problems
print("Missing values per column:\n", df.isnull().sum(), "\n")
print("Duplicate rows:", df.duplicated().sum(), "\n")

# 2) Remove duplicate rows
df = df.drop_duplicates()

# 3) Fill missing values
df["quantity"] = df["quantity"].fillna(1)                 # assume 1 item
df["price"] = df["price"].fillna(df["price"].median())    # use the middle price
df["quantity"] = df["quantity"].astype(int)               # 1.0 -> 1

# 4) Create a calculated column
df["total"] = df["quantity"] * df["price"]

# 5) Convert text dates into real dates
df["date"] = pd.to_datetime(df["date"])
df["day_name"] = df["date"].dt.day_name()

print(df[["order_id", "product", "quantity", "price", "total", "day_name"]], "\n")

# 6) groupby: total sales per city
print("Sales per city:\n", df.groupby("city")["total"].sum(), "\n")

# 7) Several summaries at once
summary = df.groupby("product").agg(orders=("order_id", "count"),
                                    items=("quantity", "sum"),
                                    revenue=("total", "sum"))
print(summary.sort_values("revenue", ascending=False))

# 8) Save the clean data
df.to_csv("sales_clean.csv", index=False)
print("\nSaved sales_clean.csv")
