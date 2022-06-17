# Median Calculation
# if list module is an odd number length then return the value
# if list module is an even number length then add the values then divide by 2

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
  
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(median(num_list))
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(median(num_list))