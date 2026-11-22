# *********** FILE HANDLING IN PYTHON ***********
# *********** READING AND WRITING BINARY FILES ***********

# We can also read and write the binary files using "rb" and "wb" mode.

# Syntax:
# with open("file_name(complete file path)", "mode("rb"/"wb")") as file:
#     f.read()
#     f.write()

# Example:
# ************ Reading a binary file ************
file_path = "03_Basic_Python_(AI-powered)/17_file_handling_in_python/img.jpeg"

with open(file_path, "rb") as f:
    file_data = f.read()
print(file_data)


# ************ Writing a binary file ************

file_path_02 = "03_Basic_Python_(AI-powered)/17_file_handling_in_python/arrow_line.png"

with open(file_path_02, "wb") as f:
    f.write(file_data)