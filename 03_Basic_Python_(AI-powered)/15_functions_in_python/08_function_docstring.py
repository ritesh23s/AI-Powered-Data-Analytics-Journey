# *************** FUNCTIONS IN PYTHON ***************
# ********* FUNCTION DOCSTRINGS *********
# Docstrings are used to describe what a function does.
# They are written right after the function header inside triple quotes (""" ... """)

# Key Points:
# 1. They are not comments, but they do not affect code execution or output.
# 2. Python stores them in a special attribute called __doc__.
# 3. They help in code readability and documentation (used by help() function).

# Syntax:
# def function_name(parameter1, parameter2,.....):
    # """function docstring/message for this function"""
    # function body
# function_name(argu1, argu2,....)

# Example 01).
def display_table(n):
    """write the table of entered number""" 
    for i in range(1,11):
        print(f"{n} x {i} = {i*n}")

num = int(input("Please enter your number: "))
display_table(num)

# Example 02).
def add(a,b):
    """ Returns the sum of two numbers """
    return a + b

result = add(23, 86)
print(result)
# Output:
# 109