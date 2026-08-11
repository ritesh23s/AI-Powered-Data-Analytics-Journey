# ******************** SETS ARE MUTABLE ********************

# Sets are mutable, which means sets can be modified
# after creation.

# We can add or remove elements from an existing set
# without creating a new set.

# Example:
# 01).
items = {"apple", "pen", 2026}

items.add("mango")

print(items)

# Possible Output:
# {'apple', 2026, 'mango', 'pen'}

# Note:
# The original set is modified after using add().
# The order of elements in a set is not guaranteed.