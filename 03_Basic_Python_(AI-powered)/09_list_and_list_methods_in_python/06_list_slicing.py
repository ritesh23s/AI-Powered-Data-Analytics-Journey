# ***************** LIST SLICING *****************

# List Slicing: It is used to extract a part (portion) of a list.

# Syntax:
# variable_name[start_index:end_index]

# Note:
# The start index is included,
# but the end index is not included.

# Example:
# 01).
items = ["apple", "banana", "orange", "mango", 2026, 8, 5, 3.5454]

print(items[5])
# Output: 8

print(items[:4])
# Output: ['apple', 'banana', 'orange', 'mango']
# Because the starting index is not given, so python automatically uses 0 as the starting index.

print(items[2:])
# Output: ['orange', 'mango', 2026, 8, 5, 3.5454]
# Because the ending index is not given, so python automatically selects the last element.

print(items[2:6])
# Output: ['orange', 'mango', 2026, 8]

print(items[3:3])
# Output: []
# It returns an empty list because the start index and end index are the same.


# *************** LIST SLICING WITH NEGATIVE INDEX ***************

# Negative Indexing: It is used to access elements from the end of a list.
# Negative indexing starts from -1.

print(items[-3])
# Output: 8

print(items[-2:])
# Output: [5, 3.5454]

print(items[:-6])
# Output: ['apple', 'banana']


# *************** EDGE CASES ***************

print(items[-3:3])
# Output: []
# It is the same as:
# items[5:3]
# Since the start index (5) is greater than
# the end index (3), Python returns an empty list.

print(items[-1:-5])
# Output: []
# It is the same as:
# items[7:3]
# Since the start index (7) is greater than
# the end index (3), Python returns an empty list.

print(items[-4:-4])
# Output: []
# It is the same as:
# items[4:4]
# Since the start index and end index
# are the same, Python returns an empty list.

# Note:
# In list slicing, if the start index is greater than
# or equal to the end index, Python returns an empty
# list ([]) when using the default step value (1).

# Note:
# By default, Python slicing uses a step value of +1.
# This means Python moves from left to right.
# Therefore, if the start index is greater than the end index,
# Python returns an empty list ([]).