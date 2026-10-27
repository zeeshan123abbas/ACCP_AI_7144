# make_rent_csv.py - create a practice dataset of flat rents (run once)
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=21)
n = 90
area = rng.choice(["DHA", "Gulshan", "North Nazimabad"], n)
size = rng.uniform(80, 500, n).round()                  # size in square yards
age = rng.integers(0, 30, n)                            # building age in years

# Rent grows with size but more slowly for big flats (a curve), plus area effect
area_bonus = pd.Series(area).map({"DHA": 1.5, "Gulshan": 1.1, "North Nazimabad": 1.0}).to_numpy()
rent = (9000 * np.sqrt(size) * area_bonus - age * 900 + rng.normal(0, 12000, n)).round(-2)

df = pd.DataFrame({"area": area, "size_sqyd": size, "building_age": age, "rent": rent})
df.to_csv("karachi_rent.csv", index=False)
print(df.head())
print("Saved karachi_rent.csv with", len(df), "rows")
