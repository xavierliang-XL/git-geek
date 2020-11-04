list=['a','b','c','a','d','c']
def count(list):
    """
    this method is to get the frequency of the elements appearance
    list: the list that user will search
    """
    list2=set(list)
    res=''
    for i in list2:
        count=0
        for j in list:
            if j==i:
                count+=1
        res+=f'there will be {count} {i} in the list     '
    return res
print(count(list))