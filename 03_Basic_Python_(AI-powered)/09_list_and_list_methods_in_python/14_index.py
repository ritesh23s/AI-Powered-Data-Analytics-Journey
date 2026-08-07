# ******************** INDEX() LIST METHOD ********************

# index(): It is used to return the index of the first occurrence of a specified value.

# Syntax:
# variable_name.index(value)

# Example:
# 01).
items = ["mango", "banana", "apple", 1245, 2.56, False]

print(items.index("banana"))
# Output:
# 1

print(items.index(1245))
# Output:
# 3

# Example:
# 02).
numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))

# Output:
# 1

# Note:
# If the same value appears multiple times, the index() method returns the index
# of its first occurrence.

# If the given value is not found in the list, the index() method raises a ValueError.