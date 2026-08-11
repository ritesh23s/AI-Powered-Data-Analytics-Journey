# ******************** REMOVING ELEMENTS FROM A SET ********************
# ******************** REMOVE() SET METHOD ********************

# remove(): It is used to remove a specified element from a set.
# It raises a KeyError if the specified element does not exist in the set.

# Syntax:
# variable_name.remove(value)

# Example:
# 01).
items = {"apple", "mango", "pen", "chair", 2026}

items.remove("chair")

print(items)

# Possible Output:
# {'mango', 'apple', 2026, 'pen'}

items.remove("pen", "mango")
# Possible Output: TypeError: set.remove() takes exactly one argument (2 given)

# Note:
# The remove() method modifies the original set.
# The remove() method accepts only one argument.
# It cannot remove multiple elements at once.



# Wrong way to passing value to remove() method:
# items.remove("pen", "mango")

# Output:
# TypeError: set.remove() takes exactly one argument (2 given)

# Error occurs because two separate values
# are passed to remove().



# Example:
# 02).
fruits = {"mango", "orange", "apple", "banana"}

fruits.remove("grapes")

# Output:
# KeyError: 'grapes'

# Here, a KeyError is raised because the specified
# value does not exist in the set.