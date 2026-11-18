# ********** LOCAL AND GLOBAL VARIABLE IN PYTHON **********
# ********** VARIABLE SCOPE RULES **********
# 01). Local variables exist only inside functions

# 02). Global variables exist throughout the program

# 03). Local variable override global variable with the same name
# Example:
score = 50

def show_score():
    #Local variable with the same name as the global variable
    score = 100 
    print(f"Inside function (Local score): {score}")

show_score()

#Printing global variable outside the function
print(f"Outside function (Global score): {score}")

# Output:
# Inside function (Local score): 100
# Outside function (Global score): 50
        #Here we see that inside the function, the local variable 'score' 
        #overrides (shadows) the global variable 'score', but the global 
        #variable remains unchanged outside the function.


# 04). The global keyword allows modifying global variables