# *************** FUNCTIONS IN PYTHON ***************
# ********* RETURN STATEMENT *********
# Return statement: the return statements sends a value back from the function
# The returned value can be stored in a variable and used outside the function.

# Syntax:
# def function_name(parameters):
    # return value
# function_name(arguments)


# Example 01).
def calc_sum(a , b):
    return a + b
result = calc_sum(10, 45)
print(result)
# Output:
# 55


# Explanation:
# Here, return sends the result of a + b back from the function.
# So, result stores the returned value 55.

# Example 02).
# write a program to calculate the average of 3 numbers
def calc_average(a, b, c):
    return (a+b+c)/3
avg = calc_average(12, 5, 75)
print(avg)

# Output:
# 30.666666666666668