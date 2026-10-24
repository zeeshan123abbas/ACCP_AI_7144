# operators.py - arithmetic, comparison and logical operators

a = 17
b = 5

# Arithmetic operators
print("a + b  =", a + b)    # addition
print("a - b  =", a - b)    # subtraction
print("a * b  =", a * b)    # multiplication
print("a / b  =", a / b)    # division (always gives float)
print("a // b =", a // b)   # floor division (whole part only)
print("a % b  =", a % b)    # remainder (modulus)
print("a ** 2 =", a ** 2)   # power

# Comparison operators give True or False
print("a > b  :", a > b)
print("a == b :", a == b)
print("a != b :", a != b)

# Logical operators combine conditions
has_id_card = True
fee_paid = False
print("Can enter exam:", has_id_card and fee_paid)  # both must be True
print("Can enter library:", has_id_card or fee_paid)  # one is enough
print("Fee not paid:", not fee_paid)
