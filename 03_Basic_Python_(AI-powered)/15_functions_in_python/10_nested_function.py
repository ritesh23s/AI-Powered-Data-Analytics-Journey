# *************** FUNCTIONS IN PYTHON ***************
# ********* NESTED FUNCTION *********
# A function defined inside another function is called a nested function.

# Syntax:
# def outer_function(parameter1, parameter2, ...):
#     # outer function body
#     
#     def inner_function(parameter1, parameter2, ...):
#         # inner function body
#     
#     # calling inner function inside outer function
#     inner_function()

# outer_function(arg1, arg2, ...)


# Example 01).
def outer_func():
    print("This is the outer function.")
    
    def inner_func():
        print("This is the inner function.")

    inner_func()  # calling inner function

outer_func()

# Output:
# This is the outer function.
# This is the inner function.


# Note:
# we only (access) call inner function in outer function beacause inner functions are 
# local scope for outer function
# we can never call a inner function globaly



# *****************************************************
#        PRACTICE QUESTION: NESTED FUNCTIONS
# *****************************************************
# Write a function calculate_net_salary(base_salary, bonus) that 
# uses a nested function to compute the final take-home salary.

# Input:
# Take base_salary (float/int) and bonus (float/int).

# Conditions & Structure:
# 1. The outer function calculate_net_salary(base_salary, bonus) should 
#    first calculate the gross salary (gross_salary = base_salary + bonus).

# 2. Inside this outer function, define a nested inner function named 
#    calculate_tax(amount).

# 3. The inner function calculate_tax should deduct 10% tax from the 
#    given amount and return the remaining net amount (amount - 10% of amount).

# 4. The outer function must call the inner function by passing the 
#    gross salary to it, and then return the final net salary.

# Output:
# The function must return the final net salary.
# Print the returned value outside the function.

# Example:
# Input: base_salary = 50000, bonus = 10000
# Gross Salary = 60000
# Tax (10% of 60000) = 6000
# Net Salary = 54000
# Output: 54000.0


def calc_net_salary(base_salr, bonus):
    gross_salr = base_salr + bonus

    def calculate_tax(amount):
        tax_amount = (amount*10)/100
        print(f"Tax amount (10%): {tax_amount}")
        net_amount = amount - tax_amount
        return net_amount
    
    return calculate_tax(gross_salr)

basic_salary = float(input("Please enter basic salary: "))    
bonus_aount = float(input("Enter bonus amount: "))

result = calc_net_salary(basic_salary, bonus_aount)
print("Final Net Salary:", result)