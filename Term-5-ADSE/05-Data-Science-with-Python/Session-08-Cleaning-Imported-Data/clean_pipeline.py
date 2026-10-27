# clean_pipeline.py - all cleaning steps together, saved as a clean file
import pandas as pd

df = pd.read_csv("raw_customers.csv")
print("Raw rows:", len(df))

df = df.drop_duplicates()                                   # 1. duplicates
df["name"] = df["name"].str.strip().str.title()             # 2. text
df["city"] = df["city"].str.strip().str.title()
df.loc[(df["age"] < 10) | (df["age"] > 100), "age"] = None  # 3. impossible ages
df["age"] = df["age"].fillna(df["age"].median())            # 4. missing values
df["monthly_spend"] = df["monthly_spend"].fillna(df.groupby("city")["monthly_spend"].transform("mean"))
df["join_date"] = pd.to_datetime(df["join_date"], format="mixed",
                                 errors="coerce")  # 5. dates

print("Clean rows:", len(df))
print("Missing left:", int(df.isnull().sum().sum()))
print(df)

df.to_csv("clean_customers.csv", index=False)
print("\nSaved clean_customers.csv")
