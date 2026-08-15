# ******************** REMOVING DICTIONARY ITEMS ********************
# ******************** POP() METHOD ********************

# pop(): It is used to remove a specified key-value pair
# from a dictionary and return the removed value.

# Syntax:
# variable_name = dictionary_name.pop("key")

# Example:
# 01).
employee = {
    "name": "Hemant",
    "age": 26,
    "company": "Google",
    "salary": 50,  # LPA
    "city": "Delhi",
    "email": "hemant@google.com"
}

print("Original dictionary:", employee)
# Output: 
# Original dictionary: {'name': 'Hemant', 'age': 26, 'company': 'Google', 'salary': 50, 'city': 'Delhi', 'email': 'hemant@google.com'}


remove_employee_email = employee.pop("email")

print("Removed value:", remove_employee_email)
# Output:
# Removed value: hemant@google.com

print("After removing the email:", employee)
# Output:
# After removing the email:
# {'name': 'Hemant', 'age': 26, 'company': 'Google', 'salary': 50, 'city': 'Delhi'}

# Note:
# The pop() method modifies the original dictionary.
# It removes the specified key-value pair.
# It returns the value of the removed key.
# If the specified key does not exist,
# pop() raises a KeyError.