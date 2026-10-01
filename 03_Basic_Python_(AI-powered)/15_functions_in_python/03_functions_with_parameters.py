# *************** FUNCTIONS IN PYTHON ***************
# ********* FUNCTIONS WITH PARAMETER *********
# parameters allow you to pass data into a functions

# Syntax:
# def function_name(parameter_1, parameter_2,...):
    # do some work/executes the block of code
    # return_result

# function_name(argu_1, argu_3,...)



# Example: 01).
def name(first_name, last_name):
    print(f"{first_name} {last_name}")
name("Shubham", "Yadav")

# Output:
# Shubham Yadav

# here first_name and last_name are parameters and 
# "Shubham", and "Yadav" is a two arguments for first_name and last_name


# Here we can also call this function for another/multiple person name
name("Anup", "Das")
# Output:
# Anup Das



# Example: 02).
def add(a, b):
    result = a + b
    print(f"Sum of {a} and {b} =", result)

add(10, 12)
# Output:
# Sum of 10 and 12 = 22

# we can also call this function for get sum of another/multiple number

add(1454, 4577)
# Output:
# Sum of 1454 and 4577 = 6031


# We can also use pass keywords in function body for smoothly run the function
# and execute the next line of code without raising any error
# Example 01).
def sum(a, b):
    pass
sum(4, 5)
