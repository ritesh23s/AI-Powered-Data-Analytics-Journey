# ********** LOCAL AND GLOBAL VARIABLE IN PYTHON **********
# ********** GLOBAL VARIABLE AND FUNCTION PARAMETER **********
# A better approach than using global is passing data explicitly.

def update_temp(value):
    return value + 400

actual_temp = 100
result = update_temp(actual_temp)
print(result)
# Output:
# 500
