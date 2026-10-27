# simple_linear_regression.py - predict salary from years of experience
# Install once:  pip install scikit-learn matplotlib numpy

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Data: years of experience (input) and salary in thousand Rs (output)
experience = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # 2-D: rows x 1 column
salary = np.array([45, 52, 60, 66, 75, 82, 88, 97, 103, 112])

# Step 1: create and train the model
model = LinearRegression()
model.fit(experience, salary)

# Step 2: the learned straight line  salary = slope * experience + intercept
print(f"Slope (m):     {model.coef_[0]:.2f}  -> salary rises this much per year")
print(f"Intercept (c): {model.intercept_:.2f}  -> predicted salary at 0 years")

# Step 3: predict for new people
for years in [3.5, 12]:
    predicted = model.predict([[years]])[0]
    print(f"{years} years of experience -> about Rs {predicted:.0f}k")

# Step 4: draw the data points and the best-fit line
plt.scatter(experience, salary, color="blue", label="actual data")
plt.plot(experience, model.predict(experience), color="red", label="best-fit line")
plt.xlabel("Years of experience")
plt.ylabel("Salary (thousand Rs)")
plt.title("Simple Linear Regression")
plt.legend()
plt.savefig("linear_regression.png")
plt.show()
