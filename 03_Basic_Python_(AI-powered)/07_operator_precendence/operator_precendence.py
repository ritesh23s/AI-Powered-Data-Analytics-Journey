# ***************************** OPERATOR PRECEDENCE *****************************

# Operator Precedence
# Operator precedence is the general order in which Python evaluates an expression.
# It is similar to the BODMAS rule in mathematics.

# Python Order (Highest to Lowest Priority)

# Step 1. ()       → Parentheses (Expression inside brackets)
# Step 2. **       → Exponent (Power Operator)
# Step 3. *, /, //, % → Multiplication, Division, Floor Division, Modulus
#                      (All have equal priority and are evaluated from left to right.)
# Step 4. +, -     → Addition, Subtraction
#                    (Both have equal priority and are evaluated from left to right.)

# Python Operator Precedence
# ()
# **
# *, /, //, %
# +, -

# Important Note:
# If multiple operators have the same precedence,
# Python evaluates the expression from left to right,
# except the exponent operator (**), which is evaluated from right to left.

# Example:
# 01). Expression:
# (5 + 2) / 7 + 2**3 - 3*4 + 5%2

print((5 + 2) / 7 + 2**3 - 3*4 + 5%2) #output = -2
# Solution:
# (5 + 2) / 7 + 2**3 - 3*4 + 5%2
# 7 / 7 + 2**3 - 3*4 + 5%2          {Parentheses Completed}
# 7 / 7 + 8 - 3*4 + 5%2             {Exponent Completed}
# 7 / 7 + 8 - 3*4 + 5%2             {Start evaluating *, /, //, % from left to right}
# 1 + 8 - 3*4 + 5%2                 {/ Completed}
# 1 + 8 - 12 + 5%2                  {* Completed}
# 1 + 8 - 12 + 1                    {% Completed}
# 1 + 8 - 12 + 1                    {Start evaluating + and - from left to right}
# 9 - 12 + 1                        {+ Completed}
# -3 + 1                            {- Completed}
# -2                                {Final Answer}

# Example:
# 02). Expression:
# (5 + 2) / 7 + 20//3 + 2**3 - 3*4 + 5%2
print((5 + 2) / 7 + 20//3 + 2**3 - 3*4 + 5%2)

# Solution:
# (5 + 2) / 7 + 20//3 + 2**3 - 3*4 + 5%2
# 7 / 7 + 20//3 + 2**3 - 3*4 + 5%2        {Parentheses Completed}
# 7 / 7 + 20//3 + 8 - 3*4 + 5%2           {Exponent Completed}
# 7 / 7 + 20//3 + 8 - 3*4 + 5%2           {Start evaluating *, /, //, % from left to right}
# 1 + 20//3 + 8 - 3*4 + 5%2               {/ Completed}
# 1 + 6 + 8 - 3*4 + 5%2                   {// Completed}
# 1 + 6 + 8 - 12 + 5%2                    {* Completed}
# 1 + 6 + 8 - 12 + 1                      {% Completed}
# 1 + 6 + 8 - 12 + 1                      {Start evaluating + and - from left to right}
# 7 + 8 - 12 + 1                          {+ Completed}
# 15 - 12 + 1                             {+ Completed}
# 3 + 1                                   {- Completed}
# 4                                       {Final Answer}