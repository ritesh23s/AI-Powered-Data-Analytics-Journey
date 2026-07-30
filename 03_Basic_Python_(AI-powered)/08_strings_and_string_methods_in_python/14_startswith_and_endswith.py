# *************** STARTSWITH() AND ENDSWITH() STRING METHOD ***************
print("01). startswith()")
# 01). startswith(): It is used to checks whether a string starts with a given value.

# It returns a boolean value (True or False)

# Syntax:
# variable_name.startswith("given_value")

# Example:
# 01).
name = "Dravin"

print(name.startswith("D"))
# output: True

print(name.startswith("i"))
# output: False



print("02). endswith()")
# 02). endswhith(): It is used to checks whether a string starts with a given value.

# Its returns a boolean value (True or False)

# Syntax:
# variable_name.endswith("given_value")

# Example:
# 01).
word = "Bokachoda"

print(word.endswith("a"))
# output: True

print(word.endswith("k"))
# output: False


# Note:
# Both startswith() and endswith()
# return a boolean value (True or False).
# They do not modify the original string.