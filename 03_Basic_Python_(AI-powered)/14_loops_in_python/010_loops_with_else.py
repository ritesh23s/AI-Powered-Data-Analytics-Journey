# ************* FOR LOOPS IN PYTHON *************
# ************* FOR LOOPS WITH ELSE  *************

# We can use for loop with else statement to continue our work 
# when loop is ended
# this else is optional for used.

# Syntax:
# for element in variable_name:
#     do something
# else:
#     do something


# Here, 
# "element" represents one item/value from the given variable.


# Example:
# 01).
items = [1, 2, 3, 45, "shubham", "apple", 25.45]
for n in items:
    print(n)
else:
    print("loop ended")


# 02).
nums = [1, 5, 4, 45, 23, 78]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
else:
    print("loop end..")