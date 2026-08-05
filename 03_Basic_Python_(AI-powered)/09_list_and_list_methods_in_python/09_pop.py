# ******************** POP() LIST METHOD ********************

# pop(): It is used to remove and return an element from a list.
# If an index is provided, it removes the element at that index.
# If no index is provided, it removes the last element.

# Syntax:
# variable_name.pop(index)

# Example:
# 01).
toys = ["drone", "robot dog", "teddy bear", "cube", "RC car"]

print("Original Toys List:", toys)

removed_cube = toys.pop(3)

print("List After Removing Cube:", toys)
print("Removed Value:", removed_cube)

# Output:
# Original Toys List: ['drone', 'robot dog', 'teddy bear', 'cube', 'RC car']
# List After Removing Cube: ['drone', 'robot dog', 'teddy bear', 'RC car']
# Removed Value: cube


# 02).
print("Original Toys List:", toys)

removed_last = toys.pop()

print("List After Removing Last Element:", toys)
print("Removed Value:", removed_last)

# Output:
# Original Toys List: ['drone', 'robot dog', 'teddy bear', 'RC car']
# List After Removing Last Element: ['drone', 'robot dog', 'teddy bear']
# Removed Value: RC car


# Note:
# The pop() method modifies the original list.
# It returns the removed element list.
# It accepts only one optional index argument.
