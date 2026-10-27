# categorical_variables.py - nominal vs ordinal data and how to encode each
# Install once:  pip install pandas scikit-learn

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

pd.set_option("display.width", 150)          # show all columns on one line
pd.set_option("display.max_columns", None)

df = pd.DataFrame({
    "city": ["Karachi", "Lahore", "Islamabad", "Karachi"],             # NOMINAL: no order
    "education": ["Matric", "Bachelor", "Master", "Intermediate"],      # ORDINAL: has order
    "approved": ["Yes", "No", "Yes", "No"],                            # BINARY target
})
print(df, "\n")

# 1) Binary: map two values to 1 and 0
df["approved_num"] = df["approved"].map({"No": 0, "Yes": 1})

# 2) Ordinal: keep the natural order with OrdinalEncoder
levels = [["Matric", "Intermediate", "Bachelor", "Master"]]           # low -> high
ordinal = OrdinalEncoder(categories=levels)
df["education_num"] = ordinal.fit_transform(df[["education"]]).astype(int)

# 3) Nominal: one-hot encoding with scikit-learn
one_hot = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
city_columns = one_hot.fit_transform(df[["city"]])
city_df = pd.DataFrame(city_columns.astype(int), columns=one_hot.get_feature_names_out())

result = pd.concat([df, city_df], axis=1)
print(result)

# handle_unknown="ignore": a new city never seen before becomes all zeros (no crash)
print("\nUnknown city 'Quetta' ->", one_hot.transform(pd.DataFrame({"city": ["Quetta"]})))
