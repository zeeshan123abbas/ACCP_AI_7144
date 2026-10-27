# heatmap_and_counts.py - correlation heatmap and category counts
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

# 1. Correlation heatmap: which numbers move together? (-1 to +1)
corr = df[["study_hours", "attendance", "marks"]].corr()
print("Correlation table:\n", corr.round(2))

plt.figure(figsize=(5, 4))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.close()

# 2. Count plot: how many students pass or fail in each campus?
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="campus", hue="result", palette="Set2")
plt.title("Pass / Fail count per campus")
plt.savefig("countplot.png")
plt.close()
print("Saved heatmap.png and countplot.png")
