# *************** IF STATEMENT ***************

# if: The if statement is used to check a condition.
# If the condition is True, the code inside the if block runs.
# If the condition is False, the code inside the if block does not run.

# Syntax:
# if condition:
#     do something

# Example:
# 01).
age = 18

if age >= 18:
    print("You can vote.")

# Output:
# You can vote.


# ******************** PRACTICE QUESTION ********************

# Question: 01).
# A website allows users to create an account only if
# their age is 13 or above.
#
# Write a program that checks the user's age.
# If the age is 13 or above, print:
# "You can create an account."

user_age = int(input("Enter your age to create account: "))

if user_age >= 13:
    print("You can create an account.")