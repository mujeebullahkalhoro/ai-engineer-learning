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

# String repetition
print("Hi " * 3)











"""
06 - String Operations Complete Demo

Run:
    python 06-string-operations.py
"""

print("=" * 60)
print("PYTHON STRING OPERATIONS")
print("=" * 60)

# -------------------------------------------------
# Creating Strings
# -------------------------------------------------
text = "Hello, Python!"
name = "Mujeeb"

print("\n1. Original String")
print("Text:", text)

# -------------------------------------------------
# Length
# -------------------------------------------------
print("\n2. Length")
print("Length:", len(text))

# -------------------------------------------------
# Concatenation
# -------------------------------------------------
print("\n3. Concatenation")
message = "Hi " + name + "! Welcome to " + text
print(message)

# -------------------------------------------------
# String Repetition
# -------------------------------------------------
print("\n4. Repetition")
print("Python " * 3)

# -------------------------------------------------
# f-Strings
# -------------------------------------------------
print("\n5. f-Strings")
score = 98.56789
print(f"{name}'s score is {score:.2f}")

# -------------------------------------------------
# Indexing
# -------------------------------------------------
print("\n6. Indexing")
print("First Character :", text[0])
print("Second Character:", text[1])
print("Last Character  :", text[-1])

# -------------------------------------------------
# Slicing
# -------------------------------------------------
print("\n7. Slicing")
print("text[0:5]  :", text[0:5])
print("text[:5]   :", text[:5])
print("text[7:]   :", text[7:])
print("text[-7:]  :", text[-7:])
print("Every 2nd  :", text[::2])
print("Reverse    :", text[::-1])

# -------------------------------------------------
# Case Conversion
# -------------------------------------------------
print("\n8. Case Conversion")
print("Upper      :", text.upper())
print("Lower      :", text.lower())
print("Title      :", text.title())
print("Capitalize :", text.capitalize())

# -------------------------------------------------
# Strip
# -------------------------------------------------
print("\n9. Strip")
spaces = "     Python Programming     "
print("Before:", repr(spaces))
print("After :", repr(spaces.strip()))

# -------------------------------------------------
# Replace
# -------------------------------------------------
print("\n10. Replace")
print(text.replace("Python", "World"))

# -------------------------------------------------
# Find
# -------------------------------------------------
print("\n11. Find")
print("Position of 'Python':", text.find("Python"))
print("Position of 'Java'  :", text.find("Java"))

# -------------------------------------------------
# Count
# -------------------------------------------------
print("\n12. Count")
fruit = "banana"
print("String:", fruit)
print("Count of 'a':", fruit.count("a"))

# -------------------------------------------------
# Startswith / Endswith
# -------------------------------------------------
print("\n13. Startswith / Endswith")
print(text.startswith("Hello"))
print(text.endswith("!"))

# -------------------------------------------------
# Split
# -------------------------------------------------
print("\n14. Split")
sentence = "Apple,Banana,Mango"
fruits = sentence.split(",")
print(fruits)

# -------------------------------------------------
# Join
# -------------------------------------------------
print("\n15. Join")
joined = " | ".join(fruits)
print(joined)

# -------------------------------------------------
# Membership
# -------------------------------------------------
print("\n16. Membership")
print("'Python' in text :", "Python" in text)
print("'Java' in text   :", "Java" in text)

# -------------------------------------------------
# Character Checking
# -------------------------------------------------
print("\n17. Character Checking")
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("HELLO".isupper())
print("hello".islower())

# -------------------------------------------------
# Comparison
# -------------------------------------------------
print("\n18. Comparison")
print("abc == abc :", "abc" == "abc")
print("abc > abb  :", "abc" > "abb")

# -------------------------------------------------
# Escape Characters
# -------------------------------------------------
print("\n19. Escape Characters")
print("Hello\nWorld")
print("Hello\tPython")
print("He said \"Hello\"")

# -------------------------------------------------
# Reverse String
# -------------------------------------------------
print("\n20. Reverse String")
print(text[::-1])

# -------------------------------------------------
# Word Count
# -------------------------------------------------
print("\n21. Word Count")
sentence = "Python is easy to learn"
words = sentence.split()
print("Words:", words)
print("Total Words:", len(words))

# -------------------------------------------------
# Immutable String Example
# -------------------------------------------------
print("\n22. String Immutability")
original = "Python"
modified = "J" + original[1:]
print("Original:", original)
print("Modified:", modified)

# -------------------------------------------------
# Mini Real World Example
# -------------------------------------------------
print("\n23. Mini User Example")

user_name = input("Enter your name: ").strip()
city = input("Enter your city: ").strip()

print(f"\nHello {user_name.title()}!")
print(f"You live in {city.title()}.")
print(f"Your name has {len(user_name)} characters.")
print(f"Uppercase Name : {user_name.upper()}")
print(f"Lowercase Name : {user_name.lower()}")
print(f"Reversed Name  : {user_name[::-1]}")
print(f"Starts with 'M': {user_name.startswith('M')}")
print(f"Contains 'a'   : {'a' in user_name.lower()}")

print("\n" + "=" * 60)
print("End of String Operations Demo")
print("=" * 60)
