# ******************** MODIFYING LIST ELEMENTS ********************

# Modifying List Elements: Lists are mutable, which means their elements can be changed
# after the list is created.

# Syntax:
# variable_name[index] = new_value

# Example:
# 01).
items = ["bat", "ball", "mobile"]
print("Original list:", items)

items[len(items) - 1] = "wicket"
print("Modified List:", items)


# Output:
# ['bat', 'ball', 'wicket']

# Note:
# len(items) - 1 always returns the index of the last element.

# 02).
items_01 = ["bat", "ball", "mobile"]
print("Original List:", items_01)

items_01[-1] = "wicket"

print("Modified List:", items_01)

# Output:
# ['bat', 'ball', 'wicket']

# Note:
# -1 always represents
# the last element of the list.