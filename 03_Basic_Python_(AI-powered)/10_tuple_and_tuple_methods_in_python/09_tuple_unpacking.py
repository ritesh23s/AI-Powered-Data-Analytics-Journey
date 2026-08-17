# ******************** TUPLE UNPACKING ********************

# Tuple Unpacking: Tuple unpacking is the process of assigning
# the elements of a tuple to multiple variables.

# Syntax:
# variable1, variable2, variable3 = tuple_name

# Example:
# 01).
person = ("Shubham", 24, "Siwan")

name, age, city = person

print(name)
print(age)
print(city)

# Output:
# Shubham
# 24
# Siwan

# Note:
# The number of variables must match the number of elements in the tuple.

# Example:
# 02).
items = ("pen", "book", "mouse")

item1, item2, item3 = items

print(item1)
print(item2)
print(item3)

# Output:
# pen
# book
# mouse

ites_details = ("apple", "bat", 2026)
fruit, cricket, year = ites_details
print(fruit)
print(cricket)
print(year)