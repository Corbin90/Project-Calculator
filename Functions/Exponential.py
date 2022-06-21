#Exponential functions
# Example 2^2 = 4, 2^3 = 8
def power(base, exponent):
    total = base ** exponent
    if total - int(total) == 0:
        return f"{int(base)}^{int(exponent)} = {int(total)}"
    else:
        return f"{int(base)}^{int(exponent)} = {round(total, 3)}"

# Testcases
print(power(2,3))
print(power(2,-3))
print(power(-2,2))
print(power(-2,-2))
