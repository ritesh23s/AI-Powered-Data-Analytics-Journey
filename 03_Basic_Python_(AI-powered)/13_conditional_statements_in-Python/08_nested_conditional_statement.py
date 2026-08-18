# *************** NESTED CONDITIONAL STATEMENTS ***************

# A conditional statement can be placed inside another
# conditional statement.
# This is called a nested conditional statement.

# Syntax:
# if condition:
#     if condition:
#         do something
#     else:
#         do something
# else:
#     do something


# Example:
# 01).
age = 21

if age >= 18:

    if age >= 60:
        print("Senior citizen")
    elif age >= 25:
        print("Working age")
    else:
        print("College going")

else:
    print("Child")

# Output:
# College going


# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given the age and student status of a person, determine
# whether the person is eligible for a student discount.
#
# Input:
# An integer age and a student status ("yes" or "no").
#
# Conditions:
# If age is 18 or above, check the student status.
# If the person is a student, print "Student discount available".
# Otherwise, print "No student discount".
#
# If age is below 18, print "Not eligible".
#
# Output:
# Print the appropriate result based on the given conditions.
#
# Example:
# Input:
# Age: 21
# Student status: yes
#
# Output:
# Student discount available

student_age = int(input("Please enter your age: "))

if student_age >= 18:

    is_student = input("You are a student? Please enter yes or no: ")
    is_student = is_student.strip().lower()
    
    if is_student == "yes":
        print("Student discount available")
    else:
        print("No student discount")
else:
    print("Not eligible")
