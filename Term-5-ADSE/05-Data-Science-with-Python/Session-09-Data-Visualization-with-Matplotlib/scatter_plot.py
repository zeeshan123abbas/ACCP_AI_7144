# scatter_plot.py - a scatter plot shows the RELATIONSHIP between two numbers
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ad_spend = [5, 8, 12, 15, 18, 22, 25, 30]          # thousand rupees on ads
sales = [40, 52, 60, 75, 80, 95, 102, 120]         # thousand rupees of sales
city_size = [30, 60, 90, 40, 120, 70, 150, 100]    # used for dot size

plt.figure(figsize=(6, 4))
plt.scatter(ad_spend, sales, s=city_size, c=sales, cmap="viridis", alpha=0.8)
plt.colorbar(label="Sales")                        # explains the colours
plt.title("Advertising spend vs sales")
plt.xlabel("Ad spend (Rs 000)")
plt.ylabel("Sales (Rs 000)")

# Point out one interesting dot with an annotation
plt.annotate("best month", xy=(30, 120), xytext=(18, 112),
             arrowprops={"arrowstyle": "->"})

plt.savefig("scatter_plot.png")
print("Saved scatter_plot.png")
