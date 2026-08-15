# ******************** REMOVING DICTIONARY ITEMS ********************
# ******************** POPITEM() METHOD ********************

# popitem(): It is used to remove and return
# the last inserted key-value pair from a dictionary.

# Syntax:
# variable_name = dictionary_name.popitem()

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

# Adding a new key-value pair
employee["email"] = "hemant@google.com"
print("After adding new key:", employee)


# Remove the last inserted key-value pair
removed_item = employee.popitem()
print("Removed item:", removed_item)
# Possible Output:
# Removed item: ('email', 'hemant@google.com')


print("After popitem():", employee)
# Output:
# After popitem(): {'name': 'Hemant', 'age': 26, 'company': 'Google', 'salary': 50, 'city': 'Delhi'}


# Note:
# The popitem() method modifies the original dictionary.
# It removes the last inserted key-value pair.
# It returns the removed key-value pair as a tuple.