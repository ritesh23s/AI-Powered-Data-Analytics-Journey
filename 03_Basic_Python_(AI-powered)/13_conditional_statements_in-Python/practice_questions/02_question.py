# ******************** HARD LEVEL PRACTICE ********************

# Question: 02).
# Given the marks of a student and their attendance percentage,
# determine whether the student passes, fails, or needs an
# attendance shortage warning.
#
# Input:
# Two integers:
# 1. Marks obtained
# 2. Attendance percentage
#
# Conditions:
#
# 1. If marks are 40 or above AND attendance is 75 or above:
#       - If marks are 90 or above, print "Excellent"
#       - If marks are 60 or above, print "Good"
#       - Otherwise, print "Pass"
#
# 2. If marks are 40 or above BUT attendance is below 75:
#       - Print "Attendance Shortage"
#
# 3. If marks are below 40:
#       - Print "Fail"

# Solution:

student_marks = int(input("Enter your marks: "))
attendance_percentage = int(input("Enter your attendance percentage: "))

if student_marks >= 40:
    if attendance_percentage >= 75:
        if student_marks >= 90:
            print("Excellent")
        elif student_marks >= 60:
            print("Good")
        else:
            print("Pass")
    else: 
        print("Attendance Shortage")
else:
    print("Fail")
