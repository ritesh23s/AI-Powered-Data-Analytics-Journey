# **************** LOOPING THROUGH A DICTIONARY ****************
# ******************** LOOP THROUGH KEYS ********************

# we can access the dictionaried key using loop.
# Example:
# 01).
student = {
    "name": "Shubham",
    "age": 23,
    "Course": "Btech",
    "roll_no": 25,
    "email": "shubham@sumanicAI.com"
}

print("******* Access the key using for loop *******")
for key in student:
    print(key)


# Output:
# name
# age
# Course
# roll_no
# email

# Here we access the all keys of dictionary "student" using loop 



# *********** Access the key using while loop ***********
print("******* Access the key using while loop ******* ")
# firstly we have to convert this dictionary key 
# into list/tuple for indexing

dict_idx = list(student.keys())
i = 0
while i < len(dict_idx):
    print(dict_idx[i])
    i += 1
    
# Output:
# name
# age
# Course
# roll_no
# email