# *********************** LOOPS IN PYTHON ***********************
# ************* FOR LOOPS IN PYTHON *************

# for loop: The for loop is used to repeat a block of code
# for each item in a sequence.

# ********** IMPORTANT **********
# for loops are commonly used for sequential traversal. for traversing
# list, string, tuples, sets, dictionaries etc


# Syntax:
# for element in variable_name:
#     do something

# Here, 
# "element" represents one item/value from the given variable.

# Example:

# ************** 01). for loop with list. **************
items = ["mango", "banana", "cherry", "pen", "books", 25]
for item in items:
    print(item)

# Output:
# mango
# banana
# cherry
# pen
# books
# 25



# ************** 02). for loop with string. **************
name = "SHUBHAM"
for letter in name:
    print(letter)

# Output:
# S
# H
# U
# B
# H
# A
# M




# ************** 03). for loop with tuple. **************
details = ("Shubham", "MPU", 2026, "2023 to 2027")
for element in details:
    print(element)

# Output:
# Shubham
# MPU
# 2026
# 2023 to 2027




# ************** 04). for loop with sets. **************
marks = {23, 20, 56, 45, "shubham"}
for elmnt in marks:
    print(elmnt)

# Possible Output:
# 23
# 20
# 56
# 45
# shubham

# unique element behavior of set
num = {12, 45, 56, 12, 10, 86, 10, 12}
for n in num:
    print(n)

# Possible Output:
# 86
# 56
# 10
# 12
# 45    #here It remove dublicates values and return it.


# Note:
# A for loop can be used with different sequences such as 
# strings, lists, tuples, sets, dictionaries, etc.



# **************** Practice Question ****************
# Question:01
# Search for a number x in this tuple using loop.
# x = 64
# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 110, 75, 64, 45, 10)
# Solution:

tpl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 110, 75, 64, 45, 10)
x = 64
indx = 0
for elmnt in tpl:
    if elmnt == x:
        print(x, "is founded at index:" , indx)
    indx += 1

# Output:
# 64 is founded at index: 7
# 64 is founded at index: 12