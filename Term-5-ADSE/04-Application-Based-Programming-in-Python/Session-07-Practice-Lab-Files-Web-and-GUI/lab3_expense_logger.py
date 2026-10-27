# lab3_expense_logger.py - save expenses to a CSV file and read them back
# Skills: csv module, append mode, totals, exceptions

import csv
import os

FILE_NAME = "expenses.csv"


def add_expense(item, amount):
    """Append one row. Write the header only if the file is new."""
    is_new_file = not os.path.exists(FILE_NAME)
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if is_new_file:
            writer.writerow(["item", "amount"])
        writer.writerow([item, amount])


def total_expenses():
    total = 0
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            try:
                total += float(row["amount"])
            except ValueError:
                print("Skipping bad amount:", row["amount"])
    return total


# Start fresh each time we run the demo
if os.path.exists(FILE_NAME):
    os.remove(FILE_NAME)

add_expense("Bus fare", 150)
add_expense("Lunch", 450)
add_expense("Notebook", "abc")      # bad value on purpose
add_expense("Internet", 2500)

print("Total spent: Rs", total_expenses())
