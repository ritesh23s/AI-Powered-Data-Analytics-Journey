# ********** Practice Questions **********
print("Questions 01")

# ********** Questions 01 **********
# Print the elements of the following list using while loop.
# lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Solution
lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(lst):
    print(lst[idx])
    idx += 1

# Output:
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100




# ********** Questions 02 **********
# Search for a number x in this tuple using while loop.
# tpl = (1, 4, 9, 16, 25, 36, 49, 16, 81, 100, 16, 10)
# x = 16

tpl = (1, 4, 9, 16, 25, 36, 49, 16, 81, 100, 16, 10)
x = 16
indx = 0
while indx < len(tpl):
    print("finding..")
    if tpl[indx] == x:
        print(f"{x} is founded at index", indx)
    else:
        print("finding")
    indx += 1