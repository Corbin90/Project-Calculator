while True:
    print("What operation would you like to use?")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("0. To exit")
    option = input(": ")
    if option != "0":
       #test = input()
       # user_list = test.split()
        #print(mean_average(user_list))
        if option == "1":
            print("Mean/Average!!")
        elif option == "2":
            print("Mode!!")
        elif option == "3":
            print("Median!!")
    elif option == "0":
        print("Thank you for choose Rahsaan's Basic Calculator! Have a great day!\n")
        break
    else:
        print("Error input!")
        print("Please enter a different input")