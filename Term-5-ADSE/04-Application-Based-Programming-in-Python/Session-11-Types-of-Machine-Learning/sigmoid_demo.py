# sigmoid_demo.py - the S-shaped sigmoid curve used inside logistic regression
# Install once:  pip install numpy matplotlib

import matplotlib.pyplot as plt
import numpy as np


def sigmoid(z):
    """Turns ANY number into a value between 0 and 1 (a probability)."""
    return 1 / (1 + np.exp(-z))


# A few values to see the idea in numbers
for z in [-6, -2, 0, 2, 6]:
    print(f"sigmoid({z:>2}) = {sigmoid(z):.3f}")

# Draw the curve
z_values = np.linspace(-8, 8, 100)
plt.plot(z_values, sigmoid(z_values))
plt.axhline(0.5, color="red", linestyle="--", label="0.5 threshold")
plt.title("Sigmoid function")
plt.xlabel("z (weighted sum of inputs)")
plt.ylabel("probability")
plt.legend()
plt.savefig("sigmoid.png")
plt.show()
