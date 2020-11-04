#0~4 1-5
def isosceles():
    """
    this method is to print an isosceles triangle
    """
    i = 1
    while i<=5:

        j=1
        while j<=i:
            print("*  ",end="")
            j+=1
    #一行打印结束，换行
        print()
        i+=1