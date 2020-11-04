#bubble sort model:排队

num_list=[3,5,6,1,2,0]
for i in range(len(num_list)-1,0,-1):
    for j in range(i):
        if num_list[j]>num_list[j+1]:
            num=num_list[j]
            num_list[j]=num_list[j+1]
            num_list[j+1]=num
print(num_list)