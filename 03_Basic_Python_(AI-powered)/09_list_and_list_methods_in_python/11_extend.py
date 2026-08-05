# ******************** EXTEND() LIST METHOD ********************

# extend(): It is used to add all elements from another list to the end of a list.

# Syntax:
# variable_name.extend(other_list)

# Example:
# 01).
items = ["apple", "mango", "banana"]
more_items = ["orange", 200, 45.5]

items.extend(more_items)

print(items)

# Output:
# ['apple', 'mango', 'banana', 'orange', 200, 45.5]

# Note:
# The extend() method modifies the original list.
# It adds all elements one by one from another list.

# ******************** append() vs extend() ********************

items = ["apple", "mango"]
more_items = ["orange", "banana"]

# append()
items1 = ["apple", "mango"]
items1.append(more_items)
print(items1)
# Output:
# ['apple', 'mango', ['orange', 'banana']]

# extend()
items2 = ["apple", "mango"]
items2.extend(more_items)
print(items2)
# Output:
# ['apple', 'mango', 'orange', 'banana']