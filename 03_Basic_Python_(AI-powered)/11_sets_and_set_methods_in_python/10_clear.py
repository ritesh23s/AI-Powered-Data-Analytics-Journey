# ******************** REMOVING ELEMENTS FROM A SET ********************
# ******************** CLEAR() SET METHOD ********************

# clear(): It is used to remove all elements from a set.

# Syntax:
# variable_name.clear()

# Example:
# 01).
fruits = {"apple", "mango", "banana", "orange"}

print(fruits)

# Possible Output:
# {'banana', 'orange', 'mango', 'apple'}

fruits.clear()

print("After clearing the fruits:", fruits)

# Output:
# set()

# Note:
# The clear() method removes all elements from the set.
# It modifies the original set and makes it an empty set.