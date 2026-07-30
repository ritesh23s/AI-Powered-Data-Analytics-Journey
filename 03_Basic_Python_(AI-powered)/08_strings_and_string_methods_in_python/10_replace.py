# *************** REPLACE() STRING METHOD ***************
# replace(): It is used to replace a part of a string with another string.

# syntax:
# variable_name.replace("old_value", "new_value")

# Example:
# 01).
text = "I like Java"

after_replace = text.replace("Java", "Python")

print("Original String:", text)
print("Replaced String:", after_replace)


# Note:
# The replace() method returns a new string.
# It does not modify the original string because strings are immutable.