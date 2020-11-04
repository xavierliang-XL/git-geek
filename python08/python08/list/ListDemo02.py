list=[1,2,3,4]
# list.append(5)
# print(list)
# list=["byte","tube"]
# list.extend("dal")
# print(list)
def insertList(list):
    """
    this method is to insert 1 element to the list and print out the length of the list
    list:list
    """
    list.insert(10,100)
    return len(list)
