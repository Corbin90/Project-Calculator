while True:
    print("What operation would you like to use?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division without remainder")
    print("5. Division with remainder")
    print("6. Calculating percentage")
    print("7. Calculating equations with an exponent")
    print("8. Calculating the mean (use spaces when separating numbers for list)")
    print("9. Calculating median")
    print("10. Calculating mode")
    print("11. Calculating square root")
    print("0. To exit")
    option = input(": ")
    if option != "0":
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
            print("Percentage calculation!!")
        elif option == "7":
            print("Calculating equations with exponents!!")
        elif option == "8":
            print("Calculating the mean")
        elif option == "9":
            print("Calculating median")
        elif option == "10":
            print("Calculating mode")
        elif option == "11":
            print("Calculating square root")
    elif option == "0":
        print("Thank you for choose Rahsaan's Basic Calculator! Have a great day!\n")
        break
    else:
        print("Error input!")
        print("Please enter a different input")