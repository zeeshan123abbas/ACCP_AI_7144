# array_operations.py - indexing, slicing, reshaping and maths
import numpy as np

scores = np.array([55, 72, 89, 40, 95, 63])

# Indexing and slicing (same as lists)
print("first:", scores[0], "last:", scores[-1])
print("first three:", scores[:3])

# Boolean filtering: keep scores of 60 or more
passed = scores[scores >= 60]
print("passed:", passed)

# Element-wise maths
print("plus 5 bonus:", scores + 5)
print("as percentage of 100:", scores / 100)

# Reshape 6 values into 2 rows x 3 columns
grid = scores.reshape(2, 3)
print("grid:\n", grid)
print("row 0:", grid[0])          # first row
print("column 1:", grid[:, 1])    # second column of every row

# Two arrays of the same shape can be combined item by item
quiz = np.array([8, 9, 7])
lab = np.array([10, 6, 9])
print("quiz + lab:", quiz + lab)
