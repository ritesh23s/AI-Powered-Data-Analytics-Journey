# ******************** REMOVE() LIST METHOD ********************

# remove(): It is used to remove the first occurrence of a specified value from a list.

# Syntax:
# variable_name.remove(value)

# Example:
# 01).
subjects = ["Hindi", "English", "Math", "Science"]

subjects.remove("Math")

print(subjects)

# Output:
# ['Hindi', 'English', 'Science']

# Example:
# 02).
numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)

# Output:
# [10, 30, 20, 40]

# Here: Only the first occurrence of 20 is removed.

# Note:
# The remove() method modifies the original list.
# It removes only the first occurrence of the given value.
# If given argument(specified value) not persents in list it will cause an error.