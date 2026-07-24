# ******************************** LOGICAL OPERATORS ********************************


print("03). Logical NOT Operator")
# 03). Logical NOT (not) Operator - It reversr the result. Returns false if the result is True, and Returns true if result is False.

# Its returns always reverse value of any expression and its work on single expression.

# Logical NOT Charts (Truth Table)
# -------------------------
# | Input    | Output      |
# -------------------------
# | True     | False       |
# -------------------------
# | False    | True        |
# -------------------------

# Example: 
# 01).
is_logged_in = False
print(not is_logged_in)

print("Q 01).")
# Q 01). Write a Python program to print the opposite of the following Boolean value.
is_student = True
print(not is_student)

print("Q 02).")
# Q 02). Write a Python program to check whether a user is not logged in.
logged_in = False
print(not logged_in)

print("Q 03).")
# Q 03). Write a Python program to check whether the light is not ON.
light_on = True
print(not light_on)

print("Q 04).")
# Q 04). Write a Python program to check whether a person is not eligible.
eligible = False
print(not eligible)

print("Q 05).")
# Q 05). Write a Python program to check whether a machine is not running.
machine_running = True
print(not machine_running)

print("Q 06).")
# Q 06). Write a Python program to check whether a report is not approved.
report_approved = False
print(not(report_approved))

print("Q 07).")
# Q 07). Write a Python program to print the opposite of the following comparison result.
# Check:
# marks >= 33
marks = 45
print(not (marks >= 33))

print("Q 08).")
# Q 08). Print the opposite of:
# age > 18
age = 25
print(not (age > 18))

print("Q 09).") 
# Q 09). Print the opposite of: salary < 50000
salary = 40000
print(not (salary < 5000))



print("Q 10).")
# Q 10). Print the opposite of: number % 2 == 0
number = 20
print(not(number % 2 == 0))