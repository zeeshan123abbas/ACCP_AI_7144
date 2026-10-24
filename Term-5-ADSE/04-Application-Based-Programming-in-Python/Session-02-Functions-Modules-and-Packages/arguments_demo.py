# arguments_demo.py - default, keyword and variable-length arguments

# Default value: discount is 0 unless we pass something else
def final_price(price, discount=0):
    return price - (price * discount / 100)

print(final_price(1000))          # uses default discount 0
print(final_price(1000, 10))      # positional: discount = 10
print(final_price(discount=25, price=2000))  # keyword arguments, any order

# *args collects any number of positional values into a tuple
def add_all(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

print("Sum:", add_all(2, 4, 6, 8))

# **kwargs collects named values into a dictionary
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Zara", city="Karachi", course="ADSE")

# A function can return more than one value (as a tuple)
def min_max(values):
    return min(values), max(values)

lowest, highest = min_max([45, 88, 67])
print("Lowest:", lowest, "Highest:", highest)
