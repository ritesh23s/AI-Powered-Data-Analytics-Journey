# ******************** SET OPERATIONS ********************
# ******************** DIFFERENCE() SET OPERATION ********************

# difference(): It is used to find the elements that are present in
# the first set but not present in the second set.

# Syntax:
# set1.difference(set2)

# Example:
# 01).
a = {1, 2, 3, 4, 3, 2, 4, 0}
b = {2, 4, 5, 6, 7, 8, 9, 10}

result = a.difference(b)

print(result)

# Output:
# {0, 1, 3}

# Note:
# The difference() method returns a new set.
# It does not modify the original sets.