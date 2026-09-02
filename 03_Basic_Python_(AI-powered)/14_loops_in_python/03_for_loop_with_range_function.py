# ************* FOR LOOPS IN PYTHON *************
# ************* FOR LOOPS WITH RANGE FUNCTION *************

# range(): The range function generates a sequence of numbers.

# range function returns a sequence of numbers, starting from 0 by default, and  
# increments by 1 (by default), and stops before a specified numbers

# Syntax:
# for iterable in range(starting_value, ending_value, step_value):
#     do something

# Here:
# starting_value: The value from where the sequence starts.

# ending_value: The value before which the sequence stops.

# step_value: The value by which the sequence increments
            # or decrements after each step.
 

# There are different ways for decide the range value in loop
# 01). range() with single value
# 02). range() with starting and ending_value
# 03). range() with starting , ending_value and step_value




# ************* 01). range() with single value: *************
# In the range() with single value we can use a single value for decide a range
# Syntax:
# for iterable in range(range_value):
#     do something

# Example:
# 01).
for i in range(5):
    print(i)
    
# Output:
# 0
# 1
# 2
# 3
# 4     # It prints 0 to 4 because the sequence starts from 0 by default, and  
        # increments by 1 (by default), and stops before a specified range value



# ************* 02). range() with starting and ending_value: *************
# In the range() with starting and ending value we decide range using
# starting_value and ending_value

# Syntax:
# for iterable in range(starting_value, ending_value):
#     do something

# Example:
# 01).
for i in range(1, 8):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7     # It print 1 to 7 because starting_value is 1 and ending_value is 8,
        # so sequence starts from 1 and increment by default 1 and the
        # ending_value is 8 which not included




# ********** 03). range() with starting , ending_value and step_value: **********
# In the range() with starting, ending and step_value we can decide range using
# start_value, end_value and step_value

# Where, 
        # step_value: The value by which the sequence increments
        # or decrements after each step.
 
# Syntax:
# for iterable in range(starting_value, ending_value, step_value):
#     do something

# Example:
# 01).
for i in range(0, 10, 2):
    print(i)
    
# Output:
# 0
# 2
# 4
# 6
# 8     # It prints number from 0 to 10 with a step of 2 