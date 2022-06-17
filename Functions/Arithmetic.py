# Basic Arithmetic Functions

def addition(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    total = num1 / num2
    if total - int(total) == 0:
        return int(total)
    else:
        return float(total)

#Division test cases
print("Division")
print(divide(200, 6)) # Return decimal
print(divide(200, 5)) # Return integer

#Multiplication test case
print("Multiplication")
print(multiply(3, 9))

#Subtraction test cases
print("Subtraction")
print(subtract(2, 3)) # Return negative number
print(subtract(3, 2)) # Return Positive number
print(subtract(-2,-3)) # Two negatives returning negative

#Addition
print("Addition")
print(addition(2,3)) # Two positive return positive
print(addition(-2,-3)) # Two negatives return negative
print(addition(-3, 4)) # Negative then positive returning positive
print(addition(3,-4)) # Positive then negative returning negative)

