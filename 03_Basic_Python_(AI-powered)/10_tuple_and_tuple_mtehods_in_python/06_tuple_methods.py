# ******************** TUPLE METHODS ********************

# Tuple Methods:
# Tuples have only two built-in methods:
# 01). count()
# 02). index()

# Note:
# Tuples are immutable, so tuple methods do not modify the original tuple.


# ******************** 01). COUNT() TUPLE METHOD ********************

# count(): It is used to count how many times
# a specified value appears in a tuple.

# Syntax:
# variable_name.count(value)

# Example:
# 01).
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))

# Output:
# 3

# Note:
# If the given value is not found in the tuple,
# count() returns 0.


# ******************** 02). INDEX() TUPLE METHOD ********************

# index(): It is used to return the index
# of the first occurrence of a specified value in a tuple.

# Syntax:
# variable_name.index(value)

# Example:
# 01).
fruits = ("apple", "banana", "mango", "banana", "orange")

print(fruits.index("banana"))

# Output:
# 1

# Note:
# If the same value appears multiple times,
# index() returns the index of its first occurrence.

# If the given value is not found in the tuple,
# index() raises a ValueError.


# ******************** TUPLE BUILT-IN FUNCTION ********************

# len(): It is used to get the number of elements
# in a tuple.

# Syntax:
# len(variable_name)

# Example:
# 01).
items = ("pen", "book", "mouse", "keyboard")

print(len(items))

# Output:
# 4


# ******************** TUPLE SLICING ********************

# Tuple slicing: It is used to extract a portion
# of a tuple.

# Syntax:
# variable_name[start_index:end_index]

# Note:
# The start index is included,
# but the end index is not included.

# Example:
# 01).
fruits = ("apple", "banana", "mango", "orange", "grapes")

print(fruits[1:4])

# Output:
# ('banana', 'mango', 'orange')


# ******************** TUPLE MEMBERSHIP ********************

# The "in" keyword is used to check
# whether an element exists in a tuple.

# It returns a Boolean value:
# True or False

# Syntax:
# value in variable_name

# Example:
# 01).
fruits = ("apple", "banana", "mango", "orange")

print("banana" in fruits)

# Output:
# True 