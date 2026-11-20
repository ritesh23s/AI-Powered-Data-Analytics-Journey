# *********** FILE HANDLING IN PYTHON ***********
# *********** READING A FILE ***********
# There are following methods to read a file
# 01). .read()
# 02). .readline()
# 03). .readlines()

# ************** .READ() **************
# It is used to read the entire file content as a single string.

# Syntax:
# file = open("file_name(with complete path)", "r")
# file_content = file.read()
# file.close()

# Example 01).
file = open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_01.txt", "r")
file_content = file.read()
file.close()

print(file_content)
# Output:
# (Displays the complete text inside file_01.txt)
# Ka hal ba


# We can also pass the parameter inside the read() function.
# Example:
another_file = open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_02.txt", "r")
data = another_file.read(5)
another_file.close()
print(data)
# Output:
# (Display the first 5 characters of the file because we pass argument inside the
# read() function 5 so that display 5 characters from starting.) 
# Month




# ************** .READLINE() **************
# It is used to reads one line at a time.

# Syntax:
# file = open("file_name(with complete path)", "r")
# file_content = file.readline()
# file.close()

# Example 01).
file_for_readline = open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_03.txt", "r")

data_line1 = file_for_readline.readline()
print(data_line1)
# Output:
# (display the first line of this file with space because of \n )
# Hii, my self Shubh.


data_line2 = file_for_readline.readline()
print(data_line2)
# Output:
# (display the second line of this file with space because of \n )
# Good morning.


data_line3 = file_for_readline.readline()
print(data_line3)
# Output:
# (display the third line of this file with space because of \n )
# How are you..?


file_for_readline.close()


# ************** .READLINES() **************
# It reads all lines and return them as a list

# Syntax:
# file = open("file_name(with complete path)", "r")
# file_content = file.readlines()
# file.close()

f = open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_03.txt", "r")
data_for_f = f.readlines()
f.close()
print(data_for_f)
print(type(data_for_f))

# Output:
# (display the entire file text as a list)
# ['Hii, my self Shubh.\n', 'Good morning.\n', 'How are you..?\n', '\n', 'Nice to meet you.']
# <class 'list'>
