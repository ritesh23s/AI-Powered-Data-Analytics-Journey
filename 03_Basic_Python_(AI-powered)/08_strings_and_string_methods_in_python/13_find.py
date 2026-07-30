# *************** FIND() STRING METHOD ***************
# find(): It is used to find the position of a character or substring
# in a string.

# Syntax:
# variable_name.find("given_value")

# Rules:
# If the given value is found, the find() method returns the index of its first occurrence.
# It returns -1 if the given value is not found in the string.

# Example:
# 01).
text = "We Love Python"
print(text.find("Python"))
# output: 8

# We can also find a single character inside a string.
print(text.find("e"))
# output: 1 (it returns first "e" index)

# It returns -1 if the given value is not foundin the string.
print(text.find("z"))
# output: -1

# It returns -1 because
# the given value is not found
# in the string.