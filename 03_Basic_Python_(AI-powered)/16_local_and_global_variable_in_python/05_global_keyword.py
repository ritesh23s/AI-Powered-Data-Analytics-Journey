# ********** LOCAL AND GLOBAL VARIABLE IN PYTHON **********
# ********** THE GLOBAL KEYWORD **********
# By default, we can read a global variable inside a function, but we cannot 
# modify (change) it. 

# The 'global' keyword used to modify a global variable from inside a function.

# Example:
x = 10  

def update():
    global x  
    x = 56    
    print(f"Inside function, updated x: {x}")

update()
# Output:
# Inside function, updated x: 56


# here we printing outside to check the global variable value actually changed..?
print(f"Outside function, x is also updated which is: {x}")
# Output:
# Outside function, x is also updated which is: 56
               # Here we see that using the 'global' keyword, the original 
               # global variable 'x' value changed from 10 to 56 globally!


# Example 02).
max_temp = 100

def update_max_temp():
    global max_temp
    max_temp = 4000
    print(f"Updated maximum temperature: {max_temp}")
update_max_temp()
# Output:
# Updated maximum temperature: 4000

# Here we also printing the value of max_temp for see that it changed or not.
print(f"Outside the function max_temp is: {max_temp}")
# Output:
# Outside the function max_temp is: 4000    
            #here we see that max_temp value is also changed globally.