list1=[1,2,3,4]
list2=[1,2,5]
def getCom(list1,list2):
    """
    this method is to get common elements
    list1:the first list
    list2:the second list
    """
    com=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list2[j]==list1[i]:
                com.append(list2[j])
    return com
print(getCom(list1,list2))