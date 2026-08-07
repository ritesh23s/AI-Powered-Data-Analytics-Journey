# ******************** SORTING LIST ********************
# ******************** REVERSE() LIST METHOD ********************

# reverse(): It is used to reverse the order of elements in a list.

# Syntax:
# variable_name.reverse()

# Example:
# 01).
items = ["apple", "banana", "mango", "orange"]

print("Original List:", items)

items.reverse()

print("Reversed List:", items)

# Output:
# Original List: ['apple', 'banana', 'mango', 'orange']
# Reversed List: ['orange', 'mango', 'banana', 'apple']

# Note:
# The reverse() method modifies the original list.
# It does not sort the list.
# It only reverses the current order of elements.

# ******************** sort(reverse=True) vs reverse() ********************

# sort(reverse=True)
# - Sorts the list in descending order.

# reverse()
# - Only reverses the current order of the list.
# - It does not sort the list.