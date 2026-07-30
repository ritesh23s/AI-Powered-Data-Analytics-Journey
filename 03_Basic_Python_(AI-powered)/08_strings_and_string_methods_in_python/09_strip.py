# *************** STRIP() STRING METHOD ***************
print("STRIP() STRING METHOD")
# strip(): It is used to remove extra spaces from the beginning (start) and the end of a string.

# syntax:
# variable_name.strip()

# Example:
# 01)
enter_password = input("Enter Your Password: ")

password = enter_password.strip()
print("Password Entered by User:", enter_password)
print("Length of Password Entered by User:", len(enter_password))
print("Password After strip():", password)
print("Length of Password After strip():", len(password))


# Note:
# The strip() method always returns a new string.
# It does not modify the original string because strings are immutable.

print("#). THERE ARE TWO MORE STRIP() METHODS")
# There are two more strip() methods:

# 01). lstrip():
# It is used to remove extra spaces from the beginning (start)
# of a string.

# Syntax:
# variable_name.lstrip()

# Example 1:
text = "     Python"

print("Original String:", text)
print("After lstrip():", text.lstrip())


# 02). rstrip():
# It is used to remove extra spaces from the end of a string.

# Syntax:
# variable_name.rstrip()

# Example 1:
text = "Python     "

print("Original String:", text)
print("After rstrip():", text.rstrip())


# Note:
# lstrip() removes spaces only from the beginning (start).
# rstrip() removes spaces only from the end.
# Both methods return a new string.
# They do not modify the original string because strings are immutable.