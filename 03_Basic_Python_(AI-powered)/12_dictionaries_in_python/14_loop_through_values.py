# **************** LOOPING THROUGH A DICTIONARY ****************
# ******************** LOOP THROUGH VALUES ********************

# we can also access the dictionary value using loop
# Example:
cars = {
    "name": "Scorpio",
    "brand": "Mahindra",
    "price": "19.2L base model",
    "color": "White",
    "wheel": 4,
    "top_speed": 160.2
}

print("******* Access the value using for loop *******")

for value in cars.values():
    print(value)

# Output:
# Scorpio
# Mahindra
# 19.2L base model
# White
# 4
# 160.2


# *********** Access the value using while loop ***********
print("******* Access the value using while loop *******")
# firstly we have to convert this dictionary value 
# into list/tuple for indexing

cars_value = tuple(cars.values())
i = 0
while i < len(cars_value):
    print(cars_value[i])
    i += 1

# Output:
# Scorpio
# Mahindra
# 19.2L base model
# White
# 4
# 160.2