# *********** FILE HANDLING IN PYTHON ***********
# *********** CHECKING FILE EXISTENCE ***********

# we can also check the file or folder existence using os module(inbuilt module)
# in python.

# os.path.exists() returns True if the path exists, and False if does not exist.

# Syntax:
# import os
# if os.path.exists("fine_name(complete file path)"):
    # Runs when the path exists (returns True)


# Example:
file_path = "03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_08.txt"

import os
if os.path.exists(file_path):
    print("File already esist.")
else:
    print("does not exist.")

# There are another way to checking existence:

result = os.path.exists(file_path)
print(result)
# Output:
# True
# here, 
    # it returns True if file does exists.
    # it returns False if file does not exist.