# Deliberately broken examples, then fixed.
# This file is a teaching example for debugging.

# Example 1: missing parentheses
print("This is fine")

# Example 2: wrong variable name
name = "Ada"
print(f"Hello, {name}!")

# Example 3: wrong file path demonstration
try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("We caught the file error and fixed the problem by checking the path.")
