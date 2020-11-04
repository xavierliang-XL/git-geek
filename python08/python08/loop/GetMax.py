#[11,12,6,88,21,4]
list = [11,12,6,88,21,4]
def getMax(list):
    """
    this method is to get the max number from a list
    list:list
    """
    max=11
    for i in range(1,len(list)):
        if list[i] > max:
            max = list[i]
    return(max)

