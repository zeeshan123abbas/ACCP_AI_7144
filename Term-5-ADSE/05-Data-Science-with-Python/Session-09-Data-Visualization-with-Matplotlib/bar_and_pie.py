# bar_and_pie.py - bar charts COMPARE categories, pie charts show PARTS OF A WHOLE
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

courses = ["Python", "Web", "AI", "Mobile"]
students = [120, 95, 150, 70]

# --- Bar chart ---
plt.figure(figsize=(6, 4))                          # width, height in inches
bars = plt.bar(courses, students, color="steelblue")
plt.bar_label(bars)                                 # print the value on each bar
plt.title("Students per course")
plt.ylabel("Number of students")
plt.savefig("bar_chart.png")
plt.close()                                         # finish this figure

# --- Horizontal bar: good when labels are long ---
plt.figure(figsize=(6, 4))
plt.barh(courses, students, color="seagreen")
plt.title("Students per course (horizontal)")
plt.savefig("barh_chart.png")
plt.close()

# --- Pie chart: use only for a few parts that add to 100% ---
plt.figure(figsize=(5, 5))
plt.pie(students, labels=courses, autopct="%1.0f%%", startangle=90)
plt.title("Share of students")
plt.savefig("pie_chart.png")
plt.close()

print("Saved bar_chart.png, barh_chart.png, pie_chart.png")
