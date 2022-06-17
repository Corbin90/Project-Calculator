def addition(num1, num2):
    total = num1 + num2
    return f"Answer: {num1} + {num2} = {total} \n" 
def subtract(num1, num2):
    total = num1 - num2
    return f"Answer: {num1} - {num2} = {total} \n"
def multiply(num1, num2):
    total = num1 * num2
    return f"Answer: {num1} * {num2} = {total} \n"
def divideWithOutRemainder(num1, num2):
    total = num1 / num2
    if total - int(total) == 0:
        return f"Answer: {num1} / {num2} = {int(total)} \n"
    else:
        return f"Answer: {num1} / {num2} = {round(float(total), 2)} \n"
def divideWithRemainder(num1, num2):
    total = num1 / num2
    remainder = num1 % num2
    return f"Answer: {int(total)}, Remainder: {remainder} \n"
def percentage(num1, num2):
    total = (num1 / num2) * 100
    if total - int(total) == 0:
        return f"Answer: {int(total)}% \n"
    else:
        return f"Answer: {round(total, 2)}% \n"
def power(num1, num2):
    total = num1 ** num2
    return f"Answer: {num1} ^ {num2} = {total} \n"
while True:
    print("What operation would you like to use?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division without remainder")
    print("5. Division with remainder")
    print("6. To exit")
    option = input(": ")
    if option != "6":
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        if option == "1":
            print("Addition!!")
            print(addition(number1, number2))
        elif option == "2":
            print("Subtraction!!")
            print(subtract(number1, number2))
        elif option == "3":
            print("Multiplication!!")
            print(multiply(number1, number2))
        elif option == "4":
            print("Division without remainder!!\n")
            print(divideWithOutRemainder(number1, number2))
        elif option == "5":
            print("Division with remainder!!")
            print(divideWithRemainder(number1, number2))
    elif option == "6":
        print("Thank you for choose Rahsaan's Basic Calculator! Have a great day!\n")
        break
    else:
        print("Error input!")