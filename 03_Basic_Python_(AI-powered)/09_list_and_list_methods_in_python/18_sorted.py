# ******************** SORTING LIST ********************
# ******************** SORTED() FUNCTION ********************

# sorted(): It is used to return a new sorted list without modifying the original list.

# Numbers: Small to Large (1 → 10)
# Strings: Alphabetical Order (A → Z)

# Syntax:
# sorted(variable_name)

# Example:
# 01).
numbers = [65, 20, 56, 86, 45, 30, 22, 12, 89]

sorted_numbers = sorted(numbers)

print("Original Numbers:", numbers)
print("Sorted Numbers:", sorted_numbers)

# Output:
# Original Numbers: [65, 20, 56, 86, 45, 30, 22, 12, 89]
# Sorted Numbers: [12, 20, 22, 30, 45, 56, 65, 86, 89]

# Note:
# The sorted() function does not modify the original list.
# It returns a new sorted list.




# ******************** sort() vs sorted() ********************

# sort()
# - List Method
# - Modifies the original list.

# sorted()
# - Built-in Function
# - Returns a new sorted list.
# - Does not modify the original list.