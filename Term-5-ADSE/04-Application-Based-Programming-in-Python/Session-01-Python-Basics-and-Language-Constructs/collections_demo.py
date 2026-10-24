# collections_demo.py - list, tuple, set and dictionary

# LIST: ordered, changeable, allows duplicates
marks = [78, 85, 62, 90]
marks.append(70)               # add at the end
print("Marks:", marks)
print("First:", marks[0], "Last:", marks[-1])
print("Highest:", max(marks), "Average:", sum(marks) / len(marks))

# TUPLE: ordered but cannot be changed
location = (24.86, 67.01)      # latitude, longitude of Karachi
print("Latitude:", location[0])

# SET: no duplicates, no order
cities = {"Karachi", "Lahore", "Karachi", "Quetta"}
print("Unique cities:", cities)

# DICTIONARY: key -> value pairs
student = {"name": "Bilal", "batch": "ADSE-5", "cgpa": 3.2}
student["cgpa"] = 3.4          # update a value
student["city"] = "Karachi"    # add a new key
print("Name:", student["name"])
for key, value in student.items():
    print(key, "=>", value)

# LIST COMPREHENSION: build a new list in one line
passed = [m for m in marks if m >= 70]
print("Marks 70 or above:", passed)

# Strings are sequences too
course = "Application Based Programming"
print(course.upper())
print(course.split())          # list of words
print(course[0:11])            # slicing -> "Application"
