# Type Conversion - Type conversion means changing one data type into another data type
# This is extremely common when working with real data

# 01). Converting String to Integer - Data comming from CSV iles or user input is often in string format 
age = "23"
# To convert into an integer
age =int(age)  #it convert into integer. now we perform calculation on it
print(type(age))


# 02). Converting String to Float - Decimal values are converted using Float(). This is commonly used for prices, ratings, and averages.
price = 2565.234
price = str(price)  #it convert inti string
print(type(price))


# 03). Converting number to string - Sometimes you need to convert numbers into strings, specially while generating reposts or messages.
overalSales = 500
message = "Total sales:" + str(overalSales)
print(message)
print(type(message))



# *********************** Common Errors in Type Conversion ***********************
#***************************************************************************************** 
# Not every string can be converted into a number 

value = "454abc"
# int(value)                               #here if we convert value into integer we get error - "ValueError: invalid literal for int() with base 10: '454abc'"
print(type(value))

# This will cause an error - Always vakidate your data before converting it. Later, we will handle such cases using error handling
