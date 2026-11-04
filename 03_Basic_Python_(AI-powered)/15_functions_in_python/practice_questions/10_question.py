# Question 10):

# Write a Python program that uses functions to create a Student Result & Performance Analyzer.

# Input:
# First, take the student's name as input.

# Then take marks of 5 subjects as integers.

# Subjects:
# 1. Python
# 2. SQL
# 3. Excel
# 4. Statistics
# 5. Power BI


# Conditions:

# 1. Student name should not be empty.
#    If the entered name is empty, return "Invalid student name".

# 2. Each subject's marks must be between 0 and 100.
#    If any mark is below 0 or above 100, return "Invalid marks".


# 3. Calculate the total marks.


# 4. Calculate the percentage.


# 5. Determine the result:
#    - If marks in ANY subject are below 40 → "Fail"
#    - Otherwise → "Pass"

# 6. If the student passes, calculate the grade based on percentage:

#    90–100 → "A"
#    75–89 → "B"
#    60–74 → "C"
#    40–59 → "D"

# 7. Calculate the number of subjects in which the student scored
#    75 or above.

# 8. Store all subject names and marks in a dictionary.

# 9. Use a loop to:
#    - Display every subject and its marks.
#    - Count how many subjects have marks >= 75.

# 10. Create a function:

#     calculate_result(name, marks)

#     The function should return the final result information.

# 11. Use at least one default parameter in a function.

# 12. Use at least one keyword argument while calling a function.

# 13. The final result should be returned from the function,
#     not directly printed inside the calculation function.

# Output:

# Display:

# Student Name
# Total Marks
# Percentage
# Result
# Grade
# Subjects with 75+ marks
# Subject-wise marks


# Example:

# Input:

# Student Name: Shubham
# Python: 85
# SQL: 72
# Excel: 91
# Statistics: 68
# Power BI: 80


# Output:

# Student Name: Shubham
# Total Marks: 396
# Percentage: 79.2
# Result: Pass
# Grade: B
# Subjects with 75+ marks: 3

# Subject-wise Marks:
# Python: 85
# SQL: 72
# Excel: 91
# Statistics: 68
# Power BI: 80


# Important Requirements:

# - Function compulsory.
# - Parameters compulsory.
# - return compulsory.
# - Dictionary compulsory.
# - Loop compulsory.
# - At least one default parameter compulsory.
# - At least one keyword argument compulsory.
# - Do not use concepts that have not been learned yet.