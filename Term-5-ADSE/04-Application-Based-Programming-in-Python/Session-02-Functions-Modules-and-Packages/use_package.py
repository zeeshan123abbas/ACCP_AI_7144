# use_package.py - importing modules from our "school" package

from school.grades import get_grade
from school import fees
import school

print("Package version:", school.__version__)
print("Grade for 75:", get_grade(75))
print("Monthly fee:", fees.monthly_fee(120000, 12))
