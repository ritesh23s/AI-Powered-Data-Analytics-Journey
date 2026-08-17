# ******************** TUPLES ARE IMMUTABLE ********************

# Tuples are immutable, which means their elements
# cannot be changed, added, or removed after creation.

# Example:
# 01).
items = ("mango", "banana", "orange", "pen", 2026)

items[3] = "apple"

print(items)

# Output:
# TypeError: 'tuple' object does not support item assignment