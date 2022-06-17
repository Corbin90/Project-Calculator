# Additional features on top basic arithmetic features
def percentage(num1, num2):
    total = (num1 / num2) * 100
    if total - int(total) == 0:
        return f"{int(total)}%"
    else:
        return f"{round(total, 2)}%"


# Test case for percentage
print(percentage(1,4))
print(percentage(3,4))
print(percentage(4,4))
print(percentage(1,3))