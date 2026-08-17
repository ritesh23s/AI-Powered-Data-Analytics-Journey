# **************** DICTIONARY KEYS, VALUES, AND ITEMS ****************
# ******************** VALUES() METHOD ********************

# values(): It is used to get all the values of a dictionary.
# It does not return the keys it only returns values.

# Syntax:
# variable_name.values()

# Example:
# 01).
student = {
    "name": "Shubham",
    "age": 23,
    "Course": "Btech",
    "roll_no": 25,
    "email": "shubham@sumanicAI.com"
}

print(student.values())
# Output: 
# dict_values(['Shubham', 23, 'Btech', 25, 'shubham@sumanicAI.com'])


# Here, values() returns all the values of the "student" dictionary.