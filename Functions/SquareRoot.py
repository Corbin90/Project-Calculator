def squareRoot(number, root):
    total = number ** (1/root)
    if total - int(total) == 0:
        return f"Square root: {int(total)}"
    else:
        return f"Square root: {round(total, 3)}"
