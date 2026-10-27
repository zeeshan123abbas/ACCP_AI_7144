# mongo_to_pandas_chart.py - load MongoDB data into pandas and visualise it
from pymongo import MongoClient
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
orders = client["shop"]["orders"]

# Sample data so the demo works on an empty database
orders.delete_many({})
orders.insert_many([
    {"city": "Karachi", "category": "Mobiles", "amount": 45000},
    {"city": "Lahore", "category": "Mobiles", "amount": 38000},
    {"city": "Karachi", "category": "Laptops", "amount": 120000},
    {"city": "Islamabad", "category": "Laptops", "amount": 95000},
    {"city": "Lahore", "category": "Accessories", "amount": 4500},
    {"city": "Karachi", "category": "Accessories", "amount": 3000},
    {"city": "Islamabad", "category": "Mobiles", "amount": 52000},
])

# Option 1: MongoDB does the grouping (aggregation pipeline)
pipeline = [
    {"$group": {"_id": "$city", "total": {"$sum": "$amount"}}},
    {"$sort": {"total": -1}},
]
for row in orders.aggregate(pipeline):
    print(row)

# Option 2: bring documents into pandas, then analyse there
docs = list(orders.find({}, {"_id": 0}))   # list of dictionaries
df = pd.DataFrame(docs)
print("\n", df)

by_category = df.groupby("category")["amount"].sum()
print("\nSales by category:\n", by_category)

# Visualise the result
by_category.plot(kind="pie", autopct="%1.0f%%", title="Share of sales by category")
plt.ylabel("")
plt.savefig("sales_by_category.png")
print("\nChart saved as sales_by_category.png")

client.close()
