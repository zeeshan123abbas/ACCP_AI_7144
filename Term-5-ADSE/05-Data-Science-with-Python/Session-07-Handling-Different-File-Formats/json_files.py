# json_files.py - save and load JSON data (the format of web APIs)
import json
import pandas as pd

# A Python dictionary with a nested list
course = {
    "course": "Data Science with Python",
    "sessions": 18,
    "students": [
        {"name": "Ayesha", "city": "Karachi"},
        {"name": "Bilal", "city": "Lahore"},
    ],
}

# 1. Python -> JSON file
with open("course.json", "w", encoding="utf-8") as file:
    json.dump(course, file, indent=2)    # indent makes it readable
print("Saved course.json")

# 2. JSON file -> Python
with open("course.json", encoding="utf-8") as file:
    data = json.load(file)
print("Course:", data["course"])
print("First student:", data["students"][0]["name"])

# 3. JSON text (string) <-> Python
text = json.dumps({"ok": True, "count": 2})
print("As text:", text)
print("Back to dict:", json.loads(text))

# 4. A list of records -> DataFrame
df = pd.json_normalize(data, record_path="students", meta=["course"])
print("\n", df)
df.to_json("students.json", orient="records", indent=2)
