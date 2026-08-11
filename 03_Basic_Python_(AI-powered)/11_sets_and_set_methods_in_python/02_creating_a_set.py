# ******************** CREATING A SET ********************

# Sets can be created using curly brackets {}
# or the set() function.

# Syntax:
# variable_name = {value1, value2, value3, ...}

# Example:
# 01).
numbers = {1, 2, 3, 4}

names = {"Shubham", "Dravin", "Anand"}

print(numbers)
# Output: {1, 2, 3, 4}

print(names)
# Output: {'Shubham', 'Dravin', 'Anand'}



# ******************** CREATING AN EMPTY SET ********************

# An empty set is created using the set() function.

empty_set = set()

print(empty_set)

# Output:
# set()

print(type(empty_set))

# Output:
# <class 'set'>


# ******************** CONVERTING TUPLE TO SET ********************

details = "Shubham", "Siwan", 2002

print(details)

# Output:
# ('Shubham', 'Siwan', 2002)

set_details = set(details)

print(set_details)

# Output:
# {'Shubham', 'Siwan', 2002}

print("Type of details:", type(details))
# Output:
# Type of details: <class 'tuple'>

print("Type of set_details:", type(set_details))
# Output:
# Type of set_details: <class 'set'>