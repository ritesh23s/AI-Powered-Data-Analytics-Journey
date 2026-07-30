# *************** F-STRING IN PYTHON ***************

# f-string: It is used to insert variables or expressions into a string
# in an easy and readable way.

# It was introduced in Python 3.6.

# To use an f-string,
# add the letter f before the string
# and place variables or expressions
# inside curly braces {}.

# Syntax:
# f"text {variable_or_expression}"

# Example:
# 01).
name = "Shubham Yadav"
age = 23
print(f"My name is {name} and I am {age} years old.")

# Output:
# My name is Shubham Yadav and I am 23 years old.

# 02).
pen_price = 26
pencil_price = 15
total = f"total price is ₹{pen_price + pencil_price}"
print(total)

# Output:
# total price is ₹41

# Note:
# Variables and expressions
# are written inside curly braces {}.


# Why f-string ?
# 01). Cleaner than string concatenation (+) and format()
# 02). Faster and easier to read.
# 03). Supports expressions and method calls