# *********************** LOOPS IN PYTHON ***********************
# ************* WHILE LOOPS IN PYTHON *************

# while loop: The while loop runs as a condition remains true.


# Syntax:

# variable_name = initial_value
# while condition:
#     do something
#     update variable


# Example:
# 01).
i = 1
while i <= 5:
    print(i)
    i += 1

# Output:
# 1
# 2
# 3
# 4
# 5


# *********************** PRACTICE QUESTION ***********************

# Question: 01).
# A data analyst is processing daily sales records.
# The sales amount for each day is entered one by one.
# The program should keep accepting sales amounts until the
# analyst enters -1.

# Calculate and display:
# 1. The total number of valid sales entries.
# 2. The total sales amount.
# 3. The average sales amount.
#
# Input:
# Enter sales amounts one by one.
# Enter -1 to stop entering data.
#
# Conditions:
# -1 is only used to stop the input and should not be included in the calculations.
# Sales amount cannot be negative except -1.
# If no valid sales amount is entered, display:
#  "No sales data available"

# Output:
# Display the number of sales entries, total sales amount,
# and average sales amount.
#
# Example:
#
# Input:
# 1200
# 850
# 1500
# 950
# -1
#
# Output:
# Number of sales entries: 4
# Total sales: 4500
# Average sales: 1125.0
#
# Solution:

sales = []
while True:
    amount = input("Enter sales amounts one by one. \nEnter -1 to stop entering data: ").strip()

    if amount == "-1":
        break
    elif amount.isdigit():
        sales.append(int(amount)) 
    else:
        print("Sales amount cannot be negative except -1")


if len(sales) > 0:
    print("Number of sales entries:", len(sales))
    print("Total sales:", sum(sales))
    print("Average sales:", sum(sales)/len(sales))
else:
    print("No sales data available")