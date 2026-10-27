# histogram_boxplot.py - see how values are DISTRIBUTED
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 200 made-up exam marks around 65, plus two unusual high scores
rng = np.random.default_rng(seed=1)
marks = rng.normal(loc=65, scale=10, size=200).round()
marks = np.append(marks, [99, 100])

# Histogram: how many students fall in each range (bin) of marks
plt.figure(figsize=(6, 4))
plt.hist(marks, bins=15, color="orange", edgecolor="black")
plt.axvline(marks.mean(), color="red", linestyle="--", label=f"mean = {marks.mean():.1f}")
plt.title("Distribution of marks")
plt.xlabel("Marks")
plt.ylabel("Number of students")
plt.legend()
plt.savefig("histogram.png")
plt.close()

# Box plot: median, middle 50% (the box) and outliers (dots)
plt.figure(figsize=(4, 5))
plt.boxplot(marks)
plt.title("Box plot of marks")
plt.ylabel("Marks")
plt.savefig("boxplot.png")
plt.close()

print("Saved histogram.png and boxplot.png")
