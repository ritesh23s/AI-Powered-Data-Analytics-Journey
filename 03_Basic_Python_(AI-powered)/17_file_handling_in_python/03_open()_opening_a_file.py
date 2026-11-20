# *********** FILE HANDLING IN PYTHON ***********
# *********** OPENING A FILE ***********
# open(): files are opened using the open() function.
 
# we have to open a file before reading or writing the file so that time
# we used open() function

# Syntax:
# variable_name = open("file_name", "mode") 

# here,
       #file_name: sample.txt, demo.docx, img.jpeg, etc. (file name with complete
                   # path
       #mode:
           # r: read mode
           # w: write mode
           # a: append mode
           # x: create file
           # rb: read binary
           # wb: write binary

# Example 01).
file = open("03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_01.txt", "r")
content = file.read()
file.close()

print(content)
# Out put:
# (Displays the contents of file_1.txt)
# Here.
    # file_1.txt is opened in read mode, read into 'content', and closed properly.


# Note:
# open() function have default mode "r"(read mode)