# lab1_explore_seaborn.py - Lab 1: explore the rent data visually
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("karachi_rent.csv")
print(df.describe().round(0))

sns.set_theme(style="whitegrid", palette="Set2")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Q1: how are rents spread?
sns.histplot(data=df, x="rent", kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Q1: Distribution of rent")

# Q2: which area is most expensive?
sns.boxplot(data=df, x="area", y="rent", ax=axes[0, 1])
axes[0, 1].set_title("Q2: Rent by area")

# Q3: is the size-rent link straight or curved?
sns.scatterplot(data=df, x="size_sqyd", y="rent", hue="area", ax=axes[1, 0])
axes[1, 0].set_title("Q3: Size vs rent")

# Q4: which numbers move together?
corr = df[["size_sqyd", "building_age", "rent"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=axes[1, 1])
axes[1, 1].set_title("Q4: Correlation")

fig.tight_layout()
fig.savefig("lab1_explore.png")
print("Saved lab1_explore.png")
