# parse_dates_and_types.py - turn messy text into real dates and numbers
import pandas as pd

df = pd.read_csv("raw_customers.csv")
print("Types before:\n", df.dtypes, "\n")

# 1. Dates written in different styles -> one real date type
#    format="mixed" lets pandas guess each value; errors="coerce" turns bad ones into NaT
df["join_date"] = pd.to_datetime(df["join_date"], format="mixed", errors="coerce")
print(df[["name", "join_date"]], "\n")

# Now we can use date parts
df["join_month"] = df["join_date"].dt.month_name()
print(df[["name", "join_month"]], "\n")

# 2. Numbers stored as text -> real numbers
prices = pd.Series(["1,200", "850", "Rs 499", "unknown"])
clean = prices.str.replace("Rs", "").str.replace(",", "").str.strip()
numbers = pd.to_numeric(clean, errors="coerce")    # "unknown" -> NaN
print("Prices as numbers:\n", numbers, "\n")

# 3. Change a type directly
df["customer_id"] = df["customer_id"].astype(str)
print("Types after:\n", df.dtypes)
