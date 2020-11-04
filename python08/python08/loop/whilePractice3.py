#打印一个 5*5 matrix（while loop）
def matrix():
    """
    this method is to print a 5*5 matrix
    """
    i = 0
    while i<5:

        j=0
        while j<5:
            print("*  ",end="")
            j+=1
    #一行打印结束，换行
        print()
        i+=1