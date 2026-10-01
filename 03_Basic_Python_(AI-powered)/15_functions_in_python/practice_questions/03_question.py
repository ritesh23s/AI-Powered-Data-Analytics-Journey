# Question 03):
# WAF to find the factorial of n. (n is the parameter)

num = int(input("Please enter the number to calculate the factorial: "))
def calc_fact(n):
    fctl = 1
    for i in range(1, n+1):
        fctl *= i
    print(fctl)
calc_fact(num)



# Another way to get the factorial using the return statement.
num1 = int(input("Please enter the number to calculate the factorial: "))
def fact(n):
    fctl = 1
    for i in range(1, n+1):
        fctl *= i
    return fctl
fact_of_num1 = fact(num1)
print(fact_of_num1)
