# Week 03: Data structures and loops

## Analogy

A list is like a shopping basket. A dictionary is like a labeled shelf where each item has a name. A loop is a shortcut for repeating the same task many times.

## Mon: lists

```python
shopping_list = ["milk", "bread", "eggs"]
for item in shopping_list:
    print(f"- {item}")
```

Line by line:
- `shopping_list` is a list of strings.
- `for item in shopping_list` means: "take each item in the list, one by one."
- `print(...)` shows each item.

Real output:

```text
- milk
- bread
- eggs
```

## Tue: dictionaries

```python
student = {"name": "Ada", "age": 20, "course": "Python"}
print(student["name"])
print(student["course"])
```

This data structure uses key-value pairs. Keys are labels like `name` and `course`.

Real output:

```text
Ada
Python
```

## Wed: loops

```python
for score in [10, 15, 20]:
    print(f"Score: {score}")

count = 0
while count < 3:
    print(f"Count is now {count}")
    count += 1
```

A `for` loop is best for a known list. A `while` loop keeps running until a condition is no longer true.

## Thu: functions with return values

```python
def square(number):
    return number * number

print(square(4))
```

This function returns data, not just prints it. That is useful when you want your function to give a result back to the rest of the program.

## Friday challenge

Write a script that stores a few student names and scores, then prints each score in a loop.

## Saturday project

This week builds the mental model needed for the expense tracker: lists, functions and loops help us store and summarize expense data.

## Did it stick? Repeat checklist

- I know when to use a list vs a dictionary.
- I can loop over a list.
- I understand how `for` and `while` differ.
- I can write a small function that returns data.
