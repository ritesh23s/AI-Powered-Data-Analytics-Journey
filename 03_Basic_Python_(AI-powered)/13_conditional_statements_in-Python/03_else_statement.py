# *************** ELSE STATEMENT ***************

# else: The else block runs when the if condition is False.

# Syntax:
# if condition:
#     do something
# else:
#     do something

# Example:
# 01).
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Output:
# You are an adult.

# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given an integer number, determine whether the number is
# positive or negative.
#
# Input:
# An integer number.
#
# Output:
# Print "Positive" if the number is greater than or equal to 0.
# Otherwise, print "Negative".
#
# Example:
# Input:
# -5
#
# Output:
# Negative

num = int(input("Enter your number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")