students = ["mujeeb", "john", "alice", "bob"]

# python list can contain differnt data types such as strings, integers, floats, and even other lists and mixed data types
data = ["Ali", 21, 3.8, True]

#Although Python allows mixed types, in real projects it's usually better if a list stores similar kinds of data (e.g., all names, all prices, or all IDs). This makes the code easier to understand and process.

"""
Accessing list elements: You can access individual elements in a list using their index. Python uses zero-based indexing, so the first element is at index 0, the second at index 1, and so on.
For example, to access the first student in the list, you would use students[0], and to access the second student, you would use students[1].   

"""

print(students[0] , students[1])  

print(students[::-1])


#mutable: You can change the value of an element in a list by assigning a new value to a specific index. For example, if you want to change the first student's name from "mujeeb" to "mohammed", you would do students[0] = "mohammed". After this operation, the list would look like ["mohammed", "john", "alice", "bob"].

students[0] = "mohammed"
print(students)

# Strings are immutable.

# name = "Ali"

# name[0] = "S"


"""
list of lists: You can create a list that contains other lists as its elements. This is often referred to as a "list of lists" or a "nested list." Each inner list can contain its own set of elements, and you can access them using multiple indices.
For example, if you have a list of lists representing a matrix, you can access individual elements
"""
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists[1][2])  # Output: 6 

# modifying a list of lists
students = [
    ["Ali", 20],
    ["Ahmed", 21]
]

students[0][1] = 25

print(students)
#list(iterable)
list_of_numbers = list(range(1, 6))  # Creates a list of numbers from 1 to 5
print(list_of_numbers)  # Output: [1, 2, 3, 4, 5]


numbers = (10, 20, 30, 40)

new_list = list(numbers)

print(new_list)
print(type(new_list))
"""
String → List

Each character becomes a separate element.
"""
name = "Python"

letters = list(name)

print(letters)



# Notice that spaces are also treated as characters:

text = "Hi AI"

print(list(text))



"""
List Methods: Python provides a variety of built-in methods that allow you to manipulate lists. Some common list methods include:
- append(): Adds an element to the end of the list.
- extend(): Adds multiple elements to the end of the list.
- insert(): Inserts an element at a specific index.
- remove(): Removes the first occurrence of a specified element from the list.
- pop(): Removes and returns the element at a specified index (or the last element if no index is specified).
- index(): Returns the index of the first occurrence of a specified element.
- count(): Returns the number of occurrences of a specified element in the list.
- sort(): Sorts the elements of the list in ascending order.
- reverse(): Reverses the order of the elements in the list.
"""

# Genral syntax for using a list method is: list_name.method_name(arguments)


"""
1 .Adding Elements
append()
extend()
insert()
"""
numbers = [10, 20, 30]

numbers.append(40)
print(numbers)  # Output: [10, 20, 30, 40]

#extending a list with multiple elements using extend()
numbers.extend([50, 60])
print(numbers)
    # Output: [10, 20, 30, 40, 50, 60]



#inserting an element at a specific index
numbers.insert(1, 15)  # Insert 15 at index 1
print(numbers)      



# Common Beginner Mistakes
# Mistake 1
numbers = [1, 2]

numbers = numbers.append(3)

print(numbers)

# Output

# None

# Why?

# append() modifies the existing list in place and returns None.

# Correct:

numbers = [1, 2]

numbers.append(3)

print(numbers)
# Mistake 2
# numbers = [1, 2]

# numbers.extend(3)

# Output

# TypeError

# Why?

# extend() expects an iterable, but an integer is not iterable.

# Correct:

numbers.extend([3])

# or

numbers.append(3)

# Mistake 3

# Expecting append() to flatten a list.

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

# # Output

# # [1, 2, [3, 4]]

# If you want 3 and 4 as separate elements, use extend() instead.

# delete elements from a list
# remove(): Removes the first occurrence of a specified element from the list.
# pop(): Removes and returns the element at a specified index (or the last element if no index is specified).
# clear(): Removes all elements from the list.
#examples of remove() and pop()
numbers = [10, 20, 30, 40, 50]  
numbers.remove(30)  # Removes the first occurrence of 30
print(numbers)  # Output: [10, 20, 40, 50]
numbers.pop(1)  # Removes and returns the element at index 1 (20)
print(numbers)          
numbers.clear()  # Removes all elements from the list
print(numbers)  # Output: []




# Original List
numbers = [50, 20, 10, 40, 20, 30]

print("=" * 50)
print("Original List:", numbers)

# ----------------------------------------
# remove()
print("\n1. remove()")
numbers.remove(20)          # Removes first occurrence of 20
print(numbers)

# ----------------------------------------
# pop()
print("\n2. pop()")
removed = numbers.pop()     # Removes last element
print("Removed:", removed)
print(numbers)

# ----------------------------------------
# index()
print("\n3. index()")
position = numbers.index(40)
print("Index of 40:", position)

# ----------------------------------------
# count()
print("\n4. count()")
count = numbers.count(20)
print("20 appears", count, "time(s)")

# ----------------------------------------
# sort()
print("\n5. sort()")
numbers.sort()
print(numbers)

# Descending order
numbers.sort(reverse=True)
print("Descending:", numbers)

# ----------------------------------------
# reverse()
print("\n6. reverse()")
numbers.reverse()
print(numbers)

# ----------------------------------------
# copy()
print("\n7. copy()")
copy_list = numbers.copy()

print("Original :", numbers)
print("Copied   :", copy_list)

copy_list.append(100)

print("\nAfter modifying copied list")
print("Original :", numbers)
print("Copied   :", copy_list)

# ----------------------------------------
# clear()
print("\n8. clear()")
numbers.clear()
print(numbers)

print("=" * 50)





import copy

# ---------------- Indexing & Slicing ----------------
numbers = [10, 20, 30, 40, 50, 60, 70]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice 1:5:", numbers[1:5])
print("Every second element:", numbers[::2])
print("Reversed:", numbers[::-1])

# ---------------- Assignment ----------------
a = [1, 2, 3]
b = a
b.append(4)

print("\nAssignment")
print("a:", a)
print("b:", b)

# ---------------- Shallow Copy ----------------
a = [[1, 2], [3, 4]]
b = a.copy()

b[0][0] = 100

print("\nShallow Copy")
print("a:", a)
print("b:", b)

# ---------------- Deep Copy ----------------
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100

print("\nDeep Copy")
print("a:", a)
print("b:", b)



"""
defination of list comprehension: List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) and optionally filtering the items based on a condition.
new_list = [expression for item in iterable]

"""

names = ["ali", "ahmed", "sara"]

upper_names = [name.upper() for name in names]

print(upper_names)


names = ["Ali", "Ahmed", "Sara"]

lengths = [len(name) for name in names]

print(lengths)



"""
General syntax

[
 expression
 for item in iterable
 if condition
]

"""


even = [i for i in range(11) if i % 2 == 0]

print(even)




""""

[ value_if_true if condition else value_if_false for item in iterable]

"""



result = [item for row in matrix for item in row]

print(result)




names = ["ali", "ahmed", "sara", "fatima"]

print("Original:", names)

upper_names = [name.upper() for name in names]
print("Upper:", upper_names)

lengths = [len(name) for name in names]
print("Lengths:", lengths)

numbers = list(range(1, 11))

squares = [n ** 2 for n in numbers]
print("Squares:", squares)

even = [n for n in numbers if n % 2 == 0]
print("Even:", even)

odd = [n for n in numbers if n % 2 != 0]
print("Odd:", odd)

labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print("Labels:", labels)

