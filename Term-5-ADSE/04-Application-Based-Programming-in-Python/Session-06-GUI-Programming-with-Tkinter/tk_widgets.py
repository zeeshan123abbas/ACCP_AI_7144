# tk_widgets.py - a tour of the most common widgets and their properties
# Run: python tk_widgets.py

import tkinter as tk

window = tk.Tk()
window.title("Widget Tour")
window.geometry("320x380")

# Label: shows text. Properties: text, fg (text colour), bg, font
tk.Label(window, text="Student Form", fg="white", bg="#1565C0",
         font=("Arial", 14, "bold")).pack(fill="x")

# Entry: a one-line text box
tk.Label(window, text="Name:").pack(anchor="w", padx=10)
name_entry = tk.Entry(window, width=30)
name_entry.pack(padx=10)

# Checkbutton: on/off choice, stored in a BooleanVar
likes_python = tk.BooleanVar()
tk.Checkbutton(window, text="I like Python", variable=likes_python).pack(anchor="w", padx=10)

# Radiobutton: choose ONE option, all share the same StringVar
gender = tk.StringVar(value="Male")
tk.Radiobutton(window, text="Male", variable=gender, value="Male").pack(anchor="w", padx=10)
tk.Radiobutton(window, text="Female", variable=gender, value="Female").pack(anchor="w", padx=10)

# Listbox: a list of items
courses = tk.Listbox(window, height=3)
for course in ["Python", "Flutter", "Dart"]:
    courses.insert(tk.END, course)
courses.pack(padx=10, pady=5)

# Label used to show the result
result = tk.Label(window, text="", fg="green")

# Button: runs a function when clicked (command=)
def show_details():
    selected = courses.curselection()          # tuple of selected positions
    course = courses.get(selected[0]) if selected else "none"
    result.config(text=f"{name_entry.get()} | {gender.get()} | "
                       f"Python fan: {likes_python.get()} | {course}")

tk.Button(window, text="Show", width=12, command=show_details).pack(pady=5)
result.pack()

window.mainloop()
