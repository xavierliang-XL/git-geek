# 应用一：计算1 - 100 累加和
# count = 5#初始条件
# while count>=1:#判断条件
#     print("sorry")
#     count-=1#while的步进

def cumulate():
    """
    this method is to calculate the cumulative sum from 1 to 100
    """
    sum = 0
    num=1#初始条件
    while num<=100:#判断条件
        sum = sum+num
        num+=1#while的步进


    return(sum)
