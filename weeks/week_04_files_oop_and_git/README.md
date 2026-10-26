# Week 04: Files, OOP and Git

## Analogy

A class is a blueprint for a house. An object is the real house built from that blueprint. Git is like saving checkpoints in your project so you can go back if something breaks.

## Mon: OOP with a `Contact` class

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

alice = Contact("Alice", "555-0101")
print(alice)
```

Line by line:
- `class Contact:` creates a blueprint.
- `__init__` runs when we create an object.
- `self.name` and `self.phone` store data on the object.
- `__str__` tells Python how to print the object nicely.

Real output:

```text
Alice: 555-0101
```

## Tue: saving to a file

This script writes the contact to a text file.

```python
with open("contact_book.txt", "a", encoding="utf-8") as file:
    file.write(f"{alice.name},{alice.phone}\n")
```

The `a` means "append" so the file grows instead of being overwritten each time.

## Wed: debugging examples

The debugging log includes five broken and fixed examples, including:
- missing parentheses
- file not found
- typo in a function name
- missing key in a dictionary
- divide by zero

See `debugging_log.md` for the full details.

## Thu: Git and GitHub basics

A real commit history matters because it records what changed and when. We committed the repo scaffold earlier in this session.

Commands used:

```bash
git status
git add .
git commit -m "Initialize roadmap scaffold and setup"
```

## Friday challenge

Add a second contact and save both contacts to the file. Then read the file back and print its contents.

## Saturday project

The Month 1 expense tracker uses the same beginner skills: files, functions, loops, and clear project structure.

## Did it stick? Repeat checklist

- I can explain the difference between a class and an object.
- I can save data to a file.
- I can read a Python error message.
- I can stage and commit a change.
