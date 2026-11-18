# ********** LOCAL AND GLOBAL VARIABLE IN PYTHON **********
# ********** LOCAL VARIABLE **********

# Local variables are created inside a function.
# they can be used only within that function.

# Example:
# 01).
def show_value():
    x = 10
    print(x)

show_value()
# Output
# 10       #here x is local variable which writted within this show_value function


# If we try to access x outside the function, it will cause an error.
# print(x)
# Output:
# NameError: name 'x' is not defined


# 02).
def std_details(name, enroll):
    math_marks = 78     
    print(f"Name: {name}")
    print(f"Enrollment: {enroll}")
    print(f"Maths sunject marks: {math_marks}")

std_details("Shubham", "ABC23102R02025")
# Output:
# Name: Shubham
# Enrollment: ABC23102R02025
# Maths sunject marks: 78


# if we change the math_marks value here, and agail call the std_details function
math_marks = 45
std_details("Aman", "ABC23102R02045")
# Output:
# Name: Aman
# Enrollment: ABC23102R02045
# Maths sunject marks: 78
                            #here we see that the math_marks value not change
                            #because of the math_marks = 78 assigned as a local  
                            #variable for the std_details function.

