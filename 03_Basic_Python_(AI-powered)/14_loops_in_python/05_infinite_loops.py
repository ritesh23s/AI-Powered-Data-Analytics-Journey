# ************* INFINITE LOOPS IN PYTHON *************
# infinite loop: if the condition never becomes false the loops runs forever
# that called infinite loop

# Example:
# 01).
items = [1]
for x in items:
    print("infinite loop using for loop")
    items.append(1)


# 02).
i = 1
while i <= 5:
    print("infinite loop using while loop")

# 03).
while True:
    print("This codition is always true")