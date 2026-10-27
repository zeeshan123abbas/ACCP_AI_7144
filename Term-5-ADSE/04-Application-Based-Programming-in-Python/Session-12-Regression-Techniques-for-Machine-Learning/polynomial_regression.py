# polynomial_regression.py - fit a CURVE when a straight line is not enough

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

# Data: engine speed (x) vs fuel use (y) - it bends like a U
speed = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110]).reshape(-1, 1)
fuel = np.array([9.0, 7.4, 6.3, 5.8, 5.6, 5.9, 6.5, 7.4, 8.6, 10.1])

# 1) A straight line (degree 1)
line_model = LinearRegression().fit(speed, fuel)
print("Straight line R2:", round(r2_score(fuel, line_model.predict(speed)), 3))

# 2) A curve (degree 2): adds a new column speed^2, then uses linear regression
poly = PolynomialFeatures(degree=2, include_bias=False)
speed_poly = poly.fit_transform(speed)          # columns: [speed, speed^2]
print("First row after transform:", speed_poly[0])

curve_model = LinearRegression().fit(speed_poly, fuel)
print("Curve (degree 2) R2:", round(r2_score(fuel, curve_model.predict(speed_poly)), 3))

# 3) Predict fuel use at 65 km/h with the curve
new_speed = poly.transform([[65]])
print("Fuel at 65 km/h:", round(curve_model.predict(new_speed)[0], 2), "litres/100km")
