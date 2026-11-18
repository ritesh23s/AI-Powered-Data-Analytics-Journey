# ********** LOCAL AND GLOBAL VARIABLE IN PYTHON **********
# ********** GLOBAL VARIABLE **********
# Global variable are created outside of all functions.
# They can be accessed from anywhere in the program.

# Example:
# 01).
score = 202 
first_team = "RCB"

def show_winning_score():
    print(f"Winning score is: {score}")

show_winning_score()
# Output:
# Winning score is: 202

def show_team_name():
    print(f"First inning team name: {first_team}")

show_team_name()
# Output:
# First inning team name: RCB
                #here we see that the global variable
                # score = 202 
                # first_team = "RCB" is accessed anywhere in this program.


# here we also accessed the both variable outside the function or anywhere 
# of this program.
print(score)
print(first_team)
# Output:
# 202
# RCB


# Example 01).
def another_team_name():
    first_team = "SRH"
    print(f"First inning team name: {first_team}")
    print(f"Winning score is: {score}")
another_team_name()
# Output:
# First inning team name: SRH
# Winning score is: 202
                        #here we see that we also assigned here a local variable 
                        #for the another_team_name() function