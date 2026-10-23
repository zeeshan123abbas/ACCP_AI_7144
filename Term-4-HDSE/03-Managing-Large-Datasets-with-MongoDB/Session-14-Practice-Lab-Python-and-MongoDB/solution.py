"""pip install pymongo pandas   then  python solution.py"""
import random
from datetime import datetime, timedelta, timezone

import pandas as pd
from pymongo import MongoClient

products = ["Mouse", "Keyboard", "Monitor", "Cable"]
cities = ["Karachi", "Lahore", "Islamabad"]
now = datetime.now(timezone.utc)

with MongoClient("mongodb://localhost:27017") as client:
    sales = client.pylab.sales
    sales.drop()
    sales.insert_many([
        {"product": random.choice(products), "city": random.choice(cities), "qty": random.randint(1, 5),
         "price": random.choice([1200, 5500, 38000, 650]), "date": now - timedelta(days=random.randint(0, 150))}
        for _ in range(30)
    ])

    revenue = {"$sum": {"$multiply": ["$qty", "$price"]}}
    print("Revenue per city:")
    for r in sales.aggregate([{"$group": {"_id": "$city", "revenue": revenue}}, {"$sort": {"revenue": -1}}]):
        print(f"  {r['_id']}: Rs. {r['revenue']:,}")

    print("Best seller per month:")
    pipeline = [
        {"$group": {"_id": {"m": {"$dateToString": {"format": "%Y-%m", "date": "$date"}}, "p": "$product"}, "qty": {"$sum": "$qty"}}},
        {"$sort": {"qty": -1}},
        {"$group": {"_id": "$_id.m", "product": {"$first": "$_id.p"}, "qty": {"$first": "$qty"}}},
        {"$sort": {"_id": 1}},
    ]
    for r in sales.aggregate(pipeline):
        print(f"  {r['_id']}: {r['product']} ({r['qty']})")

    df = pd.DataFrame(list(sales.find({}, {"_id": 0})))
    df["revenue"] = df["qty"] * df["price"]
    print(df.groupby("city")["revenue"].sum().sort_values(ascending=False))

    print("Deleted old:", sales.delete_many({"date": {"$lt": now - timedelta(days=90)}}).deleted_count)
