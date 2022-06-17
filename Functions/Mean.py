# Calculating the mean
# Be sure to enter a list when doing this

def mean_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    if average - int(average) == 0:
        return int(total/len(numbers))
    else:
        return round(total/len(numbers), 2)

# Test Case
test = [9,3,2,3,4,5,2]
print(mean_average(test))
test = [9,3,2,3,4,5,2,3,1]
print(mean_average(test))