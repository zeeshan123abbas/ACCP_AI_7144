# conditions.py - making decisions with if / elif / else

# Step 1: a fixed value so the program runs without typing
marks = 72

# Step 2: check conditions from top to bottom
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Marks: {marks}  Grade: {grade}")

# Step 3: one-line conditional (ternary) expression
result = "Pass" if marks >= 60 else "Fail"
print("Result:", result)

# Step 4: match-case (Python 3.10+) compares one value to many cases
day = "Sat"
match day:
    case "Sat" | "Sun":
        print("Weekend: lab is open 10am - 2pm")
    case "Fri":
        print("Friday: short day")
    case _:
        print("Normal working day")
