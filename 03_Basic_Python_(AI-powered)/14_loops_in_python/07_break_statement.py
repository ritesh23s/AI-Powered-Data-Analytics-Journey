# *********************** LOOP CONTROL STATEMENTS ***********************
# ************* BREAK CONTROL STATEMENTS *************
# break: break is a reserved statement which stop the loop completely.
# It is used to terminate the loop when reached. 

# Example
# 01).
for i in range(0, 11):
    print(i)
    if i == 6:
        break
print("LOOP ENDED BREAK STETEMENT WORK SUCCESSFULLY USING FOR LOOP")

# Output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# LOOP ENDED BREAK STETEMENT WORK SUCCESSFULLY USING FOR LOOP


j = 1
while j <= 10:
    print(j)
    if j == 4:
        break
    j += 1
print("LOOP ENDED BREAK STETEMENT WORK SUCCESSFULLY USING WHILE LOOP")

# Output:
# 1
# 2
# 3
# 4
# LOOP ENDED BREAK STETEMENT WORK SUCCESSFULLY USING WHILE LOOP


# ********** Question:01 **********
# Search for a number x in this tpl using loop.
# x = 64
# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 110, 75, 64, 45, 10)
# Solution:

tpl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 110, 75, 64, 45, 10)
x = 64

idx = 0
for num in tpl:
    if num == x:
        print("Founded at index", idx)
        break
    else:
        print("Finding... at index", idx)
    idx += 1

print("END OF LOOP X IS FOUNDED...!")

# Output:
# Finding... at index 0
# Finding... at index 1
# Finding... at index 2
# Finding... at index 3
# Finding... at index 4
# Finding... at index 5
# Finding... at index 6
# Founded at index 7
# END OF LOOP X IS FOUNDED...!
