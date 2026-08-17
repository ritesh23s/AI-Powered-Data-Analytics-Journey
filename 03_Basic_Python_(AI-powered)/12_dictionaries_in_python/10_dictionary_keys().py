# **************** DICTIONARY KEYS, VALUES, AND ITEMS ****************
# ******************** KEYS() METHOD ********************

# keys(): It is used to get all the keys of a dictionary.
# It does not return the values it only returns keys.

# Syntax:
# variable_name.keys()

# Example:
# 01).
student = {
    "name": "Shubham",
    "age": 23,
    "Course": "Btech",
    "roll_no": 25,
    "email": "shubham@sumanicAI.com"
}

print(student.keys())

# Output:
# dict_keys(['name', 'age', 'Course', 'roll_no', 'email'])

# Here, keys() returns all the keys of the "student" dictionary.