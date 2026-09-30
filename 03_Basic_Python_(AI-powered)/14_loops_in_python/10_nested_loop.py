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
# 01).
for i in range(3):
    for j in range(2):
        print(i, j)