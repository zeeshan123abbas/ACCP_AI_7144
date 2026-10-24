# csv_and_json.py - reading a CSV file and saving JSON

import csv
import json

# Step 1: read students.csv as dictionaries (first row = headers)
students = []
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["marks"] = int(row["marks"])   # CSV values are text, convert
        students.append(row)

# Step 2: process the data
for s in students:
    print(f"{s['name']:<8} {s['city']:<10} {s['marks']}")
average = sum(s["marks"] for s in students) / len(students)
print("Class average:", round(average, 1))

# Step 3: save the result as JSON
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)
print("Saved students.json")

# Step 4: load the JSON back into Python
with open("students.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)
print("First record from JSON:", loaded[0])
