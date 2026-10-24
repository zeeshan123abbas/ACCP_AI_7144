# grade_report.py - Lab 1: student grade report using lists, dicts and functions

# Step 1: data - each student is a dictionary
students = [
    {"name": "Ayesha", "marks": [85, 78, 92]},
    {"name": "Bilal",  "marks": [55, 61, 48]},
    {"name": "Sana",   "marks": [72, 69, 80]},
]

# Step 2: small helper functions (one job each)
def average(marks):
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    return "F"

# Step 3: print a report table
print(f"{'Name':<10}{'Average':>8}{'Grade':>7}")
print("-" * 25)
for student in students:
    avg = average(student["marks"])
    print(f"{student['name']:<10}{avg:>8.1f}{grade(avg):>7}")

# Step 4: find the top student with max() and a lambda
top = max(students, key=lambda s: average(s["marks"]))
print("\nTop student:", top["name"])
