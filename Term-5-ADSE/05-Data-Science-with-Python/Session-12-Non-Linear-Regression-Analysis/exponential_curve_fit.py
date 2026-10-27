# exponential_curve_fit.py - exponential growth fitted with scipy curve_fit
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Followers of a new YouTube channel each month (grows faster and faster)
month = np.array([1, 2, 3, 4, 5, 6, 7, 8])
followers = np.array([110, 160, 250, 370, 560, 830, 1250, 1900])

# Step 1: write the shape of the curve as a Python function
def exponential(x, a, b):
    return a * np.exp(b * x)          # a = start size, b = growth rate

# Step 2: let curve_fit find the best a and b (p0 = first guesses)
params, _ = curve_fit(exponential, month, followers, p0=[100, 0.3])
a, b = params
print(f"Model: followers = {a:.1f} * e^({b:.3f} * month)")
print(f"Growth per month: {(np.exp(b) - 1) * 100:.1f}%")

# Step 3: predict month 10
print("Month 10 prediction:", round(exponential(10, a, b)))

x_smooth = np.linspace(1, 10, 100)
plt.scatter(month, followers, label="real")
plt.plot(x_smooth, exponential(x_smooth, a, b), color="green", label="exponential fit")
plt.title("Exponential regression")
plt.xlabel("month")
plt.ylabel("followers")
plt.legend()
plt.savefig("exponential_fit.png")
print("Saved exponential_fit.png")
