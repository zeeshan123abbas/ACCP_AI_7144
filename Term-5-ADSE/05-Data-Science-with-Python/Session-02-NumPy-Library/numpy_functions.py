# numpy_functions.py - built-in statistics and maths functions
import numpy as np

# Daily temperatures in Karachi for one week (made-up)
temps = np.array([31, 33, 34, 32, 35, 36, 30])

print("mean:", temps.mean())
print("median:", np.median(temps))
print("std (spread):", round(temps.std(), 2))
print("min/max:", temps.min(), temps.max())
print("day of max (index):", temps.argmax())
print("sorted:", np.sort(temps))
print("rounded square roots:", np.round(np.sqrt(temps), 2))

# Statistics along an axis of a 2-D array
# rows = students, columns = subjects
marks = np.array([[70, 80, 90],
                  [60, 75, 85],
                  [88, 92, 79]])
print("average per student (axis=1):", marks.mean(axis=1).round(1))
print("average per subject (axis=0):", marks.mean(axis=0).round(1))

# np.where: choose a value based on a condition
result = np.where(temps >= 34, "Hot", "Warm")
print("labels:", result)
