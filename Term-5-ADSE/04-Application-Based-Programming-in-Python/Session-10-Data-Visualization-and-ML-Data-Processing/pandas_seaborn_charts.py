# pandas_seaborn_charts.py - quick charts straight from a DataFrame + Seaborn
# Install once:  pip install pandas matplotlib seaborn

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame({
    "course": ["Python", "Python", "Flutter", "Flutter", "Dart", "Dart", "Python", "Flutter"],
    "hours":  [5, 8, 4, 7, 3, 6, 9, 5],
    "marks":  [62, 81, 58, 77, 50, 70, 90, 66],
    "attendance": [70, 90, 65, 85, 60, 80, 95, 75],
})

# 1) Pandas can draw directly (it uses Matplotlib behind the scenes)
df.groupby("course")["marks"].mean().plot(kind="bar", title="Average marks per course")
plt.ylabel("Average marks")
plt.tight_layout()
plt.savefig("pandas_bar.png")
plt.show()

# 2) Seaborn box plot: median, spread and outliers per group
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks spread per course")
plt.savefig("seaborn_box.png")
plt.show()

# 3) Seaborn heatmap of correlations (how strongly columns move together)
correlation = df[["hours", "marks", "attendance"]].corr()
print(correlation.round(2))
sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation heatmap")
plt.tight_layout()
plt.savefig("seaborn_heatmap.png")
plt.show()
