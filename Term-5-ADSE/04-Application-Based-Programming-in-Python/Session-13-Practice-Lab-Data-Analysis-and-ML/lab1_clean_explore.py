# lab1_clean_explore.py - load, clean and summarise employee data with Pandas

import pandas as pd

df = pd.read_csv("employees.csv")

# 1) First look
print(df.head(), "\n")
print("Rows and columns:", df.shape)
print("Missing values:\n", df.isnull().sum(), "\n")

# 2) Clean: fill each gap with a sensible value
df["experience_years"] = df["experience_years"].fillna(df["experience_years"].median())
df["salary_k"] = df["salary_k"].fillna(df["salary_k"].mean()).round()
df["rating"] = df["rating"].fillna(df["rating"].mean()).round(1)

# 3) Summaries
print("Average salary per department:\n",
      df.groupby("department")["salary_k"].mean().round(1), "\n")
print("Head-count by department and education:\n",
      pd.crosstab(df["department"], df["education"]), "\n")

# 4) Top 3 earners
print("Top 3 earners:\n",
      df.sort_values("salary_k", ascending=False)[["name", "department", "salary_k"]].head(3))

# 5) Save clean data for the next labs
df.to_csv("employees_clean.csv", index=False)
print("\nSaved employees_clean.csv")
