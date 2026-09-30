# *********************** LOOP CONTROL STATEMENTS ***********************
# ************* CONTINUE CONTROL STATEMENTS *************
# continue: continue is a reserved statement which skips the current
# iteration and moves to the next one.

# It is used to terminates execution in the current iteration & continue
# execution of the loop whith the next iteration.

# Example:
# Example 01).
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print("LOOP ENDED BREAK STETEMENT WORK SUCCESSFULLY USING FOR LOOP")

# Output:
# 1
# 2
# 3
# 4
    # Here countinue statement skip 5 and continue next iteration 
# 6
# 7
# 8
# 9
# 10
# LOOP ENDED BREAK STETEMENT WORK SUCCESSFULLY USING FOR LOOP



# Example 02).
j = 1
while j <= 10:
    if j == 3:
        j += 1
        continue
    print(j) 
    j += 1
print("LOOP ENDED BREAK STETEMENT WORK SUCCESSFULLY USING WHILE LOOP")

# Output:
# 1
# 2
    # Here countinue statement skip 3 and continue next iteration
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# LOOP ENDED BREAK STETEMENT WORK SUCCESSFULLY USING WHILE LOOP

# ********** Question:01 **********
# Print 0 to 20 even and odd number using continue statement

# ************ For odd number ************
count = 0
while count <= 20:
    if count%2 == 0:
        count += 1
        continue
    print(count)
    count += 1
# Output:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19


# ************ For even number ************
even_count = 0
while even_count <= 20:
    if even_count%2 != 0:
        even_count += 1
        continue
    print(even_count)
    even_count += 1

# Output:
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20