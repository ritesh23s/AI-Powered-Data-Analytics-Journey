# ******************** SET OPERATIONS ********************
# ******************** INTERSECTION() SET OPERATION ********************

# intersection(): It is used to find the elements that are common in both sets.

# Syntax:
# set1.intersection(set2)

# Example:
# 01).
a = {1, 2, 3, 4, 3, 2}
b = {2, 4, 5, 6, 7, 8, 9, 10}

result = a.intersection(b)

print(result)

# Output: {2, 4}

# Note:
# Only the elements that are present in both sets are included in the result.
# The intersection() method does not modify the original sets.
# It returns a new set.