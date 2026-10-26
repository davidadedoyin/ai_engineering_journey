import sys

print(f"Python version: {sys.version}")
if sys.version_info < (3, 11):
    print("Warning: Python 3.11 or newer is recommended.")
else:
    print("Python version meets the 3.11+ requirement.")
