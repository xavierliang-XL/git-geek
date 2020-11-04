# 3.2 应用二：计算1-100偶数累加和
def even():
    """
    this method is to get the sum of all the even numbers from 1-100
    """
    sum = 0
    num=1#初始条件
    while num<=100:#判断条件
        if num%2==0:
            sum = sum+num

        num+=1#while的步进


    return(sum)