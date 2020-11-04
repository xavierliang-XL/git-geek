def getMax(list,left,right):
    if left==right:
        return list[left]
    mid=int((left+right)/2)
    left_max=getMax(list,left,mid)
    right_max=getMax(list,mid+1,right)
    return max(left_max,right_max)
list=[3,7,9,102,55,43,65,77,99,2]
print(getMax(list,0,len(list)-1))