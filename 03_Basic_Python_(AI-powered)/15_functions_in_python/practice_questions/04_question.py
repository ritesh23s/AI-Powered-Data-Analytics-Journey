# Question 04):
# WAF to convert USD to INR

usd = int(input("Please enter USD for convert to INR: "))

def usd_to_inr(usd_value):
    return f"{usd_value} USD = {usd_value * 96.21} INR"

INR_value = usd_to_inr(usd)
print(INR_value)