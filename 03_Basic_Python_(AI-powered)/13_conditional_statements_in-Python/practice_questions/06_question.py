# ******************** HARD LEVEL PRACTICE ********************

# Question: 06).
# A website wants to determine whether a user is eligible
# for a special offer.
#
# Input:
# The program should take:
# 1. User's age
# 2. Country
# 3. Membership type ("premium" or "regular")
# 4. Account status ("active" or "inactive")
#
# Conditions:
#
# 1. If the account is inactive:
#       Print "Offer Not Available"
#
# 2. If the account is active:
#
#       The user is eligible for the special offer if:
#
#       - The user is from India AND age is 18 or above
#       OR
#       - The user has a Premium membership AND age is 21 or above
#
#       However:
#       - A user below 18 can NEVER receive the offer.
#
#       If the user is eligible:
#           Print "Special Offer Available"
#
#       Otherwise:
#           Print "Not Eligible"


# Solution
account_status = input("Enter account status (active or inactive): ")
account_status = account_status.strip().lower() == "active"

if not account_status:
    print("Offer Not Available")
else:
    country = input("Enter your country: ")
    country = country.strip().lower() == "india"

    user_age = int(input("Please enter your age: "))

    membership = input("Enter membership type premium or regular: ")
    membership = membership.strip().lower()

    if (country and user_age >= 18) or (membership == "premium" and user_age >= 21):
        print("Special Offer Available")
    else:
        print("Not Eligible")

