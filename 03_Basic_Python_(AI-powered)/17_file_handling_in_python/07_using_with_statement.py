# *********** FILE HANDLING IN PYTHON ***********
# *********** USING WITH STATEMENT ***********
# With syntax:
# The 'with' statement automatically closes the file once the block ends,
# even if an error occurs inside the block.

# Syntax:
# with open("file_name(complete file path)", "mode(r,w,a,rb,wb)") as file:
#     content = file.read()

# Example 01:
with open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_05.txt", "r") as file:
    data = file.read()

print(data)
# Output: November 2026 is going on and winter is on peak.!
# Here, it displays the entire content of file_05.txt as a string.

# Example 02:
with open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_06.txt", "w") as file_A:
    file_A.write("Hello Mr, \nGood  morning. \nHow are you..?")

# Output:
# It creates a new file file_06.txt(if this file does not exist) or 
# It overwrites the entire content if the file already exists.


# Example 03:
with open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_06.txt", "a") as file_B:
    file_B.write("\nNice to meet you.!")
# Output:
# It appends the content provided inside the write() method at the end of 
# file_06.txt.


# Note:
# 01). Using the 'with' statement is a best practice because it automatically closes
# the file when the block finishes, even if an error happens inside the block.