# insert_and_find.py - create documents and read them back
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
db = client["college"]                  # database (created on first insert)
students = db["students"]               # collection (like a table)

students.delete_many({})                # start clean each time we run the demo

# Insert ONE document (a Python dictionary)
result = students.insert_one({"name": "Ayesha", "city": "Karachi", "marks": 88})
print("Inserted id:", result.inserted_id)

# Insert MANY documents at once
students.insert_many([
    {"name": "Bilal", "city": "Lahore", "marks": 72},
    {"name": "Hira", "city": "Karachi", "marks": 95},
    {"name": "Usman", "city": "Multan", "marks": 64},
    {"name": "Sana", "city": "Lahore", "marks": 81},
])
print("Total documents:", students.count_documents({}))

# Find ONE document
print("\nfind_one:", students.find_one({"name": "Hira"}))

# Find MANY with a filter; {"_id": 0} hides the id field
print("\nStudents from Karachi:")
for doc in students.find({"city": "Karachi"}, {"_id": 0}):
    print(" ", doc)

# Comparison operators: $gt (greater than), $lt (less than), $in (in a list)
print("\nMarks above 80, highest first:")
for doc in students.find({"marks": {"$gt": 80}}, {"_id": 0}).sort("marks", -1):
    print(" ", doc["name"], doc["marks"])

client.close()
