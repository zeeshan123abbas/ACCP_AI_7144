# dataframe_basics.py - Pandas DataFrame: a table of rows and columns

import pandas as pd

# 1) Create a DataFrame from a dictionary (each key = one column)
data = {
    "name": ["Ali", "Sara", "Usman", "Hira"],
    "course": ["Python", "Flutter", "Python", "Dart"],
    "marks": [78, 92, 65, 88],
}
df = pd.DataFrame(data)
print(df, "\n")

# 2) Basic information
print("Shape (rows, columns):", df.shape)
print("Columns:", list(df.columns))
print("Data types:\n", df.dtypes, "\n")

# 3) One column is a Series
print(type(df["marks"]))

# 4) Add a new column calculated from another
df["passed"] = df["marks"] >= 70
print(df, "\n")

# 5) Add a new row with pd.concat
new_row = pd.DataFrame([{"name": "Zara", "course": "Python", "marks": 81, "passed": True}])
df = pd.concat([df, new_row], ignore_index=True)
print(df, "\n")

# 6) Remove a column
df = df.drop(columns=["passed"])
print(df)
