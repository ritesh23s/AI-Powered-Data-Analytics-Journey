# ******************** HARD LEVEL PRACTICE ********************

# Question: 04).
# Given the age, country, account status, and transaction amount
# of a user, determine whether the transaction should be allowed.
#
# Input:
# The program should take:
# 1. An integer age
# 2. A country name
# 3. Account status ("active" or "inactive")
# 4. Transaction amount (integer or float)
#
# Conditions:
#
# 1. If the account is inactive:
#       Print "Account Inactive"
#
# 2. If the account is active:
#       Check the user's country and age.
#
#       If the user is from India AND age is 18 or above:
#           - If transaction amount is 50,000 or below:
#               Print "Transaction Approved"
#           - If transaction amount is above 50,000:
#               Check whether the user is 60 or above.
#               - If age is 60 or above:
#                   Print "Transaction Approved with Verification"
#               - Otherwise:
#                   Print "Transaction Requires Verification"
#
#       If the user is from India BUT age is below 18:
#           Print "Minor Account - Transaction Not Allowed"
#
#       If the user is NOT from India:
#           - If transaction amount is 10,000 or below:
#               Print "International Transaction Approved"
#           - Otherwise:
#               Print "International Transaction Requires Verification"

# Solution:

account_status = input("Enter account status (active or inactive): ")
account_status = account_status.strip().lower() == "active"

if not account_status:
    print("Account Inactive")
else:
    user_country = input("Please enter your country: ")
    user_country = user_country.strip().lower()
    user_age = int(input("Please enter your age: "))

    if user_country == "india" and user_age >= 18:

        transaction_amount = float(input("Enter amount: "))

        if transaction_amount <= 50000:
            print("Transaction Approved")
        else:
            if user_age >= 60:
                print("Transaction Approved with Verification")
            else:
                print("Transaction Requires Verification")
    elif user_country == "india" and user_age < 18:
        print("Minor Account - Transaction Not Allowed")
    else:
        transaction_amount = float(input("Enter amount: "))
        if transaction_amount <= 10000:
            print("International Transaction Approved")
        else:
            print("International Transaction Requires Verification")