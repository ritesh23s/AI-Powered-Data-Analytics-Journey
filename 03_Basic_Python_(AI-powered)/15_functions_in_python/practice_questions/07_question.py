# Question 07):

# Write a function calculate_grade(marks) that returns the grade based on the student's marks.

# Input:
# Take the student's marks as an integer.

# Conditions:
# 01). 90–100 → "A"
# 02). 75–89 → "B"
# 03). 60–74 → "C"
# 04). 40–59 → "D"
# 05). Below 40 → "Fail"

# Output:
# Print the grade returned by the function.

# Examples:

# Input:
# Enter your marks: 82

# Output:
# B


# Input:
# Enter your marks: 35

# Output:
# Fail


# Input:
# Enter your marks: 95

# Output:
# A


def marks_validation(marks):
    if marks >= 0 and marks <= 100:
        return True
    else:
        return False

def grade_calculation(marks):
    if marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 75 and marks <= 89:
        return "B"
    elif marks >= 60 and marks <= 74:
        return "C"
    elif marks >= 40 and marks <= 59:
        return "D"
    else:
        return "Fail"


student_marks = input("Enter your marks: ")
student_marks = int(student_marks)
if marks_validation(student_marks):
    student_grade = grade_calculation(student_marks)
    print(student_grade)
else:
    print("Please enter valid number!")

    

