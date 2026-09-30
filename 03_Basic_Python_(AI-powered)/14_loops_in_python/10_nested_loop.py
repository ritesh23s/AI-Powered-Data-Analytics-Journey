# *********************** LOOPS IN PYTHON ***********************
# ************* NESTED LOOP *************
# nested loop: a loop inside another loop is called a nested loop

# Syntax:
# for outer_variable in outer_sequence:
#     Outer loop body
#     for inner_variable in inner_sequence:
#         Inner loop body
#         Statement(s) to execute

# Example:
print("Example 01")
# Example 01).
for i in range(3):
    for j in range(2):
        print(i, j)

# Output:
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1


print("Example 02")
# Example 02).
for i in range(3):
    print("Outer loop start", i)
    for j in range(1,4):
        print(j)

# Output:
# Outer loop start 0
# 1
# 2
# 3
# Outer loop start 1
# 1
# 2
# 3
# Outer loop start 2
# 1
# 2
# 3

print("Example 03")
# Example 03). We also use while loop for nested loop
i = 1 
while i < 5:
    print("Outer loop start", i)
    i += 1
    for j in range(1, 4):
        print(j)

# Output:
# Outer loop start 1
# 1
# 2
# 3
# Outer loop start 2
# 1
# 2
# 3
# Outer loop start 3
# 1
# 2
# 3
# Outer loop start 4
# 1
# 2
# 3


# ********** Practice Question - 01 **********
print("Practice Question - 01")
# Write a program to print prime number between 2 to 20 using nested loop

for num in range(2, 20):
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        print(num)
            
# Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
