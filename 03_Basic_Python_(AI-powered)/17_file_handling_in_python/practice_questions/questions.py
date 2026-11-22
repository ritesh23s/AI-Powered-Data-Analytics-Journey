# Question 01:
print("______Question 01______")
# Create a new file "practice.txt" using python. add the 
# following data in it
    # Hi everyone
    # we are learning File I/O
    # using Java.
    # I like programming in Java.

# Write a function that replace all occurrences of "Java" with "Python" in above file
# Search if the word "learning" exists in the file or not.

# Solution

file_path = "03_Basic_Python_(AI-powered)/17_file_handling_in_python/practice_questions/practice.txt"

file_content = "Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java."

# Creating a file.
with open(file_path, "w") as f:
    f.write(file_content)


# Reading the file
with open(file_path, "r") as f:
    file_data = f.read()

print("--- Actual File Content ---")
print(file_data)


# Replace function for replace all occurrences "Java" to "Python"
def replace_fnc(data):
    replaced_value = data.replace("Java", "Python")
    return replaced_value
result = replace_fnc(file_data)


# Overwrites the replaced value inside the file
with open(file_path, "w") as f:
    f.write(result)


with open(file_path, "r") as f:
    replaced_file_data = f.read()


# Search if the target word exists in the file
word = "learning"
print("\n--- Target word existence ---")
if replaced_file_data.find(word) != -1:
    print(f"{word} exists.")
else:
    print(f"{word} does not exist.")


print("\n--- Final File Content ---")
print(replaced_file_data)



# Question 02: 
print("\n______Question 02______")
# Write a function to find which line of the file does the word "learning" 
# occur first.
# print -1 if word not found.

# Solution:

def check_line(value):
    targeted_word = "learning"
    line = 1
    for line_text in value:
        if targeted_word in line_text:
            print(f"{targeted_word} occurs in line {line}")
            break
        line += 1
    else:
        print("-1")


with open(file_path, "r") as f:
    file_data_for_Q2 = f.readlines()

check_line(file_data_for_Q2)



# Question 03: 
print("\n______Question 03______")
# From a file containing numbers saperated by comma, print the count of even nember.

# Solution:

file_path_for_Q3 = "03_Basic_Python_(AI-powered)/17_file_handling_in_python/practice_questions/practice_01.txt"

with open(file_path_for_Q3, "w") as f:
    f.write("45, 2, 46, 13, 56, 78, 12, 11, 178, 7, 23, 53, 63, 61, 81, 78, 89, 86, 48, 85, 45, 42, 14, 12")

with open(file_path_for_Q3, "r") as f:
    file_data_for_Q3 = f.read()

str_lst_for_Q3 = file_data_for_Q3.split(",")


def even_count(value):
    int_lst_for_Q3 = []
    for text in value:
        int_lst_for_Q3.append(int(text.strip()))

    even_num = []
    odd_num = []
    for int_text in int_lst_for_Q3:
        if int_text%2 == 0:
            even_num.append(int_text)
        else:
            odd_num.append(int_text)
    return len(even_num)

result = even_count(str_lst_for_Q3)
print(f"There are {result} even numbers.!")