# sqlite_crud.py - the SAME CRUD ideas with SQLite (built into Python, no server)
# Run: python sqlite_crud.py   (great for practice when MySQL is not installed)

import sqlite3

# Step 1: connect - creates college.db file if it does not exist
connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Step 2: create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        name   TEXT NOT NULL,
        course TEXT NOT NULL,
        marks  INTEGER DEFAULT 0
    )
""")
cursor.execute("DELETE FROM students")      # start empty for this demo

# Step 3: INSERT many rows (SQLite uses ? as the placeholder)
students = [("Ayesha", "Python", 88), ("Bilal", "Flutter", 67), ("Hamza", "Python", 92)]
cursor.executemany("INSERT INTO students (name, course, marks) VALUES (?, ?, ?)", students)
connection.commit()

# Step 4: UPDATE and DELETE
cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (72, "Bilal"))
cursor.execute("DELETE FROM students WHERE name = ?", ("Hamza",))
connection.commit()

# Step 5: SELECT and show
cursor.execute("SELECT id, name, course, marks FROM students ORDER BY marks DESC")
for row in cursor.fetchall():
    print(row)

# Step 6: an aggregate query
cursor.execute("SELECT AVG(marks) FROM students")
print("Average marks:", cursor.fetchone()[0])

connection.close()
