# ********** Practice Questions **********

# Question 01.)
print("Question 01:")
# Print numbers from 1 to 100
for i in range(1, 101):
    print(i)


# Question 02.)
print("Question 02:")
# Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)



# Question 03.)
print("Question 03:")
# print the multiplication table of number n.
n = int(input("Please enter numner to print table:"))
for i in range(1, 11):
    print(f"{i} x {n} = {i*n}") 


# Question:04
# Search for a number x in this tuple using loop.
# x = 64
# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 110, 75, 64, 45, 10)
# Solution:

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 110, 75, 64, 45, 10)
x = 64
idx = 0
for num in tuple:
    print("Finding.. at index", idx)
    if num == x:
        print(f"{x} is founded at index {idx}")
    idx += 1