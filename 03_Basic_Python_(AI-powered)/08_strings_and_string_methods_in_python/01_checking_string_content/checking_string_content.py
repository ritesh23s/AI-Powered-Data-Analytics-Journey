# *************** CHECKING STRING CONTENT ***************

# Python provides methods to check the content of a string.

# 01). isalpha():
print("01). isalpha()")
# It is used to check whether all characters
# in a string are alphabet letters.

# It returns True or False.

# syntax:
# variable_name.isalpha()

# Example: 
# 01)
text = "shubham"
print(text.isalpha())

# 02).
name = "12545"
print(name.isalpha())

# 03).
full_name = "Shubham Yadav"
print(full_name.isalpha())
# It returns False because
# the string contains a space.


# 02). isdigit():
print("02). isdigit()")
# It is used to check whether all characters
# in a string are digits (numbers).

# It returns True or False.

# syntax:
# variable_name.isdigit()

# Example:
# 01).
pin_code = "841210"
print(pin_code.isdigit())

# 02).
village = "Kachnar"
print(village.isdigit())

# 03).
phone_no = "98765 43210"
print(phone_no.isdigit())
# It returns False because
# the string contains a space.


# 03). isalnum():
print("03). isalnum()")

# It is used to check whether all characters
# in a string are alphabets, digits, or both.

# It returns True or False.

# Syntax:
# variable_name.isalnum()

# Example:
# 01).
username = "shubham1234"
print(username.isalnum())

# 02).
city = "Siwan"
print(city.isalnum())

# 03).
name_and_pin = "Shubham 841210"
print(name_and_pin.isalnum())

# It returns False because
# the string contains a space.