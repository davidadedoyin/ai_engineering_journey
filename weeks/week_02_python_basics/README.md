# Week 02: Python basics

## Analogy

Think of Python like a calculator that also remembers things. A variable is a box with a name. The box can hold a number, a word, or a value you want to reuse.

## Mon: arithmetic and variables

This script stores values and multiplies them.

```python
# We can do math with Python.
price = 12
quantity = 3
total = price * quantity
print(f"Each item costs ${price} and three cost ${total}.")
```

Line by line:
- `price = 12` stores the value `12` in a variable named `price`.
- `quantity = 3` stores `3`.
- `total = price * quantity` multiplies the values.
- `print(...)` shows the result in the terminal.

Real output from the script:

```text
Each item costs $12 and three cost $36.
```

## Tue: input and output

```python
name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")
```

Line by line:
- `input()` waits for the user to type something.
- The value is saved to `name`.
- `f"...{name}..."` inserts the value into the message.

Real output:

```text
What is your name? Ada
Hello, Ada! Nice to meet you.
```

## Wed: f-strings

```python
item = "notebook"
price = 7.5
print(f"The {item} costs ${price:.2f}.")
```

This prints a sentence that mixes text and values. `:.2f` means "show the number with two digits after the decimal point."

Real output:

```text
The notebook costs $7.50.
```

## Thu: a tiny calculator

```python
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
print(f"Sum: {first + second}")
```

This is a simple way to use user input and arithmetic together.

## Friday challenge

The challenge is to write a calculator that prints the sum, difference, product and quotient of two numbers.

## Saturday project

This week is a building block for the Month 1 expense tracker. We practice input, output, variables and arithmetic before adding saving to a file.

## Did it stick? Repeat checklist

- I can explain what a variable is.
- I can use `input()` and `print()` together.
- I can do arithmetic with Python.
- I can explain why f-strings are useful.
