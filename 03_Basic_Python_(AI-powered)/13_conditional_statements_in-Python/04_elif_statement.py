# *************** ELIF STATEMENT ***************

# elif: elif stands for "else if".
# It is used to check multiple conditions one by one.
# if and elif both together and also else

# Syntax:
# if condition:
#     do something
# elif condition:
#     do something
# else:
#     do something

# Example:
# 01).
marks = 65

if marks >= 90:
    print("Grade A+")
elif marks >= 60:
    print("Grade A")
elif marks >= 50:
    print("Grade B+")
elif marks >= 40:
    print("Grade B")
elif marks >= 30:
    print("Grade C")
else:
    print("You are failed")

# Output:
# Grade A


# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given an integer temperature, determine the weather condition
# based on the following rules.
#
# Input:
# An integer temperature.
#
# Conditions:
# temperature >= 35 → "Very Hot"
# temperature >= 25 → "Hot"
# temperature >= 15 → "Normal"
# temperature >= 5  → "Cold"
# otherwise          → "Very Cold"
#
# Output:
# Print the appropriate weather condition.
#
# Example:
# Input:
# 28
#
# Output:
# Hot

temperature = int(input("Enter temperature: "))
if temperature >= 35:
    print("Very Hot")
elif temperature >= 25:
    print("Hot")
elif temperature >= 15:
    print("Normal")
elif temperature >= 5:
    print("Cold")
else:
    print("Very Cold")