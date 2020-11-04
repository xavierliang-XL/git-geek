list1=[[2,1],2,3,[2,4],5,1]

def insert_list(list1):
    """
    this method is to replace the elements that have a type of list
    :param list1:
    :return:
    """
    for i in range(len(list1)):
     if type(list1[i])==list:
        list2=list1.pop(i)
        for j in range(list2[0]):
             list1.insert(i,list2[1])
    return list1
print(insert_list(list1))