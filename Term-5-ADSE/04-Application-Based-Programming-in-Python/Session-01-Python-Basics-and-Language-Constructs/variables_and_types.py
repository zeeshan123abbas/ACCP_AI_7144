# variables_and_types.py - storing values in variables

# Step 1: create variables (no type keyword needed)
student_name = "Ayesha"      # str  (text)
age = 19                     # int  (whole number)
cgpa = 3.45                  # float (decimal number)
is_enrolled = True           # bool (True or False)

# Step 2: print the values
print("Name:", student_name)
print("Age:", age)
print("CGPA:", cgpa)
print("Enrolled:", is_enrolled)

# Step 3: type() tells us the data type of a value
print(type(student_name))
print(type(age))
print(type(cgpa))
print(type(is_enrolled))

# Step 4: convert between types (type casting)
age_text = str(age)          # int  -> str
marks = int("85")            # str  -> int
price = float("99.5")        # str  -> float
print("Age as text:", age_text + " years")
print("Marks + 5 =", marks + 5)
print("Price x 2 =", price * 2)

# Step 5: f-strings put variables inside text easily
print(f"{student_name} is {age} years old and has CGPA {cgpa}")
