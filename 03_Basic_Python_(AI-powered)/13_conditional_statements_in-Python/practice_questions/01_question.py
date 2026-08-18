# ******************** HARD LEVEL PRACTICE ********************

# Question: 01).
# Given the age, country, and student status of a person,
# determine the type of access they should receive.
#
# Input:
# Three inputs:
# 1. An integer age
# 2. A country name
# 3. Student status ("yes" or "no")
#
# Conditions:
#
# 1. If the person is from India and age is 18 or above:
#       - If the person is a student, print "Student Access"
#       - Otherwise, print "Adult Access"
#
# 2. If the person is from India and age is below 18:
#       - Print "Minor Access"
#
# 3. If the person is not from India:
#       - Print "International Access"


# Solution:

student_age = int(input("Enter age: "))

student_country = input("Enter your country: ")
student_country = student_country.strip().lower() == "india"

student_status = input("You are a student ? (yes/no): ")
student_status = student_status.strip().lower() == "yes"

if student_country and student_age >= 18:
    if student_status:
        print("Student Access")
    else:
        print("Adult Access")
elif student_country and student_age < 18:
    print("Minor Access")
elif not student_country:
    print("International Access")