# lab3_visual_report.py - Lab 3: answer questions with charts
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

orders = pd.read_csv("orders_clean.csv", parse_dates=["date"])   # created by Lab 2

# Questions -> summaries
by_city = orders.groupby("city")["revenue"].sum().sort_values()
by_product = orders.groupby("product")["qty"].sum().sort_values(ascending=False)
by_day = orders.groupby("date")["revenue"].sum()
by_channel = orders.groupby("channel")["revenue"].sum()

fig, axes = plt.subplots(2, 2, figsize=(11, 7))

axes[0, 0].barh(by_city.index, by_city.values, color="teal")
axes[0, 0].set_title("Q1: Which city earns most?")

axes[0, 1].bar(by_product.index, by_product.values, color="orange")
axes[0, 1].set_title("Q2: Which product sells most units?")
axes[0, 1].tick_params(axis="x", rotation=20)

axes[1, 0].plot(by_day.index, by_day.values, marker="o")
axes[1, 0].set_title("Q3: How does daily revenue change?")
axes[1, 0].tick_params(axis="x", rotation=30)

axes[1, 1].pie(by_channel.values, labels=by_channel.index, autopct="%1.0f%%")
axes[1, 1].set_title("Q4: Online vs shop share")

fig.suptitle("Electronics store - March orders")
fig.tight_layout()
fig.savefig("orders_report.png")
print("Saved orders_report.png")
print("Top city:", by_city.idxmax(), "| Top product:", by_product.idxmax())
