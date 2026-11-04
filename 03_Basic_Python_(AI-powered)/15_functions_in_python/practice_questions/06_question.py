# Question 06):
# Write a function check_number(n) that checks whether a number is positive, negative, or zero.

num = input("Please enter your number to check positive or negative: ").strip()

def check_num(n):
    if n > 0:
        return "Positive"
    else:
        return "Negative"

if num[1:].isdigit() and num != "0":
    num = int(num)
    num_result = check_num(num)
    print(num_result)
elif num == "0":
    print("Your entered number is equal to zero.!")
else:
    print("Please enter valid number>>!")