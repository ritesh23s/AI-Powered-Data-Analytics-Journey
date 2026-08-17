# ******************** DICTIONARY CHARACTERISTICS ********************

# 01). Keys must be unique:
#      The same key cannot be used multiple times in a dictionary.
#      If the same key is used again, its old value is replaced.

# 02). Keys must be immutable (hashable).
#      Mutable data-types like list, set, and dictionary cannot be used as 
#      dictionary keys.
#      String, integer, float, and tuple can be used as keys.

# 03). Values can be of any data-type:
#      A value can be a string, integer, float, list,
#      tuple, set, dictionary, etc.

# 04). Dictionaries are mutable:
#      We can add, remove, or modify key-value pairs
#      after creating the dictionary.

# 05). Dictionary stores data in key-value pairs:
#      Each key is connected to its corresponding value.

# 06). Keys are used to access values:
#      We access a value using its key.

# Example:
student = {
    "name": "Shubham",
    "age": 23,
    "skills": ["Python", "JavaScript"],
    "address": {
        "city": "Siwan"
    }
}