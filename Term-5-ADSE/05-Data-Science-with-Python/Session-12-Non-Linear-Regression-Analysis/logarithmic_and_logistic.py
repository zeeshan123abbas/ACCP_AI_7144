# logarithmic_and_logistic.py - two more non-linear shapes
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- 1. Logarithmic: fast gains at first, then slow ("diminishing returns") ---
practice_hours = np.array([1, 2, 4, 8, 16, 32, 64])
typing_speed = np.array([20, 28, 35, 43, 50, 57, 64])    # words per minute

def logarithmic(x, a, b):
    return a + b * np.log(x)

(a1, b1), _ = curve_fit(logarithmic, practice_hours, typing_speed)
print(f"Log model: speed = {a1:.1f} + {b1:.1f} * ln(hours)")

# --- 2. Logistic (S-curve): slow start, fast middle, then levels off ---
week = np.arange(1, 13)
users = np.array([5, 9, 16, 30, 52, 85, 120, 150, 170, 182, 188, 191])  # thousands

def logistic(x, limit, rate, middle):
    return limit / (1 + np.exp(-rate * (x - middle)))

(limit, rate, middle), _ = curve_fit(logistic, week, users, p0=[200, 1, 6])
print(f"Logistic model: max ~ {limit:.0f}k users, middle at week {middle:.1f}")

# Plot both side by side
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
x1 = np.linspace(1, 64, 100)
axes[0].scatter(practice_hours, typing_speed)
axes[0].plot(x1, logarithmic(x1, a1, b1), color="orange")
axes[0].set_title("Logarithmic: typing practice")
axes[0].set_xlabel("practice hours")

x2 = np.linspace(1, 12, 100)
axes[1].scatter(week, users)
axes[1].plot(x2, logistic(x2, limit, rate, middle), color="purple")
axes[1].set_title("Logistic (S-curve): app users")
axes[1].set_xlabel("week")

fig.tight_layout()
fig.savefig("log_and_logistic.png")
print("Saved log_and_logistic.png")
