# ********** Practice Questions **********
# ********** Question 01.) **********
print("Question 01")
# Calculate the sum of first n numbers.

n = int(input("Enter number to get sum:"))
sum = 0
for i in range(1, n+1):
    sum += i
print("sum of total:", sum)



# ********** Question 02.) **********
print("Question 02")
# Write a program to find the factorial number of first n numbers.
num = int(input("Enter number to find factorial:"))
factorial = 1

for i in range(1, num+1):
    factorial *= i
print(f"factorial of {num} = {factorial}")