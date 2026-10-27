# series_basics.py - Pandas Series: a single labelled column
# Install once:  pip install pandas

import pandas as pd

# 1) Create a Series from a list (labels 0,1,2... are added automatically)
marks = pd.Series([78, 92, 65, 88])
print(marks, "\n")

# 2) Create a Series with our own labels (the "index")
marks = pd.Series([78, 92, 65, 88], index=["Ali", "Sara", "Usman", "Hira"])
print(marks, "\n")

# 3) Access values by label or by position
print("Sara:", marks["Sara"])
print("First value:", marks.iloc[0])

# 4) Vector maths - applies to every value at once (no loop needed)
print("\nWith 5 bonus marks:\n", marks + 5)

# 5) Filtering with a condition
print("\nPassed (>= 70):\n", marks[marks >= 70])

# 6) Quick statistics
print("\nMean:", marks.mean(), "| Max:", marks.max(), "| Top student:", marks.idxmax())

# 7) A Series from a dictionary
fees = pd.Series({"Python": 25000, "Flutter": 30000, "Dart": 15000})
print("\n", fees)
