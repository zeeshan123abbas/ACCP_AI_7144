# create_arrays.py - different ways to create NumPy arrays
import numpy as np

# 1. From a Python list
marks = np.array([78, 85, 62, 91])
print("marks:", marks)

# 2. A 2-D array (rows and columns) from a list of lists
table = np.array([[1, 2, 3],
                  [4, 5, 6]])
print("table:\n", table)

# 3. Ready-made arrays
print("zeros:", np.zeros(4))          # four 0.0 values
print("ones:", np.ones(3))            # three 1.0 values
print("range:", np.arange(0, 10, 2))  # start 0, stop before 10, step 2
print("linspace:", np.linspace(0, 1, 5))  # 5 evenly spaced numbers from 0 to 1

# 4. Random numbers (seed makes the result the same every run)
rng = np.random.default_rng(seed=42)
print("random ints:", rng.integers(1, 7, size=5))   # five dice rolls

# 5. Useful properties of an array
print("shape:", table.shape)   # (rows, columns)
print("ndim:", table.ndim)     # number of dimensions
print("size:", table.size)     # total number of items
print("dtype:", table.dtype)   # data type of the items
