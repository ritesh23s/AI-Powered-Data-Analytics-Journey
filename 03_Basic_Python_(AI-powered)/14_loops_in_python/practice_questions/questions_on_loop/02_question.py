# *********************** PRACTICE QUESTION ***********************

# Question: 03).
# A bank wants to analyze customer transactions.
# The program should accept transaction amounts one by one
# until the user enters 0 to stop the input.
#
# Calculate and display:
# 1. Total number of valid transactions.
# 2. Total amount of all valid transactions.
# 3. Number of deposits.
# 4. Number of withdrawals.
# 5. Largest transaction amount.
#
# Input:
# Enter transaction amounts one by one.
# Positive values represent deposits.
# Negative values represent withdrawals.
# Enter 0 to stop entering transactions.
#
# Conditions:
# 0 is used only to stop the input.

# A transaction amount cannot be less than -50000
# or greater than 50000.

# Invalid transactions should not be included in the calculations.

# If no valid transaction is entered, display:
#   "No valid transactions available"


# Output:
# Display the required transaction statistics.

# Example:

# Input:
# 15000
# -5000
# 25000
# -2000
# 7500
# 0

# Output:
# Total transactions: 5
# Total amount: 40500
# Deposits: 3
# Withdrawals: 2
# Largest transaction: 25000

# Solution:


transactions_details = []
print("***** Enter transaction amounts one by one  *****")
print("***** Positive values represent deposits    *****")
print("***** Negative values represent withdrawals *****")
print("***** Enter 0 to stop entering transactions *****")


while True:
    transactions_amount = input("Please enter transaction amount: ").strip()

    if transactions_amount == "0" or transactions_amount == "-0":
        break
    elif(
            transactions_amount.isdigit() or 
            (
                transactions_amount.startswith("-") and 
                transactions_amount[1:].isdigit()
            )
        ):

        transactions_amount = int(transactions_amount)

        if transactions_amount <= 50000 and transactions_amount >= -50000: 
            transactions_details.append(transactions_amount)
        else:
            print("Please enter amount <= 50000 or >= -50000")
    else:
        print("Please enter valid amount")

print("***** RESULTS *****")
if len(transactions_details) > 0:
    print("Total transactions:", len(transactions_details))
    credited_amount = []
    debited_amount = []
    for amount in transactions_details:
        if amount > 0:
            credited_amount.append(amount)
        else:
            debited_amount.append(amount)
    
    current_amount = sum(transactions_details)

    print("Total amount:", current_amount)
    print("Deposits:", len(credited_amount))
    print("Withdrawals:", len(debited_amount))
    print("Largest transaction:", max(transactions_details))
else:
    print("No valid transactions available")