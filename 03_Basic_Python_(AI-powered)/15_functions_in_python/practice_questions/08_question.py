# Question 08):

# Write a function calculate_bill(amount) that calculates the final bill amount
# based on the purchase amount.

# Input:
# Take the purchase amount as an integer.

# Conditions:
# 01). If amount is less than 1000: No discount.

# 02). If amount is between 1000 and 4999: Give a 5% discount.

# 03). If amount is between 5000 and 9999: Give a 10% discount.

# 04). If amount is 10000 or more: Give a 15% discount.

# 05). If amount is less than or equal to 0: Return "Invalid amount".



# Output:
# Return the final bill amount from the function and print it outside the function.


def calculate_bill(amount):
    if amount <= 0:
        return "Invalid amount"
    elif amount < 1000:
        return amount
    elif amount >= 1000 and amount <= 4999:
        return amount*0.95
    elif amount >= 5000 and amount <= 9999:
        return amount*0.90
    else:
        return amount*0.85


purchase_amount = input("Please enter your purchase amount for check discount: ")
purchase_amount = int(purchase_amount)

result = calculate_bill(purchase_amount)
print(result)