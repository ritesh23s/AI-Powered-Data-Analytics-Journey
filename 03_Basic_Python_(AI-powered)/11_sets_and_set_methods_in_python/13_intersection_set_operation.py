# ******************** SET OPERATIONS ********************

# ******************** INTERSECTION() SET OPERATION ********************

# The intersection() function is really useful when we want to find out what is common between two sets of things.

It helps us figure out what elements are the same in both the sets we are looking at.

# Syntax:

# set1.intersection(set2)

# Example:

# 01).

# We have two sets let us call them a and b.

A is a set that contains the numbers 1, 2 3 4, 3 and 2.

b is a set that contains the numbers 2, 4 5 6 7 8, 9 and 10.

We use the intersection() function to find the elements, in set a and set b.

result = a.intersection(b)

Then we print the result to see what we get.

print(result)

# Output: {2, 4}

# Note:

When we use the intersection() function it only gives us the elements that're in both sets.

The intersection() function does not change the sets, which are set a and set b in this case.

It gives us a brand set that contains only the common elements from set a and set b.