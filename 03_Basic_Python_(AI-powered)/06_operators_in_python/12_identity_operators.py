# ***************************** IDENTITY OPERATORS *****************************
# Object Identity vs Value Equality
# Identity operators are used to check whether two variables refer to the same object in memory.They do not compare only the values; they also compare the memory location (object identity).
# This is crucial when working with mutable objects like lists.
# syntax: 01). print(a is b), 02). a is b

# THE DIFFERENCE
# == checks if value are the same.
# is checks if they are the same object in memory.

# There are Two types of Identity Operators
# 01.) is identity operator
# 02.) is not identity operator

print("01). is identity operator")
# 01). is identity operator: It returns True if both variables refer to the same object in memory.
# It does not compare only the values. it also checks whether both variables point to the same memory location.
# Example:
a = [1, 2, 3]
b = [1, 2, 3]
c = a
# if we compare with == it returns "True". because it compare their value not memory location
print(a == b)

# if we compare with "is identity operator":
# It returns "False" because 'a' and 'b' have the same values,
# but they are different objects stored at different memory locations.
print(a is b)

# if we check a is c: 
# It returns "True" because 'c' refers to the same object as 'a'.
# Both variables point to the same memory location.
print(c is a)


print("02). is not identity operator")
# 02). is not identity operator: It returns True if both variables refer to different objects in memory.
# It does not compare only the values; it checks whether both variables point to different memory locations.
x = [4, 5, 6]
y = [4, 5, 6]
z = x

# if we compare with == it returns "True". because it compare their value not memory location
print(x == y)

# if we compare with "is not identity operator": 
# It returns True because 'x' and 'y' are different objects,
# even though their values are the same.
print(x is not y)

# if we check x is not z: 
# It returns False because 'z' refers to the same object as 'x'.
# Both variables point to the same memory location.
print(x is not z)