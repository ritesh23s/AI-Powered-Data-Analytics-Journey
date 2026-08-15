# ******************** ACCESSING DICTIONARY VALUES ********************
# ******************** USING GET() METHOD ********************

# get(): It is used to safely access a dictionary value using its key.

# Syntax:
# variable_name.get("key")

# Example:
# 01).
employee = {
    "city": "Delhi",
    "company": "Meta",
    "salary": 45  # LPA
}

print("₹", employee.get("salary"), "LPA")

# Output:
# ₹ 45 LPA


# Example:
# 02).
print(employee.get("age"))

# Output:
# None

# Note:
# If the specified key does not exist in the dictionary,
# get() returns None instead of raising an error.