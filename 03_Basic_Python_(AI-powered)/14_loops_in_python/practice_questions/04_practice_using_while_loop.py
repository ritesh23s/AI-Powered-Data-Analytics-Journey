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
print("Questions 02")
# Search for a number x in this tuple using while loop.
# tpl = (1, 4, 9, 16, 25, 36, 49, 16, 81, 100, 16, 10)
# x = 16

tpl = (1, 4, 9, 16, 25, 36, 49, 16, 81, 100, 16, 10)
x = 16
indx = 0
while indx < len(tpl):
    if tpl[indx] == x:
        print(f"{x} is founded at index", indx)
    else:
        print("finding at index", indx)
    indx += 1

# Output:
# finding at index 0
# finding at index 1
# finding at index 2
# 16 is founded at index 3
# finding at index 4
# finding at index 5
# finding at index 6
# 16 is founded at index 7
# finding at index 8
# finding at index 9
# 16 is founded at index 10
# finding at index 11