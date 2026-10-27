# groupby_analysis.py - split rows into groups, then summarise each group
import pandas as pd

df = pd.read_csv("shop_sales.csv")
df["revenue"] = df["quantity"] * df["unit_price"]

# Total revenue for each branch
by_branch = df.groupby("branch")["revenue"].sum()
print("Revenue per branch:\n", by_branch)

# Average quantity sold per category
print("\nAverage quantity per category:\n",
      df.groupby("category")["quantity"].mean().round(1))

# Several summaries at once with agg()
summary = df.groupby("category").agg(
    total_revenue=("revenue", "sum"),
    orders=("item", "count"),
    biggest_order=("quantity", "max"),
)
print("\nCategory summary:\n", summary)

# Group by TWO columns
print("\nRevenue per branch and category:\n",
      df.groupby(["branch", "category"])["revenue"].sum())
