# numpy_vs_list.py - why NumPy arrays beat Python lists for numbers
import time
import numpy as np

prices_list = [100, 250, 400]
prices_array = np.array([100, 250, 400])

# Adding 10% tax
# List: we need a loop (or comprehension)
taxed_list = [p * 1.10 for p in prices_list]
# Array: one operation applies to every item (vectorisation)
taxed_array = prices_array * 1.10
print("list :", taxed_list)
print("array:", taxed_array)

# Careful: * means something different for lists!
print("list * 2  ->", prices_list * 2)    # repeats the list
print("array * 2 ->", prices_array * 2)   # doubles each number

# Speed test on one million numbers
size = 1_000_000
big_list = list(range(size))
big_array = np.arange(size)

start = time.perf_counter()
squared_list = [x * x for x in big_list]
list_time = time.perf_counter() - start

start = time.perf_counter()
squared_array = big_array * big_array
array_time = time.perf_counter() - start

print(f"list time : {list_time:.4f} s")
print(f"array time: {array_time:.4f} s")
print(f"NumPy was about {list_time / array_time:.0f}x faster")
