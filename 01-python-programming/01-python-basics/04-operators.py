"""
04 - Operators

Run:
  python 04-operators.py
"""

from math import floor

a = 10
b = 3

# Arithmetic operators
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)  # floor division
print("a % b =", a % b)    # remainder
print("a ** b =", a**b)    # power

# Comparison operators
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical operators
is_rich = True
is_student = False
can_access = is_rich and not is_student
print("can_access (and/not):", can_access)

# Assignment operators
x = 5
x += 2
x *= 3
print("x after += and *=:", x)

# A quick example using the operators result
number = 7.9
print("floor(number):", floor(number))

