"""
03 - Data Types

Run:
  python 03-data-types.py
"""

from datetime import date

# variable_name = value
#student-name = "Ali" erro varible name can not have - @ # , but underscroe can have 
name: str = "Mujeeb"
age: int = 20
height_m: float = 1.72
is_student: bool = True

# Collection types
numbers: list[int] = [1, 2, 3]
coordinates: tuple[int, int] = (10, 20)
person: dict[str, object] = {"name": name, "age": age}
unique_tags: set[str] = {"python", "learning"}

today: date = date.today()

print("name:", name, "type:", type(name))
print("age:", age, "type:", type(age))
print("height_m:", height_m, "type:", type(height_m))
print("is_student:", is_student, "type:", type(is_student))
print("numbers:", numbers, "type:", type(numbers))
print("coordinates:", coordinates, "type:", type(coordinates))
print("person:", person, "type:", type(person))
print("unique_tags:", unique_tags, "type:", type(unique_tags))
print("today:", today, "type:", type(today))

# Type conversion (casting)
text_number = "123"
converted = int(text_number)
print("converted:", converted, "type:", type(converted))




# Multiple Variables
name = "Ali"
age = 20
city = "Lahore"

print(name)
print(age)
print(city)




# Multiple Assignment blow equivalent to above assigned 
name, age, city = "Ali", 20, "Karachi"




"""
#Swapping Variables

#Traditional way:

a = 10
b = 20

temp = a
a = b
b = temp
"""
#Python way:

a = 10
b = 20

print(id(a))
a, b = b, a



print(a)
print(b)

print(id(a))
