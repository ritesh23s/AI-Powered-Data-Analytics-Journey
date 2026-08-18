# *************** COMPARISON OPERATORS IN CONDITIONS ***************

# Comparison operators are used to compare two values.
# They return either True or False.
#
# Common comparison operators:
# ==   → Equal to
# !=   → Not equal to
# >    → Greater than
# <    → Less than
# >=   → Greater than or equal to
# <=   → Less than or equal to


# Example:
x = 10

if x == 10:
    print("Equal")

if x != 5:
    print("Not equal")

# Output:
# Equal
# Not equal


# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given two integers a and b, compare the two numbers.
#
# Input:
# Two integers a and b.
#
# Output:
# Print "Equal" if both numbers are equal.
# Otherwise, print "Not Equal".
#
# Example:
# Input:
# 10
# 10
#
# Output:
# Equal

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Equal")
else:
    print("Not Equal")