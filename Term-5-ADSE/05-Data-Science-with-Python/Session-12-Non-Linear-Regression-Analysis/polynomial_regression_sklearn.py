# polynomial_regression_sklearn.py - polynomial regression with scikit-learn
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

# Temperature during a day: rises until afternoon, then falls (a hill shape)
hour = np.array([6, 8, 10, 12, 14, 16, 18, 20, 22])
temp = np.array([24, 27, 31, 34, 35, 34, 31, 28, 26])

X = hour.reshape(-1, 1)        # scikit-learn wants X as a 2-D table (rows, columns)

# Pipeline: first make hour, hour^2 ; then fit an ordinary linear regression on them
model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(X, temp)

predicted = model.predict(X)
print("R2 score:", round(r2_score(temp, predicted), 3))      # 1.0 = perfect fit
print("Temperature at 13:00 ->", model.predict([[13]]).round(1)[0], "°C")

# Draw the smooth curve
x_smooth = np.linspace(6, 22, 100).reshape(-1, 1)
plt.scatter(hour, temp, label="measured")
plt.plot(x_smooth, model.predict(x_smooth), color="red", label="degree 2 model")
plt.title("Polynomial regression: temperature over a day")
plt.xlabel("hour")
plt.ylabel("°C")
plt.legend()
plt.savefig("polynomial_regression.png")
print("Saved polynomial_regression.png")
