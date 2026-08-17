# ******************** TUPLE PACKING ********************

# Tuple Packing: Tuple packing is the process of packing multiple values
# into a single tuple without explicitly using parentheses.

# Example:
# 01).
name = "Shubham"
age = 24
city = "Siwan"

person = name, age, city

print(person)

# Output: ('Shubham', 24, 'Siwan')

print("Datatype of person:", type(person))
# Output: Datatype of person: <class 'tuple'>


# Note:
# Python automatically creates a tuple
# when multiple values are assigned to a single variable
# using commas.



# Parentheses are optional when creating a tuple.

# Example:
# 02).
items = "pen", "book", "mouse"

print(items)

# Output: ('pen', 'book', 'mouse')


print("Datatype of items:", type(items))
# Output: Datatype of items: <class 'tuple'>