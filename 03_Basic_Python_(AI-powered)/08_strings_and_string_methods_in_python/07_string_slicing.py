# ******************** STRING SLICING ********************

# String Slicing:
# It is used to extract a part (portion) of a string.

# Syntax:
# variable_name[start_index:end_index]

# Note:
# The character at the start index is included,
# but the character at the end index is not included.

# Example:
# 01).
text = "Python Programming"

return_text = text[0:6]

print("Original String:", text)
print("Sliced String:", return_text)

# Output: 
# Original String: Python Programming
# Sliced String: Python

# 02).
fullname = "Shubham Yadav"

print(fullname[1:11])
# It returns: hubham Yad

print(fullname[:11])
# It returns: Shubham Yad
# Because the starting index is not given, Python automatically uses 0 as the starting index.

print(fullname[:])
# It returns: Shubham Yadav
# Because both the starting index and ending index are not given, Python automatically selects the complete string.

print(fullname[4])
# It returns: h
# Because Python returns the character present at index 4 of the string.

print(fullname[2:])
# It returns: ubham Yadav
# Because the ending index is not given, Python automatically selects the last character.

print(fullname[0:10000])
# It returns: Shubham Yadav
# If the ending index is greater than the length of the string, Python returns all available characters.

print(fullname[3:3])
# It returns an empty string (""). Because the start index and end index are the same.


# *************** NEGATIVE STRING SLICING ***************
# We can also use negative indexes in string slicing.
# Python counts negative indexes from the end of the string. Negative indexing starts from -1.

# Example:
print("Length of fullname:", len(fullname))

# 01).
print(fullname[-1])       
# is same as:
# fullname[-1 + len(fullname)] or fullname[12]
# It returns: v

# 02).
print(fullname[-7])       
# is same as:
# fullname[-7 + len(fullname)] or fullname[6]
# It returns: m

# 03).
print(fullname[-3:])        
# is same as:
# fullname[-3 + len(fullname):] or fullname[10:]           
# It returns: dav

# 04).
print(fullname[-5:-2])       
# is same as:
# fullname[-5 + len(fullname):-2 + len(fullname)] or fullname[8:11]
# It returns: Yad

# Note:
# Python automatically converts negative indexes internally.
# The calculations shown above are only for understanding.