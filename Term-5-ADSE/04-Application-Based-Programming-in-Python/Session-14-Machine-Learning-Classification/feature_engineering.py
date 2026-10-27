# feature_engineering.py - create better input columns from the raw ones

import numpy as np
import pandas as pd

pd.set_option("display.width", 150)          # show all columns on one line
pd.set_option("display.max_columns", None)

df = pd.read_csv("loan_applications.csv")

# 1) Ratio feature: loan size compared to income (often more useful than either alone)
df["loan_to_income"] = (df["loan_amount_k"] / df["monthly_income_k"]).round(2)

# 2) Binning: turn a number into ranges (categories)
df["credit_band"] = pd.cut(df["credit_score"],
                           bins=[0, 580, 670, 740, 850],
                           labels=["Poor", "Fair", "Good", "Excellent"])

# 3) Flag feature: a simple yes/no rule from domain knowledge
df["is_high_income"] = (df["monthly_income_k"] > 200).astype(int)

# 4) Log transform: reduces the effect of very large values
df["log_loan"] = np.log1p(df["loan_amount_k"]).round(2)

print(df[["monthly_income_k", "loan_amount_k", "loan_to_income",
          "credit_score", "credit_band", "is_high_income", "log_loan"]].head(8))

# Does the new feature help? compare approval rate per credit band
print("\nApproval rate by credit band:")
approval = (df["approved"] == "Yes").groupby(df["credit_band"], observed=True).mean()
for band, rate in approval.items():
    print(f"  {band:<10} {rate:.0%}")
