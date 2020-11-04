import random

def generateRand(size,bound):
    """
    this method is to generate a random list
    size:the length of the list
    bound:range of the random number
    """
    list=[]
    for i in range(size):
        list.append(random.randint(0,bound))
    print(list)
    return list

def Min(list):
    """
    this method is to get minimum in a list
    list:the list we use
    """
    min= 9999999
    for i in range(len(list)):
        if min>list[i]:
            min=list[i]
    return(min)


print(Min(generateRand(10,100)))