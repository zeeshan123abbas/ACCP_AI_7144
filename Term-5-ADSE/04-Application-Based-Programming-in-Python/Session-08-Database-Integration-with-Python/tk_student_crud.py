# tk_student_crud.py - Tkinter app to Add / Update / Delete / View students in MySQL
# Install once:  pip install mysql-connector-python
# Needs: MySQL running and create_database.sql executed
# Run: python tk_student_crud.py

import tkinter as tk
from tkinter import messagebox
import mysql.connector

DB_SETTINGS = {"host": "localhost", "user": "student_app",
               "password": "Pass@1234", "database": "college"}


# ---------- database helper ----------
def run_query(sql, values=()):
    """Run one SQL statement. Returns rows for SELECT, else None."""
    connection = mysql.connector.connect(**DB_SETTINGS)
    cursor = connection.cursor()
    cursor.execute(sql, values)
    rows = cursor.fetchall() if sql.strip().upper().startswith("SELECT") else None
    connection.commit()
    cursor.close()
    connection.close()
    return rows


# ---------- button actions ----------
def read_form():
    return id_entry.get(), name_entry.get(), course_entry.get(), marks_entry.get()


def add_student():
    _, name, course, marks = read_form()
    if not name or not course or not marks.isdigit():
        messagebox.showerror("Error", "Fill name, course and numeric marks")
        return
    run_query("INSERT INTO students (name, course, marks) VALUES (%s, %s, %s)",
              (name, course, int(marks)))
    show_all()


def update_student():
    student_id, name, course, marks = read_form()
    if not student_id.isdigit():
        messagebox.showerror("Error", "Select a student first")
        return
    run_query("UPDATE students SET name=%s, course=%s, marks=%s WHERE id=%s",
              (name, course, int(marks), int(student_id)))
    show_all()


def delete_student():
    student_id = id_entry.get()
    if student_id.isdigit() and messagebox.askyesno("Confirm", "Delete this student?"):
        run_query("DELETE FROM students WHERE id=%s", (int(student_id),))
        show_all()


def show_all():
    student_list.delete(0, tk.END)
    for row in run_query("SELECT id, name, course, marks FROM students"):
        student_list.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")


def fill_form(event):
    """When a row is clicked, copy its values into the boxes."""
    selected = student_list.curselection()
    if not selected:
        return
    values = student_list.get(selected[0]).split(" | ")
    for entry, value in zip([id_entry, name_entry, course_entry, marks_entry], values):
        entry.delete(0, tk.END)
        entry.insert(0, value)


# ---------- window layout ----------
window = tk.Tk()
window.title("Student Records (MySQL)")

labels = ["ID (auto)", "Name", "Course", "Marks"]
entries = []
for row_number, text in enumerate(labels):
    tk.Label(window, text=text).grid(row=row_number, column=0, padx=8, pady=4, sticky="w")
    entry = tk.Entry(window, width=25)
    entry.grid(row=row_number, column=1, padx=8)
    entries.append(entry)
id_entry, name_entry, course_entry, marks_entry = entries

buttons = tk.Frame(window)
buttons.grid(row=4, column=0, columnspan=2, pady=8)
tk.Button(buttons, text="Add", width=9, command=add_student).pack(side="left", padx=3)
tk.Button(buttons, text="Update", width=9, command=update_student).pack(side="left", padx=3)
tk.Button(buttons, text="Delete", width=9, command=delete_student).pack(side="left", padx=3)
tk.Button(buttons, text="Refresh", width=9, command=show_all).pack(side="left", padx=3)

student_list = tk.Listbox(window, width=45, height=8)
student_list.grid(row=5, column=0, columnspan=2, padx=8, pady=(0, 8))
student_list.bind("<<ListboxSelect>>", fill_form)

show_all()
window.mainloop()
