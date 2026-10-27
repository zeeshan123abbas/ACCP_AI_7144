# linear_vs_nonlinear.py - a straight line cannot follow a curve
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Car speed (km/h) and stopping distance (m): distance grows FASTER than speed
speed = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100])
distance = np.array([6, 12, 20, 30, 42, 56, 72, 90, 110])

# np.polyfit(x, y, degree) finds the best curve of that degree
line = np.polyfit(speed, distance, deg=1)       # straight line: y = a*x + b
curve = np.polyfit(speed, distance, deg=2)      # parabola: y = a*x^2 + b*x + c
print("Line coefficients :", line.round(3))
print("Curve coefficients:", curve.round(4))

# np.polyval calculates y values from the coefficients
x_smooth = np.linspace(20, 100, 100)
plt.scatter(speed, distance, color="black", label="real data")
plt.plot(x_smooth, np.polyval(line, x_smooth), "--", label="linear (degree 1)")
plt.plot(x_smooth, np.polyval(curve, x_smooth), label="polynomial (degree 2)")
plt.title("Stopping distance vs speed")
plt.xlabel("speed (km/h)")
plt.ylabel("distance (m)")
plt.legend()
plt.savefig("linear_vs_nonlinear.png")

# Prediction for 120 km/h with both models
print("Predict 120 km/h -> line:", round(np.polyval(line, 120), 1),
      "m | curve:", round(np.polyval(curve, 120), 1), "m")
