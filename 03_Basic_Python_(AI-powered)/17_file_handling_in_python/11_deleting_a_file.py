# *********** FILE HANDLING IN PYTHON ***********
# *********** DELETING A FILE ***********
# 01). Using the os module


# ********** USING THE OS MODULE **********
# A module (like a code library) is a file written by another programmer that
# generally has functions we can use.

# Syntax:
# import os
# os.remove("file_name(complete file path)")

# Example:
file_path = "03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_07(for delete).txt"

# Here we create a new file (file_07(for delete).txt)
with open(file_path, "w") as f:
    f.write("This is a file to see how a file is deleted using the os module.")


# Now we read the file (file_07(for delete).txt)
with open(file_path, "r") as f:
    file_data = f.read()
print(file_data)


# Here we delete the file (file_07(for delete).txt)
import os
os.remove(file_path)

print("File deleted successfully..!!")

# Output:
# This is a file to see how a file is deleted using the os module.
# File deleted successfully..!!