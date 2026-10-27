# lab6_tk_notepad.py - a mini notepad: Text widget + open/save dialogs
# Run: python lab6_tk_notepad.py
# Skills: Tkinter, file dialogs, reading/writing files

import tkinter as tk
from tkinter import filedialog, messagebox

window = tk.Tk()
window.title("Mini Notepad")
window.geometry("500x350")

text_box = tk.Text(window, wrap="word", font=("Consolas", 11))
text_box.pack(fill="both", expand=True)


def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not path:                         # user pressed Cancel
        return
    with open(path, "r", encoding="utf-8") as file:
        text_box.delete("1.0", tk.END)   # clear old text
        text_box.insert("1.0", file.read())
    window.title(f"Mini Notepad - {path}")


def save_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not path:
        return
    with open(path, "w", encoding="utf-8") as file:
        file.write(text_box.get("1.0", tk.END))
    messagebox.showinfo("Saved", "Your file was saved.")


# A menu bar with File > Open / Save / Exit
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

window.mainloop()
