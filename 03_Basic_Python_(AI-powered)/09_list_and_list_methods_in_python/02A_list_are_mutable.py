# ******************** LISTS ARE MUTABLE ********************

# Lists are Mutable:
# A list can be changed after it is created.
# When a list is modified, Python changes the original list.
# It does not create a new list.

# Example:
# 01).
fruits = ["apple", "banana", "mango"]

print("Original List:", fruits)

fruits[1] = "orange"

print("Modified List:", fruits)

# Output:
# Original List: ['apple', 'banana', 'mango']
# Modified List: ['apple', 'orange', 'mango']

# Note:
# The value at index 1 is replaced with "orange".
# The original list is modified.
# A new list is not created.