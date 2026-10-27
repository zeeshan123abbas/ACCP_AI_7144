# case_study_bakery.py - a short real-time style case study
# Owner asks: "Which branch earns most, what sells best, and which day was busiest?"
import pandas as pd
import matplotlib
matplotlib.use("Agg")                 # save charts to files
import matplotlib.pyplot as plt

# 1. Load and prepare
df = pd.read_csv("shop_sales.csv", parse_dates=["date"])
df["revenue"] = df["quantity"] * df["unit_price"]

# 2. Best branch
branch_revenue = df.groupby("branch")["revenue"].sum().sort_values(ascending=False)
print("Best branch:", branch_revenue.index[0], "Rs", branch_revenue.iloc[0])

# 3. Best-selling item by quantity
item_qty = df.groupby("item")["quantity"].sum().sort_values(ascending=False)
print("Best-selling item:", item_qty.index[0], "-", item_qty.iloc[0], "units")

# 4. Busiest day by revenue
day_revenue = df.groupby("date")["revenue"].sum()
print("Busiest day:", day_revenue.idxmax().date(), "Rs", day_revenue.max())

# 5. Share of revenue per category (in percent)
share = df.groupby("category")["revenue"].sum() / df["revenue"].sum() * 100
print("\nRevenue share %:\n", share.round(1))

# 6. Quick bar chart of branch revenue
branch_revenue.plot(kind="bar", color="orange", title="Revenue by branch (Rs)")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("branch_revenue.png")
print("\nChart saved as branch_revenue.png")
