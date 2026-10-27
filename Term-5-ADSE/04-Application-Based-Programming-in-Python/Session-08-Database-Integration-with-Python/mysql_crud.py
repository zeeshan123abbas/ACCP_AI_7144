# mysql_crud.py - Insert, Update, Delete and Select with MySQL
# Install once:  pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="student_app", password="Pass@1234", database="college"
)
cursor = connection.cursor()

# INSERT - always use %s placeholders, never f-strings (prevents SQL injection)
cursor.execute(
    "INSERT INTO students (name, course, marks) VALUES (%s, %s, %s)",
    ("Zara", "Dart", 75),
)
connection.commit()                       # save the change permanently
new_id = cursor.lastrowid
print("Inserted student with id", new_id)

# UPDATE
cursor.execute("UPDATE students SET marks = %s WHERE id = %s", (81, new_id))
connection.commit()
print("Rows updated:", cursor.rowcount)

# SELECT with a condition
cursor.execute("SELECT name, marks FROM students WHERE marks >= %s", (80,))
print("Students with 80+:", cursor.fetchall())

# DELETE
cursor.execute("DELETE FROM students WHERE id = %s", (new_id,))
connection.commit()
print("Rows deleted:", cursor.rowcount)

cursor.close()
connection.close()
