# ******************** FINAL CHALLENGE ********************

# Question: 0 A8).
# A bank wants to determine whether a customer can make
# a high-value transaction and what level of verification
# is required.
#
# Input:
# The program should take:
# 1. Customer age
# 2. Account type ("premium" or "regular")
# 3. Account status ("active" or "blocked")
# 4. KYC status ("verified" or "unverified")
# 5. Transaction amount (integer or float)
#
#
# Conditions:
#
# 1. If the account is blocked:
#       Print "Transaction Denied - Account Blocked"
#
#
# 2. If the account is active but KYC is unverified:
#       Print "Transaction Denied - KYC Verification Required"
#
#
# 3. If the account is active AND KYC is verified:
#
#       If the customer is below 18:
#           Print "Transaction Denied - Age Restriction"
#
#       Otherwise:
#           Check the transaction amount.
#
#           If transaction amount is 25,000 or below:
#               Print "Transaction Approved"
#
#           If transaction amount is above 25,000:
#               Check the account type.
#
#               If the account is Premium:
#
#                   If transaction amount is 100,000 or below:
#                       Print "Transaction Approved"
#
#                   Otherwise:
#                       Check the customer's age.
#
#                       If age is 60 or above:
#                           Print "Transaction Approved with Verification"
#
#                       Otherwise:
#                           Print "Transaction Requires Manual Verification"
#
#               If the account is Regular:
#
#                   If transaction amount is 50,000 or below:
#                       Print "Transaction Approved with Verification"
#
#                   Otherwise:
#                       Print "Transaction Requires Manual Verification"
# Solution

account_status = input("Enter account status (active or blocked): ")
account_status = account_status.strip().lower() == "active"

if not account_status:
    print("Transaction Denied - Account Blocked")
else:
    kyc_status = input("Enter your kyc ststus (verified/unverified): ")
    kyc_status = kyc_status.strip().lower() == "verified"
    if not kyc_status:
        print("Transaction Denied - KYC Verification Required")
    else:
        customer_age = int(input("Enter your age: "))
        if customer_age < 18:
            print("Transaction Denied - Age Restriction")
        else:
            transaction_amount = float(input("Please enter your transaction amount: "))
            if transaction_amount <= 25000:
                print("Transaction Approved")
            else:
                account_type = input("Enter your account type (premium or regular): ")
                account_type = account_type.strip().lower() == "premium"

                if account_type:
                    if transaction_amount <= 100000:
                        print("Transaction Approved")
                    else:
                        if customer_age >= 60:
                            print("Transaction Approved with Verification")
                        else:
                            print("Transaction Requires Manual Verification")
                else:
                    if transaction_amount <= 50000:
                        print("Transaction Approved with Verification")
                    else:
                        print("Transaction Requires Manual Verification")


