list=[1,1]
num=int(input('how many times you wanna repeat????'))
def getSum(list,num):
    """
    this method is to get the sum of the first two elements, and keep superimposing
    list:the list with two elements of 1,1
    num:times the user wants t repeat
    """
    for i in range(num-1):
        list.append(list[i]+list[i+1])
    return list
print(getSum(list,num))