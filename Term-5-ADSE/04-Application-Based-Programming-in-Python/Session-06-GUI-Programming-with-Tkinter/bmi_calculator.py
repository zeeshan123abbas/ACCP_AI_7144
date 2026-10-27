# bmi_calculator.py - a complete small GUI app: input, button, result, message box
# Run: python bmi_calculator.py

import tkinter as tk
from tkinter import messagebox


def calculate_bmi(weight_kg, height_cm):
    """Pure calculation, kept separate from the GUI so it is easy to test."""
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def on_calculate():
    # Step 1: read text from the entries and convert to numbers
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        messagebox.showerror("Input error", "Please type numbers only.")
        return
    # Step 2: calculate and show the result
    bmi = calculate_bmi(weight, height)
    result_label.config(text=f"BMI: {bmi}  ({bmi_category(bmi)})")


window = tk.Tk()
window.title("BMI Calculator")
window.resizable(False, False)

tk.Label(window, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=6, sticky="w")
weight_entry = tk.Entry(window, width=12)
weight_entry.grid(row=0, column=1, padx=10)

tk.Label(window, text="Height (cm):").grid(row=1, column=0, padx=10, pady=6, sticky="w")
height_entry = tk.Entry(window, width=12)
height_entry.grid(row=1, column=1, padx=10)

tk.Button(window, text="Calculate", command=on_calculate).grid(row=2, column=0, columnspan=2, pady=8)
result_label = tk.Label(window, text="BMI: -", font=("Arial", 12, "bold"))
result_label.grid(row=3, column=0, columnspan=2, pady=(0, 10))

window.mainloop()
