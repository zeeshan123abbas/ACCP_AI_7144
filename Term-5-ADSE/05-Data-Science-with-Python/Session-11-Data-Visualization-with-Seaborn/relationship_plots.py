# relationship_plots.py - how do two or more numbers relate?
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")
sns.set_theme(style="ticks")

# 1. Scatter plot with colour (hue) and marker style for extra variables
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="study_hours", y="marks", hue="result", style="gender")
plt.title("Study hours vs marks")
plt.savefig("scatter_hue.png")
plt.close()

# 2. Regression plot: scatter + best-fit straight line
plt.figure(figsize=(6, 4))
sns.regplot(data=df, x="attendance", y="marks", color="purple")
plt.title("Attendance vs marks with trend line")
plt.savefig("regplot.png")
plt.close()

# 3. Pair plot: every numeric column against every other in one picture
grid = sns.pairplot(df, vars=["study_hours", "attendance", "marks"], hue="result")
grid.savefig("pairplot.png")
print("Saved scatter_hue.png, regplot.png, pairplot.png")
