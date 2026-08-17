# ******************** DICTIONARY UPDATE() METHOD ********************

# update(): It is used to add multiple key-value pairs
# to a dictionary at once.

# Syntax:
# variable_name.update({
#     "key1": value1,
#     "key2": value2,
#     "key3": value3,
#     ...
# })

# Example:
# 01).
address = {
    "village": "Kachnar",
    "pin_code": 841210,
    "police_station": "Siswan"
}

print("Original:", address)

address.update({
    "district": "Siwan",
    "state": "Bihar"
})

print("After adding key-value pairs:", address)

# Output:
# After adding key-value pairs:
# {'village': 'Kachnar', 'pin_code': 841210,
#  'police_station': 'Siswan', 'district': 'Siwan', 'state': 'Bihar'}