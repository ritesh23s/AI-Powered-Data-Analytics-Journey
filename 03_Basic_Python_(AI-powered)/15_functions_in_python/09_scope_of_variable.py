# *************** FUNCTIONS IN PYTHON ***************
# ********* SCOPE OF VARIABLE *********
# 1. LOCAL VARIABLE:
# Variables defined inside a function are local to that function.
# They cannot be accessed outside of that function.

# Example 01).
def test():
    x = 10  # Local variable
    print("Inside function:", x)

test()
# Output:
# Inside function: 10

# print(x) 
# This will give a NameError because 'x' is local to test() function 
# and does not exist outside.


# 2. GLOBAL VARIABLE:
# Variables defined outside any function (at the main level of the script) 
# are global variables. They can be accessed both inside and outside functions.

# Example 02).
name = "Shubham"  # Global variable

def show_name():
    print("Accessing global variable inside function:", name)

show_name()
print("Accessing global variable outside function:", name)

# Output:
# Accessing global variable inside function: Shubham
# Accessing global variable outside function: Shubham