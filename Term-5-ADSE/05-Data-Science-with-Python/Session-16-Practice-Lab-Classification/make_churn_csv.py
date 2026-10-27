# make_churn_csv.py - create a practice dataset of mobile customers (run once)
import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=11)
n = 400
months = rng.integers(1, 72, n)                          # months with the company
monthly_bill = rng.uniform(500, 4000, n).round()         # rupees
complaints = rng.poisson(1.2, n)                         # complaints last year
package = rng.choice(["Prepaid", "Postpaid"], n, p=[0.7, 0.3])
city = rng.choice(["Karachi", "Lahore", "Islamabad"], n)

# Churn (leaving) is more likely with many complaints, high bills, short stay, prepaid
score = (0.9 * complaints + monthly_bill / 1500 - months / 20
         + (package == "Prepaid") * 0.8 + rng.normal(0, 1, n))
churn = np.where(score > 1.5, "Yes", "No")

df = pd.DataFrame({"city": city, "package": package, "months": months,
                   "monthly_bill": monthly_bill, "complaints": complaints, "churn": churn})
df.to_csv("customer_churn.csv", index=False)
print(df.head())
print(df["churn"].value_counts())
