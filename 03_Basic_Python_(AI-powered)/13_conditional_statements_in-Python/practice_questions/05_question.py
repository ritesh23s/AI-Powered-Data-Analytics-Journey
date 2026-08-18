# ******************** FINAL HARD LEVEL PRACTICE ********************

# Question: 05).
# A company wants to determine whether an employee is eligible
# for a promotion and what type of promotion they should receive.
#
# Input:
# The program should take:
# 1. Years of experience
# 2. Performance rating
# 3. Employee status ("active" or "inactive")
# 4. Department ("IT", "HR", or "Finance")
#
# Conditions:
#
# 1. If the employee is inactive:
#       Print "Not Eligible - Inactive Employee"
#
# 2. If the employee is active but has less than 2 years
#    of experience:
#       Print "Not Eligible - Insufficient Experience"
#
# 3. If the employee has 10 or more years of experience
#    AND a performance rating of 8 or above:
#       Print "Senior Promotion"
#
#    This condition has priority over the other promotion
#    conditions.
#
# 4. If the performance rating is 9 or above:
#       Check the department:
#
#       - If department is IT:
#           Print "Senior Promotion"
#
#       - If department is HR or Finance:
#           Print "Managerial Promotion"
#
#       - Otherwise:
#           Print "Invalid Department"
#
# 5. If the performance rating is 7 or above
#    BUT below 9:
#       Print "Promotion Under Review"
#
# 6. If the performance rating is below 7:
#       Print "No Promotion"

# Solution:

employee_status = input("Employee status (active or inactive): ")
employee_status = employee_status.strip().lower() == "active"

if not employee_status:
    print("Not Eligible - Inactive Employee")
else:
    experience = int(input("Enter your experience: "))
    if experience < 2:
        print("Not Eligible - Insufficient Experience")
    else:
        rating = float(input("Enter performance rating out of 10: "))
        if experience >= 10 and rating >= 8:
            print("Senior Promotion")
        elif rating >= 9:
            department = input("Enter your department (IT, HR, or Finance): ")
            department = department.strip().lower()
            if department == "it":
                print("Senior Promotion")
            elif department == "hr" or department == "finance":
                print("Managerial Promotion")
            else:
                print("Invalid Department")
        elif rating >= 7 and rating < 9:
            print("Promotion Under Review")
        else:
            print("No Promotion")
    