# python_for_data.py - plain Python tools that every data scientist uses

marks = [78, 85, 62, 91, 70, 88]    # a list of exam marks

# Basic statistics with built-in functions
total = sum(marks)
count = len(marks)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", round(average, 2))
print("Highest:", max(marks), "Lowest:", min(marks))

# A list comprehension: keep only the marks of students who passed (>= 70)
passed = [m for m in marks if m >= 70]
print("Passed marks:", passed)

# A dictionary: count how many students are in each city
cities = ["Karachi", "Lahore", "Karachi", "Islamabad", "Karachi"]
city_count = {}
for c in cities:
    city_count[c] = city_count.get(c, 0) + 1   # add 1 to this city's count
print("Students per city:", city_count)

# A small function we can reuse on any list of numbers
def describe(values):
    """Return the min, max and average of a list."""
    return min(values), max(values), sum(values) / len(values)

low, high, avg = describe([3, 7, 5, 9])
print(f"min={low}, max={high}, avg={avg}")
