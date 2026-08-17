# ******************** NESTED DICTIONARIES ********************

# A dictionary can contain another dictionary as a value.
# A dictionary inside another dictionary is called
# a nested dictionary.

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

print(user_details)

# Output:
# {
#     'username': 'ritesh23s',
#     'password': '######',
#     'profile_details': {
#         'name': 'Shubham Yadav',
#         'email': 'shubh@sumanicAI.com',
#         'content': {
#             'post': 45,
#             'reels': 23,
#             'reposts': 15,  
#         }
#     },
#     'dashboard': {
#         'likes': 1265,
#         'comments': 545,
#         'new_followers': 12,
#         'views': '986K'
#     }
# }


# Here, "profile_details" is a dictionary
# inside the "user_details" dictionary.

# Also, "content" is another dictionary
# inside the "profile_details" dictionary.

# This is called a nested dictionary.