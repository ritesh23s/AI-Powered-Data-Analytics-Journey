# ******************************** LOGICAL OPERATORS ********************************


print("02). Logical OR Operator")
# 02). Logical OR (or) Operator - It returns True if at least one of the conditions is True.
# It returns False only when both conditions are False.

# Logical OR Charts (Truth Table)
# ------------------------------------------
# | Condition1  | Conditions2 | Output(Ans)|
# ------------------------------------------
# | True        | True        | True       |
# ------------------------------------------
# | True        | False       | True       |
# ------------------------------------------
# | False       | True        | True       |
# ------------------------------------------
# | False       | False       | False      |
# ------------------------------------------

# Example = 
# 01).
A = 12
B = 6
print(A < B or A / B == 2)
print(A > B or A % B == 0)
print(A / B == 1 or A // B == 1)

print("Q 01).")
# Q 01).Write a Python program to check whether a student has passed in at least one subject using the Logical OR (or) operator.
# Passing marks = 33
math_marks = 25
science_marks = 40
print(math_marks >= 33 or science_marks >= 33)

print("Q 02).")
# Q 02). Write a Python program to check whether a person is eligible for a discount.
# Rules:
# Age ≥ 60 OR Student = True
age = 20
student = True
print(age >= 60 or student)

print("Q 03).")
# Q 03). Write a Python program to check whether a number is divisible by 2 or 5.
num = 25
print(num % 2 == 0 or num % 5 == 0)

print("Q 04).")
# Q 04). Write a Python program to check whether a person can enter a water park.
# Rules:
# Height ≥ 140 cm OR Age ≥ 18
height = 135
person_age = 20
print(height >= 140 or person_age >= 18)

print("Q 05).")
# Q 05). Write a Python program to check whether a customer gets free delivery.
# Rules:
# Order Amount ≥ 1000 OR Premium Member = True
order_amount = 750
premium_member = True
print(order_amount >= 1000 or premium_member)

print("Q 06).")
# Q 06). Write a Python program to check whether a player is selected for the team.
# Rules:
# Runs ≥ 100 OR Wickets ≥ 5
runs = 85
wickets = 5
print(runs >= 100 or wickets >= 5)

print("Q 07).")
# Q 07). Write a Python program to check whether a website login is successful.
# Rules:
# Password is correct OR Fingerprint is verified
password_correct = False
fingerprint_verified = True
print(password_correct or fingerprint_verified)

print("Q 08).")
# Q 08). Write a Python program to check whether a mobile phone can be unlocked.
# Rules:
# Face ID = True OR PIN is correct
face_id = False
pin_correct = True
print (face_id or pin_correct)

print("Q 09).")
# Q 09). Write a Python program to check whether a person is eligible for a scholarship.
# Rules:
# Marks ≥ 90 OR Sports Quota = True
marks = 82
sports_quota = True
print(marks >= 90 or sports_quota)

print("Q 10).")
# Q 10). Write a Python program to check whether a sales report should be reviewed.
# Rules:
# Total Sales > 100000 OR Total Orders > 500
total_sales = 85000
total_orders = 620
print(total_sales > 100000 or total_orders > 500)