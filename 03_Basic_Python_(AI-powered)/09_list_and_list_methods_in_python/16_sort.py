# ******************** SORTING LIST ********************
# ******************** SORT() LIST METHOD ********************

# sort(): It is used to sort the elements of a list in ascending order by default.

# Numbers: Small to Large (1 → 10)
# Strings: Alphabetical Order (A → Z)

# Syntax:
# variable_name.sort()

# Example:
# 01).
marks = [20, 10, 8, 18, 10]

marks.sort()

print(marks)

# Output:
# [8, 10, 10, 18, 20]


# Example:
# 02).
fruits = ["mango", "banana", "apple", "orange"]

fruits.sort()

print(fruits)

# Output:
# ['apple', 'banana', 'mango', 'orange']


# Note:
# The sort() method modifies the original list.
# By default, it sorts the list in ascending order.
# All elements should be of compatible data types.
# Otherwise, the sort() method raises a TypeError.