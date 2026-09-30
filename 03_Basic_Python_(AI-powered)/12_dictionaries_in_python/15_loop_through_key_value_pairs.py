# **************** LOOPING THROUGH A DICTIONARY ****************
# ******************** LOOP THROUGH KEY VALUE PAIRS ********************

# we can access the dictionaries key-value-pairs using loop
# Example:
# 01).
cars = {
    "name": "Scorpio",
    "brand": "Mahindra",
    "price": "19.2L base model",
    "color": "White",
    "wheel": 4,
    "top_speed": 160.2
}

for key, value in cars.items():
    print(key, value)

# Output:
# name Scorpio
# brand Mahindra
# price 19.2L base model
# color White
# wheel 4
# top_speed 160.2


for key_value_pairs in cars.items():
    print(key_value_pairs)

# Output:
# ('name', 'Scorpio')
# ('brand', 'Mahindra')
# ('price', '19.2L base model')
# ('color', 'White')
# ('wheel', 4)
# ('top_speed', 160.2)

# Here it all key value pairs are returns as a  tuple


# *********** Access the KEY VALUE PAIRS using while loop ***********
print("******* Access the KEY VALUE PAIRS using while loop *******")
# firstly we have to convert this dictionary key values pairs  
# into list/tuple for indexing

kvp_lst = list(cars.items())
i = 0 
while i < len(kvp_lst):
    print(kvp_lst[i])
    i += 1
# Output:
# ('name', 'Scorpio')
# ('brand', 'Mahindra')
# ('price', '19.2L base model')
# ('color', 'White')
# ('wheel', 4)
# ('top_speed', 160.2)

# Here it also all key value pairs are returns as a  tuple