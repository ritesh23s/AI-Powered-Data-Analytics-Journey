# ******************** HARD LEVEL PRACTICE ********************

# Question: 07).
# A company wants to determine whether a customer is eligible
# for a loan and what type of loan they can receive.
#
# Input:
# The program should take:
# 1. Customer's age
# 2. Monthly income
# 3. Credit score
# 4. Employment status ("employed" or "unemployed")
# 5. Existing loan status ("yes" or "no")
#
# Conditions:
#
# 1. If the customer is unemployed:
#       Print "Loan Not Available"
#
# 2. If the customer is employed:
#
#       If age is below 21:
#           Print "Loan Not Available - Age Requirement"
#
#       Otherwise:
#           Check the credit score.
#
#           If credit score is below 600:
#               Print "Loan Not Available - Low Credit Score"
#
#           If credit score is 600 or above:
#               Check monthly income.
#
#               If monthly income is below 30,000:
#                   Print "Loan Not Available - Low Income"
#
#               If monthly income is 30,000 or above:
#                   Check existing loan status.
#
#                   If there is NO existing loan:
#
#                       If credit score is 750 or above
#                       AND monthly income is 60,000 or above:
#                           Print "Premium Loan Approved"
#
#                       Otherwise:
#                           Print "Standard Loan Approved"
#
#                   If there IS an existing loan:
#
#                       If credit score is 750 or above
#                       OR monthly income is 80,000 or above:
#                           Print "Loan Approved with Verification"
#
#                       Otherwise:
#                           Print "Loan Rejected - Existing Loan"
#
#
# Solution

employee_status = input("Employment status employed or unemployed: ")
employee_status = employee_status.strip().lower() == "employed"

if not employee_status:
    print("Loan Not Available")
else:
    age = int(input("Enter your age: "))
    if age < 21:
        print("Loan Not Available - Age Requirement")
    else:
        credit_score = float(input("Please enter your credit score: "))
        if credit_score < 600:
            print("Loan Not Available - Low Credit Score")
        else:
            monthly_income = float(input("Enter your monthly income: "))
            if monthly_income < 30000:
                print("Loan Not Available - Low Income") 
            else:
                loan_status = input("Enter your existing loan status (yes/no): ")
                loan_status = loan_status.strip().lower() == "yes"
                if not loan_status:
                    if credit_score >= 750 and monthly_income >= 60000: 
                        print("Premium Loan Approved")
                    else:
                        print("Standard Loan Approved")
                else:
                    if credit_score >= 750 or monthly_income >= 80000:
                        print("Loan Approved with Verification")
                    else:
                        print("Loan Rejected - Existing Loan")

