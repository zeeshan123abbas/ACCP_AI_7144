# input_output.py - reading input from the keyboard
# Run it and type your answers in the terminal.

name = input("Enter your name: ")          # input() always returns text
year_text = input("Enter your birth year: ")

birth_year = int(year_text)                 # convert text to number
age = 2026 - birth_year

print(f"Hello {name}! You will be about {age} years old in 2026.")
