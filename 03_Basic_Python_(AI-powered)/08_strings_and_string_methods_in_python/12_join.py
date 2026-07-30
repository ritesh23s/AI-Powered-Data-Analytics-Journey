# *************** JOIN() STRING METHOD ***************

# join(): It is used to join the elements of a list into a single string
# using a separator.

# Syntax:
# "separator".join(list_name)

# Example:
# 01).
items = ["apple", "banana", "mango"]

print(",".join(items))

# Output:
# apple,banana,mango

# 02).
languages = ["Python", "Java", "C++"]

print(" ".join(languages))

# Output:
# Python Java C++

# 03).
date = ["30", "07", "2026"]

print("-".join(date))

# Output:
# 30-07-2026

# Note:
# The join() method returns a new string.
# It does not modify the original list.
# The join() method works only with string elements.
# The join() method does not have a default separator.
# You must specify a separator.