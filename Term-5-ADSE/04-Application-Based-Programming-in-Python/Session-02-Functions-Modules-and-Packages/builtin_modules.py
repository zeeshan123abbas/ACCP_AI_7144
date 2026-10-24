# builtin_modules.py - using modules from the Python Standard Library

import math                      # import the whole module
from random import randint       # import one function
import datetime as dt            # import with a short alias

print("Square root of 49:", math.sqrt(49))
print("Pi:", round(math.pi, 4))

dice = randint(1, 6)             # random whole number from 1 to 6
print("Dice rolled:", dice)

today = dt.date.today()
print("Today is:", today)
print("Year:", today.year)
