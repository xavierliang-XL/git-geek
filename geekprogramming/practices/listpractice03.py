list=[0,1,2,3,4,5]
def switch(list):
    """
    this method is to switch the elements in pairs
    list:the list which contains the elements
    """
    i=0
    while i<len(list)-1:
        num=list[i]
        list[i]=list[i+1]
        list[i+1]=num
        i+=2
    return list
print(switch(list))
