list=[11,12,6,88,21,4]
max=0
for i in range(1,len(list)):
    if list[i]>max:
        max=list[i]
print(max)
i=0
j=len(list)-1
while(i<j):
    res=list[i]
    list[i]=list[j]
    list[j]=res
    i+=1
    j-=1
print(list)
