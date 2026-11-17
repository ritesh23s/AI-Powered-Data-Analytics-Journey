# *************** FUNCTIONS IN PYTHON ***************
# ********* LAMBDA FUNCTIONs *********
# lambda functions are small anonymouse functions written in one line.
# Syntax:
# function_name = lambda parameter1, parameter2,...: perform_operation/function_body

# function_name(argu1, argu3,..)

# Example 01).
add_num = lambda a , b: a + b

print(add_num(458, 78))

# Output:
# 536

# Example 02).

average = lambda a, b, c, d , e: (a+b+c+d+e)/5
print(average(1,2,3,4,5))


# Example 03).
# write multiplication table of entered number by user input
num = int(input("Enter a number to print multiplication table: "))
table = lambda n: list(map(lambda i: n * i, range(1, 11)))

for result in table(num):
    print(result) 