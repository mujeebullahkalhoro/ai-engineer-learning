"""
04 - Python Operators Complete Demo

Run:
    python 04-operators.py
"""

print("=" * 60)
print("PYTHON OPERATORS DEMO")
print("=" * 60)

# -------------------------------------
# Variables
# -------------------------------------
a = 10
b = 3

print("\n1. Arithmetic Operators")
print("a =", a)
print("b =", b)

print("Addition (+)        :", a + b)
print("Subtraction (-)     :", a - b)
print("Multiplication (*)  :", a * b)
print("Division (/)        :", a / b)
print("Floor Division (//) :", a // b)
print("Modulus (%)         :", a % b)
print("Power (**)          :", a ** b)

# -------------------------------------

print("\n2. Assignment Operators")

x = 10
print("Initial x =", x)

x += 5
print("x += 5  ->", x)

x -= 3
print("x -= 3  ->", x)

x *= 2
print("x *= 2  ->", x)

x /= 4
print("x /= 4  ->", x)

x //= 2
print("x //= 2 ->", x)

x %= 3
print("x %= 3  ->", x)

x **= 2
print("x **= 2 ->", x)

# -------------------------------------

print("\n3. Comparison Operators")

print("10 == 3 :", a == b)
print("10 != 3 :", a != b)
print("10 > 3  :", a > b)
print("10 < 3  :", a < b)
print("10 >= 3 :", a >= b)
print("10 <= 3 :", a <= b)

# -------------------------------------

print("\n4. Logical Operators")

age = 22
salary = 50000

print("Age >18 AND Salary >40000")
print(age > 18 and salary > 40000)

print("Age >30 OR Salary >40000")
print(age > 30 or salary > 40000)

print("NOT Age >18")
print(not(age > 18))

# -------------------------------------

print("\n5. Identity Operators")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)

print("list1 == list3 :", list1 == list3)
print("list1 is list3 :", list1 is list3)

# -------------------------------------

print("\n6. Membership Operators")

text = "Python Programming"

print("'Python' in text      :", "Python" in text)
print("'Java' in text        :", "Java" in text)
print("'Java' not in text    :", "Java" not in text)

numbers = [10, 20, 30, 40]

print("20 in numbers :", 20 in numbers)
print("100 in numbers:", 100 in numbers)

# -------------------------------------

print("\n7. Bitwise Operators")

x = 5
y = 3

print("x =", x)
print("y =", y)

print("x & y :", x & y)
print("x | y :", x | y)
print("x ^ y :", x ^ y)
print("~x    :", ~x)
print("x << 1:", x << 1)
print("x >> 1:", x >> 1)

# -------------------------------------

print("\n8. Operator Precedence")

print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# -------------------------------------

print("\n9. Real World Examples")

# Even or Odd
num = 17
print(f"{num} is Even? ->", num % 2 == 0)

# Discount
price = 1000
discount = 20

final_price = price - (price * discount / 100)
print("Final Price:", final_price)

# Gmail Check
email = "mujeeb@gmail.com"
print("Is Gmail?", "@gmail.com" in email)

# Login
username = "admin"
password = "1234"

print("Login Successful?",
      username == "admin" and password == "1234")

# Floor Division Example
students = 165
capacity = 40

print("Full buses needed:", students // capacity)

print("\n" + "=" * 60)
print("End of Operators Demo")
print("=" * 60)