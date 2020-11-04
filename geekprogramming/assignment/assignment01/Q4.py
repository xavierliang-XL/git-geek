list=(1,2,3,4,5,6)
counto=0
counte=0
for i in range(0,len(list)):
    if list[i]%2==0:
        counte+=1
        continue
    counto+=1
print(f'odd num:{counto}')
print(f'even num{counte}')