# distribution_plots.py - how are the marks spread out?
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")
sns.set_theme(style="whitegrid")                   # one line for a clean look

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# 1. Histogram with a smooth density curve (kde)
sns.histplot(data=df, x="marks", kde=True, ax=axes[0])
axes[0].set_title("Histogram + KDE")

# 2. Box plot per campus: median, spread and outliers side by side
sns.boxplot(data=df, x="campus", y="marks", ax=axes[1])
axes[1].set_title("Box plot by campus")

# 3. Violin plot: box plot + shape of the distribution
sns.violinplot(data=df, x="result", y="study_hours", ax=axes[2])
axes[2].set_title("Study hours for Pass vs Fail")

fig.tight_layout()
fig.savefig("distributions.png")
print("Saved distributions.png")
