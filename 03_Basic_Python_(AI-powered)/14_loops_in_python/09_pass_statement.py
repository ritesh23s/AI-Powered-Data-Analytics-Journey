# *********************** LOOP CONTROL STATEMENTS ***********************
# ************* PASS CONTROL STATEMENTS *************
# pass: pass is a null statement that does nothing.
# It is used as a placeholder for future code.

# Example:
# 01).
for i in range(1, 5):
    pass
print("LOOP ENDED PASS STETEMENT WORK SUCCESSFULLY USING FOR LOOP")



j = 0
while j <= 10:
    pass
    j += 1
print("LOOP ENDED PASS STETEMENT WORK SUCCESSFULLY USING WHILE LOOP")


# Note:
# We can also used this pass statement in if-else statement



num = int(input("enter number to get sum: "))

sum = 0
x = 1
while x <= num:
    sum += x
    x += 1
print(sum)