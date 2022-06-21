def mean_average(numbers):
    total = 0
    for number in numbers:
        total += int(number)
    average = total / len(numbers)
    if average - int(average) == 0:
        return f"The mean is {int(total/len(numbers))}\n"
    else:
        return f"The mean is {round(total/len(numbers), 2)}\n"

def median(nums):
    num_list = []
    if len(nums) % 2 == 0:
        for num in range((len(nums)//2) + 2):
            num_list.append(num)
        return f"The median is {(num_list[-1] + num_list[-2])/2}\n"
    else:
        for num in range((len(nums)//2) + 1):
            num_list.append(num)
        return f"The median is {num_list[-1]}\n"

def mode(number_list):
    number_list.sort()
    amount = 0
    temp = 0
    index = 0
    for num in number_list:
        temp = number_list.count(num)

        if temp > amount:
            amount = temp
            index = num
    mostFrequent = index
    return f"The most frequent number is {mostFrequent} \nOccuring {amount} times \n"
     
while True:
    print("What operation would you like to use?")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("0. To exit")
    option = input(": ")
    if option != "0":
        test = input("Please separate numbers with a space for list: ")
        user_list = test.split()
        if option == "1":
            print("Mean/Average!!")
            print(mean_average(user_list))
        elif option == "2":
            print("Median!!")
            print(median(user_list))
        elif option == "3":
            print("Mode!!")
            print(mode(user_list))
    elif option == "0":
        print("Thank you for choose Rahsaan's Basic Calculator! Have a great day!\n")
        break
    else:
        print("Error input!")
        print("Please enter a different input")