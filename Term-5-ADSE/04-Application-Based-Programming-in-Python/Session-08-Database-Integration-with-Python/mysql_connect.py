# mysql_connect.py - connect Python to MySQL and read rows
# Install once:  pip install mysql-connector-python
# Needs: MySQL server running and create_database.sql already executed

import mysql.connector
from mysql.connector import Error

connection = None          # so we can check it in 'finally'

try:
    # Step 1: open a connection
    connection = mysql.connector.connect(
        host="localhost",
        user="student_app",
        password="Pass@1234",
        database="college",
    )
    print("Connected to MySQL version", connection.server_info)

    # Step 2: a cursor sends SQL and holds the results
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, course, marks FROM students")

    # Step 3: fetch all rows (a list of tuples)
    for student_id, name, course, marks in cursor.fetchall():
        print(f"{student_id:<3} {name:<10} {course:<8} {marks}")

except Error as error:
    print("Database error:", error)

finally:
    # Step 4: always close what you opened
    if connection is not None and connection.is_connected():
        connection.close()
        print("Connection closed")
