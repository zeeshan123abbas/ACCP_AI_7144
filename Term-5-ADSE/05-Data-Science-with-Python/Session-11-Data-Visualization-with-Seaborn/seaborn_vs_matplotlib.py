# seaborn_vs_matplotlib.py - the same question answered with both libraries
# Question: average marks per campus
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

# --- Matplotlib: we must calculate the averages ourselves ---
averages = df.groupby("campus")["marks"].mean()
plt.figure(figsize=(5, 4))
plt.bar(averages.index, averages.values)
plt.title("Matplotlib: average marks per campus")
plt.ylabel("marks")
plt.savefig("compare_matplotlib.png")
plt.close()

# --- Seaborn: give the DataFrame and column names; it groups, averages,
#     adds axis labels and even error bars (95% confidence interval) ---
plt.figure(figsize=(5, 4))
sns.barplot(data=df, x="campus", y="marks", hue="gender")
plt.title("Seaborn: average marks per campus and gender")
plt.savefig("compare_seaborn.png")
plt.close()

print("Saved compare_matplotlib.png and compare_seaborn.png")
