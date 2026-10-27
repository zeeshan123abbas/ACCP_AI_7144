# data_types_demo.py - the different kinds of data a data scientist meets

# 1. Numerical data (numbers we can do maths on)
age = 21                 # discrete: whole numbers you can count
height_cm = 172.5        # continuous: can have decimals

# 2. Categorical data (labels or groups)
city = "Karachi"         # nominal: no natural order
grade = "B"              # ordinal: has an order (A > B > C)

# 3. Boolean data (yes / no)
has_laptop = True

# 4. Text data (free sentences)
feedback = "The class was very helpful!"

# Print each value with its Python type
print("age        ->", age, type(age))
print("height_cm  ->", height_cm, type(height_cm))
print("city       ->", city, type(city))
print("grade      ->", grade, type(grade))
print("has_laptop ->", has_laptop, type(has_laptop))
print("feedback   ->", feedback, type(feedback))

# Structured data looks like a table: rows (records) and columns (fields)
students = [
    {"name": "Ayesha", "age": 20, "city": "Karachi"},
    {"name": "Bilal", "age": 22, "city": "Lahore"},
]
print("\nStructured data (list of rows):")
for row in students:
    print(row)
