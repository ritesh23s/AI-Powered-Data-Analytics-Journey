# Question 09):

# Write a function calculate_bill(units) that calculates the final electricity bill based on the number of units consumed.

# Input:
# Take electricity units as an integer.

# Conditions:
# 1. If units <= 0 → return "Invalid units"
# 2. First 100 units → ₹5 per unit
# 3. Next 100 units (101–200) → ₹7 per unit
# 4. Next 200 units (201–400) → ₹10 per unit
# 5. Above 400 units → ₹12 per unit

# Important:
# Slab calculation should be cumulative.

# Example:
# If units = 250:

# First 100 units  → 100 × 5
# Next 100 units   → 100 × 7
# Remaining 50     → 50 × 10

# Final bill = ₹1700

# Output:
# The function must return the final bill amount.
# Print the returned value outside the function.

# Examples:

# Input: 80
# Output: 400

# Input: 150
# Output: 850

# Input: 250
# Output: 1700

# Input: 500
# Output: 4400

# Input: 0
# Output: Invalid units



def calculate_bill(units):
    if units <= 0:
        return "Invalid units"
    elif units <= 100:
        first_slab = units*5
        return first_slab
    elif units > 100 and units <= 200:
        first_slab = 100*5
        second_slab = (units - 100)*7
        return first_slab + second_slab    
    elif units > 200 and units <= 400:
        first_slab = 100*5
        second_slab = 100 * 7
        third_slab = (units - 200)*10
        return first_slab + second_slab + third_slab
    else:
        first_slab = 100*5
        second_slab = 100 * 7
        third_slab = 200 * 10
        fourth_slab = (units - 400)*12
        return first_slab + second_slab + third_slab + fourth_slab
        

consumed_units = int(input("Enter units: "))
bill_amount = calculate_bill(consumed_units)
print(bill_amount)
