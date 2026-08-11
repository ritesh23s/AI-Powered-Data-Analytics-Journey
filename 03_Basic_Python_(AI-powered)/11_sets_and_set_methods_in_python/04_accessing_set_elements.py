# ******************** ACCESSING SET ELEMENTS ********************

# Sets do not support indexing and slicing because
# they do not maintain a specific order.

# To access the elements of a set,
# we can use a for loop to access each element one by one.

# Example:
# 01).
items = {"apple", "mango", 2026, 2.24}

for item in items:
    print(item)

# Possible Output:
# 2026
# 2.24
# apple
# mango

# Note:
# The order of elements in a set is not guaranteed.
# Therefore, the output order may be different.