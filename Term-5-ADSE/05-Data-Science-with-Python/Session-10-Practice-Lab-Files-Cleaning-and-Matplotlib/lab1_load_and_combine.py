# lab1_load_and_combine.py - Lab 1: load two different formats and combine them
import json
import pandas as pd

# Task 1: online orders come as JSON
with open("orders_online.json", encoding="utf-8") as file:
    online_records = json.load(file)           # a list of dictionaries
online = pd.DataFrame(online_records)
online["channel"] = "online"
print("Online orders:", online.shape)

# Task 2: shop orders come as CSV with prices like "1,200" and dates like 02/03/2026
shop = pd.read_csv("orders_shop.csv", thousands=",")   # thousands="," turns "1,200" into 1200
shop["date"] = pd.to_datetime(shop["date"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")
shop["channel"] = "shop"
print("Shop orders:", shop.shape)

# Task 3: stack both tables on top of each other
orders = pd.concat([online, shop], ignore_index=True)
print("\nCombined:\n", orders)

# Task 4: save the combined raw data (Excel for the manager, pickle for us)
orders.to_excel("orders_combined.xlsx", index=False)
orders.to_pickle("orders_combined.pkl")
print("\nSaved orders_combined.xlsx and orders_combined.pkl")
