# series_operations.py - maths, filtering and statistics on a Series
import pandas as pd

sales = pd.Series([1200, 950, 1800, 400, 1500],
                  index=["Mon", "Tue", "Wed", "Thu", "Fri"])

# Maths applies to every value (like NumPy)
print("Sales after 5% discount:\n", sales * 0.95)

# Filtering with a condition
print("\nGood days (> 1000):\n", sales[sales > 1000])

# Quick statistics
print("\nTotal:", sales.sum())
print("Average:", sales.mean())
print("Best day:", sales.idxmax())    # label of the largest value
print("\nSorted high to low:\n", sales.sort_values(ascending=False))

# Two Series line up by label automatically
target = pd.Series([1000, 1000, 1500, 1000, 1200],
                   index=["Mon", "Tue", "Wed", "Thu", "Fri"])
print("\nAbove target by:\n", sales - target)
