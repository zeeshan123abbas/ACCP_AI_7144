# more_charts.py - histogram, pie, scatter and subplots in ONE figure

import matplotlib.pyplot as plt
import numpy as np

# Make sample data (seed = same "random" numbers every run)
rng = np.random.default_rng(seed=42)
marks = rng.normal(loc=65, scale=12, size=200)        # 200 students' marks
study_hours = rng.uniform(1, 10, size=50)
exam_score = study_hours * 8 + rng.normal(0, 6, size=50)

# subplots(2, 2) gives a 2x2 grid of small charts ("axes")
fig, axes = plt.subplots(2, 2, figsize=(10, 7))

# 1) Histogram: how values are spread (distribution)
axes[0, 0].hist(marks, bins=15, color="skyblue", edgecolor="black")
axes[0, 0].set_title("Histogram: marks distribution")

# 2) Pie chart: parts of a whole
axes[0, 1].pie([45, 30, 25], labels=["Mobile", "Desktop", "Tablet"],
               autopct="%1.0f%%", startangle=90)
axes[0, 1].set_title("Pie: visitors by device")

# 3) Scatter plot: relationship between two numbers
axes[1, 0].scatter(study_hours, exam_score, color="green")
axes[1, 0].set_xlabel("Study hours")
axes[1, 0].set_ylabel("Exam score")
axes[1, 0].set_title("Scatter: hours vs score")

# 4) Horizontal bar chart
axes[1, 1].barh(["Laptop", "Mouse", "Monitor"], [603, 13, 125], color="orange")
axes[1, 1].set_title("Revenue by product (thousand Rs)")

plt.tight_layout()                    # stop titles from overlapping
plt.savefig("dashboard.png")
plt.show()
