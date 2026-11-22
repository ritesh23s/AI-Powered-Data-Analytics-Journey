# *********** FILE HANDLING IN PYTHON ***********
# *********** WRITING MULTIPLE LINES ***********
# writelines(): Used to write a list (or iterable) of strings to a file.

# Note: writelines() does NOT automatically add newline characters ('\n')
# between items, so we include '\n' inside each string where needed.

# Syntax:
# with open("file_name(complete file path)", "mode") as f:
#     f.writelines(list_of_strings)

# Example 01:
file_path = "03_Basic_Python_(AI-powered)/17_file_handling_in_python/file_08.txt"
lines = ["line 1\n", "line 2\n", "line 3\n"]

# Write multiple lines to the file
with open(file_path, "w") as f:
    f.writelines(lines)

# Read back the file to verify the written content
with open(file_path, "r") as f:
    data = f.read()

print(data)

# Output:
# line 1
# line 2
# line 3