# ******************** ADDING ELEMENTS TO A SET ********************
# ******************** UPDATE() SET METHOD ********************

# update(): It is used to add multiple elements
# from a list, tuple, or another set to a set.

# Syntax:
# variable_name.update(iterable)

# Example:
# 01).
details = {"Shubham", 23, 2002}

details.update(["Siwan", "April"])

print(details)

# Possible Output:
# {'Shubham', 23, 2002, 'Siwan', 'April'}

# Note:
# The update() method modifies the original set.
# It can add multiple elements at once.
# List, tuple, or set can be used to provide multiple elements.


# Example:
# 02).
details = {"Shubham", 23, 2002}

details.update(("Siwan", "April", 25))

print(details)

# Possible Output:
# {'Shubham', 23, 2002, 'Siwan', 'April', 25}


# ******************** IMPORTANT NOTE ********************

# Multiple values cannot be passed directly to update().
# Multiple values should be provided inside a list, tuple, or set.

# Example:
# Wrong:
# details.update("Siwan", "April")
# Here, Error will occur because multiple values are passed directly as separate arguments.

# Correct way to pass multiple values to update():
details.update(["Siwan", "April"])




# Wrong:
# details.update(25)
# An error will occur because 25 is a single integer value
# and update() requires an iterable containing elements.


# ******************** STRING CASE ********************

# When a string is passed directly to update(), 
# Python treats each character of the string as a separate element.

# Example:
details = {"Shubham", 23}

details.update("Siwan")

print(details)

# Possible Output:
# {'Shubham', 23, 'S', 'i', 'w', 'a', 'n'}

# Here, "Siwan" is not added as a single element.
# Python divides the string into individual characters
# and adds them separately: 'S', 'i', 'w', 'a', 'n'