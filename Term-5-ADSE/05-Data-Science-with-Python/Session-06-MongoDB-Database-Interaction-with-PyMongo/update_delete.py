# update_delete.py - change and remove documents
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
products = client["shop"]["products"]

products.delete_many({})                         # clean start for the demo
products.insert_many([
    {"item": "Pen", "price": 30, "stock": 500},
    {"item": "Notebook", "price": 150, "stock": 0},
    {"item": "Bag", "price": 1200, "stock": 25},
])

# $set changes a field in ONE matching document
products.update_one({"item": "Pen"}, {"$set": {"price": 35}})

# $inc adds to a number field in ALL matching documents (here: every product)
products.update_many({}, {"$inc": {"stock": 10}})

# Delete documents that match a filter
deleted = products.delete_many({"price": {"$gt": 1000}})
print("Deleted:", deleted.deleted_count)

# Show what is left
for doc in products.find({}, {"_id": 0}):
    print(doc)

client.close()
