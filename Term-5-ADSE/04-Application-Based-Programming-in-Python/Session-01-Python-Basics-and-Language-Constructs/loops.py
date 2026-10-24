# loops.py - repeating work with for and while

# for loop with range(start, stop) -> stop is NOT included
print("Counting 1 to 5:")
for number in range(1, 6):
    print(number)

# for loop over a list
subjects = ["Python", "Flutter", "DevOps"]
for subject in subjects:
    print("I am studying", subject)

# while loop: repeats while the condition is True
balance = 1000
month = 0
while balance > 0:
    balance = balance - 300   # spend 300 every month
    month = month + 1
print(f"Money finished after {month} months")

# break stops the loop, continue skips one round
for number in range(1, 11):
    if number == 8:
        break          # stop completely at 8
    if number % 2 == 0:
        continue       # skip even numbers
    print("Odd number:", number)
