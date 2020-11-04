def add(*args):
    return sum(args)
print(add(10,10,10))

def add2(*args):
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    return sum
print(add2(10,10,10))