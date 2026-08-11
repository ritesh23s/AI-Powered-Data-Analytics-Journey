# ******************** SET OPERATIONS ********************
# ******************** UNION() SET OPERATION ********************

# union(): It is used to combine the unique elements
# from two or more sets into a new set.

# Syntax:
# set1.union(set2)

# Example:
# 01).
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(result)

# Output:
# {1, 2, 3, 4, 5}

# Note:
# The union() method does not modify the original sets.
# It returns a new set.
# Duplicate elements are automatically removed.