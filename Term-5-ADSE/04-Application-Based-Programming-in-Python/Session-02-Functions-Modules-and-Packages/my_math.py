# my_math.py - OUR OWN module (any .py file is a module)

PI = 3.14159

def circle_area(radius):
    return PI * radius * radius

def rectangle_area(length, width):
    return length * width

# This block runs only when you run my_math.py directly,
# NOT when another file imports it.
if __name__ == "__main__":
    print("Testing my_math:", circle_area(2))
