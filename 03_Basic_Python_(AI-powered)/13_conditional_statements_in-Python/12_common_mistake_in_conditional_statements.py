# *************** COMMON MISTAKES IN CONDITIONAL STATEMENTS ***************

# 01). Forgetting spaces before the code inside a condition.
#      Python uses spaces to identify which code belongs
#      to the if, elif, or else block.

# Example:
# if age >= 18:
# print("Adult")       # Incorrect


# if age >= 18:
#     print("Adult")   # Correct


# 02). Using = instead of == in conditions.
#      = is used to assign a value.
#      == is used to compare two values.

# Example:
# age = 18              # Assignment
# age == 18             # Comparison


# 03). Making conditions unnecessarily complicated.
#      Try to keep conditions simple and easy to understand.
#      Avoid using too many nested if statements
#      when a simpler condition can do the same work.


# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given two integers a and b, determine the greater number.
#
# Input:
# Two integers a and b.
#
# Conditions:
# If a is greater than b, print "A is greater".
# Otherwise, print "B is greater or equal".
#
# Output:
# Print the appropriate result.
#
# Example:
# Input:
# 15
# 10
#
# Output:
# A is greater

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

result = "A is greater" if a > b else "B is greater or equal"
print(result)