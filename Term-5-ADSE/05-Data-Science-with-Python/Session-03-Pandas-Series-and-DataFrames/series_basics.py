# series_basics.py - a Series is ONE column of data with labels
import pandas as pd

# 1. Series from a list (labels are 0, 1, 2 ... by default)
marks = pd.Series([78, 85, 62, 91])
print(marks)

# 2. Series with our own labels (the index)
prices = pd.Series([250, 120, 80], index=["burger", "fries", "drink"])
print("\n", prices)

# 3. Series from a dictionary (keys become labels)
population = pd.Series({"Karachi": 20.4, "Lahore": 13.0, "Faisalabad": 3.6})
print("\nPopulation in millions:\n", population)

# Reading values
print("\nPrice of fries:", prices["fries"])     # by label
print("First mark:", marks[0])                   # by default number label
