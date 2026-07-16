"""
05 - String Operations

Run:
  python 05-string-operations.py
"""

text = "Hello, Python!"

# Concatenation
greeting = "Hi"
message = greeting + " -> " + text
print(message)

# f-strings (recommended formatting)
name = "Mujeeb"
score = 98.5
print(f"{name}'s score is {score:.1f}")

# Indexing + slicing
print("First char:", text[0])
print("Last char:", text[-1])
print("Slice [0:5]:", text[0:5])
print("Slice [-7:]:", text[-7:])

# Common string methods
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Stripped:", "   spaced   ".strip())
print("Replaced:", text.replace("Python", "World"))

# Splitting / joining
parts = text.split(", ")
print("Split parts:", parts)
joined = " | ".join(parts)
print("Joined:", joined)

