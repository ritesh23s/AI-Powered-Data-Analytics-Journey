# *********************** PRACTICE QUESTION ***********************

# Question: 01).
# Write a Python program to process the marks of students one by one.
# The program should continue accepting marks until the user enters -1.

# Calculate and display:
# 1. Total number of students.
# 2. Number of students who passed.
# 3. Number of students who failed.
# 4. Highest marks.
# 5. Lowest marks.

# Input:
# Enter marks of students one by one.
# Enter -1 to stop entering marks.

# Conditions:
# Marks must be between 0 and 100.
# -1 is used only to stop the input.
# Invalid marks should not be included in the calculations.
# If no valid marks are entered, display:
# "No valid marks available"

# Output:
# Display the required statistics.

# Example:
# Input:
# 78
# 45
# 32
# 91
# 56
# -1

# Output:
# Total students: 5
# Passed students: 4
# Failed students: 1
# Highest marks: 91
# Lowest marks: 32

# Solution:

std_marks_details = []
while True:
    marks = input("Enter marks of students one by one. \nEnter -1 to stop entering marks: ").strip()
    if marks == "-1":
        break
    elif marks.isdigit():
        marks = int(marks)
        if marks <= 100:
            std_marks_details.append(marks)
        else:
            print("Please enter marks <= 100")
    elif marks.startswith("-") and marks[1: len(marks)].isdigit():
        print("Please enter marks >= 0")
    else:
        print("Please enter valid marks!")


print("******* RESULTS *******")
if len(std_marks_details) > 0:
    print("Total students:", len(std_marks_details))
    passed_std = []
    failed_std = []
    
    for std_marks in std_marks_details:
        if std_marks >= 33:
            passed_std.append(std_marks)
        else:
            failed_std.append(std_marks)
    
    print("Passed students:", len(passed_std))
    print("Failed students:", len(failed_std))
    print("Highest marks:", max(std_marks_details))
    print("Lowest marks:", min(std_marks_details))
else:
    print("No valid marks available")