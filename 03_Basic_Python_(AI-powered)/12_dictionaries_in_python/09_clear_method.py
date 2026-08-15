# ******************** REMOVING DICTIONARY ITEMS ********************
# ******************** CLEAR() METHOD ********************

# clear(): It is used to remove all items
# (key-value pairs) from a dictionary.

# Syntax:
# variable_name.clear()

# Example:
# 01).
student = {
    "name": "Shubham",
    "age": 23,
    "Course": "Btech",
    "roll_no": 25
}

print(student)

# Output:
# {'name': 'Shubham', 'age': 23, 'Course': 'Btech', 'roll_no': 25}


# Using clear() method to clear the dictionary.
student.clear()

print("After clearing the dictionary:", student)

# Output:
# After clearing the dictionary: {}

# Note:
# The clear() method removes all key-value pairs from the original dictionary.
# It does not delete the dictionary itself.
# After using clear(), the dictionary becomes empty.

print(student)
# Output: {}