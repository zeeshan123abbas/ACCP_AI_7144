# lab1_numpy_marks.py - Lab 1: analyse class marks with NumPy
import numpy as np

# Rows = 6 students, columns = 3 subjects (Python, Stats, English)
names = np.array(["Ali", "Sara", "Omar", "Zoya", "Hamza", "Iqra"])
marks = np.array([
    [78, 65, 80],
    [92, 88, 85],
    [45, 52, 60],
    [67, 74, 70],
    [55, 40, 58],
    [88, 91, 79],
])

# Task 1: total and average per student (across the row -> axis=1)
totals = marks.sum(axis=1)
averages = marks.mean(axis=1).round(1)
for name, total, avg in zip(names, totals, averages):
    print(f"{name:<6} total={total}  average={avg}")

# Task 2: average per subject (down the column -> axis=0)
print("\nSubject averages:", marks.mean(axis=0).round(1))

# Task 3: the topper
print("Topper:", names[totals.argmax()])

# Task 4: grade labels with np.select (several conditions)
conditions = [averages >= 80, averages >= 60, averages >= 50]
grades = ["A", "B", "C"]
labels = np.select(conditions, grades, default="F")
print("Grades:", dict(zip(names.tolist(), labels.tolist())))

# Task 5: how many students failed any subject (mark below 50)?
failed_any = (marks < 50).any(axis=1)
print("Failed at least one subject:", names[failed_any])
