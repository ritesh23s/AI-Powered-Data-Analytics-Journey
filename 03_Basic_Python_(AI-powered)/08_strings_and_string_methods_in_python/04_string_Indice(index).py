# *************** STRING ***************
# *************** STRING AND ACCESSING CHARACTER IN A STRING ***************
# String Indices (index)= A sting index is the number used to identify the position of each character in a string.

# Note - Indexing is always starts from 0

# Example: 
# 01).
word = "HELLO"
print("Example: 01).", word)

# |character  | H | E | L | L | O |
# |index      | 0 | 1 | 2 | 3 | 4 |

# # We can access any individual character of a string using its index.
# like this:
# syntex:  variable_name[char_position]

# ACCESSING CHARACTER OF THIS STRING

# word[0]; is "H"
# word[2]; is "L
print("word[0] = ", word[0])
print("word[2] = ", word[2])


# 02).
name = "Shubham Yadav"
print("Example: 02).", name)

# |Character | S | h | u | b | h | a | m |   | Y | a | d  | a  | v  |
# |index     | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

# now here, we acces the individual character of this string variable "name"
# ACCESSING CHARACTER OF THIS STRING

# name[0]; = "S"
# name[7]; = " " (space)
# name[10]; = "d"
print("name[0] = " , name[0])
print("name[7] = " , name[7])       # Space clearly dikhega
print("name[10] = " , name[10])
