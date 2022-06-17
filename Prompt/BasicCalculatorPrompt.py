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
        elif option == "2":
            print("Subtraction!!")
        elif option == "3":
            print("Multiplication!!")
        elif option == "4":
            print("Division without remainder!!")
        elif option == "5":
            print("Division with remainder!!")
    elif option == "6":
        print("Thank you for choose Rahsaan's Basic Calculator! Have a great day!\n")
        break
    else:
        print("Error input!")
        print("Please enter a different input")