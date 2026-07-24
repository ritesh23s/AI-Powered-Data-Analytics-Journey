# ******************************** LOGICAL OPERATORS ********************************


print("01). Logical AND Operator")
# 01). Logical AND (and) Operator - It returns "True" only if both conditions are True.
# If either condition is False, it returns False.
# We used AND operators to combine two expression

# Logical AND Charts (Truth Table)
# ------------------------------------------
# | Condition1  | Conditions2 | Output(Ans)|
# ------------------------------------------
# | True        | True        | True       |
# ------------------------------------------
# | True        | False       | False      |
# ------------------------------------------
# | False       | True        | False      |
# ------------------------------------------
# | False       | False       | False      |
# ------------------------------------------

# Example = 
# 01).
A = 12
B = 6
print(A > B and A / B == 2)

print("Q 01).")
# Q 01).Write a Python program to check whether both numbers are positive using the Logical AND (and) operator.
a = 15
b = 20
print(a > 0 and b > 0)

print("Q 02).")
# Q 02). Write a Python program to check whether a student has passed in both subjects. 
# Rule - Passing marks = 33

math = 45
science = 38
print(math >= 33 and science >= 33)

print("Q 03).")
# Q 03). Write a Python program to check whether a person's age is strictly between 18 and 60.
age = 25
print(age > 18 and age < 60)

print("Q 04).")
# Q 04). Write a Python program to check whether a number is greater than 100 and less than 500.
num = 250
print(num > 100 and num < 500)

print("Q 05).")
# Q 05). Write a Python program to check whether a number is divisible by 2 and 5.
num1 = 40
print(num1%2 == 0 and num1%5 == 0)

print("Q 06).")
# Q 06). Write a Python program to check whether an employee is eligible for a bonus.
# Rules
# 1. Experience ≥ 5 years
# 2. Salary < 50000
experience = 6
salary = 45000
print(experience >= 5 and salary < 50000)

print("Q 07).")
# Q 07). Write a Python program to check whether a product is eligible for free delivery.
# Rules
# 1. Price ≥ 1000
# 2. Stock > 0
price = 1500
stock = 25
print(price >= 1000 and stock > 0)

print("Q 08).")
# Q 08). Write a Python program to check whether a voter is eligible to vote.
# Rules
# 1. Age1 ≥ 18
# 2. Citizenship = True
age1 = 20
citizenship = True
print( age1 >= 18 and citizenship == True)


print("Q 09).")
# Q 09). Write a Python program to check whether a person can apply for a driving license.
# Rules
# 1. Age2 ≥ 18
# 2. Medical Test = True 
age2 = 22
medical_test = True
print(age2 >= 18 and medical_test == True)

print("Q 10).")
# Q 10). Write a Python program to check whether a sales report is valid.
# Rules
# Total Sales > 50000
# Total Orders > 100
total_sales = 65000
total_orders = 120
print(total_sales > 50000 and total_orders > 100)