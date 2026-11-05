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

# 02).
img_details = {
    'location': 'Siwan, Bihar',
    'name': 'xyz.jpeg',
    'size': '256kb',
    'file_code': 45721
}

print(img_details)
# Output:
# {'location': 'Siwan, Bihar', 'name': 'xyz.jpeg', 'size': '256kb', 'file_code': 45721}

# Note: Always write the dictionaries key inside a singal quotes or dounle quotes



# ******************** CREATING A DICTIONARY USING dict() ********************

# We can also create a dictionary using the dict() function.

# Syntax:
# variable_name = dict(key1=value1, key2=value2, ...)

# Example:
# 03).
student = dict(name="Shubham", roll_no=25, branch="CSE")

print(student)

# Output:
# {'name': 'Shubham', 'roll_no': 25, 'branch': 'CSE'}

# 04).
phone_specification = dict(model = "Vivo T4x 5G", brand = "vivo", storage = "6/128gb", battery = "6500mah")
print(phone_specification)

# Output:
# {'model': 'Vivo T4x 5G', 'brand': 'vivo', 'storage': '6/128gb', 'battery': '6500mah'}

