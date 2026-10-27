# read_write_csv.py - load a CSV file into a DataFrame and save results back
import pandas as pd

# Read the CSV file that sits in the same folder
df = pd.read_csv("shop_sales.csv")
print("Loaded", len(df), "rows")
print(df.head())                # first 5 rows

# Add a calculated column: money earned on each row
df["revenue"] = df["quantity"] * df["unit_price"]

# Keep only the Bakery rows
bakery = df[df["category"] == "Bakery"]

# Save to a new CSV file (index=False means do not write the 0,1,2 row numbers)
bakery.to_csv("bakery_sales.csv", index=False)
print("\nSaved", len(bakery), "bakery rows to bakery_sales.csv")

# Read only some columns, and tell pandas which column holds dates
small = pd.read_csv("shop_sales.csv", usecols=["date", "item", "quantity"],
                    parse_dates=["date"])
print("\n", small.dtypes)
