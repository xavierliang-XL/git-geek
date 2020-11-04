list=[1,1]
num=int(input('how many times you wanna repeat????'))
def getSum(list,num):
    for i in range(num-1):
        list.append(list[i]+list[i+1])
    return list
print(getSum(list,num))