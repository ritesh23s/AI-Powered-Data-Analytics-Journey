# ********** Practice Questions **********
# ********** Questions 01 **********
print("Questions 01")
# Print the number 1 to 10.
i = 1
while i <= 10:
    print(i) 
    i += 1

# Output:
# print 1 to 10


# ********** Questions 02 **********
print("Questions 02")
# Print the number 10 to 1
x = 10
while x >= 1:
    print(x)
    x -= 1

# Output:
# print 10 to 1


# ********** Questions 03 **********
print("Questions 03")
# Print the table using user input

num = int(input("Please enter number to print table:"))
y = 1
while y <= 10:
    print(f"{num} x {y} = {num*y}")
    y += 1

rev_num = int(input("Please enter number to print table in reverse way:"))
z = 10
while z >= 1:
    print(f"{rev_num} x {z} = {rev_num*z}")
    z -= 1