list=[[1,2,3],[2,3,4],[3,4,5]]
def Max(list):
    max=0
    for i in range(len(list)):
        new_list=list[i]
        list[i]=sum(new_list[:])
        if i==0:
            max=list[i]
        elif list[i-1]<list[i]:
            max=new_list
    return max
print(Max(list))