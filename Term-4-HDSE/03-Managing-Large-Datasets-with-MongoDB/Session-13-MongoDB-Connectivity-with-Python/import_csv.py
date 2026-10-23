"""Import results.csv into MongoDB with type conversion. Run: python import_csv.py"""
import csv
from pathlib import Path
from pymongo import MongoClient

rows = []
with open(Path(__file__).with_name("results.csv"), newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows.append({"name": r["name"], "module": r["module"], "marks": int(r["marks"])})

with MongoClient("mongodb://localhost:27017") as client:
    col = client.school.results
    col.delete_many({})
    col.insert_many(rows)
    print("Imported", col.count_documents({}), "rows")
    print("Pass rate:", round(100 * col.count_documents({"marks": {"$gte": 40}}) / len(rows), 1), "%")
