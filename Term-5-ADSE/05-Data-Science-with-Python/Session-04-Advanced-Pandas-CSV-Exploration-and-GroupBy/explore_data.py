# explore_data.py - the first commands to run on ANY new dataset
import pandas as pd

df = pd.read_csv("shop_sales.csv")

print("1) shape:", df.shape)                 # rows, columns
print("\n2) first rows:\n", df.head(3))
print("\n3) last rows:\n", df.tail(2))
print("\n4) info (types, missing values):")
df.info()
print("\n5) describe (number statistics):\n", df.describe())
print("\n6) unique branches:", df["branch"].unique())
print("   how many items:", df["item"].nunique())
print("\n7) value counts per category:\n", df["category"].value_counts())
print("\n8) missing values per column:\n", df.isnull().sum())
print("\n9) sorted by quantity (top 3):\n",
      df.sort_values("quantity", ascending=False).head(3))
