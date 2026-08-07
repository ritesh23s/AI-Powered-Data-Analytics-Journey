# ******************** COUNT() LIST METHOD ********************

# count(): It is used to count how many times a specified value appears in a list.

# Syntax:
# variable_name.count(value)

# Example:
# 01).
items = ["apple", "banana", "orange", "pen", "chair", "mango", "apple", "banana", "apple"]

print(items.count("banana"))

# Output: 2

# Example:
# 02).
numbers = [10, 20, 30, 20, 40, 20]

print(numbers.count(20))

# Output: 3

# Note:
# If the given value is not found in the list,
# the count() method returns 0.

print(numbers.count(50))
# Output: 0