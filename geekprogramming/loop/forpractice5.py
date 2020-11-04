integer=100
res=0
while integer>=1:
    if integer%2==0:
        if integer==66:
            integer-=1
            continue
        res+=integer
    integer-=1
else:
    print(res)