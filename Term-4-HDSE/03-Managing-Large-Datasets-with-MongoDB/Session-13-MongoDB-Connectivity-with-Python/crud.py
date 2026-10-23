"""Run: pip install "pymongo[srv]" python-dotenv  then  python crud.py"""
import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import DuplicateKeyError, ServerSelectionTimeoutError

load_dotenv()
URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")


def main() -> None:
    with MongoClient(URI, serverSelectionTimeoutMS=5000) as client:
        client.admin.command("ping")
        db = client["school"]
        students = db["students"]
        students.drop()
        students.create_index([("roll_no", ASCENDING)], unique=True)

        # CREATE
        students.insert_many([
            {"roll_no": 1, "name": "Ali", "city": "Karachi", "marks": 78, "joined": datetime.now(timezone.utc)},
            {"roll_no": 2, "name": "Hira", "city": "Lahore", "marks": 91},
            {"roll_no": 3, "name": "Usman", "city": "Karachi", "marks": 55},
            {"roll_no": 4, "name": "Sana", "city": "Islamabad", "marks": 84},
        ])
        try:
            students.insert_one({"roll_no": 1, "name": "Duplicate"})
        except DuplicateKeyError:
            print("Roll number 1 already exists")

        print("Databases:", client.list_database_names())
        print("Collections:", db.list_collection_names())

        # READ: filter, projection, sort, limit
        for s in students.find({"marks": {"$gte": 60}}, {"_id": 0, "name": 1, "marks": 1}).sort("marks", DESCENDING).limit(3):
            print(s)
        print("Karachi students:", students.count_documents({"city": "Karachi"}))

        # UPDATE
        r = students.update_one({"name": "Usman"}, {"$inc": {"marks": 10}})
        print("Modified:", r.modified_count)
        students.update_many({"city": "Karachi"}, {"$set": {"province": "Sindh"}})

        # AGGREGATE
        for row in students.aggregate([{"$group": {"_id": "$city", "avg": {"$avg": "$marks"}}}, {"$sort": {"avg": -1}}]):
            print(f"{row['_id']}: {row['avg']:.1f}")

        # DELETE
        print("Deleted:", students.delete_many({"marks": {"$lt": 60}}).deleted_count)


if __name__ == "__main__":
    try:
        main()
    except ServerSelectionTimeoutError:
        print("Could not reach MongoDB. Is the server running / is MONGODB_URI correct?")
