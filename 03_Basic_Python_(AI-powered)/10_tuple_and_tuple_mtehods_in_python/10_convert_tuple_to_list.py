# ******************** CONVERTING BETWEEN LIST AND TUPLE ********************

# Python provides list() and tuple() functions
# to convert between lists and tuples.


# ******************** TUPLE TO LIST ********************

# A tuple can be converted into a list using the list() function.

# Syntax:
# list(tuple_name)

# Example:
# 01).
items = ("apple", "banana", 12541, 20.2354, "mango")

items_list = list(items)

print(items_list)

# Output:
# ['apple', 'banana', 12541, 20.2354, 'mango']

# Note:
# After converting the tuple into a list,
# we can use list methods and perform list operations
# on the new list.


# ******************** LIST TO TUPLE ********************

# A list can be converted into a tuple using the tuple() function.

# Syntax:
# tuple(list_name)

# Example:
# 02).
items = ["apple", "banana", 12541, 20.2354, "mango"]

items_tuple = tuple(items)

print(items_tuple)

# Output:
# ('apple', 'banana', 12541, 20.2354, 'mango')

# Note:
# After converting the list into a tuple,
# the new tuple becomes immutable.