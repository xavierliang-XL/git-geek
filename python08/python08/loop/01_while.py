count = 5#初始条件
def whileLoop(count):
    """
    this method is to print out sorry by using while loop
    count:times you print out sorry
    """
    result=''
    while count>=1:#判断条件
        result+="sorry"
        count-=1#while的步进
    return result