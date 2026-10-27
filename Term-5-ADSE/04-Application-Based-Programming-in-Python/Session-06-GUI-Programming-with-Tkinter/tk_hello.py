# tk_hello.py - the smallest Tkinter window
# Run: python tk_hello.py   (Tkinter comes with Python, nothing to install)

import tkinter as tk

# Step 1: create the main window (the "root")
window = tk.Tk()
window.title("My First GUI")      # text on the title bar
window.geometry("300x150")        # width x height in pixels

# Step 2: create a Label widget and place it in the window
label = tk.Label(window, text="Hello from Tkinter!", font=("Arial", 14))
label.pack(pady=40)               # pack() puts it on screen, pady adds space

# Step 3: start the event loop (keeps the window open and listening)
window.mainloop()
