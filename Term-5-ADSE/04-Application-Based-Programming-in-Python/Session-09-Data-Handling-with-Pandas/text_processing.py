# text_processing.py - clean text columns with the .str accessor

import pandas as pd

df = pd.read_csv("sales.csv")

# The customer names are messy: extra spaces, upper/lower case mixed
print("Before:", df["customer"].tolist()[:3])

# .str lets us use string methods on the WHOLE column
df["customer"] = df["customer"].str.strip()          # remove spaces at the ends
df["customer"] = df["customer"].str.title()          # "ali khan" -> "Ali Khan"
print("After: ", df["customer"].tolist()[:3], "\n")

# Split full name into first and last name
df[["first_name", "last_name"]] = df["customer"].str.split(" ", n=1, expand=True)
print(df[["customer", "first_name", "last_name"]].head(4), "\n")

# Other useful string functions
df["name_length"] = df["customer"].str.len()
df["city_code"] = df["city"].str[:3].str.upper()     # first 3 letters
print(df[["customer", "name_length", "city", "city_code"]].head(4), "\n")

# Search inside text
print("Names containing 'ali':")
print(df[df["customer"].str.contains("ali", case=False)]["customer"].tolist())

# Replace text
df["product"] = df["product"].str.replace("Monitor", "LED Monitor")
print("\nProducts:", df["product"].unique().tolist())
