# *************** PASS KEYWORD IN CONDITIONAL STATEMENTS ***************

# pass: The pass statement is used when we want
# to do nothing inside a block of code.

# It is used as a placeholder when no action is needed
# at that time.

# Syntax:
# if condition:
#     pass
# else:
#     pass


# Example:
# 01).
age = 10

if age >= 18:
    pass
else:
    print("Minor")

# Output:
# Minor

# Here, pass does nothing when the condition is True.
# It simply allows the if block to remain empty.

# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given an integer number, check whether the number is zero,
# positive, or negative.
#
# Input:
# An integer number.
#
# Conditions:
# If the number is zero, do nothing.
# If the number is positive, print "Positive".
# If the number is negative, print "Negative".
#
# Output:
# Print the appropriate result according to the given conditions.
#
# Example:
# Input:
# -8
#
# Output:
# Negative

num = int(input("Enter your number: "))
if num == 0:
    pass
elif num > 0:
    print("Positive")
else:
    print("Negative")