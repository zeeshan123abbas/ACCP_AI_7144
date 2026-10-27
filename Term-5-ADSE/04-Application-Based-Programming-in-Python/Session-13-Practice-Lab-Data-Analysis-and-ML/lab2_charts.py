# lab2_charts.py - three charts that explain the employee data
# Run lab1_clean_explore.py first (it creates employees_clean.csv)

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("employees_clean.csv")

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Chart 1: bar - average salary per department
avg_salary = df.groupby("department")["salary_k"].mean()
axes[0].bar(avg_salary.index, avg_salary.values, color="teal")
axes[0].set_title("Average salary (k Rs)")

# Chart 2: scatter - experience vs salary
axes[1].scatter(df["experience_years"], df["salary_k"], color="purple")
axes[1].set_xlabel("Experience (years)")
axes[1].set_ylabel("Salary (k Rs)")
axes[1].set_title("Experience vs salary")

# Chart 3: histogram - performance ratings
axes[2].hist(df["rating"], bins=6, color="orange", edgecolor="black")
axes[2].set_title("Rating distribution")

plt.tight_layout()
plt.savefig("employee_charts.png")
plt.show()
