# tk_counter.py - events: buttons, a key press and a variable that updates the screen
# Run: python tk_counter.py

import tkinter as tk

window = tk.Tk()
window.title("Click Counter")
window.geometry("250x160")

# IntVar is a "live" variable: when it changes, the Label changes too
count = tk.IntVar(value=0)
tk.Label(window, textvariable=count, font=("Arial", 32)).pack(pady=10)

def add_one():
    count.set(count.get() + 1)

def reset():
    count.set(0)

frame = tk.Frame(window)          # a Frame groups widgets together
frame.pack()
tk.Button(frame, text="+1", width=8, command=add_one).pack(side="left", padx=5)
tk.Button(frame, text="Reset", width=8, command=reset).pack(side="left", padx=5)

# bind() connects a keyboard/mouse event to a function
# The function receives an "event" object (we do not need it here)
window.bind("<space>", lambda event: add_one())
tk.Label(window, text="Tip: press SPACE to add one").pack(pady=5)

window.mainloop()
