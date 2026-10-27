# lab3_prediction_report.py - Lab 3: predict rents and show the curve per area
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

df = pd.read_csv("karachi_rent.csv")
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

sizes_to_ask = pd.DataFrame({"size_sqyd": [120, 240, 400]})
x_smooth = pd.DataFrame({"size_sqyd": np.linspace(80, 500, 100)})

# One small model per area
for area_name, group in df.groupby("area"):
    model = make_pipeline(PolynomialFeatures(2), LinearRegression())
    model.fit(group[["size_sqyd"]], group["rent"])

    predictions = model.predict(sizes_to_ask).round(-2)
    print(f"{area_name:<16} 120/240/400 sq yd ->", predictions)

    plt.scatter(group["size_sqyd"], group["rent"], s=15, alpha=0.6)
    plt.plot(x_smooth["size_sqyd"], model.predict(x_smooth), label=area_name)

plt.title("Predicted rent curve by area")
plt.xlabel("size (square yards)")
plt.ylabel("monthly rent (Rs)")
plt.legend()
plt.savefig("lab3_rent_curves.png")
print("Saved lab3_rent_curves.png")
