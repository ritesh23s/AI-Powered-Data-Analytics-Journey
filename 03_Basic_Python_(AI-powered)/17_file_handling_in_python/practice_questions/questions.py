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




# Question 03: 
print("\n______Question 03______")
# From a file containing numbers saperated by comma, print the count of even nember.