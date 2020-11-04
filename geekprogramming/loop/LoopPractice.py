h=10
count=1
res=h
while count<=10:
    print(f'height:{h},total:{res}')
    h = h / 2
    res+=h if count<2 else  h + h*2
    count+=1