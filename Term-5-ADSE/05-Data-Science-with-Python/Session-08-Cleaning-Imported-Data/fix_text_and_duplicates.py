# fix_text_and_duplicates.py - tidy text, remove duplicates, fix impossible values
import pandas as pd

df = pd.read_csv("raw_customers.csv")

# 1. Remove exact duplicate rows
print("Duplicates found:", df.duplicated().sum())
df = df.drop_duplicates()

# 2. Clean text: remove extra spaces and use one style of capital letters
df["city"] = df["city"].str.strip().str.title()     # " karachi " -> "Karachi"
df["name"] = df["name"].str.title()                 # "bilal ahmed" -> "Bilal Ahmed"
print("\nCities now:", df["city"].unique())

# 3. Fix an impossible value: nobody is 250 years old
print("\nSuspicious ages:\n", df[df["age"] > 100][["name", "age"]])
df.loc[df["age"] > 100, "age"] = None              # mark as missing for now
print("\nAfter fix:\n", df[["name", "city", "age"]])
