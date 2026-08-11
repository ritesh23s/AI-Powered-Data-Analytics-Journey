# ******************** UNIQUE ELEMENTS IN A SET ********************

# A set automatically removes duplicate values.
# Each value can appear only once in a set.

# Example:
# 01).
numbers = {1, 2, 3, 4, 5, 3, 4, 1}

print(numbers)

# Output:
# {1, 2, 3, 4, 5}

# Note:
# Duplicate values are automatically removed from a set.



# ******************** SET LENGTH (lenght of set) ********************

# We can find the number of elements in a set
# using the len() function.

# Example:
# 01).
numbers = {1, 2, 2, 3, 3, 4, 4}

print("The length of numbers:", len(numbers))

# Output:
# The length of numbers: 4

# Note:
# A set does not allow duplicate values.
# Therefore, duplicate values are removed automatically.
# The len() function then counts the unique elements in the set.