# loc_vs_iloc.py - two ways to select rows and columns
import pandas as pd

df = pd.DataFrame({
    "product": ["Pen", "Notebook", "Bag", "Ruler"],
    "price":   [30, 150, 1200, 50],
    "stock":   [500, 200, 25, 300],
}, index=["P1", "P2", "P3", "P4"])     # our own row labels
print(df, "\n")

# loc  -> select by LABEL (row label, column name)
print("loc['P3']:\n", df.loc["P3"], "\n")
print("loc['P2', 'price']:", df.loc["P2", "price"])
print("loc['P1':'P3', ['product', 'stock']]:\n", df.loc["P1":"P3", ["product", "stock"]], "\n")
# Note: with loc the END label 'P3' IS included

# iloc -> select by POSITION number (0, 1, 2 ...)
print("iloc[0]:\n", df.iloc[0], "\n")
print("iloc[1, 1]:", df.iloc[1, 1])
print("iloc[0:2, 0:2]:\n", df.iloc[0:2, 0:2])
# Note: with iloc the END position 2 is NOT included (like Python slices)

# loc with a condition: products that cost more than 100
print("\nExpensive products:\n", df.loc[df["price"] > 100, ["product", "price"]])
