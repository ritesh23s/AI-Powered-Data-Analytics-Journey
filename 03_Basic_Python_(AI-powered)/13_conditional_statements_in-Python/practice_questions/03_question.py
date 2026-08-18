# ******************** HARD LEVEL PRACTICE ********************

# Question: 03).
# Given the age, membership type, and purchase amount of a customer,
# determine the discount they should receive.
#
# Input:
# Three inputs:
# 1. An integer age
# 2. Membership type ("gold", "silver", or "regular")
# 3. Purchase amount (integer or float)
#
# Conditions:
#
# 1. If the customer is a Gold member:
#       - If purchase amount is 5000 or above:
#           Print "20% Discount"
#       - If purchase amount is 2000 or above:
#           Print "15% Discount"
#       - Otherwise:
#           Print "10% Discount"
#
# 2. If the customer is a Silver member:
#       - If purchase amount is 5000 or above:
#           Print "15% Discount"
#       - Otherwise:
#           Print "10% Discount"
#
# 3. If the customer is a Regular member:
#       - If age is below 18:
#           Print "5% Discount"
#       - Otherwise:
#           Print "No Discount"
#
# 4. If the membership type is not "gold", "silver",
#    or "regular":
#       Print "Invalid Membership"


# Solution:

membership_type = input("Enter Membership type (gold, silver, or regular)")
membership_type = membership_type.strip().lower()


if membership_type == "gold":
    purchase_amount = float(input("Enter your purchase amount: "))
    if purchase_amount >= 5000:
        print("20% Discount")
    elif purchase_amount >= 2000:
        print("15% Discount")
    else:
        print("10% Discount")
elif membership_type == "silver":
    purchase_amount = float(input("Enter your purchase amount: "))
    if purchase_amount >= 5000:
        print("15% Discount")
    else:
        print("10% Discount")
elif membership_type == "regular":
    customer_age = int(input("Enter your age: "))
    if customer_age < 18:
        print("5% Discount")
    else:
        print("No Discount")
else:
    print("Invalid Membership")

