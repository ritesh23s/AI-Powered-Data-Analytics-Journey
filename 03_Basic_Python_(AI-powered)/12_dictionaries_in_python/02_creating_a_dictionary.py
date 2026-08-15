# ******************** DICTIONARIES IN PYTHON ********************
# ******************** CREATING A DICTIONARY ********************

# Dictionaries are created using curly brackets {}
# with key-value pairs separated by colons (:).

# Syntax:
# variable_name = {
#     "key1": value1,
#     "key2": value2,
#     ...
# }

# Example:
# 01).
car = {
    "name": "Bolero",
    "brand": "Mahindra",
    "color": "white",
    "engine": "Diesel"
}

print(car)

# Output:
# {'name': 'Bolero', 'brand': 'Mahindra', 'color': 'white', 'engine': 'Diesel'}


# ******************** CREATING A DICTIONARY USING dict() ********************

# We can also create a dictionary using the dict() function.

# Syntax:
# variable_name = dict(key1=value1, key2=value2, ...)

# Example:
# 02).
student = dict(name="Shubham", roll_no=25, branch="CSE")

print(student)

# Output:
# {'name': 'Shubham', 'roll_no': 25, 'branch': 'CSE'}