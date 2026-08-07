# ******************** SORTING LIST ********************
# ******************** SORT() LIST METHOD ********************
# ******************** DESCENDING ORDER ********************

# sort(reverse=True): It is used to sort the elements of a list in reverse way.

# Numbers: Large to Small (10 → 1)
# Strings: Reverse Alphabetical Order (Z → A)

# Syntax:
# variable_name.sort(reverse=True)

# Example:
# 01).
marks = [85, 30, 95, 70, 40, 65]

marks.sort(reverse=True)

print(marks)

# Output:
# [95, 85, 70, 65, 40, 30]


# Example:
# 02).
fruits = ["mango", "banana", "apple", "orange"]

fruits.sort(reverse=True)

print(fruits)

# Output:
# ['orange', 'mango', 'banana', 'apple']


# Note:
# The sort() method modifies the original list.
# reverse=True sorts the list in descending order.