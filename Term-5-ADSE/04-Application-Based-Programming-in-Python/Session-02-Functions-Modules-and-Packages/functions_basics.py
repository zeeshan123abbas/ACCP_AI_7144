# functions_basics.py - defining and calling functions

# Step 1: a function with no parameters
def greet():
    print("Welcome to the Python module!")

# Step 2: a function with parameters
def greet_student(name, batch):
    print(f"Hello {name} from batch {batch}")

# Step 3: a function that RETURNS a value
def calculate_average(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return average

# Step 4: call (use) the functions
greet()
greet_student("Hamza", "ADSE-5")

my_marks = [80, 72, 91]
avg = calculate_average(my_marks)
print(f"Average marks: {avg:.2f}")   # :.2f = 2 decimal places
