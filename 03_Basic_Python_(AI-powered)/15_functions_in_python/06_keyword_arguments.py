# *************** FUNCTIONS IN PYTHON ***************
# ********* KEYWORD ARGUMENTS *********
# Keyword arguments allow us to pass arguments using parameter names.

# We provide arguments in the form of key=value. python matches the argument
# with the parameter name.

# Therefore, the order of arguments does not matter.

# Syntax:
# def function_name(parameter_1, parameter_2,...):
    # function body/some works
    # return value 
# function_name(argu_1 = "value", argu_2 = "value",...)

# Example 01).
def user_info(name, age):
    return f"{name} {age}"

user_1 = user_info(name = "Shhubham", age = 24)
print(user_1)
# Output:
# Shubham 24

user_2 = user_info(age = 21, name = "abc")
print(user_2)
# Output:
# abc 21

# Here, 
# we write age first and name second, but python match by parameter name
# so value 21 use for age parameter and abc use for name parameter




# Example 02).
def user_address(name = "username", adrs = "this address.."):
    return f"{name} from {adrs}"

print(user_address()) 
# Output:
# username from this address.. #because here both default value are used 

user1_add = user_address(name="aman", adrs="siwan")
print(user1_add)
# Output:
# aman from siwan

user2_add = user_address(adrs="saran", name="hemant")
print(user2_add)
# Output:
# hemant from saran


print(user_address(adrs="patna"))
# Output:
# username from patna
# here only adrs is changed, and name is default value.