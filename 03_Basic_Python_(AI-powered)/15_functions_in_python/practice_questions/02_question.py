# Question 02):
# WAF to print the elements of a list in a single line.

fruits = ["mango", "banana", "papaya", "apple", "orrange", "pinapple"]

def print_element(lst): 
    for elmnt in lst:
        print(elmnt, end=" ")
print_element(fruits)


# Output:
# mango banana papaya apple orrange pinapple 

print() #this print() used for print another value single line to next line
    
# Here another way to print the elements of a list in a single line 
# using return statement
items = ["mouse", "keybpard", "phone", "battery", "pen", "paper", "table"]
def show_element(lst):
    elements = ""
    for elmnt in lst:
        elements += elmnt +" "
    return elements

lst_element = show_element(items)
print(lst_element)

# Output:
# mouse keybpard phone battery pen paper table 

# ********** HERE SOME LISTS FOR CALL THIS FUNCTIONS **********
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
print_element(colors)
# Output:
# Red Blue Green Yellow Purple Orange 
print()


animals = ["Lion", "Tiger", "Elephant", "Kangaroo", "Dolphin", "Monkey", "Rabbit"]
print_element(animals)
# Output:
# Lion Tiger Elephant Kangaroo Dolphin Monkey Rabbit
print()


cities = ["Tokyo", "Paris", "New York", "London", "Mumbai", "Sydney"]
print_element(cities)
# Output:
# Tokyo Paris New York London Mumbai Sydney 
print()

countries = ["India", "Japan", "Germany", "Brazil", "Canada", "Australia", "Egypt"]
print_element(countries)
# Output:
# India Japan Germany Brazil Canada Australia Egypt 
print()


languages = ["Python", "JavaScript", "Java", "C++", "Ruby", "Swift"]
print_element(languages)
# Output:
# Python JavaScript Java C++ Ruby Swift 
print()


sports = ["Cricket", "Football", "Basketball", "Tennis", "Badminton", "Swimming", "Hockey"]
print_element(sports)
# Output:
# Cricket Football Basketball Tennis Badminton Swimming Hockey
print()


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn"]
print_element(planets)
# Output:
# Mercury Venus Earth Mars Jupiter Saturn
print()

vegetables = ["Potato", "Tomato", "Onion", "Spinach", "Carrot", "Broccoli", "Cabbage"]
print_element(vegetables)
# Output:
# Potato Tomato Onion Spinach Carrot Broccoli Cabbage 
print()


months = ["January", "February", "March", "April", "May", "June"]
month_lst = show_element(months)
print(month_lst)
# Output:
# January February March April May June


subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography", "Economics"]
sjct_lst = show_element(subjects)
print(sjct_lst)
# Output:
# Mathematics Physics Chemistry Biology History Geography Economics 