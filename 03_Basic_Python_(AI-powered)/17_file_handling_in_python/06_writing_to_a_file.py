# *********** FILE HANDLING IN PYTHON ***********
# *********** WRITING TO A FILE ***********
# There are two modes for writing to a file
# 01). Write Mode("w")
# 02). Append Mode("a")


# ********************* WRITE MODE ("w") *********************
# It is used to create a new file or overwrites an existing file.

# Syntax:
# file = open("file_name(with complete path)", "w")
# file.write("content for writing or overwriting")
# file.close()

# Example 01): For creating a new file.
file = open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_04(new).txt", "w")
file.write("Hii, Mr Shubham, how are you.?")
file.close()

# Output: Hii, Mr Shubham, how are you.?
# It creates a new file(file_04(new).txt) and writes the content inside it
# which we provided inside the write function.


# Example_02): For overwriting an existing file.
file_A = open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_05.txt", "w")
file_A.write("November 2026 is going on and winter is on peak.!")
file_A.close()
# Output: November 2026 is going on and winter is on peak.!
# It overwrites the existing file content which we provide inside the write()
# function.



# ********************* APPEND MODE ("a") *********************
# It is used to add content to the end of a file.

# Syntax:
# file = open("file_name(with complete path)", "a")
# file.write("content to add at the end of a file")
# file.close()

# Example 01):
append_content = "\nThis line is added using append mode.! in file_02.txt"

file_B = open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_02.txt", "a")
file_B.write(append_content)
file_B.close()
# Output: This line is added using append mode.! in file_02.txt
# It add the content inside the file_02.txt at the end line which content 
# we provided inside the write() function.


# Note:
# 01). Whenever we open any file in "w" or "a" mode, if that file does not
#exist then python automatically create a new file with the given name in path.

# 02). Using "\n" at the start of appended text helps place new content on 
# a fresh line