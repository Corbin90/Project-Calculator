#Mode is finding what number occurs the most
#Enter a list of numbers
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
#Test case
test = [2,2,2,3,2,2,1,2,3,4,5,4,9,2,3,4] 
print(mode(test))     
test = [4,4,4,4,4,8,8,9,10,10,10,10,10,10,2,3,4,10,10]
print(mode(test))  