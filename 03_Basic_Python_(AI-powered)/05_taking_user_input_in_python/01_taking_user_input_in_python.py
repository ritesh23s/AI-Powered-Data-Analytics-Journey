# *************** Taking User Input in Python ***************
#****************************************************************************************

# The input() Function - The input() function pouses the program and waits for the user to type something. 
# Example - 
name = input()
print(name) 

# Whatever the user types is stored in the variable "name"

# 01). Taking input with a prompt message - We can guide the user by showing a message inside  input() 
yourName = input("Enter your name: ")
print(yourName)


# **************** Important Note about input function ****************
#******************************************************************************
# 1). By default, all input taken using input() is a string. means it always returns the input as a string
# 2). Even if user enters a number, python will treat it as text
# Example - 
age = input("Enter your age: ")
print(type(age))            #The DataType of "age" will be string