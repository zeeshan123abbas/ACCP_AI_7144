# scale_data.py - put numbers on the same scale
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.DataFrame({
    "age": [22, 35, 47, 29, 60],
    "salary": [40000, 85000, 150000, 62000, 210000],
})
print("Original:\n", df)

# 1. Min-max normalisation BY HAND: (x - min) / (max - min) -> values 0 to 1
by_hand = (df - df.min()) / (df.max() - df.min())
print("\nMin-max by hand:\n", by_hand.round(2))

# 2. The same with scikit-learn
minmax = MinMaxScaler()
scaled = minmax.fit_transform(df)                  # returns a NumPy array
print("\nMinMaxScaler:\n", pd.DataFrame(scaled, columns=df.columns).round(2))

# 3. Standardisation (z-score): (x - mean) / std -> mean 0, std 1
standard = StandardScaler()
z = standard.fit_transform(df)
print("\nStandardScaler:\n", pd.DataFrame(z, columns=df.columns).round(2))
