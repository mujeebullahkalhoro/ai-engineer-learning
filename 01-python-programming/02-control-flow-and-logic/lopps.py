"""
for loop and iteration in python

Syntax:
for variable in iterable:
    # code
"""

# range(start , stop , step) function is used to generate a sequence of numbers. It can take one, two, or three arguments:
# range(stop): Generates numbers from 0 to stop-1.  
for number in range(5):
    print("Number:", number)

for letter in "Python":
    print("Letter:", letter)

fruits = ["Apple","Banana","Mango"]

for fruit in fruits:
    print(fruit) 

# break
for i in range(10):

    if i == 5:
        break

    print(i)       

#skip the current iteration and continue with the next one
for i in range(6):

    if i == 3:
        continue

    print(i)



"""
else with Loop
""" 

for i in range(5):
    print(i)
else:
    print("Loop Finished")

"""
while condition:
    # code    
"""

password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted")



number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print(total)

"""
How to simulate a do...while loop in Python

Use while True with a break.
"""
while True:
    number = int(input("Enter a positive number: "))

    if number > 0:
        break

print("Thank you!")





"""
Loop Optimization
"""


