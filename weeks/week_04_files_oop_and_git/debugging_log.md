# Debugging log

## 1. Example: missing parentheses

Broken code:

```python
print("Hello"
```

Error:

```text
SyntaxError: '(' was never closed
```

Fix:

```python
print("Hello")
```

## 2. Example: wrong file name

Broken code:

```python
open("wrong_name.txt")
```

Error:

```text
FileNotFoundError
```

Fix:

- Re-check the actual file name.
- Make sure the path is correct.

## 3. Example: variable name typo

Broken code:

```python
prnit("Hello")
```

Error:

```text
NameError: prnit is not defined
```

Fix: use `print` instead.

## 4. Example: wrong dictionary key

Broken code:

```python
student = {"name": "Ada"}
print(student["age"])
```

Error:

```text
KeyError: 'age'
```

Fix: use a key that exists or create it first.

## 5. Example: divide by zero

Broken code:

```python
print(10 / 0)
```

Error:

```text
ZeroDivisionError
```

Fix: only divide when the number is not zero.
