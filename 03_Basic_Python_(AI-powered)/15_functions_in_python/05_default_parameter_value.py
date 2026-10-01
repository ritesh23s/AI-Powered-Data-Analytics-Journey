# *************** FUNCTIONS IN PYTHON ***************
# ********* DEFAULT PARAMETER VALUES *********
# we can provide a default value while creating a function. 

# If no value is provided for that parameter, the function 
# uses the default value.

# In another words:
# Assigning a default value to parameter, which is used when
# no argument is passed

# Syntax:
# def function_name(parameter = default_value):
    # do some work/executes the block of code
    # return_result

# function_name(argument)

# Example 01).
def name(first_name = "user", last_name = "name"):
    return f"Hello..! {first_name} {last_name}"
full_name = name()
print(full_name)

# Output:
# Hello..! user name

# Here, "user" and "name" are the default values of the parameters.
# We did not provide any arguments while calling name().
# So,
    # the function automatically uses the default values. which is


# We can also provide our own values.
full_name = name("Aman", "Yadav")
print(full_name)


# Output:
# Hello..! Aman Yadav


# Here, we provided "Aman" and "Yadav" as arguments.
# So, 
    # the function uses these values instead of the default values.


# Example 02).
def average(a = 1, b = 1):
    return (a+b)/2
avg = average()
print(avg)

# Output:
# 1.0   
    #beacouse here se provide default value a = 1, b = 1


# If we call this average function with argument
another_avg = average(12, 45)
print(another_avg)

# Output:
# 28.5

# note:
# 01). whenever we provide a default value for function parameter we should
# provide default value from last parameter.

# Right way to provide a default value for function parameter
def sum(a , b = 2):
    return a+b
add = sum(5)
print(add)
# Output:
# 7

# Wrong way to provide a default value for function parameter

# def sum(a = 5, b):
#     return a+b
# add = sum(5)
# print(add)

# Output:
# SyntaxError: parameter without a default follows parameter with a default