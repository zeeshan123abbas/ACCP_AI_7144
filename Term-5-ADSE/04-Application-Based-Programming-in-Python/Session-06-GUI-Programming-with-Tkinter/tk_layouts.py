# tk_layouts.py - placing widgets with grid() (rows and columns)
# Run: python tk_layouts.py

import tkinter as tk

window = tk.Tk()
window.title("Login (grid layout)")

# grid(row, column) works like a table; sticky="w" aligns to the left (west)
tk.Label(window, text="Username:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
user_entry = tk.Entry(window)
user_entry.grid(row=0, column=1, padx=8)

tk.Label(window, text="Password:").grid(row=1, column=0, padx=8, pady=8, sticky="w")
pass_entry = tk.Entry(window, show="*")       # show="*" hides the typed text
pass_entry.grid(row=1, column=1, padx=8)

message = tk.Label(window, text="")
message.grid(row=3, column=0, columnspan=2)   # columnspan: stretch over 2 columns

def login():
    # Very simple check, only for learning (never hard-code real passwords)
    if user_entry.get() == "admin" and pass_entry.get() == "1234":
        message.config(text="Welcome, admin!", fg="green")
    else:
        message.config(text="Wrong username or password", fg="red")

tk.Button(window, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=8)

window.mainloop()
