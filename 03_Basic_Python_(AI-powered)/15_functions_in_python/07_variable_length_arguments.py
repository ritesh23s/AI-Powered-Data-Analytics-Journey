# *************** FUNCTIONS IN PYTHON ***************
# ********* VARIABLE LENGTH ARGUMENTS *********
# sometimes we needs to pass multiple arguments than those defined in the 
# actual function. this can be done using variable length arguments.

# There are two way to achieve this 

# ********** USING SINGLE ASTERISK (*) BEFORE PARAMETER **********
# 01). * : it is used to pass multiple positional arguments.

# while creating a function, pass a * before the parameter name while
# defining the function. the function accesses the arguments by processing them
# in the form of tuple.

# Syntax:
# def function_name(*parameter):
    # function body/some works
    # return value 
# function_name(argu_1, argu_2, argu3,...)

# Example 01).
def all(*date):
    print(date)

all(3, "october", 2026)
# Output:
# (3, 'october', 2026)
#here its returns output as a tuple

# Example 02).
# calculate the average of numbers

def average(*nums):
    sum = 0
    for i in nums:
        sum += i
    print("Average of given numbers is ",sum/len(nums))

average(2,4,6,8,10,12,14,16)

# Output:
# Average of given numbers is  9.0

# Example 03).
def sum(*num):
    num_sum = 0
    for i in num:
        num_sum += i
    print("Sum of given number is ", num_sum)

sum(1,2,3,4,5,6,7,8,9,10)
# Output:
# Sum of given number is  55
    


# ********** USING DOUBLE ASTERISK (**) BEFORE PARAMETER **********
# 02).
