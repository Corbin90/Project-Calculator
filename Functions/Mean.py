# Calculating the mean
# Be sure to enter a list when doing this

def mean_average(numbers):
    total = 0
    for number in numbers:
        total += int(number)
    average = total / len(numbers)
    if average - int(average) == 0:
       return f"The mean is {int(total/len(numbers))}"
    else:
        return f"The mean is {round(total/len(numbers), 2)}"

# Test Case
#test = [9,3,2,3,4,5,2]
test = input()
user_list = test.split()
print(mean_average(user_list))
test = [9,3,2,3,4,5,2]
print(mean_average(test))