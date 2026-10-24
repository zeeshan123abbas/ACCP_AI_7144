# number_guess.py - Lab 3: guessing game (random module + while loop)

import random

secret = random.randint(1, 20)   # computer picks a number
tries = 0

print("I am thinking of a number between 1 and 20.")
while True:
    guess = int(input("Your guess: "))
    tries = tries + 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You found it in {tries} tries.")
        break
