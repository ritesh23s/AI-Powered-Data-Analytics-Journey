# ******************** REMOVING ELEMENTS FROM A SET ********************
# ******************** DISCARD() SET METHOD ********************

# discard(): It is used to remove a specified element from a set
# without raising an error if the element does not exist.

# We use discard() when we are not sure whether
# the specified element exists in the set or not.

# If the element exists, discard() removes it.
# If the element does not exist, it does nothing and
# does not raise any error.

# Syntax:
# variable_name.discard(value)

# Example:
# 01).
fruits = {"apple", "mango", "orange", "banana"}

fruits.discard("grapes")

print(fruits)

# Possible Output:
# {'mango', 'banana', 'orange', 'apple'}

# No error is raised because "grapes"
# does not exist in the set.


# Example:
# 02).
fruits.discard("orange")

print(fruits)

# Possible Output:
# {'banana', 'apple', 'mango'}

# "orange" exists in the set,
# so discard() removes it.


# Wrong:
# fruits.discard("banana", "orange")

# Output:
# TypeError: set.discard() takes exactly one argument (2 given)

# Error occurs because discard() accepts only one argument.

# Note:
# The discard() method modifies the original set.
# It does not raise an error if the specified element
# does not exist in the set.