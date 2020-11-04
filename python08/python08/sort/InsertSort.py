num_list = [3, 5, 6, 0, 1, 2]
def InsertSort(num_list):
    """
    this method is to sort the elements form smallest to greatest
    num_list:array which contains elements
    """
    for i in range(1,len(num_list)):
        for j in range (i,0,-1):
            if num_list[j]<num_list[j-1]:
                num_list[j],num_list[j-1] = num_list[j-1],num_list[j]
    return num_list

print(InsertSort(num_list))