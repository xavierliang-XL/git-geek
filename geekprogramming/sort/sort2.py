num_list=[3,4,7,6,10,5,2]
res_list=[]
count=len(num_list)
for i in range(count):
    min=num_list[0]
    print(min)
    for j in range(0,len(num_list)):
        if min>num_list[j]:
            min=num_list[j]
        else:
            min=min

    print(num_list)
    print(min)
    num_list.remove(min)
    res_list.append(min)
print(res_list)