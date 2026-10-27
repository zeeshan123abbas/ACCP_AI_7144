# electricity_bill.py - real-world use case: monthly bills for many homes
import numpy as np

# Units used by 6 homes this month
units = np.array([120, 340, 90, 510, 275, 60])

# A simple slab rate: up to 200 units = Rs 25 per unit, above 200 = Rs 40 per unit
rate = np.where(units <= 200, 25, 40)
bill = units * rate

print("units:", units)
print("rate :", rate)
print("bill :", bill)
print("total collected: Rs", bill.sum())
print("average bill   : Rs", round(bill.mean(), 2))
print("homes above Rs 10,000:", np.count_nonzero(bill > 10000))
