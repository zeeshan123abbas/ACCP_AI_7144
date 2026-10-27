# select_filter_sort.py - choose rows and columns, filter and sort

import pandas as pd

df = pd.read_csv("sales.csv")

# 1) Select columns
print(df[["city", "product", "price"]].head(3), "\n")

# 2) loc[] - select by LABEL (row labels, column names)
print("loc rows 0-2:\n", df.loc[0:2, ["product", "price"]], "\n")

# 3) iloc[] - select by POSITION (numbers only)
print("iloc first 2 rows, first 3 columns:\n", df.iloc[0:2, 0:3], "\n")

# 4) Filter with one condition
karachi = df[df["city"] == "Karachi"]
print("Karachi orders:", len(karachi), "\n")

# 5) Filter with two conditions: & means AND, | means OR (use brackets!)
big_laptops = df[(df["product"] == "Laptop") & (df["price"] > 150000)]
print("Laptops above 150k:\n", big_laptops, "\n")

# 6) isin() - match any value from a list
print(df[df["city"].isin(["Lahore", "Islamabad"])][["city", "product"]], "\n")

# 7) Sort by a column (highest price first)
print(df.sort_values("price", ascending=False)[["product", "price"]].head(3))
