# ******************** COPYING LIST ********************
# ******************** COPY() LIST METHOD ********************

# copy(): It is used to create a copy of a list.

# Syntax:
# variable_name.copy()

# Example:
# 01).
fruits = ["apple", "mango", "orange", "banana"]

copy_of_fruits = fruits.copy()

print("Original List:", fruits)
print("Copied List:", copy_of_fruits)

# Output:
# Original List: ['apple', 'mango', 'orange', 'banana']
# Copied List: ['apple', 'mango', 'orange', 'banana']

# Note:
# The copy() method returns a new list.
# It does not modify the original list.