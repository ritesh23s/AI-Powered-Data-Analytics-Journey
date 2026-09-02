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
# ******************** 01). len(): FUNCTION ********************

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

# ******************** 02). sorted(): FUNCTION ********************
# sorted(): It is used to short a tupple as a list.
# it returns a new list of tuple after sorted

# for string case:
# It sorted as A to Z

# for number case:
# It sorted as increasing order 1 to 100


# Syntax: sorted(variable_name)
# Example:
# 01).
movie = ("bahubali", "shidhat", "mirzapur", "drishyam", "avtar")
sorted_movies = sorted(movie)
print("Origina:", movie)
print("After sorted:", sorted_movies)

# Output: 
# Origina: ('bahubali', 'shidhat', 'mirzapur', 'drishyam', 'avtar')
# After sorted: ['avtar', 'bahubali', 'drishyam', 'mirzapur', 'shidhat']

# 02).
quantity = (100, 56, 12, 32, 1, 45, 8, 78, 98, 46)
sorted_quantity = sorted(quantity)
print("Original:", quantity)
print("After shorted:", sorted_quantity)

# Output
# Original: (100, 56, 12, 32, 1, 45, 8, 78, 98, 46)
# After shorted: [1, 8, 12, 32, 45, 46, 56, 78, 98, 100]

# Note:
# it alwas return a new list.
# It does not modifies the original tuple



# ************************* 02). sum(): FUNCTION *************************
# sum(): it is used to calculate sum of a tuple
# Syntax:
# sum(variable_name)

# Example:
# 01).
numbers = (1, 5, 7, 8, 125)
print(sum(numbers))
# Output: 146



# ************************* 02). min()/max(): FUNCTION *************************
# min(): It is used to find minimun value of a tuple.
# max(): It is used to find maximum value of a tuple.

# Suntax:
# min(variable_name)
# max(variable_name)

# Example:
# 01).
marks = (45, 56, 23, 45, 12, 10, 45, 5, 78, 68, 82)
print("Minimum marks:" , min(marks))
print("Maximum marks:" , max(marks))

# Output:
# Minimum marks: 5
# Maximum marks: 82


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