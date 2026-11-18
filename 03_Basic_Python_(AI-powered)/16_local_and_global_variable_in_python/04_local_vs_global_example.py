# ********** LOCAL AND GLOBAL VARIABLE IN PYTHON **********
# ********** LOCAL VS GLOBAL EXAMPLE**********
# Example 01).

x = 20
y = 45

def test():
    x = 56
    print(f"Local variable value inside the function: {x}")
    print(f"Global variable value inside the function: {y}")
test()
# Output:
# Local variable value inside the function: 56
# Global variable value inside the function: 45
        #here we see that if we assigned a local variable inside the function than
        #the function give priority for local variable.


print(f"Global variable outside the function: {x}")
print(f"Global variable outside the function: {y}")
# Output:
# Global variable outside the function: 20
# Global variable outside the function: 45