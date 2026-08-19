# ******************** SET OPERATIONS ********************

# ******************** INTERSECTION() SET OPERATION ********************

# The intersection() function is really useful when we want to find out what is common between two sets of things.

# It helps us figure out what elements are the same in both the sets we are looking at.

# Syntax:

# set1.intersection(set2)

# Example:

# 01).

a = {1, 2, 3, 4, 3, 2, 4, 0}
b = {2, 4, 5, 6, 7, 8, 9, 10}

result = a.intersection(b)
print(result)

# Note:
# Only the elements that are present in both sets are included in the result.
# The intersection() method does not modify the original sets.
# It returns a new set.