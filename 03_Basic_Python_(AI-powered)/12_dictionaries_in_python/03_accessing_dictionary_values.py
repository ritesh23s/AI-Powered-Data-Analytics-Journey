# ******************** ACCESSING DICTIONARY VALUES ********************

# Dictionary values are accessed using their keys.

# Syntax:
# variable_name["key"]

# Example:
# 01).
car = {
    "name": "Scorpio",
    "brand": "Mahindra",
    "price": "19.2L base model",
    "color": "White",
    "wheel": 4,
    "top_speed": 160.2
}

print(car["top_speed"])
# Output: 160.2

print(car["name"])
# Output: Scorpio

print(car["brand"])
# Output: Mahindra

print(car["color"])
# Output: White


# If we try to access a key that does not exist:
# print(car["model"])

# Output:
# KeyError: 'model'

# Note:
# Using a key that does not exist in the dictionary will raise a KeyError.


# Note:
# To access a dictionary value, write the key inside quotes.

# Example:
print(car["name"])

# Output:
# Scorpio

# We can use either double quotes or single quotes:
print(car["name"])    
print(car['name'])    

# Wrong:
# print(car[name])

# Without quotes, Python treats "name" as a variable,
# not as the dictionary key.


# Example:
# 02).
motercycle_details = dict(
    name = "Himalyan 450", 
    brand_name = "royal enfield",
    variant = "hanle black",
    onroad_price = 376701,
    city = "siwam",
    kerb_weight = "196kg",
    tyre_type = "tubed",
    wheel_type = "spoke wheel",
    engine_name = "Sherpa 450",
    engine_cc = "451.65cc"
)

print(motercycle_details["name"])
# Output:
# Himalyan 450

print(motercycle_details["brand_name"])
# Output:
# royal enfield

print(motercycle_details["variant"])
# Output:
# hanle black

print(motercycle_details["wheel_type"])
# Output:
# spoke wheel

print(motercycle_details["kerb_weight"])
# Output:
# 196kg

print(motercycle_details["engine_cc"])
# Output:
# 451.65cc