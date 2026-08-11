# ******************** REMOVING ELEMENTS FROM A SET ********************
# ******************** POP() SET METHOD ********************

# pop(): It is used to remove and return an arbitrary element
# from a set.

# Syntax:
# variable_name.pop()

# Example:
# 01).
items = {"apple", "banana", "mango"}

removed_item = items.pop()

print("Removed Item:", removed_item)
print("Remaining Items:", items)

# Possible Output:
# Removed Item: apple
# Remaining Items: {'banana', 'mango'}

# Note:
# The pop() method removes an any random element from the set.
# The pop() method also returns the removed element.
# We cannot specify which element will be removed.