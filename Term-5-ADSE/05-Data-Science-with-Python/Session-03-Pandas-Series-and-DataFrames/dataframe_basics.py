# dataframe_basics.py - a DataFrame is a TABLE: many Series side by side
import pandas as pd

# Build a DataFrame from a dictionary: each key is a column
students = pd.DataFrame({
    "name":  ["Ayesha", "Bilal", "Hira", "Usman", "Sana"],
    "city":  ["Karachi", "Lahore", "Karachi", "Multan", "Lahore"],
    "age":   [20, 22, 21, 23, 20],
    "marks": [88, 72, 95, 64, 81],
})

print(students)
print("\nShape (rows, columns):", students.shape)
print("Columns:", list(students.columns))

# One column = a Series
print("\nMarks column:\n", students["marks"])

# Several columns = a smaller DataFrame (note the double brackets)
print("\nName and marks:\n", students[["name", "marks"]])

# Add a new column calculated from another
students["passed"] = students["marks"] >= 70
print("\nWith new column:\n", students)

# Filter rows
print("\nStudents from Karachi:\n", students[students["city"] == "Karachi"])
