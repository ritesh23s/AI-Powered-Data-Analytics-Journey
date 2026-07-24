a = int(input("Enter Your First Number:"))
b = int(input("Enter Your Second Number:"))

operation = input("Please chooes your operation: +, -, *, /, //, %, ** :     ")

# result = ((a + b) * (operation == "+") + (a - b) * (operation == "-") + (a * b) * (operation == "*") + (a / b) * (operation == "/"))

result = (
    (a + b) * (operation == "+") +
    (a - b) * (operation == "-") +
    (a * b) * (operation == "*") +
    (a / b) * (operation == "/") +
    (a // b) * (operation == "//") +
    (a % b) * (operation == "%") +
    (a ** b) * (operation == "**")
)
print("Your Result:" ,result)



# Disclaimer

# This calculator is a personal learning project created using only the basic Python concepts learned so far:

# * Variables
# * `input()`
# * Arithmetic Operators
# * Comparison Operators
# * `print()`

# No conditional statements (`if`, `elif`, `else`), loops, functions, dictionaries, or advanced Python features have been used.

# The calculator works by using Python's Boolean arithmetic, where `True` is treated as `1` and `False` as `0`. This approach is intended purely for learning and experimentation and is **not recommended for production or real-world applications**.

# The purpose of this project is to explore Python expressions and understand how Boolean values can be used in arithmetic operations.
