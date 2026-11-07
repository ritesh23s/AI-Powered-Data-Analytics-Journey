# *************** LOGICAL OPERATORS IN CONDITIONS ***************

# Logical operators are used to combine or reverse conditions.
# They return either True or False.

# Logical operators:
# and → Returns True if both conditions are True.
# or  → Returns True if at least one condition is True.
# not → Reverses the result of a condition.


# ******************** AND OPERATOR ********************

age = 25
country = "India"

if age >= 18 and country == "India":
    print("You can vote.")
else:
    print("You can't vote.")

# Output:
# You can vote.


# ******************** OR OPERATOR ********************

if age >= 18 or country == "USA":
    print("Allow entry to India.")
else:
    print("Entry not allowed.")

# Output:
# Allow entry to India.


# ******************** NOT OPERATOR ********************

if not age >= 18:
    print("You are not 18 years old.")
    print("You are not eligible for vote.")
else:
    print("You are 18 years old.")
    print("You can vote.")

# Output:
# You are 18 years old.
# You can vote.


# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given the age and country of a person, determine whether
# the person is eligible to vote in India.

# Input:
# An integer age and a country name.

# Conditions:
# The person must be 18 or above AND the country must be "India".

# Output:
# Print "Eligible to vote" if both conditions are True.
# Otherwise, print "Not eligible to vote".

# Example:
# Input:
# Age: 25
# Country: India

# Output:
# Eligible to vote

person_age = int(input("Enter your age: "))
person_country = input("Enter your country: ")
person_country = person_country.strip().lower()

if person_age >= 18 and person_country == "india":
    print("Eligible to vote. ")
else:
    print("Not eligible to vote. ")