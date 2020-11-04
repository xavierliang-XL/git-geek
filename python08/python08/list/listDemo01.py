list=[1,2,3,4,5,1]
# print(list.index(5,3))
# print(list.count(6))

print(list[1])
def ele(list):
    """
    this method is to print out all the elements in on list
    list:list
    """
    result=''
    for i in range(len(list)):
        result+=str(list[i])+" "
    return result
print(ele(list))