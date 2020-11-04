list=[3,5,6,0,1,2]
for i in range(1,len(list)):
    for j in range(i,0,-1):
        if list[j]<list[j-1]:
            list[j], list[j-1]=list[j-1], list[j]
print(list)