# *************** MATCH-CASE STATEMENT ***************

# match-case is used to compare one value
# with multiple possible values.

# Syntax:
# match variable:
#     case value1:
#         do something
#     case value2:
#         do something
#     case _:               # default case
#         do something

# Example:
# 01).
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

# Output:
# Tuesday


# 02).
color = "yellow"
match color:
    case "red":
        print("Stop! signal is Red")
    case "green":
        print("Please Go! signal is green")
    case "yellow":
        print("Go slow! Signal is yellow")
    case _:
        print("Traffic signal failed")

# Output:
# Go shlow! signal is yellow

# 03).
a = int(input("Enter your fisrt number: "))
b = int(input("Enter your second number: "))
operation = input("Choose operation (+, -, *, /, //, %): ")
match operation:
    case "+":
        print(f"{a} + {b} = ", a+b)
    case "-":
        print(f"{a} - {b} = ", a-b)
    case "*":
        print(f"{a} * {b} = ", a*b)
    case "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(f"{a} / {b} = ", a / b)
    case "//":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(f"{a} // {b} = ", a // b)

    case "%":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(f"{a} % {b} = ", a % b)
    case _:
        print("Please enter valid operation")

        
            
# Note:
# case _ works like a default case.
# It runs when none of the above cases match.

# match-case is available in Python 3.10 and later.


# ******************** PRACTICE QUESTION ********************

# Question: 01).
# Given an integer representing a menu choice,
# print the corresponding food item.
#
# Input:
# An integer choice.
#
# Conditions:
# 1 → "Pizza"
# 2 → "Burger"
# 3 → "Pasta"
# 4 → "Sandwich"
# Any other number → "Invalid choice"
#
# Output:
# Print the corresponding food item.
#
# Example:
# Input:
# 3
#
# Output:
# Pasta

choice = int(input("""
Please choose:
1 → Pizza
2 → Burger
3 → Pasta
4 → Sandwich

Enter choice: 
"""))

match choice:
    case 1:
        print("Pizza")
    case 2:
        print("Burger")
    case 3:
        print("Pasta")
    case 4:
        print("Sandwich")
    case _:
        print("Invalid choice")