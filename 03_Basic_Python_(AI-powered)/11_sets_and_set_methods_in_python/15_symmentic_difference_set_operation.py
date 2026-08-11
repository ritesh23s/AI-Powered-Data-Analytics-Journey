# ******************** SET OPERATIONS ********************
# ******************** SYMMETRIC DIFFERENCE() SET OPERATION ********************

# symmetric_difference(): It returns all the elements
# except the elements that are common in both sets.

# Syntax:
# set1.symmetric_difference(set2)

# Example:
# 01).
x = {1, 2, 3, 4, 3, 2, 4, 0}
y = {2, 4, 5, 6, 7, 8, 9, 10}

result = x.symmetric_difference(y)

print(result)

# Output:
# {0, 1, 3, 5, 6, 7, 8, 9, 10}

# Note:
# Common elements are removed from the result.
# Only the elements that are present in one set
# but not in the other set are included.
# The symmetric_difference() method returns a new set.
# It does not modify the original sets.