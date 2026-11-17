# *************** FUNCTIONS IN PYTHON ***************
# ********* VARIABLE LENGTH ARGUMENTS *********
# Sometimes, we need to pass more arguments than the number of parameters
# defined in a function. This can be done using variable length arguments.

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
# Here, the arguments are collected and displayed in the form of a tuple.

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
# calculate the sum of numbers.
def sum(*num):
    num_sum = 0
    for i in num:
        num_sum += i
    print("Sum of given number is ", num_sum)

sum(1,2,3,4,5,6,7,8,9,10)
# Output:
# Sum of given number is  55
    
# Example 04).
# calculate the factorial of entered numbers one by one.

def fact(*num):
    for n in num:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(f"{n}! = {fact}")

fact(5,6,7)
# Output
# 5! = 120
# 6! = 720
# 7! = 5040


# ********** USING DOUBLE ASTERISK (**) BEFORE PARAMETER **********
# 02). It is used to pass multiple keyword arguments.

# while creating a function, pass double ** before the parameter name while
# defining the function. the function accesses the arguments by processing them
# in the form of dictionary.

# Syntax:
# def function_name(**parameter):
#     function body/some works
#     return value 
# function_name(argu1 = "value", argu2 = "value",...)

# Example 01).
def date(**value):
    print(value)
date(date = 13, month = "November", year = 2026)
# Output:
# {'date': 13, 'month': 'November', 'year': 2026}



# ************* Practice Questions *************
# # Question 01).

# Write a function calculate_statistics(*numbers) that performs
# the following operations on multiple numbers.

# Input:
# Pass multiple integer arguments to the function.

# Conditions:

# 1. Calculate the sum of all numbers.
# 2. Calculate the average of all numbers.
# 3. Count how many numbers are even.
# 4. Count how many numbers are odd.
# 5. Find the largest number without using the max() function.

# Output:

# Return all five results from the function.

# Print the returned results outside the function.

# Example:
# Input:
# calculate_statistics(12, 25, 30, 17, 40, 9, 22)

# Output:
# Sum: 155
# Average: 22.14
# Even Numbers: 4
# Odd Numbers: 3
# Largest Number: 40

def calculate_statistics(*numbers):
    total = 0
    odd = []
    even = []
    largest_num = numbers[0]    

    for num in numbers:
        total += num
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)

        if num > largest_num:
            largest_num = num

    return (
        f"Sum: {total} \n"
        f"Average: {total/len(numbers)} \n"
        f"Even numbers: {len(even)} \n"
        f"Odd numbers: {len(odd)} \n"
        f"Largest number: {largest_num}"
    )

result = calculate_statistics(12, 25, 30, 17, 40, 9, 22)
print(result)
