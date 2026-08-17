# **************** DICTIONARY KEYS, VALUES, AND ITEMS ****************
# ******************** ITEMS() METHOD ********************

# items(): It is used to get all the key-value pairs of a dictionary.
# Each key-value pair is returned as a tuple.

# Syntax:
# variable_name.items()

# Example:
# 01).
student = {
    "name": "Shubham",
    "age": 23,
    "Course": "Btech",
    "roll_no": 25,
    "email": "shubham@sumanicAI.com"
}

print(student.items())

# Output:
# dict_items([
#     ('name', 'Shubham'),
#     ('age', 23),
#     ('Course', 'Btech'),
#     ('roll_no', 25),
#     ('email', 'shubham@sumanicAI.com')
# ])


# Here, items() returns all the key-value pairs
# of the "student" dictionary.
# Each key-value pair is represented as a tuple.