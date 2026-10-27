# line_plot.py - a line plot shows CHANGE OVER TIME
import matplotlib
matplotlib.use("Agg")                 # save to file; remove this line to see a window
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
karachi = [24, 26, 29, 32, 34, 33]     # average temperature (made-up)
lahore = [13, 16, 22, 28, 33, 35]

# Draw two lines on the same axes
plt.plot(months, karachi, marker="o", label="Karachi")
plt.plot(months, lahore, marker="s", linestyle="--", label="Lahore")

# Always add a title, axis labels and a legend
plt.title("Average temperature, Jan-Jun")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(alpha=0.3)                    # light grid helps reading values

plt.savefig("line_plot.png", dpi=100)
print("Saved line_plot.png")
