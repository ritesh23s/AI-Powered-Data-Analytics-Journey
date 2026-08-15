# ******************** ADDING AND UPDATING VALUES ********************

# We can add a new key-value pair or update
# the value of an existing key.

# Syntax:
# variable_name["key"] = value

# Example:
# 01).
employee = {
    "name": "Himanshu",
    "city": "Delhi",
    "company": "Meta",
    "salary": 45  # LPA
}

print("Original dictionary:", employee)

# Output:
# Original dictionary: {'name': 'Himanshu', 'city': 'Delhi', 'company': 'Meta', 'salary': 45}


# ******************** ADDING A NEW KEY-VALUE PAIR ********************

# We can add a new key-value pair
# by using a new key.

employee["age"] = 23

print("After adding a new key-value pair:", employee)

# Output:
# After adding a new key-value pair:
# {'name': 'Himanshu', 'city': 'Delhi', 'company': 'Meta', 'salary': 45, 'age': 23}

# Note:
# When a new key-value pair is added,
# it is added to the end of the dictionary.


# ******************** UPDATING AN EXISTING KEY-VALUE PAIR ********************

# We can update the value of an existing key.

# Syntax:
# variable_name["existing_key"] = new_value

# Example:
# 01).
employee["name"] = "Anurag"

print("After updating the existing key-value pair:", employee)

# Output:
# After updating the existing key-value pair:
# {'name': 'Anurag', 'city': 'Delhi', 'company': 'Meta', 'salary': 45, 'age': 23}

# Note:
# If the key already exists, its value is replaced
# with the new value.
# If the key does not exist, a new key-value pair is added.