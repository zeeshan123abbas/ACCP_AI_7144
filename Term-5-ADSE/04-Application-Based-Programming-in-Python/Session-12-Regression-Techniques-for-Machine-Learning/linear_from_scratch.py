# linear_from_scratch.py - find the best-fit line with the least squares formula
# No libraries needed. This shows what LinearRegression does inside.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                  # experience
y = [45, 52, 60, 66, 75, 82, 88, 97, 103, 112]       # salary

n = len(x)
mean_x = sum(x) / n
mean_y = sum(y) / n

# slope m = sum((x - mean_x) * (y - mean_y)) / sum((x - mean_x) ** 2)
top = 0
bottom = 0
for xi, yi in zip(x, y):
    top += (xi - mean_x) * (yi - mean_y)
    bottom += (xi - mean_x) ** 2
m = top / bottom

# intercept c = mean_y - m * mean_x
c = mean_y - m * mean_x
print(f"Line: salary = {m:.2f} * experience + {c:.2f}")

# Errors: how far each prediction is from the truth
squared_errors = [(yi - (m * xi + c)) ** 2 for xi, yi in zip(x, y)]
mse = sum(squared_errors) / n
print(f"Mean Squared Error: {mse:.2f}")
print(f"Prediction for 12 years: {m * 12 + c:.1f}")
