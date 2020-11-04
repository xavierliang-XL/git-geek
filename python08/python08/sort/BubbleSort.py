num_list = [3,5,6,0,1,2]
#res_list[]
#假设min=3 min=0
#num_list = [3,5,6,1,2]
def BubbleSort(num_list):
    """
    this method is to sort the elements form smallest to greatest
    num_list:array which contains elements
    """
    num = len(num_list)-1
    while num>0:

        for j in range(num):
            if num_list[j]>num_list[j+1]:
                temp = num_list[j]
                num_list[j]=num_list[j+1]
                num_list[j+1] = temp

            num-=1#1已经排好序的数
    return num_list

print(BubbleSort(num_list))