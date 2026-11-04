# ******************** SETS ARE MUTABLE ********************

# Sets are mutable, which means sets can be modified
# after creation.

# We can add or remove elements from an existing set
# without creating a new set.

# ************* Add element in a set *************
# Example:
# 01).
items = {"apple", "pen", 2026}

items.add("mango")

print(items)

# Possible Output:
# {'apple', 2026, 'mango', 'pen'}



# ************* Add element in a set *************
# Example:
# 01).
names = {"shubham", "jone", "anil", "shivam"}
names.remove("jone")
print(names)
# Possible Output:
# {'shubham', 'anil', 'shivam'}

# Note:
# The original set is modified after using add().
# The order of elements in a set is not guaranteed.