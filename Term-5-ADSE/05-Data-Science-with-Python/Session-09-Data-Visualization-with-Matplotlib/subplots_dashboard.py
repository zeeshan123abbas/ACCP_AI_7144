# subplots_dashboard.py - several charts in ONE figure (a mini dashboard)
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Weekly data of a small online shop
df = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "orders": [32, 28, 40, 35, 50, 72, 65],
    "returns": [2, 1, 3, 2, 4, 6, 5],
})

# 2 rows x 2 columns of charts; axes is a 2x2 grid of plot areas
fig, axes = plt.subplots(2, 2, figsize=(10, 7))

axes[0, 0].plot(df["day"], df["orders"], marker="o")
axes[0, 0].set_title("Orders per day (trend)")

axes[0, 1].bar(df["day"], df["returns"], color="tomato")
axes[0, 1].set_title("Returns per day (compare)")

axes[1, 0].scatter(df["orders"], df["returns"])
axes[1, 0].set_title("Orders vs returns (relationship)")
axes[1, 0].set_xlabel("orders")
axes[1, 0].set_ylabel("returns")

weekend = df["orders"][df["day"].isin(["Sat", "Sun"])].sum()
weekday = df["orders"].sum() - weekend
axes[1, 1].pie([weekday, weekend], labels=["Weekdays", "Weekend"], autopct="%1.0f%%")
axes[1, 1].set_title("Share of orders (part of whole)")

fig.suptitle("Shop dashboard - one week")
fig.tight_layout()                                  # stop titles from overlapping
fig.savefig("dashboard.png")
print("Saved dashboard.png")
