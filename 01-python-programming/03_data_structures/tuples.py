"""
tuples are ordered collections of elements that are immutable, meaning their contents cannot be changed after creation. They are defined by enclosing elements in parentheses () and can contain elements of different data types. Tuples are often used to group related data together and can be used as keys in dictionaries due to their immutability.

"""


tuple=("mujeeb" , 3 , "hassan" , 2 , "suhail" , 1)

print(tuple[0] , tuple[1])

empty = ()

print(empty)

"""
tuple packaging and unpackaging
 Without parentheses (Tuple Packing)

Python automatically packs values into a tuple.
"""
number=10, 30, 50

print(type(number))


# Tuple Unpacking
name, age, city = ("Ali", 22, "Karachi")

print(name)
print(age)
print(city)




"""
you can not change the value of an element in a tuple by assigning a new value to a specific index. For example, if you want to change the first number from 10 to 100, you would do number[0] = 100. This will raise a TypeError because tuples are immutable.
and you can not delete  add , append or remove elements from a tuple. For example, if you want to delete the first number, you would do del number[0]. This will raise a TypeError because tuples are immutable.
"""

# The tuple is immutable, but the variable can point to a new tuple.

numbers = (1, 2, 3)

numbers = (10, 20, 30)

print(numbers)




"""
Mutable Objects Inside Tuples

This is a very important interview question.

The tuple itself is immutable, but if it contains a mutable object (like a list), that object can still be changed.
"""

data = (1, 2, [3, 4])

print(data)

data[2].append(5)

print(data)


"""
Common Tuple Methods

Tuples have only two built-in methods because they are immutable.
"""
numbers = (10, 20, 30, 20, 40)

print(numbers.count(20))
print(numbers.index(30))


"""
Named Tuple  why ?
because it solve main problem of tuple that is we can not access the elements of tuple by name we can only access them by index. and it is not readable and understandable. so named tuple solve this problem by giving name to the elements of tuple and we can access them by name.

"""
# create a named tuple
from collections import namedtuple

student = namedtuple('Student', ['name', 'age', 'grade'])
john = student('John', 20, 'A')

print(john)

print(john.name)
print(john.age)
print(john.grade)