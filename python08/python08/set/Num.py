num_set1 = {1,2,3,4}
def GetIndex(num_set):
    """
    this method is to print the index and value in a list
    num_set:list
    """
    for i in enumerate(num_set1):
        print(i)

    for index, num in enumerate(num_set1, start=5):
         print(f'下标是{index}, 对应的数字是{num}')