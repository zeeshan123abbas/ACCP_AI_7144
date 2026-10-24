# scope_and_lambda.py - local vs global variables, and lambda functions

college = "Aptech"          # GLOBAL: visible everywhere in this file

def show_info():
    room = "Lab 3"          # LOCAL: exists only inside this function
    print(college, room)

show_info()
# print(room)  # would cause NameError: room is not defined outside

# lambda = a tiny one-line function without a name
square = lambda x: x * x
print("Square of 6:", square(6))

# lambdas are handy with sorted(), map() and filter()
students = [("Ali", 72), ("Sana", 91), ("Omar", 65)]

by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print("Sorted by marks:", by_marks)

marks = [72, 91, 65]
bonus = list(map(lambda m: m + 5, marks))       # add 5 to each
passed = list(filter(lambda m: m >= 70, marks)) # keep 70+
print("With bonus:", bonus)
print("Passed:", passed)
