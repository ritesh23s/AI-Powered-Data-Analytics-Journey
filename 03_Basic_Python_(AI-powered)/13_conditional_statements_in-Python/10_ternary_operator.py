# *************** CONDITIONAL EXPRESSION / TERNARY OPERATOR ***************

# Python allows us to write a simple if-else condition
# in a single line.
# This is called a conditional expression or ternary operator.

# Syntax:
# variable_name = value_if_true if condition else value_if_false


# Example:
# 01).
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)

# Output:
# Adult


# Note:
# Ternary operator is mainly used for simple if-else conditions.
# The elif keyword cannot be used directly in a ternary operator.
# For multiple conditions, use if-elif-else.


# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given an integer number, determine whether the number is
# even or odd using a conditional expression.
#
# Input:
# An integer number.
#
# Output:
# Print "Even" if the number is divisible by 2.
# Otherwise, print "Odd".
#
# Example:
# Input:
# 15
#
# Output:
# Odd
num = int(input("Enter your number: "))

number_type = "Even" if num%2 == 0 else "Odd"
print(number_type)


