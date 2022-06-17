def mean_average(numbers):
    total = 0
    for number in numbers:
        total += int(number)
    average = total / len(numbers)
    if average - int(average) == 0:
        return int(total/len(numbers))
    else:
        return round(total/len(numbers), 2)
def median(nums):
    num_list = []
    if len(nums) % 2 == 0:
        for num in range((len(nums)//2) + 2):
            num_list.append(num)
        return (num_list[-1] + num_list[-2])/2
    else:
        for num in range((len(nums)//2) + 1):
            num_list.append(num)
        return num_list[-1]
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
    return f"The most frequent number is {mostFrequent} \nOccuring {amount} times"
     
test = input()
user_list = test.split()
print(mean_average(user_list))
