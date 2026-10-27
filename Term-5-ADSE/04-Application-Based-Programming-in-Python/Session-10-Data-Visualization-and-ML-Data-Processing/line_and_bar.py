# line_and_bar.py - your first charts with Matplotlib
# Install once:  pip install matplotlib

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_karachi = [120, 135, 150, 145, 170, 190]
sales_lahore = [100, 110, 130, 150, 160, 175]

# ---- Chart 1: line chart (good for a trend over time) ----
plt.figure(figsize=(7, 4))                         # size in inches
plt.plot(months, sales_karachi, marker="o", label="Karachi")
plt.plot(months, sales_lahore, marker="s", linestyle="--", label="Lahore")
plt.title("Monthly Sales (thousand Rs)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()                                       # shows the labels
plt.grid(True, alpha=0.3)
plt.savefig("line_chart.png")                      # save as an image
plt.show()                                         # open the chart window

# ---- Chart 2: bar chart (good for comparing categories) ----
courses = ["Python", "Flutter", "Dart", "React"]
students = [45, 30, 18, 25]

plt.figure(figsize=(6, 4))
plt.bar(courses, students, color=["#3776AB", "#02569B", "#0175C2", "#61DAFB"])
plt.title("Students per Course")
plt.ylabel("Number of students")
for index, value in enumerate(students):           # write the value on each bar
    plt.text(index, value + 0.5, str(value), ha="center")
plt.savefig("bar_chart.png")
plt.show()
