# Question 05):
# Write a function for 
# take input: number

# condition:
# 01). if number is odd it return a string "odd number"
# 02). if number is even it return a string "even number"

num = int(input("Please enter number to check even or odd: "))
def check(check_num):
    odd = f"Your entered number {check_num} is ODD number.!"
    even = f"Your entered number {check_num} is EVEN number.!"
    if check_num%2 == 0:
        return even
    else:
        return odd
    
result = check(num)

print(result)