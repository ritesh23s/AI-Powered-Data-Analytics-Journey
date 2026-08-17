# ******************** NESTED DICTIONARIES ********************
# ******************** ACCESSING NESTED VALUES ********************

# Syntax:
# variable_name["outer_key"]["inner_key"]

# If the value is inside another nested dictionary:
# variable_name["outer_key"]["inner_key"]["nested_key"]


# Example:
# 01).
user_details = {
    "username": "ritesh23s",
    "password": "######",

    "profile_details": {
        "name": "Shubham Yadav",
        "email": "shubh@sumanicAI.com",

        "content": {
            "post": 45,
            "reels": 23,
            "reposts": 15
        }
    },

    "dashboard": {
        "likes": 1265,
        "comments": 545,
        "new_followers": 12,
        "views": "986K"
    }
}


# Accessing a normal value:
print("Access username of user_details:", user_details["username"])

# Output:
# Access username of user_details: ritesh23s


# Accessing a value from a nested dictionary:
print("Access the name of user_details:", user_details["profile_details"]["name"])

# Output:
# Access the name of user_details: Shubham Yadav


# Accessing a complete nested dictionary:
print("Access the content of user_details:", user_details["profile_details"]["content"])

# Output:
# Access the content of user_details:
# {'post': 45, 'reels': 23, 'reposts': 15}


# Accessing a specific value from a deeper nested dictionary:
print("Number of posts:", user_details["profile_details"]["content"]["post"])

# Output:
# Number of posts: 45