# exceptions_demo.py - handling errors with try / except / else / finally

# Example 1: dividing safely
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    else:
        return result          # runs only when no error happened
    finally:
        print("Division attempted")   # always runs

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# Example 2: catching different errors separately
values = ["25", "abc", "0"]
for text in values:
    try:
        number = int(text)          # may raise ValueError
        print(100 / number)         # may raise ZeroDivisionError
    except ValueError:
        print(f"'{text}' is not a number")
    except ZeroDivisionError:
        print("Zero is not allowed")

# Example 3: a missing file
try:
    with open("does_not_exist.txt") as f:
        print(f.read())
except FileNotFoundError as error:
    print("File problem:", error)

# Example 4: raising our own error
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as error:
    print("Error:", error)
