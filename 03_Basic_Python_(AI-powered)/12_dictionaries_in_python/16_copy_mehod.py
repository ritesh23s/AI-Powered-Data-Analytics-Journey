# ******************** DICTIONARY COPY ********************
# ******************** COPY() METHOD ********************

# copy(): It is used to create a shallow copy of a dictionary.

# Syntax:
# variable_village.copy()

# Example:
# 01).
address = {
    "village": "Kachnar",
    "pin_code": 841210,
    "police_station": "Siswan"
}

copy_add = address.copy()

print(address)
# Output:
# {'village': 'Kachnar', 'pin_code': 841210, 'police_station': 'Siswan'}

print(copy_add)
# Output:
# {'village': 'Kachnar', 'pin_code': 841210, 'police_station': 'Siswan'}

# Note:
# copy() creates a separate copy of the dictionary.
# Changes made to the copied dictionary do not affect the original dictionary.