# ******************** SPLIT() STRING METHOD ********************

# split(): It is used to split a string into a list using a separator.

# Syntax:
# variable_name.split("separator")

# Example:
# 01).
text = "apple, banana, mango"

print(text.split(","))

# Output:
# ['apple', ' banana', ' mango']

# 02).
date = "30-07-2026"
print(date.split("-"))
# Output: ['30', '07', '2026']

# 03).
computer_languages = "Python Java C++"

print(computer_languages.split())

# Output:
# ['Python', 'Java', 'C++']

# Note:
# If no separator is provided, the split() method uses spaces as the default separator.


# **************** Note For Split() ****************
# The split() method returns a new list.
# It does not modify the original string.

languages = "Python, JavaScript, Java, MySQL"
language_list  = languages.split(",")
print(language_list)
# Output: ['Python', ' JavaScript', ' Java', ' MySQL']

print(languages)
# Output:
# Python, JavaScript, Java, MySQL
# (Original string)