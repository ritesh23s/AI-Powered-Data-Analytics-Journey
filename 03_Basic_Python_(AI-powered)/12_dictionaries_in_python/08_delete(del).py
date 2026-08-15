# ******************** REMOVING DICTIONARY ITEMS ********************
# ******************** DEL KEYWORD ********************

# del: It is used to delete a specified key-value pair
# from a dictionary.

# Syntax:
# del variable_name["key"]

# Example:
# 01).
employee = {
    "name": "Hemant",
    "age": 26,
    "company": "Google",
    "salary": 50,  # LPA
    "city": "Delhi"
}

print("Original Dictionary:", employee)

# Delete a key-value pair
del employee["age"]

print("After deleting a key-value pair:", employee)

# Output:
# After deleting a key-value pair:
# {'name': 'Hemant', 'company': 'Google', 'salary': 50, 'city': 'Delhi'}

# Note:
# The del keyword modifies the original dictionary.
# It deletes the specified key and its value.
# If the specified key does not exist, it raises a KeyError.