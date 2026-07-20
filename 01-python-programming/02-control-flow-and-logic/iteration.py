# enumerate
# why enumerate is used in python
#enumerate() is a built-in function in Python that adds a counter to an iterable and returns it as an enumerate object. This is particularly useful when you need both the index and the value of items in a loop.
#enumerate(iterable)
#enumerate(iterable, start=0)
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")


"""
Why zip is used in python
The zip() function in Python is used to combine two or more iterables (like lists,  tuples, etc.) element-wise into a single iterable of tuples. It pairs elements from the input iterables based on their positions, creating tuples that contain one element from each iterable. The resulting iterable stops when the shortest input iterable is exhausted.
Syntax:             zip(iterable1, iterable2, ...)

"""   



for name, mark in zip(names, marks):
    print(name, mark)


"""
when iterable has different lengths, zip() will stop creating tuples when the shortest iterable is exhausted. This means that if one iterable has fewer elements than the others, the resulting zipped object will only contain as many tuples as there are elements in the shortest iterable.                              
"""
#code example
names = ["Alice", "Bob", "Charlie"]   
marks = [85, 90]  # Shorter list

for name, mark in zip(names, marks):
    print(name, mark)   

"""
Iterator Protocol

"""


text = "ABC"

it = iter(text)

print(next(it))
print(next(it))
print(next(it))
